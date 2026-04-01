"""Snapshot command group."""

from __future__ import annotations

import typer

from .create import snapshot_create_command
from .inspect import snapshot_inspect_command
from .list import snapshot_list_command
from .restore import snapshot_restore_command

snapshot_app = typer.Typer(
    help="Create, inspect, and restore snapshots.",
    no_args_is_help=True,
)

snapshot_app.command("create")(snapshot_create_command)
snapshot_app.command("list")(snapshot_list_command)
snapshot_app.command("inspect")(snapshot_inspect_command)
snapshot_app.command("restore")(snapshot_restore_command)
