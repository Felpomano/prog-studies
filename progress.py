"""Persist which lessons are done and quiz scores between runs."""
import json
import os

PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "progress.json")


def load() -> dict:
    if not os.path.exists(PROGRESS_FILE):
        return {"completed": [], "quiz_scores": {}}
    with open(PROGRESS_FILE, "r", encoding="utf-8") as fh:
        try:
            data = json.load(fh)
        except json.JSONDecodeError:
            return {"completed": [], "quiz_scores": {}}
    data.setdefault("completed", [])
    data.setdefault("quiz_scores", {})
    return data


def save(data: dict) -> None:
    with open(PROGRESS_FILE, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)


def mark_complete(data: dict, lesson_key: str) -> None:
    if lesson_key not in data["completed"]:
        data["completed"].append(lesson_key)
    save(data)


def record_quiz(data: dict, lesson_key: str, correct: int, total: int) -> None:
    data["quiz_scores"][lesson_key] = [correct, total]
    save(data)


def reset(data: dict) -> None:
    data["completed"] = []
    data["quiz_scores"] = {}
    save(data)
