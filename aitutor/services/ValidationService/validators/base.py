"""Base validator interface for all validation types."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional


class ErrorCode(Enum):
    """Standard error codes for validation results."""
    CORRECT = "CORRECT"
    WRONG_VALUE = "WRONG_VALUE"
    WRONG_UNIT = "WRONG_UNIT"
    UNIT_MISMATCH = "UNIT_MISMATCH"
    PARSE_ERROR = "PARSE_ERROR"
    SIGN_ERROR = "SIGN_ERROR"
    PARTIAL_CREDIT = "PARTIAL_CREDIT"
    WRONG_ANSWER = "WRONG_ANSWER"
    TIMEOUT = "TIMEOUT"
    RUNTIME_ERROR = "RUNTIME_ERROR"
    SYNTAX_ERROR = "SYNTAX_ERROR"


@dataclass
class ValidationResult:
    """Standard result returned by all validators."""
    correct: bool
    score: float  # 0.0 to 1.0
    error_code: ErrorCode
    feedback: Optional[str] = None
    details: Optional[dict] = None

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "correct": self.correct,
            "score": self.score,
            "error_code": self.error_code.value,
            "feedback": self.feedback,
            "details": self.details
        }


class BaseValidator(ABC):
    """
    Abstract base class for all validators.

    Each validator type (numeric, code, mcq, rubric, etc.) must implement
    the validate() method with subject-specific logic.
    """

    def __init__(self, config: Optional[dict] = None):
        """
        Initialize validator with optional configuration.

        Args:
            config: Validator-specific configuration options
        """
        self.config = config or {}

    @abstractmethod
    def validate(self, problem: dict, student_answer: Any) -> ValidationResult:
        """
        Validate a student's answer against the expected answer.

        Args:
            problem: Problem definition including expected answer and metadata
            student_answer: The student's submitted answer

        Returns:
            ValidationResult with correctness, score, and feedback
        """
        pass

    @abstractmethod
    def parse_answer(self, raw_answer: Any) -> Any:
        """
        Parse and normalize a student's raw answer.

        Args:
            raw_answer: The raw answer input from student

        Returns:
            Parsed/normalized answer for comparison
        """
        pass

    def generate_feedback(
        self,
        problem: dict,
        student_answer: Any,
        result: ValidationResult
    ) -> str:
        """
        Generate helpful feedback based on the validation result.

        Can be overridden by subclasses for subject-specific feedback.

        Args:
            problem: The problem definition
            student_answer: What the student submitted
            result: The validation result

        Returns:
            Feedback string for the student
        """
        if result.correct:
            return "Correct!"

        feedback_map = {
            ErrorCode.WRONG_VALUE: "Your answer is incorrect. Check your calculations.",
            ErrorCode.WRONG_UNIT: "The value is correct but check your units.",
            ErrorCode.UNIT_MISMATCH: "Your answer has incompatible units.",
            ErrorCode.PARSE_ERROR: "Could not understand your answer. Please use the expected format.",
            ErrorCode.SIGN_ERROR: "Check the sign of your answer.",
            ErrorCode.PARTIAL_CREDIT: "Partially correct. Review the feedback for improvements.",
            ErrorCode.WRONG_ANSWER: "Incorrect. Try again.",
        }

        return feedback_map.get(result.error_code, "Incorrect answer.")
