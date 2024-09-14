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
    from pytest_mock.plugin import MockerFixture

# Exit code constants
EXIT_SUCCESS = 0
EXIT_ERROR = 1
EXIT_MISUSE = 2


def test_cli_file_single(tmp_path: Path, cli_runner: CliRunner) -> None:
    """
    Test linting a file

    Args:
        tmp_path (Path): test's temp dir
        cli_runner (CliRunner): click runner
    """
    file_path = create_temp_file(tmp_path, "test.py")
    result = cli_runner.invoke(cli, [file_path])
    assert result.exit_code == EXIT_SUCCESS
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
    assert result.exit_code == EXIT_SUCCESS
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
    assert result.exit_code == EXIT_SUCCESS
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
    assert result.exit_code == EXIT_SUCCESS
    assert result.output == (
        get_file_messages(file_path_0) + get_file_messages(file_path_1)
    )


def test_cli_ruff_error(cli_runner: CliRunner, mocker: MockerFixture) -> None:
    """
    Test a ruff error

    Args:
        cli_runner (CliRunner): click runner
        mocker (MockerFixture): mock module interface
    """
    mock_stdout = mocker.MagicMock()
    mock_stdout.configure_mock(
        stderr=b"This is an error!\n\n",
        stdout=b"",
    )

    mock_run = mocker.patch("ruff_quickfix.lint.run")
    mock_run.return_value = mock_stdout

    result = cli_runner.invoke(cli, ["test"])

    assert result.exit_code == EXIT_ERROR
    msgs = [
        "test:0:0:e:ruff message",
        "ruff-quickfix:0:0:e:\u2001This is an error!",
    ]
    assert "\n".join(msgs) in result.output


def test_cli_decode_error(cli_runner: CliRunner, mocker: MockerFixture) -> None:
    """
    Test a json decode error

    Args:
        cli_runner (CliRunner): click runner
        mocker (MockerFixture): mock module interface
    """
    mock_stdout = mocker.MagicMock()
    mock_stdout.configure_mock(
        stderr=b"",
        stdout=b"This is a decode error!\n\n",
    )

    mock_run = mocker.patch("ruff_quickfix.lint.run")
    mock_run.return_value = mock_stdout

    result = cli_runner.invoke(cli, ["test"])

    assert result.exit_code == EXIT_ERROR
    msgs = [
        "test:0:0:e:ruff-quickfix decode error",
        "ruff-quickfix:0:0:e:\u2001This is a decode error!",
    ]
    assert "\n".join(msgs) in result.output


def test_cli_none(cli_runner: CliRunner) -> None:
    """
    Test no arguments

    Args:
        cli_runner (CliRunner): click runner
    """
    result = cli_runner.invoke(cli)
    assert result.exit_code == EXIT_MISUSE
    assert "Error: No targets" in result.output
