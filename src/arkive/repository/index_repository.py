"""Snapshot index persistence."""

from __future__ import annotations

import json
from pathlib import Path

from arkive.constants import INDEX_FILE_NAME
from arkive.domain.snapshot import SnapshotRecord
from arkive.errors import RepositoryError


def get_index_file(vault_dir: Path) -> Path:
    """Return the snapshot index file path."""
    return vault_dir / INDEX_FILE_NAME


def read_snapshot_index(vault_dir: Path) -> list[SnapshotRecord]:
    """Read all snapshot records for a vault."""
    path = get_index_file(vault_dir)

    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except json.JSONDecodeError as exc:
        raise RepositoryError(f"Invalid snapshot index: {path}") from exc
    except OSError as exc:
        raise RepositoryError(f"Failed to read snapshot index: {path}") from exc

    if not isinstance(payload, list):
        raise RepositoryError(f"Snapshot index must be a list: {path}")

    return [SnapshotRecord.model_validate(item) for item in payload]


def write_snapshot_index(vault_dir: Path, records: list[SnapshotRecord]) -> None:
    """Persist the snapshot index."""
    path = get_index_file(vault_dir)

    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="\n") as handle:
            json.dump(
                [record.model_dump() for record in records],
                handle,
                indent=2,
                sort_keys=True,
            )
            handle.write("\n")
    except OSError as exc:
        raise RepositoryError(f"Failed to write snapshot index: {path}") from exc
