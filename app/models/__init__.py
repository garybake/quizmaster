"""Holds all of the applications models."""

from .user import User
from .quiz import Quiz
from .question import Question
from .answer import Answer
from .answerselect import AnswerSelect

__all__ = [
    "User",
    "Quiz",
    "Question",
    "Answer",
    "AnswerSelect",
]
