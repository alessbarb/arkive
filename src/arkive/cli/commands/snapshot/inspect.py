"""CLI command for snapshot inspection."""

from __future__ import annotations

from pathlib import Path

import typer

from arkive.cli.helpers.arguments import REPO_PATH_ARGUMENT, SNAPSHOT_ID_ARGUMENT
from arkive.cli.serializers import to_pretty_json
from arkive.services.snapshot_inspect_service import run_snapshot_inspect


def snapshot_inspect_command(
    snapshot_id: str = SNAPSHOT_ID_ARGUMENT,
    path: Path = REPO_PATH_ARGUMENT,
) -> None:
    """Inspect a snapshot and its manifest metadata."""
    result = run_snapshot_inspect(path, snapshot_id)

    typer.echo("Snapshot record:")
    typer.echo(to_pretty_json(result.record.model_dump()))
    typer.echo("")
    typer.echo("Manifest:")
    typer.echo(to_pretty_json(result.manifest))
