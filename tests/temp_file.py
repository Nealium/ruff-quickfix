"""
File:        tests/temp_file.py
Author:      Neal Joslin
Date:        2024-08-17
Email:       neal@joslin.io
Description: temporary file to lint
"""

from __future__ import annotations

from pathlib import Path

FILE_CONTENTS = """
def main():
    a = True
    c = True
    print(b + a == 1)
"""

# NOTE: it needs the file path prepended and is missing the first item
FILE_MESSAGES = [
    ":1:1:e:Missing docstring in public module [D100]",
    ":2:5:e:Missing return type annotation for public function `main` [ANN201]",
    ":2:5:e:Missing docstring in public function [D103]",
    ":4:5:e:Local variable `c` is assigned to but never used [F841]",
    ":5:5:e:`print` found [T201]",
    ":5:11:e:Undefined name `b` [F821]\n",
]


def create_temp_file(tmp_path: Path, file_name: str) -> str:
    """
    Create temporary file that will be linted

    Args:
        tmp_path (Path): test's temp dir
        file_name (str): file name

    Returns:
        file path (str)
    """
    """TMP"""
    file_path = tmp_path / file_name
    with Path.open(file_path, "w") as f:
        f.write(FILE_CONTENTS)
    return str(file_path.resolve())


def get_file_messages(file_path: str) -> str:
    """
    Create temporary file linting messages

    Args:
        file_path (str): path to file

    Returns:
        all linting messages (str)
    """
    return "\n".join(
        [
            f"{file_path}{m}"
            for m in [
                (
                    f":1:1:e:File `{file_path}` is part of an implicit "
                    "namespace package. Add an `__init__.py`. [INP001]"
                ),
                *FILE_MESSAGES,
            ]
        ]
    )
