"""
NumericSolver - Unit-aware numeric validation for STEM subjects.

Supports Physics, Chemistry, Economics, Statistics with:
- Unit parsing and conversion using pint
- Configurable tolerance (relative/absolute)
- Sign error detection
- Unit mismatch detection
"""

import re
from dataclasses import dataclass
from typing import Any, Optional, Tuple

try:
    import pint
    PINT_AVAILABLE = True
except ImportError:
    PINT_AVAILABLE = False

from .base import BaseValidator, ValidationResult, ErrorCode


@dataclass
class ParsedNumeric:
    """Represents a parsed numeric answer with optional unit."""
    value: float
    unit: Optional[str] = None
    raw: str = ""


class NumericSolver(BaseValidator):
    """
    Validates numeric answers with optional unit awareness.

    Configuration options:
        - unit_library: Which unit definitions to load (physics, chemistry, etc.)
        - default_tolerance: Default relative tolerance (e.g., 0.02 for 2%)
        - tolerance_type: "relative" or "absolute"
        - require_units: Whether units are required in student answers
        - allow_equivalent_units: Accept equivalent units (m/s vs meters per second)
    """

    # Common unit aliases for flexible parsing
    UNIT_ALIASES = {
        # Length
        "m": "meter", "meters": "meter", "metre": "meter",
        "cm": "centimeter", "mm": "millimeter", "km": "kilometer",
        "ft": "foot", "feet": "foot", "in": "inch", "inches": "inch",
        # Time
        "s": "second", "sec": "second", "seconds": "second",
        "min": "minute", "minutes": "minute",
        "h": "hour", "hr": "hour", "hours": "hour",
        # Mass
        "kg": "kilogram", "g": "gram", "grams": "gram",
        "lb": "pound", "lbs": "pound",
        # Velocity
        "m/s": "meter/second", "m/sec": "meter/second",
        "km/h": "kilometer/hour", "kph": "kilometer/hour",
        "mph": "mile/hour",
        # Acceleration
        "m/s^2": "meter/second**2", "m/s²": "meter/second**2",
        # Force
        "N": "newton", "newtons": "newton",
        # Energy
        "J": "joule", "joules": "joule",
        "kJ": "kilojoule",
        # Power
        "W": "watt", "watts": "watt",
        "kW": "kilowatt",
        # Currency (for economics)
        "$": "dollar", "dollars": "dollar",
        # Percentage
        "%": "percent",
    }

    def __init__(self, config: Optional[dict] = None):
        super().__init__(config)
        self.default_tolerance = self.config.get("default_tolerance", 0.02)
        self.tolerance_type = self.config.get("tolerance_type", "relative")
        self.require_units = self.config.get("require_units", False)
        self.allow_equivalent = self.config.get("allow_equivalent_units", True)

        # Initialize pint unit registry if available
        if PINT_AVAILABLE:
            self.ureg = pint.UnitRegistry()
            self.ureg.default_format = "~P"  # Short pretty format
        else:
            self.ureg = None

    def validate(self, problem: dict, student_answer: Any) -> ValidationResult:
        """
        Validate a numeric answer against expected value.

        Args:
            problem: Must contain 'answer' with 'value', optional 'unit', 'tolerance'
            student_answer: String like "96 m" or "3.0 s" or just "42"

        Returns:
            ValidationResult with correctness and detailed feedback
        """
        # Parse expected answer from problem
        expected = problem.get("answer", {})
        if isinstance(expected, (int, float)):
            expected = {"value": expected}

        expected_value = expected.get("value")
        expected_unit = expected.get("unit")
        tolerance = expected.get("tolerance", self.default_tolerance)
        tolerance_type = expected.get("tolerance_type", self.tolerance_type)

        if expected_value is None:
            return ValidationResult(
                correct=False,
                score=0.0,
                error_code=ErrorCode.PARSE_ERROR,
                feedback="Problem configuration error: no expected value.",
                details={"error": "missing_expected_value"}
            )

        # Parse student answer
        try:
            parsed = self.parse_answer(student_answer)
        except ValueError as e:
            return ValidationResult(
                correct=False,
                score=0.0,
                error_code=ErrorCode.PARSE_ERROR,
                feedback=f"Could not parse your answer: {str(e)}",
                details={"raw_answer": str(student_answer), "parse_error": str(e)}
            )

        # Check if units are required but missing
        if self.require_units and expected_unit and not parsed.unit:
            return ValidationResult(
                correct=False,
                score=0.0,
                error_code=ErrorCode.PARSE_ERROR,
                feedback="Please include units in your answer.",
                details={"expected_unit": expected_unit}
            )

        # Handle unit conversion if both have units
        student_value = parsed.value
        if expected_unit and parsed.unit:
            try:
                student_value, unit_match = self._convert_units(
                    parsed.value, parsed.unit, expected_unit
                )
                if not unit_match:
                    return ValidationResult(
                        correct=False,
                        score=0.0,
                        error_code=ErrorCode.UNIT_MISMATCH,
                        feedback=f"Unit mismatch: your answer has '{parsed.unit}' but expected '{expected_unit}'.",
                        details={
                            "student_unit": parsed.unit,
                            "expected_unit": expected_unit
                        }
                    )
            except Exception as e:
                return ValidationResult(
                    correct=False,
                    score=0.0,
                    error_code=ErrorCode.UNIT_MISMATCH,
                    feedback=f"Could not convert units: {str(e)}",
                    details={"error": str(e)}
                )

        # Check value within tolerance
        is_correct, error_type = self._check_tolerance(
            student_value, expected_value, tolerance, tolerance_type
        )

        if is_correct:
            # Check if unit is wrong but value is right
            if expected_unit and parsed.unit:
                student_unit_normalized = self._normalize_unit(parsed.unit)
                expected_unit_normalized = self._normalize_unit(expected_unit)
                if student_unit_normalized != expected_unit_normalized:
                    return ValidationResult(
                        correct=False,
                        score=0.5,  # Partial credit for correct value
                        error_code=ErrorCode.WRONG_UNIT,
                        feedback=f"Correct value, but check your units. Expected: {expected_unit}",
                        details={
                            "student_value": student_value,
                            "expected_value": expected_value,
                            "student_unit": parsed.unit,
                            "expected_unit": expected_unit
                        }
                    )

            return ValidationResult(
                correct=True,
                score=1.0,
                error_code=ErrorCode.CORRECT,
                feedback="Correct!",
                details={
                    "student_value": student_value,
                    "expected_value": expected_value,
                    "tolerance": tolerance
                }
            )

        # Check for sign error (correct magnitude, wrong sign)
        if error_type == "sign":
            return ValidationResult(
                correct=False,
                score=0.0,
                error_code=ErrorCode.SIGN_ERROR,
                feedback="Check the sign of your answer.",
                details={
                    "student_value": student_value,
                    "expected_value": expected_value
                }
            )

        return ValidationResult(
            correct=False,
            score=0.0,
            error_code=ErrorCode.WRONG_VALUE,
            feedback="Incorrect value. Check your calculations.",
            details={
                "student_value": student_value,
                "expected_value": expected_value,
                "tolerance": tolerance
            }
        )

    def parse_answer(self, raw_answer: Any) -> ParsedNumeric:
        """
        Parse a raw answer string into value and unit.

        Handles formats like:
        - "96 m"
        - "3.0 s"
        - "-9.8 m/s^2"
        - "42"
        - "$150"
        - "25%"
        """
        if isinstance(raw_answer, (int, float)):
            return ParsedNumeric(value=float(raw_answer), unit=None, raw=str(raw_answer))

        raw_str = str(raw_answer).strip()

        # Handle currency prefix
        if raw_str.startswith("$"):
            match = re.match(r"\$\s*([-+]?\d*\.?\d+)", raw_str)
            if match:
                return ParsedNumeric(
                    value=float(match.group(1)),
                    unit="dollar",
                    raw=raw_str
                )

        # Handle percentage suffix
        if raw_str.endswith("%"):
            match = re.match(r"([-+]?\d*\.?\d+)\s*%", raw_str)
            if match:
                return ParsedNumeric(
                    value=float(match.group(1)),
                    unit="percent",
                    raw=raw_str
                )

        # General pattern: number followed by optional unit
        # Handles scientific notation like 1.5e-3
        pattern = r"([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)\s*(.*)?"
        match = re.match(pattern, raw_str)

        if not match:
            raise ValueError(f"Could not parse numeric value from '{raw_str}'")

        value_str = match.group(1)
        unit_str = match.group(2).strip() if match.group(2) else None

        try:
            value = float(value_str)
        except ValueError:
            raise ValueError(f"Could not convert '{value_str}' to a number")

        return ParsedNumeric(value=value, unit=unit_str if unit_str else None, raw=raw_str)

    def _normalize_unit(self, unit: str) -> str:
        """Normalize unit string for comparison."""
        if not unit:
            return ""
        unit_lower = unit.lower().strip()
        return self.UNIT_ALIASES.get(unit_lower, unit_lower)

    def _convert_units(
        self, value: float, from_unit: str, to_unit: str
    ) -> Tuple[float, bool]:
        """
        Convert value from one unit to another.

        Returns:
            Tuple of (converted_value, units_compatible)
        """
        if not PINT_AVAILABLE:
            # Without pint, just check if units match (case-insensitive)
            from_norm = self._normalize_unit(from_unit)
            to_norm = self._normalize_unit(to_unit)
            return (value, from_norm == to_norm)

        try:
            from_norm = self._normalize_unit(from_unit)
            to_norm = self._normalize_unit(to_unit)

            quantity = value * self.ureg.parse_expression(from_norm)
            converted = quantity.to(to_norm)
            return (converted.magnitude, True)
        except pint.DimensionalityError:
            return (value, False)
        except Exception:
            # Fall back to string comparison
            return (value, self._normalize_unit(from_unit) == self._normalize_unit(to_unit))

    def _check_tolerance(
        self,
        student: float,
        expected: float,
        tolerance: float,
        tolerance_type: str
    ) -> Tuple[bool, Optional[str]]:
        """
        Check if student value is within tolerance of expected.

        Returns:
            Tuple of (is_correct, error_type)
            error_type is "sign" if magnitude correct but sign wrong
        """
        if expected == 0:
            # For zero expected, use absolute comparison
            return (abs(student) <= tolerance, None)

        if tolerance_type == "relative":
            relative_error = abs(student - expected) / abs(expected)
            is_correct = relative_error <= tolerance
        else:  # absolute
            is_correct = abs(student - expected) <= tolerance

        if is_correct:
            return (True, None)

        # Check for sign error (magnitude matches but sign doesn't)
        if tolerance_type == "relative":
            magnitude_error = abs(abs(student) - abs(expected)) / abs(expected)
            if magnitude_error <= tolerance and (student * expected < 0):
                return (False, "sign")
        else:
            if abs(abs(student) - abs(expected)) <= tolerance and (student * expected < 0):
                return (False, "sign")

        return (False, None)
