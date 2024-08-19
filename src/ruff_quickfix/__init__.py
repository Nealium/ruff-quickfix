"""
File:        ruff_quickfix/__init__.py
Author:      Neal Joslin
Date:        2024-08-17
Email:       neal@joslin.io
Description: Wrapper for the `ruff` linter for (neo)vim's quickfix
"""

from .cli import cli

__all__ = ["cli"]
