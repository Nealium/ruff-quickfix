"""
File:        ruff_quickfix/lint.py
Author:      Neal Joslin
Date:        2024-08-21
Email:       neal@joslin.io
Description: Linting and formatting
"""

import json
import sys
from subprocess import run

import click


def lint(path: str) -> None:
    """
    Run ruff, filter out unusable lines and put into format that
    can be easily parsed by vim's `errorformat`

    Args:
        path (str): path to lint
    """
    cmd = f"RUFF_FORMAT=json RUFF_OUTPUT_FORMAT=json ruff check {path}"
    res = run(cmd, capture_output=True, shell=True, check=False)  # noqa: S602

    try:
        if res.stdout:
            parsed = json.loads(res.stdout)
            for e in parsed:
                click.echo(
                    f"{e['filename']}:"
                    f"{e['location']['row']}:"
                    f"{e['location']['column']}:"
                    "e:"
                    f"{e['message']} [{e['code']}]"
                )
    except json.JSONDecodeError:
        click.echo(f"{path}:0:0:e:ruff-quickfix decode error")
        for i in res.stdout.splitlines():
            if i:
                click.echo(f"ruff-quickfix:0:0:e:\u2001{i.decode('utf-8')}")
        sys.exit(1)
    finally:
        if res.stderr:
            click.echo(f"{path}:0:0:e:ruff message")
            for i in res.stderr.splitlines():
                if i:
                    click.echo(f"ruff-quickfix:0:0:e:\u2001{i.decode('utf-8')}")
            sys.exit(1)

