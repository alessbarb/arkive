"""Tilde path helpers."""

from __future__ import annotations

from pathlib import Path


def tilde_path(path: Path) -> str:
    """Render a path using ~ when it is inside the home directory."""
    home = Path.home().resolve()
    resolved = path.resolve()

    try:
        relative = resolved.relative_to(home)
        return f"~/{relative}" if str(relative) != "." else "~"
    except ValueError:
        return str(resolved)


def to_tilde_path(path: Path) -> str:
    """Alias kept for compatibility with earlier helper naming."""
    return tilde_path(path)
