"""Common presenter helpers."""

from __future__ import annotations

from pathlib import Path

from arkive.utils.filesystem import human_size
from arkive.utils.tilde import tilde_path


def present_path(path: str) -> str:
    """Render a path for terminal output."""
    return tilde_path(Path(path))


def present_size(size: int) -> str:
    """Render a human-readable size string."""
    return human_size(size)
