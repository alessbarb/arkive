"""Snapshot presenter helpers."""

from __future__ import annotations

from arkive.domain.restore import RestoreResult
from arkive.domain.snapshot import SnapshotCreateResult, SnapshotListItem

from .common import present_path, present_size


def render_snapshot_create(result: SnapshotCreateResult) -> list[str]:
    """Render snapshot creation output."""
    return [
        "Snapshot created",
        "",
        f"Snapshot ID:  {result.snapshot_id}",
        f"Created at:   {result.created_at}",
        f"Mode:         {result.capture_mode}",
        f"Compression:  {result.compression}",
        f"File:         {present_path(result.payload_path)}",
        f"Size:         {present_size(result.payload_size)}",
    ]


def render_snapshot_list(items: list[SnapshotListItem]) -> list[str]:
    """Render snapshot list output."""
    if not items:
        return ["No snapshots found."]

    lines: list[str] = []
    for item in items:
        lines.append(
            " | ".join(
                [
                    item.snapshot_id,
                    item.created_at,
                    item.capture_mode,
                    item.compression,
                    present_size(item.payload_size),
                ]
            )
        )
    return lines


def render_snapshot_restore(result: RestoreResult) -> list[str]:
    """Render restore output."""
    return [
        "Snapshot restored",
        "",
        f"Snapshot ID:  {result.snapshot_id}",
        f"Destination:  {present_path(result.destination_dir)}",
    ]
