"""CLI callback helpers."""

from __future__ import annotations

import typer


def abort_callback() -> None:
    """Abort the current CLI flow."""
    raise typer.Abort()
