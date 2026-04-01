"""Reusable CLI argument definitions."""

from __future__ import annotations

from pathlib import Path

import typer

DEFAULT_REPO_PATH = Path(".")

REPO_PATH_ARGUMENT = typer.Argument(
    DEFAULT_REPO_PATH,
    exists=False,
    file_okay=False,
    dir_okay=True,
    readable=True,
    resolve_path=False,
    help="Repository path.",
)

SNAPSHOT_ID_ARGUMENT = typer.Argument(
    ...,
    help="Snapshot identifier.",
)

RESTORE_DESTINATION_ARGUMENT = typer.Argument(
    ...,
    exists=False,
    file_okay=False,
    dir_okay=True,
    readable=True,
    resolve_path=False,
    help="Explicit restore destination directory.",
)
