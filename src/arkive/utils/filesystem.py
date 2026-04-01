"""Filesystem helpers."""

from __future__ import annotations

import os
from contextlib import suppress
from pathlib import Path

from arkive.errors import UsageError


def ensure_dir(path: Path, *, mode: int = 0o700) -> Path:
    """Create a directory if needed and try to apply restrictive permissions."""
    path.mkdir(parents=True, exist_ok=True)
    with suppress(OSError):
        path.chmod(mode)
    return path


def ensure_file(path: Path, content: str = "", *, mode: int = 0o600) -> Path:
    """Create a file if it does not exist using restrictive permissions."""
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
        fd = os.open(path, flags, mode)
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
    else:
        with suppress(OSError):
            path.chmod(mode)

    return path


def is_world_writable(path: Path) -> bool:
    """Return whether a path is world-writable when POSIX permissions are available."""
    try:
        mode = path.stat().st_mode
    except OSError:
        return False
    return bool(mode & 0o002)


def resolve_existing_directory(path: Path, label: str) -> Path:
    """Resolve and validate an existing directory."""
    try:
        resolved = path.expanduser().resolve(strict=True)
    except FileNotFoundError as exc:
        raise UsageError(f"{label} does not exist: {path}") from exc

    if not resolved.is_dir():
        raise UsageError(f"{label} is not a directory: {resolved}")

    return resolved


def ensure_directory(path: Path) -> None:
    """Create a directory if missing."""
    path.mkdir(parents=True, exist_ok=True)


def ensure_writable_directory(path: Path, label: str) -> None:
    """Ensure a directory is writable."""
    if not path.is_dir():
        raise UsageError(f"{label} is not a directory: {path}")
    if not os.access(path, os.W_OK):
        raise UsageError(f"{label} is not writable: {path}")


def human_size(size: int) -> str:
    """Format a size in bytes into a compact human-readable string."""
    units = ("B", "KB", "MB", "GB", "TB")
    value = float(size)

    for unit in units:
        if value < 1024.0 or unit == units[-1]:
            if unit == "B":
                return f"{int(value)}{unit}"
            return f"{value:.1f}{unit}"
        value /= 1024.0

    return f"{size}B"
