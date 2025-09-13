"""
File:        ruff_quickfix/cli
Author:      Neal Joslin
Date:        2024-08-17
Email:       neal@joslin.io
Description: cli commands
"""

from __future__ import annotations

from pathlib import Path

import click

from .lint import lint


@click.command()
@click.version_option(package_name="ruff-quickfix")
@click.argument(
    "targets",
    nargs=-1,
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=True,
        path_type=Path,
    ),
)
def cli(targets: list[Path]) -> None:
    """Ruff wrapper for (neo)vim's quickfix"""
    if not len(targets):
        msg = "No targets"
        raise click.UsageError(msg)
    for path in targets:
        lint(path)
