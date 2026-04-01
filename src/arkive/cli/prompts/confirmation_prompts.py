"""Simple confirmation prompts."""

from __future__ import annotations

import typer


def confirm_action(message: str, default: bool = False) -> bool:
    """Ask for a yes/no confirmation."""
    return typer.confirm(message, default=default)
