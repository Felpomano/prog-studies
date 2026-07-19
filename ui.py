"""Small terminal presentation helpers used by every lesson.

Kept dependency-free (standard library only) so the tutor runs anywhere
Python runs, with no pip install step required.
"""
import os
import shutil
import textwrap

WIDTH = min(shutil.get_terminal_size(fallback=(88, 24)).columns, 100)


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def rule(char: str = "-") -> None:
    print(char * WIDTH)


def header(title: str) -> None:
    rule("=")
    print(title.center(WIDTH))
    rule("=")


def subheader(title: str) -> None:
    print()
    print(f"-- {title} --")


def info(text: str) -> None:
    paragraph = textwrap.dedent(text).strip("\n")
    for block in paragraph.split("\n\n"):
        wrapped = textwrap.fill(" ".join(block.split()), width=WIDTH)
        print(wrapped)
        print()


def code_block(code: str) -> None:
    print("  code:")
    for line in textwrap.dedent(code).strip("\n").splitlines():
        print(f"    | {line}")


def output_line(text: str = "") -> None:
    print(f"    > {text}")


def key_points(points: list[str]) -> None:
    print()
    print("  Key points:")
    for point in points:
        print(f"    * {point}")
    print()


def pause(message: str = "Press Enter to continue...") -> None:
    input(f"\n{message}")


def ask(prompt: str) -> str:
    return input(prompt).strip()
