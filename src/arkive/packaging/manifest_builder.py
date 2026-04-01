"""Manifest construction helpers."""

from __future__ import annotations

from typing import Any

from arkive.domain.project import ProjectBinding
from arkive.domain.snapshot import SnapshotRecord


def build_snapshot_manifest(
    binding: ProjectBinding,
    record: SnapshotRecord,
) -> dict[str, Any]:
    """Build a minimal snapshot manifest."""
    return {
        "format_version": record.format_version,
        "snapshot_id": record.snapshot_id,
        "project_id": binding.project_id,
        "project_slug": binding.project_slug,
        "source_dir": binding.source_dir,
        "created_at": record.created_at,
        "capture_mode": record.capture_mode,
        "compression": record.compression,
        "payload_path": record.payload_path,
        "payload_size": record.payload_size,
    }


def payload_filename(snapshot_id: str, compression: str) -> str:
    """Return the output filename for a snapshot payload."""
    extension = {
        "gzip": "tar.gz.enc",
        "xz": "tar.xz.enc",
        "none": "tar.enc",
    }[compression]
    return f"{snapshot_id}.{extension}"
