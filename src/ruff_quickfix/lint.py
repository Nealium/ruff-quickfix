"""
File:        ruff_quickfix/lint.py
Author:      Neal Joslin
Date:        2024-08-21
Email:       neal@joslin.io
Description: Linting and formatting
"""

import re
from subprocess import run

import click

RUFF_REGEX = (
    r"(?P<path>.*):(?P<line>\d+):(?P<col>\d+): "
    r"(?P<code>\S+) (?P<fixable>\[\*\] )*(?P<msg>.*)"
)


def lint(path: str) -> None:
    """
    Run ruff, filter out unusable lines and put into format that
    can be easily parsed by vim's `errorformat`

    Args:
        path (str): path to lint
    """
    cmd = f"ruff check {path} --output-format concise"
    data = run(cmd, capture_output=True, shell=True, check=False)  # noqa: S602
    output = data.stdout.splitlines()

    for line in output:
        result = re.search(RUFF_REGEX, line.decode("utf-8"))
        if result:
            click.echo(
                f"{result.group('path')}:"
                f"{result.group('line')}:"
                f"{result.group('col')}:"
                "e:"
                f"{result.group('msg')} [{result.group('code')}]"
            )
