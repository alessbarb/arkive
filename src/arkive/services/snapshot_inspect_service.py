"""Snapshot inspection service."""

from __future__ import annotations

from pathlib import Path

from arkive.domain.snapshot import SnapshotInspectResult
from arkive.repository.index_repository import read_snapshot_index
from arkive.repository.snapshot_repository import find_snapshot, read_manifest
from arkive.services.context_service import resolve_initialized_project


def run_snapshot_inspect(repo_root: Path, snapshot_id: str) -> SnapshotInspectResult:
    """Inspect a snapshot and its manifest metadata."""
    _, binding, _ = resolve_initialized_project(repo_root)
    records = read_snapshot_index(binding.vault_path)
    record = find_snapshot(records, snapshot_id)
    manifest = read_manifest(binding.metadata_path, snapshot_id)

    return SnapshotInspectResult(record=record, manifest=manifest)
