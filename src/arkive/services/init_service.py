"""Project initialization service."""

from __future__ import annotations

from pathlib import Path
from typing import Any, cast

from pydantic import BaseModel, ConfigDict

from arkive.config.defaults import get_default_config_payload
from arkive.constants import (
    FORMAT_VERSION,
    METADATA_DIR_NAME,
    SNAPSHOTS_DIR_NAME,
    get_default_vault_root,
)
from arkive.domain.project import ProjectBinding, ProjectConfig
from arkive.errors import UsageError
from arkive.repository.project_repository import (
    get_ark_dir,
    is_initialized,
    write_binding,
    write_config,
)
from arkive.utils.project_ids import project_id_from_path
from arkive.utils.project_names import slugify_project_name


class InitResult(BaseModel):
    """Structured result for project initialization."""

    model_config = ConfigDict(frozen=True)

    repo_root: str
    ark_dir: str
    vault_dir: str
    project_id: str
    project_slug: str
    initialized: bool


def run_init(repo_root: Path) -> InitResult:
    """Initialize arkive metadata for a repository."""
    try:
        resolved_repo_root = repo_root.expanduser().resolve(strict=True)
    except FileNotFoundError as exc:
        raise UsageError(f"Repository path does not exist: {repo_root}") from exc

    if not resolved_repo_root.is_dir():
        raise UsageError(f"Repository path is not a directory: {resolved_repo_root}")

    if is_initialized(resolved_repo_root):
        raise UsageError(f"Repository is already initialized: {resolved_repo_root}")

    project_slug = slugify_project_name(resolved_repo_root.name)
    project_id = project_id_from_path(resolved_repo_root)

    ark_dir = get_ark_dir(resolved_repo_root)
    vault_dir = get_default_vault_root() / f"{project_slug}--{project_id}"
    snapshots_dir = vault_dir / SNAPSHOTS_DIR_NAME
    metadata_dir = vault_dir / METADATA_DIR_NAME

    ark_dir.mkdir(parents=True, exist_ok=False)
    snapshots_dir.mkdir(parents=True, exist_ok=True)
    metadata_dir.mkdir(parents=True, exist_ok=True)

    binding = ProjectBinding(
        format_version=FORMAT_VERSION,
        project_id=project_id,
        project_slug=project_slug,
        source_dir=str(resolved_repo_root),
        ark_dir=str(ark_dir),
        vault_dir=str(vault_dir),
        snapshots_dir=str(snapshots_dir),
        metadata_dir=str(metadata_dir),
    )

    config_payload = get_default_config_payload()
    capture = cast(dict[str, Any], config_payload["capture"])
    encryption = cast(dict[str, Any], config_payload["encryption"])

    config = ProjectConfig(
        format_version=FORMAT_VERSION,
        capture=capture,
        encryption=encryption,
    )

    write_binding(resolved_repo_root, binding)
    write_config(resolved_repo_root, config)

    return InitResult(
        repo_root=str(resolved_repo_root),
        ark_dir=str(ark_dir),
        vault_dir=str(vault_dir),
        project_id=project_id,
        project_slug=project_slug,
        initialized=True,
    )
