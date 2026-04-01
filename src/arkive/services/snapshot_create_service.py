"""Snapshot creation service."""

from __future__ import annotations

import tempfile
from pathlib import Path

from arkive.crypto.envelope import encrypt_file
from arkive.crypto.passphrase import validate_passphrase
from arkive.domain.snapshot import (
    CaptureMode,
    CompressionMode,
    SnapshotCreateResult,
    SnapshotRecord,
)
from arkive.errors import SnapshotError
from arkive.packaging.archive_builder import create_archive
from arkive.packaging.manifest_builder import build_snapshot_manifest, payload_filename
from arkive.repository.index_repository import read_snapshot_index, write_snapshot_index
from arkive.repository.snapshot_repository import write_manifest
from arkive.services.context_service import resolve_initialized_project
from arkive.utils.time import utc_now_compact, utc_now_iso


def _normalize_capture_mode(value: str) -> CaptureMode:
    allowed: set[str] = {"workspace", "untracked", "private"}
    if value not in allowed:
        raise SnapshotError(f"Unsupported capture mode: {value}")
    return value  # type: ignore[return-value]


def _normalize_compression(value: str) -> CompressionMode:
    allowed: set[str] = {"gzip", "xz", "none"}
    if value not in allowed:
        raise SnapshotError(f"Unsupported compression mode: {value}")
    return value  # type: ignore[return-value]


def run_snapshot_create(repo_root: Path, passphrase: str) -> SnapshotCreateResult:
    """Create a full encrypted snapshot for a repository."""
    repo_path, binding, config = resolve_initialized_project(repo_root)
    normalized_passphrase = validate_passphrase(passphrase)

    capture_mode = _normalize_capture_mode(str(config.capture.get("mode", "workspace")))
    compression = _normalize_compression(str(config.capture.get("compression", "gzip")))
    exclude_patterns = list(config.capture.get("exclude_patterns", []))

    snapshot_id = utc_now_compact()
    created_at = utc_now_iso()
    payload_name = payload_filename(snapshot_id=snapshot_id, compression=compression)
    payload_path = binding.snapshots_path / payload_name

    with tempfile.TemporaryDirectory(prefix="arkive-") as tmp_dir_name:
        tmp_dir = Path(tmp_dir_name)
        archive_name = payload_name.removesuffix(".enc")
        archive_path = tmp_dir / archive_name

        create_archive(
            source_dir=repo_path,
            target_file=archive_path,
            compression=compression,
            exclude_patterns=exclude_patterns,
        )
        encrypt_file(archive_path, payload_path, normalized_passphrase)

    if not payload_path.exists():
        raise SnapshotError(f"Encrypted snapshot was not created: {payload_path}")

    payload_size = payload_path.stat().st_size

    record = SnapshotRecord(
        format_version=1,
        snapshot_id=snapshot_id,
        project_id=binding.project_id,
        created_at=created_at,
        capture_mode=capture_mode,
        compression=compression,
        payload_path=str(payload_path),
        payload_size=payload_size,
    )

    manifest = build_snapshot_manifest(binding=binding, record=record)
    write_manifest(binding.metadata_path, snapshot_id, manifest)

    records = read_snapshot_index(binding.vault_path)
    records.append(record)
    records.sort(key=lambda item: item.created_at)
    write_snapshot_index(binding.vault_path, records)

    return SnapshotCreateResult(
        snapshot_id=record.snapshot_id,
        payload_path=record.payload_path,
        payload_size=record.payload_size,
        created_at=record.created_at,
        capture_mode=record.capture_mode,
        compression=record.compression,
    )
