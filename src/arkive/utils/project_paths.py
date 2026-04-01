"""Helpers for repository-local path calculations."""

from __future__ import annotations

from pathlib import Path

from arkive.constants import ARK_DIR_NAME


def ark_dir_for_repo(repo_root: Path) -> Path:
    """Return the .ark directory for a repository root."""
    return repo_root / ARK_DIR_NAME
