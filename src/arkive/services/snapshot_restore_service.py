"""Snapshot restore service."""

from __future__ import annotations

import tempfile
from pathlib import Path

from arkive.crypto.envelope import decrypt_file
from arkive.crypto.passphrase import validate_passphrase
from arkive.domain.restore import RestoreResult
from arkive.packaging.archive_builder import extract_archive
from arkive.repository.index_repository import read_snapshot_index
from arkive.repository.snapshot_repository import find_snapshot
from arkive.services.context_service import resolve_initialized_project
from arkive.utils.filesystem import resolve_existing_directory


def run_snapshot_restore(
    repo_root: Path, snapshot_id: str, destination_dir: Path, passphrase: str
) -> RestoreResult:
    """Restore a snapshot into an explicit destination directory."""
    _, binding, _ = resolve_initialized_project(repo_root)
    resolved_destination_dir = resolve_existing_directory(destination_dir, "Destination directory")
    normalized_passphrase = validate_passphrase(passphrase)

    records = read_snapshot_index(binding.vault_path)
    record = find_snapshot(records, snapshot_id)

    with tempfile.TemporaryDirectory(prefix="arkive-restore-") as tmp_dir_name:
        tmp_dir = Path(tmp_dir_name)
        archive_name = Path(record.payload_path).name.removesuffix(".enc")
        archive_path = tmp_dir / archive_name

        decrypt_file(Path(record.payload_path), archive_path, normalized_passphrase)
        extract_archive(archive_path, resolved_destination_dir)

    return RestoreResult(
        snapshot_id=record.snapshot_id,
        destination_dir=str(resolved_destination_dir),
        restored=True,
    )
