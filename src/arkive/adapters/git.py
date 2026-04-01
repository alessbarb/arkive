"""Minimal Git-aware helpers."""

from __future__ import annotations

from pathlib import Path


def is_git_repository(path: Path) -> bool:
    """Return whether a path looks like a Git repository root."""
    return (path / ".git").exists()
