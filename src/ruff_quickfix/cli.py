"""
File:        cli
Author:      Neal Joslin
Date:        2024-08-17
Email:       neal@joslin.io
Description: cli commands
"""

from __future__ import annotations

import click

from .main import lint


@click.command()
@click.argument("targets", nargs=-1)
def cli(targets: list[str]) -> None:
    """Ruff wrapper for (neo)vim's quickfix"""
    for path in targets:
        lint(path)


if __name__ == "__main__":  # pragma: no cover
    cli(obj={})
