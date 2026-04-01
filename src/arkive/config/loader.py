"""Project config loading."""

from __future__ import annotations

from pathlib import Path

from arkive.domain.project import ProjectConfig
from arkive.repository.project_repository import read_config


def load_project_config(repo_root: Path) -> ProjectConfig:
    """Load project configuration for a repository."""
    return read_config(repo_root)
