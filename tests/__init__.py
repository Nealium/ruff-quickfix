"""
File:        tests/__init__.py
Author:      Neal Joslin
Date:        2024-08-17
Email:       neal@joslin.io
Description: tests using pytest
"""

from .test_cli import (
    test_cli_file_multiple,
    test_cli_file_single,
    test_cli_multiple_directory,
    test_cli_none,
    test_cli_single_directory,
)

__all__ = [
    "test_cli_file_multiple",
    "test_cli_file_single",
    "test_cli_multiple_directory",
    "test_cli_none",
    "test_cli_single_directory",
]
