"""Filesystem adapter helpers."""

from __future__ import annotations

from pathlib import Path


def path_exists(path: Path) -> bool:
    """Return whether a path exists."""
    return path.exists()
