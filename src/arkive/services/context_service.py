"""Context resolution helpers for repository-aware commands."""

from __future__ import annotations

from pathlib import Path

from arkive.domain.project import ProjectBinding, ProjectConfig
from arkive.errors import UsageError
from arkive.repository.project_repository import is_initialized, read_binding, read_config
from arkive.utils.filesystem import resolve_existing_directory


def resolve_initialized_project(repo_root: Path) -> tuple[Path, ProjectBinding, ProjectConfig]:
    """Resolve and validate an initialized arkive project."""
    resolved_repo_root = resolve_existing_directory(repo_root, "Repository path")

    if not is_initialized(resolved_repo_root):
        raise UsageError(f"Repository is not initialized: {resolved_repo_root}")

    binding = read_binding(resolved_repo_root)
    config = read_config(resolved_repo_root)

    return resolved_repo_root, binding, config
