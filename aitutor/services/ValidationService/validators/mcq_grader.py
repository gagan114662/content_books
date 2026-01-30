"""
MCQGrader - Multiple choice question validation.

Simple but robust validation for multiple choice questions.
Supports single-answer and multiple-answer (select all that apply) formats.
"""

from typing import Any, List, Optional, Union

from .base import BaseValidator, ValidationResult, ErrorCode


class MCQGrader(BaseValidator):
    """
    Validates multiple choice question answers.

    Supports:
    - Single answer (index or letter)
    - Multiple answers (list of indices or letters)
    - Partial credit for multi-select questions

    Configuration options:
        - partial_credit: Enable partial credit for multi-select (default: True)
        - case_sensitive: Whether letter answers are case-sensitive (default: False)
    """

    def __init__(self, config: Optional[dict] = None):
        super().__init__(config)
        self.partial_credit = self.config.get("partial_credit", True)
        self.case_sensitive = self.config.get("case_sensitive", False)

    def validate(self, problem: dict, student_answer: Any) -> ValidationResult:
        """
        Validate a multiple choice answer.

        Args:
            problem: Must contain:
                - 'answer': int (0-indexed) or str (letter) or list for multi-select
                - 'options': list of option strings
                - Optional 'explanation': explanation for correct answer
            student_answer: int, str (letter), or list

        Returns:
            ValidationResult with correctness and feedback
        """
        correct_answer = problem.get("answer")
        options = problem.get("options", [])
        explanation = problem.get("explanation", "")

        if correct_answer is None:
            return ValidationResult(
                correct=False,
                score=0.0,
                error_code=ErrorCode.PARSE_ERROR,
                feedback="Problem configuration error: no correct answer specified.",
                details={"error": "missing_correct_answer"}
            )

        # Normalize answers for comparison
        try:
            student_normalized = self._normalize_answer(student_answer, len(options))
            correct_normalized = self._normalize_answer(correct_answer, len(options))
        except ValueError as e:
            return ValidationResult(
                correct=False,
                score=0.0,
                error_code=ErrorCode.PARSE_ERROR,
                feedback=str(e),
                details={"raw_answer": str(student_answer)}
            )

        # Handle multi-select questions
        if isinstance(correct_normalized, list):
            return self._validate_multi_select(
                student_normalized, correct_normalized, options, explanation
            )

        # Single answer validation
        is_correct = student_normalized == correct_normalized

        if is_correct:
            return ValidationResult(
                correct=True,
                score=1.0,
                error_code=ErrorCode.CORRECT,
                feedback="Correct!" + (f" {explanation}" if explanation else ""),
                details={
                    "selected": self._get_option_text(student_normalized, options),
                    "correct": self._get_option_text(correct_normalized, options)
                }
            )

        return ValidationResult(
            correct=False,
            score=0.0,
            error_code=ErrorCode.WRONG_ANSWER,
            feedback=f"Incorrect. The correct answer is: {self._get_option_text(correct_normalized, options)}"
                     + (f"\n\n{explanation}" if explanation else ""),
            details={
                "selected": self._get_option_text(student_normalized, options),
                "correct": self._get_option_text(correct_normalized, options)
            }
        )

    def _validate_multi_select(
        self,
        student: Union[int, List[int]],
        correct: List[int],
        options: List[str],
        explanation: str
    ) -> ValidationResult:
        """Handle multi-select (select all that apply) questions."""

        # Ensure student answer is a list
        if isinstance(student, int):
            student = [student]

        student_set = set(student)
        correct_set = set(correct)

        if student_set == correct_set:
            return ValidationResult(
                correct=True,
                score=1.0,
                error_code=ErrorCode.CORRECT,
                feedback="Correct! You selected all the right answers.",
                details={
                    "selected": [self._get_option_text(i, options) for i in student],
                    "correct": [self._get_option_text(i, options) for i in correct]
                }
            )

        # Calculate partial credit if enabled
        if self.partial_credit:
            # Points for correct selections, minus points for wrong selections
            correct_selections = len(student_set & correct_set)
            incorrect_selections = len(student_set - correct_set)
            missed_selections = len(correct_set - student_set)

            # Score = (correct - incorrect) / total_correct, minimum 0
            score = max(0, (correct_selections - incorrect_selections) / len(correct_set))

            feedback_parts = []
            if correct_selections > 0:
                feedback_parts.append(f"You got {correct_selections} correct")
            if incorrect_selections > 0:
                feedback_parts.append(f"{incorrect_selections} incorrect")
            if missed_selections > 0:
                feedback_parts.append(f"missed {missed_selections}")

            return ValidationResult(
                correct=False,
                score=score,
                error_code=ErrorCode.PARTIAL_CREDIT if score > 0 else ErrorCode.WRONG_ANSWER,
                feedback=". ".join(feedback_parts) + "."
                        + f"\n\nCorrect answers: {', '.join(self._get_option_text(i, options) for i in sorted(correct))}"
                        + (f"\n\n{explanation}" if explanation else ""),
                details={
                    "selected": [self._get_option_text(i, options) for i in student],
                    "correct": [self._get_option_text(i, options) for i in correct],
                    "correct_selections": correct_selections,
                    "incorrect_selections": incorrect_selections,
                    "missed_selections": missed_selections
                }
            )

        # No partial credit
        return ValidationResult(
            correct=False,
            score=0.0,
            error_code=ErrorCode.WRONG_ANSWER,
            feedback=f"Incorrect. The correct answers are: {', '.join(self._get_option_text(i, options) for i in sorted(correct))}"
                     + (f"\n\n{explanation}" if explanation else ""),
            details={
                "selected": [self._get_option_text(i, options) for i in student],
                "correct": [self._get_option_text(i, options) for i in correct]
            }
        )

    def parse_answer(self, raw_answer: Any) -> Union[int, List[int]]:
        """
        Parse raw answer into normalized form.

        This is a public interface; use _normalize_answer for internal use
        with knowledge of option count.
        """
        # Without option count, we can only do basic parsing
        if isinstance(raw_answer, int):
            return raw_answer
        if isinstance(raw_answer, list):
            return [self.parse_answer(a) for a in raw_answer]
        if isinstance(raw_answer, str):
            raw = raw_answer.strip()
            # Check for letter (A, B, C, D)
            if len(raw) == 1 and raw.upper() in "ABCDEFGHIJ":
                return ord(raw.upper()) - ord("A")
            # Check for number
            try:
                return int(raw)
            except ValueError:
                raise ValueError(f"Could not parse answer: '{raw_answer}'")
        raise ValueError(f"Unsupported answer type: {type(raw_answer)}")

    def _normalize_answer(
        self, answer: Any, num_options: int
    ) -> Union[int, List[int]]:
        """
        Normalize answer to 0-indexed integer(s).

        Args:
            answer: int, str (letter), or list
            num_options: Number of options for bounds checking

        Returns:
            Normalized int or list of ints
        """
        if isinstance(answer, list):
            return [self._normalize_single(a, num_options) for a in answer]
        return self._normalize_single(answer, num_options)

    def _normalize_single(self, answer: Any, num_options: int) -> int:
        """Normalize a single answer to 0-indexed integer."""
        if isinstance(answer, int):
            if 0 <= answer < num_options:
                return answer
            raise ValueError(f"Answer index {answer} out of range (0-{num_options-1})")

        if isinstance(answer, str):
            answer_str = answer.strip()
            if not self.case_sensitive:
                answer_str = answer_str.upper()

            # Check for letter (A, B, C, D, etc.)
            if len(answer_str) == 1 and answer_str in "ABCDEFGHIJ":
                idx = ord(answer_str) - ord("A")
                if 0 <= idx < num_options:
                    return idx
                raise ValueError(f"Answer '{answer}' out of range")

            # Check for number string
            try:
                idx = int(answer_str)
                if 0 <= idx < num_options:
                    return idx
                raise ValueError(f"Answer index {idx} out of range (0-{num_options-1})")
            except ValueError:
                pass

            raise ValueError(f"Could not parse answer: '{answer}'")

        raise ValueError(f"Unsupported answer type: {type(answer)}")

    def _get_option_text(self, index: int, options: List[str]) -> str:
        """Get option text with letter prefix."""
        if 0 <= index < len(options):
            letter = chr(ord("A") + index)
            return f"{letter}) {options[index]}"
        return f"Option {index}"
