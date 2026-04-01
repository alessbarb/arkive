"""CLI command for snapshot restore."""

from __future__ import annotations

from pathlib import Path

from arkive.cli.helpers.arguments import (
    REPO_PATH_ARGUMENT,
    RESTORE_DESTINATION_ARGUMENT,
    SNAPSHOT_ID_ARGUMENT,
)
from arkive.cli.helpers.io import echo_lines
from arkive.cli.presenters.snapshot_presenter import render_snapshot_restore
from arkive.cli.prompts.passphrase_prompts import prompt_passphrase
from arkive.services.snapshot_restore_service import run_snapshot_restore


def snapshot_restore_command(
    snapshot_id: str = SNAPSHOT_ID_ARGUMENT,
    destination_dir: Path = RESTORE_DESTINATION_ARGUMENT,
    path: Path = REPO_PATH_ARGUMENT,
) -> None:
    """Restore a snapshot into an explicit destination."""
    passphrase = prompt_passphrase()
    result = run_snapshot_restore(path, snapshot_id, destination_dir, passphrase)
    echo_lines(render_snapshot_restore(result))
