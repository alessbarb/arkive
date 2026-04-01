"""Snapshot payload and metadata repository helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from arkive.domain.snapshot import SnapshotRecord
from arkive.errors import RepositoryError
from arkive.utils.jsonio import read_json_file, write_json_file


def get_manifest_file(metadata_dir: Path, snapshot_id: str) -> Path:
    """Return the manifest metadata file for a snapshot."""
    return metadata_dir / f"{snapshot_id}.manifest.json"


def read_manifest(metadata_dir: Path, snapshot_id: str) -> dict[str, Any]:
    """Read snapshot manifest metadata."""
    payload = read_json_file(get_manifest_file(metadata_dir, snapshot_id))
    if not isinstance(payload, dict):
        raise RepositoryError("Snapshot manifest must be a JSON object")
    return payload


def write_manifest(
    metadata_dir: Path,
    snapshot_id: str,
    payload: dict[str, Any],
) -> Path:
    """Persist snapshot manifest metadata."""
    path = get_manifest_file(metadata_dir, snapshot_id)
    write_json_file(path, payload)
    return path


def find_snapshot(records: list[SnapshotRecord], snapshot_id: str) -> SnapshotRecord:
    """Find a snapshot record by id."""
    for record in records:
        if record.snapshot_id == snapshot_id:
            return record
    raise RepositoryError(f"Snapshot not found: {snapshot_id}")
