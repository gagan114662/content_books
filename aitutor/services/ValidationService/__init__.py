"""
ValidationService - Unified answer validation for AI Tutor

Supports multiple validator types:
- NumericSolver: Physics, Chemistry, Economics, Statistics
- MCQGrader: All subjects (multiple choice)
- RubricGrader: History, Psychology, Sociology, Philosophy
- CodeExecutor: CS, Data Structures
- FactChecker: History, Civics
- WritingRubric: Academic Writing, Public Speaking
"""

from .validators.base import BaseValidator
from .validators.numeric_solver import NumericSolver
from .validators.mcq_grader import MCQGrader

__all__ = ["BaseValidator", "NumericSolver", "MCQGrader"]
