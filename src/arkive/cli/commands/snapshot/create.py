"""CLI command for snapshot creation."""

from __future__ import annotations

from pathlib import Path

from arkive.cli.helpers.arguments import REPO_PATH_ARGUMENT
from arkive.cli.helpers.io import echo_lines
from arkive.cli.presenters.snapshot_presenter import render_snapshot_create
from arkive.cli.prompts.passphrase_prompts import prompt_passphrase
from arkive.services.snapshot_create_service import run_snapshot_create


def snapshot_create_command(path: Path = REPO_PATH_ARGUMENT) -> None:
    """Create an encrypted snapshot."""
    passphrase = prompt_passphrase()
    result = run_snapshot_create(path, passphrase)
    echo_lines(render_snapshot_create(result))
