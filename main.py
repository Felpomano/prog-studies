"""Python Fundamentals Tutor

An interactive, menu-driven command-line program that teaches the core
fundamentals of Python: variables & types, operators, strings, control
flow, data structures, functions, error handling, file I/O, OOP, modules,
and iterators/generators/decorators.

Every lesson runs real, executed example code (not just printed text) and
ends with a short quiz. Progress is saved to progress.json next to this
file, so you can pick up where you left off.

Run it with:
    python main.py
"""
import sys

import progress
from lessons import ALL_LESSONS
from models import Lesson
from ui import clear_screen, header, rule, pause, ask


def lesson_status(data: dict, lesson: Lesson) -> str:
    done = lesson.key in data["completed"]
    score = data["quiz_scores"].get(lesson.key)
    mark = "x" if done else " "
    score_text = f" ({score[0]}/{score[1]})" if score else ""
    return f"[{mark}]{score_text}"


def print_menu(data: dict) -> None:
    clear_screen()
    header("PYTHON FUNDAMENTALS TUTOR")
    total = len(ALL_LESSONS)
    done = len(data["completed"])
    print(f"Progress: {done}/{total} lessons completed\n")

    current_topic = None
    for idx, lesson in enumerate(ALL_LESSONS, start=1):
        if lesson.topic != current_topic:
            current_topic = lesson.topic
            print(f"\n{current_topic}:")
        status = lesson_status(data, lesson)
        print(f"  {idx:2d}. {status} {lesson.title}")

    rule()
    print("Enter a lesson number to study it.")
    print("  a = run every lesson in order   p = show progress   r = reset progress   q = quit")
    rule()


def run_quiz(lesson: Lesson, data: dict) -> None:
    if not lesson.quiz:
        return
    rule()
    print(f"Quick quiz: {lesson.title}  ({len(lesson.quiz)} questions, Enter to skip)")
    correct = 0
    for i, q in enumerate(lesson.quiz, start=1):
        print(f"\n{i}. {q.question}")
        for opt_idx, option in enumerate(q.options):
            print(f"   {opt_idx + 1}. {option}")
        choice = ask("Your answer (number, or Enter to skip): ")
        if not choice:
            print("   (skipped)")
            continue
        try:
            picked = int(choice) - 1
        except ValueError:
            picked = -1
        if picked == q.answer:
            correct += 1
            print("   Correct!")
        else:
            print(f"   Not quite. Correct answer: {q.answer + 1}. {q.options[q.answer]}")
        if q.explanation:
            print(f"   Why: {q.explanation}")

    print(f"\nScore: {correct}/{len(lesson.quiz)}")
    progress.record_quiz(data, lesson.key, correct, len(lesson.quiz))


def run_lesson(lesson: Lesson, data: dict) -> None:
    clear_screen()
    header(lesson.title)
    lesson.show()
    progress.mark_complete(data, lesson.key)
    pause("Press Enter for the quiz...")
    run_quiz(lesson, data)
    pause()


def run_all(data: dict) -> None:
    for lesson in ALL_LESSONS:
        run_lesson(lesson, data)


def show_progress(data: dict) -> None:
    clear_screen()
    header("Your Progress")
    for lesson in ALL_LESSONS:
        status = lesson_status(data, lesson)
        print(f"  {status} {lesson.title}  ({lesson.topic})")
    total_correct = sum(v[0] for v in data["quiz_scores"].values())
    total_questions = sum(v[1] for v in data["quiz_scores"].values())
    if total_questions:
        print(f"\nOverall quiz score: {total_correct}/{total_questions}")
    pause()


def main() -> None:
    data = progress.load()
    lessons_by_number = {i: lesson for i, lesson in enumerate(ALL_LESSONS, start=1)}

    while True:
        print_menu(data)
        choice = ask("> ").lower()

        if choice in ("q", "quit", "exit"):
            print("Happy coding!")
            sys.exit(0)
        elif choice == "a":
            run_all(data)
        elif choice == "p":
            show_progress(data)
        elif choice == "r":
            confirm = ask("Reset all progress? This cannot be undone (y/N): ")
            if confirm.lower() == "y":
                progress.reset(data)
        elif choice.isdigit() and int(choice) in lessons_by_number:
            run_lesson(lessons_by_number[int(choice)], data)
        else:
            print("Unrecognized choice.")
            pause()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)
