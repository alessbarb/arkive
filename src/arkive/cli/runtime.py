"""CLI runtime helpers."""

from __future__ import annotations

from pathlib import Path


def resolve_cli_path(path: Path) -> Path:
    """Resolve a CLI path without enforcing existence."""
    return path.expanduser()
