"""
File:        ruff_quickfix/cli
Author:      Neal Joslin
Date:        2024-08-17
Email:       neal@joslin.io
Description: cli commands
"""

from __future__ import annotations

import click

from .lint import lint


@click.command()
@click.argument("targets", nargs=-1)
def cli(targets: list[str]) -> None:
    """Ruff wrapper for (neo)vim's quickfix"""
    if not len(targets):
        msg = "No targets"
        raise click.UsageError(msg)
    for path in targets:
        lint(path)
