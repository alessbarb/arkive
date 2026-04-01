"""Project config writing."""

from __future__ import annotations

from pathlib import Path

from arkive.domain.project import ProjectConfig
from arkive.repository.project_repository import write_config


def persist_project_config(repo_root: Path, config: ProjectConfig) -> None:
    """Persist project configuration for a repository."""
    write_config(repo_root, config)
