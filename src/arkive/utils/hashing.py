"""Hashing helpers."""

from __future__ import annotations

import hashlib
from pathlib import Path

from arkive.errors import RepositoryError


def sha256_bytes(payload: bytes) -> str:
    """Return the SHA256 hex digest of bytes."""
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    """Return the SHA256 hex digest of a file."""
    digest = hashlib.sha256()

    try:
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    except OSError as exc:
        raise RepositoryError(f"Failed to hash file: {path}") from exc

    return digest.hexdigest()
