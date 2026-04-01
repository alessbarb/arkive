"""Snapshot listing service."""

from __future__ import annotations

from pathlib import Path

from arkive.domain.snapshot import SnapshotListItem
from arkive.repository.index_repository import read_snapshot_index
from arkive.services.context_service import resolve_initialized_project


def run_snapshot_list(repo_root: Path) -> list[SnapshotListItem]:
    """List available snapshots for a repository."""
    _, binding, _ = resolve_initialized_project(repo_root)
    records = read_snapshot_index(binding.vault_path)

    return [
        SnapshotListItem(
            snapshot_id=record.snapshot_id,
            created_at=record.created_at,
            capture_mode=record.capture_mode,
            compression=record.compression,
            payload_size=record.payload_size,
        )
        for record in records
    ]
