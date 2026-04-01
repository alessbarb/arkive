"""CLI command for repository status."""

from __future__ import annotations

from pathlib import Path

from arkive.cli.helpers.arguments import REPO_PATH_ARGUMENT
from arkive.cli.helpers.io import echo_lines
from arkive.cli.presenters.status_presenter import render_status
from arkive.services.status_service import run_status


def status_command(path: Path = REPO_PATH_ARGUMENT) -> None:
    """Show arkive status for a repository."""
    result = run_status(path)
    echo_lines(render_status(result))
