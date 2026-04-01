"""Helpers for local project identity."""

from __future__ import annotations

import hashlib
from pathlib import Path


def project_id_from_path(path: Path) -> str:
    """Derive a stable local project identifier from a repository path."""
    digest = hashlib.sha256(str(path).encode("utf-8")).hexdigest()
    return digest[:12]
