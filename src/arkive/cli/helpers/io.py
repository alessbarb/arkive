"""Small CLI output helpers."""

from __future__ import annotations

from collections.abc import Iterable

import typer


def echo_line(line: str = "") -> None:
    """Render one line to stdout."""
    typer.echo(line)


def echo_lines(lines: Iterable[str]) -> None:
    """Render a sequence of lines to stdout."""
    for line in lines:
        typer.echo(line)
