"""Project status service."""

from __future__ import annotations

from pathlib import Path

from arkive.domain.status import StatusResult
from arkive.errors import UsageError
from arkive.repository.index_repository import read_snapshot_index
from arkive.repository.project_repository import is_initialized, read_binding, read_config


def run_status(repo_root: Path) -> StatusResult:
    """Inspect arkive status for a repository."""
    try:
        resolved_repo_root = repo_root.expanduser().resolve(strict=True)
    except FileNotFoundError as exc:
        raise UsageError(f"Repository path does not exist: {repo_root}") from exc

    if not resolved_repo_root.is_dir():
        raise UsageError(f"Repository path is not a directory: {resolved_repo_root}")

    if not is_initialized(resolved_repo_root):
        return StatusResult(
            repo_root=str(resolved_repo_root),
            initialized=False,
            project_id=None,
            project_slug=None,
            ark_dir=None,
            vault_dir=None,
            snapshots_dir=None,
            snapshot_count=0,
            capture_mode=None,
            compression=None,
        )

    binding = read_binding(resolved_repo_root)
    config = read_config(resolved_repo_root)
    snapshot_count = len(read_snapshot_index(binding.vault_path))

    return StatusResult(
        repo_root=str(resolved_repo_root),
        initialized=True,
        project_id=binding.project_id,
        project_slug=binding.project_slug,
        ark_dir=str(binding.ark_path),
        vault_dir=str(binding.vault_path),
        snapshots_dir=str(binding.snapshots_path),
        snapshot_count=snapshot_count,
        capture_mode=str(config.capture.get("mode")),
        compression=str(config.capture.get("compression")),
    )
