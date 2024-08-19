"""
File:        tests/test_cli.py
Author:      Neal Joslin
Date:        2024-08-17
Email:       neal@joslin.io
Description: cli tests
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ruff_quickfix.cli import cli

from .temp_file import create_temp_file, get_file_messages

if TYPE_CHECKING:  # pragma: no cover
    from pathlib import Path

    from click.testing import CliRunner


def test_cli_file_single(tmp_path: Path, cli_runner: CliRunner) -> None:
    """
    Test linting a file

    Args:
        tmp_path (Path): test's temp dir
        cli_runner (CliRunner): click runner
    """
    file_path = create_temp_file(tmp_path, "test.py")
    result = cli_runner.invoke(cli, [file_path])
    assert result.exit_code == 0
    assert result.output == get_file_messages(file_path)


def test_cli_file_multiple(tmp_path: Path, cli_runner: CliRunner) -> None:
    """
    Test linting multiple files

    Args:
        tmp_path (Path): test's temp dir
        cli_runner (CliRunner): click runner
    """
    file_path_0 = create_temp_file(tmp_path, "test0.py")
    file_path_1 = create_temp_file(tmp_path, "test1.py")
    result = cli_runner.invoke(cli, [file_path_0, file_path_1])
    assert result.exit_code == 0
    assert result.output == (
        get_file_messages(file_path_0) + get_file_messages(file_path_1)
    )


def test_cli_single_directory(tmp_path: Path, cli_runner: CliRunner) -> None:
    """
    Test linting a directory

    Args:
        tmp_path (Path): test's temp dir
        cli_runner (CliRunner): click runner
    """
    file_path = create_temp_file(tmp_path, "test.py")
    result = cli_runner.invoke(cli, [str(tmp_path.resolve())])
    assert result.exit_code == 0
    assert result.output == get_file_messages(file_path)


def test_cli_multiple_directory(tmp_path: Path, cli_runner: CliRunner) -> None:
    """
    Test linting a directory with multiple files

    Args:
        tmp_path (Path): test's temp dir
        cli_runner (CliRunner): click runner
    """
    file_path_0 = create_temp_file(tmp_path, "test0.py")
    file_path_1 = create_temp_file(tmp_path, "test1.py")
    result = cli_runner.invoke(cli, [str(tmp_path.resolve())])
    assert result.exit_code == 0
    assert result.output == (
        get_file_messages(file_path_0) + get_file_messages(file_path_1)
    )


def test_cli_none(cli_runner: CliRunner) -> None:
    """
    Test no arguments

    Args:
        cli_runner (CliRunner): click runner
    """
    result = cli_runner.invoke(cli)
    assert result.exit_code == 0
    assert result.output == ""
