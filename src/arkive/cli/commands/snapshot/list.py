"""CLI command for snapshot listing."""

from __future__ import annotations

from pathlib import Path

from arkive.cli.helpers.arguments import REPO_PATH_ARGUMENT
from arkive.cli.helpers.io import echo_lines
from arkive.cli.presenters.snapshot_presenter import render_snapshot_list
from arkive.services.snapshot_list_service import run_snapshot_list


def snapshot_list_command(path: Path = REPO_PATH_ARGUMENT) -> None:
    """List available snapshots."""
    items = run_snapshot_list(path)
    echo_lines(render_snapshot_list(items))
