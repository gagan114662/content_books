"""
ValidationService API - Unified endpoint for answer validation.

Routes to appropriate validator based on problem type.
"""

from typing import Any, Optional
from pydantic import BaseModel

from .validators import BaseValidator, NumericSolver, MCQGrader
from .validators.base import ValidationResult


class ValidateRequest(BaseModel):
    """Request schema for validation endpoint."""
    problem_id: str
    student_answer: Any  # Type depends on problem type
    problem: dict  # Full problem definition
    user_id: Optional[str] = None


class ValidateResponse(BaseModel):
    """Response schema for validation endpoint."""
    correct: bool
    score: float
    error_code: str
    feedback: Optional[str] = None
    details: Optional[dict] = None


# Validator registry
VALIDATORS: dict[str, type[BaseValidator]] = {
    "numeric": NumericSolver,
    "numeric_solver": NumericSolver,
    "mcq": MCQGrader,
    "multiple_choice": MCQGrader,
    "radio": MCQGrader,
}


def get_validator(problem_type: str, config: Optional[dict] = None) -> BaseValidator:
    """
    Get appropriate validator instance for problem type.

    Args:
        problem_type: Type of problem (numeric, mcq, etc.)
        config: Optional validator configuration

    Returns:
        Validator instance

    Raises:
        ValueError: If problem type is not supported
    """
    validator_class = VALIDATORS.get(problem_type.lower())
    if not validator_class:
        raise ValueError(f"Unsupported problem type: {problem_type}")
    return validator_class(config)


def validate_answer(
    problem: dict,
    student_answer: Any,
    problem_type: Optional[str] = None,
    config: Optional[dict] = None
) -> ValidationResult:
    """
    Validate a student answer against a problem.

    This is the main entry point for validation.

    Args:
        problem: Problem definition with answer, options, etc.
        student_answer: Student's submitted answer
        problem_type: Override problem type (defaults to problem["type"])
        config: Override validator config

    Returns:
        ValidationResult with correctness, score, feedback
    """
    # Determine problem type
    p_type = problem_type or problem.get("type", "numeric")

    # Get validator config from problem if not provided
    if config is None:
        config = problem.get("validator_config", {})

    # Get and run validator
    validator = get_validator(p_type, config)
    return validator.validate(problem, student_answer)


def validate_answer_dict(
    problem: dict,
    student_answer: Any,
    problem_type: Optional[str] = None,
    config: Optional[dict] = None
) -> dict:
    """
    Validate and return result as dictionary.

    Convenience wrapper for JSON serialization.
    """
    result = validate_answer(problem, student_answer, problem_type, config)
    return result.to_dict()


# FastAPI integration (when used as a service)
def create_router():
    """Create FastAPI router for validation endpoints."""
    try:
        from fastapi import APIRouter, HTTPException
    except ImportError:
        return None

    router = APIRouter(prefix="/api/validate", tags=["validation"])

    @router.post("/", response_model=ValidateResponse)
    async def validate_endpoint(request: ValidateRequest):
        """
        Validate a student answer.

        POST /api/validate/
        {
            "problem_id": "kin1d_001",
            "student_answer": "96 m",
            "problem": {
                "type": "numeric",
                "answer": {"value": 96, "unit": "m", "tolerance": 0.02}
            }
        }
        """
        try:
            result = validate_answer(request.problem, request.student_answer)
            return ValidateResponse(
                correct=result.correct,
                score=result.score,
                error_code=result.error_code.value,
                feedback=result.feedback,
                details=result.details
            )
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @router.post("/numeric")
    async def validate_numeric(
        student_answer: str,
        expected_value: float,
        expected_unit: Optional[str] = None,
        tolerance: float = 0.02
    ):
        """Quick numeric validation without full problem object."""
        problem = {
            "type": "numeric",
            "answer": {
                "value": expected_value,
                "unit": expected_unit,
                "tolerance": tolerance
            }
        }
        result = validate_answer(problem, student_answer)
        return ValidateResponse(
            correct=result.correct,
            score=result.score,
            error_code=result.error_code.value,
            feedback=result.feedback,
            details=result.details
        )

    @router.post("/mcq")
    async def validate_mcq(
        student_answer: int,
        correct_answer: int,
        options: list[str],
        explanation: Optional[str] = None
    ):
        """Quick MCQ validation."""
        problem = {
            "type": "mcq",
            "answer": correct_answer,
            "options": options,
            "explanation": explanation
        }
        result = validate_answer(problem, student_answer)
        return ValidateResponse(
            correct=result.correct,
            score=result.score,
            error_code=result.error_code.value,
            feedback=result.feedback,
            details=result.details
        )

    return router
