"""Shared data types used to describe lessons and their quizzes."""
from dataclasses import dataclass, field
from typing import Callable


@dataclass
class QuizQuestion:
    question: str
    options: list[str]
    answer: int  # index into options
    explanation: str = ""


@dataclass
class Lesson:
    key: str          # stable id, e.g. "basics.variables"
    title: str        # shown in the menu
    topic: str        # category name, e.g. "Basics"
    show: Callable[[], None]
    quiz: list[QuizQuestion] = field(default_factory=list)
