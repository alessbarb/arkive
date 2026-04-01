"""Top-level Typer application."""

from __future__ import annotations

import typer

from arkive.constants import APP_NAME, APP_VERSION
from arkive.errors import ArkiveError, UsageError

from .commands.init.command import init_command
from .commands.snapshot.app import snapshot_app
from .commands.status.command import status_command

app = typer.Typer(
    name=APP_NAME,
    help="Local-first encrypted snapshot tool for private workspace state.",
    add_completion=False,
    no_args_is_help=True,
)


def version_callback(value: bool) -> None:
    """Print version information and exit."""
    if not value:
        return
    typer.echo(f"{APP_NAME} {APP_VERSION}")
    raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        help="Show application version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """Arkive command line interface."""


app.command("init")(init_command)
app.command("status")(status_command)
app.add_typer(snapshot_app, name="snapshot")


def run() -> None:
    """Run the CLI application with consistent error boundaries."""
    try:
        app()
    except UsageError as exc:
        typer.echo(f"Error: {exc}", err=True)
        raise typer.Exit(code=2) from exc
    except ArkiveError as exc:
        typer.echo(f"Error: {exc}", err=True)
        raise typer.Exit(code=1) from exc
    except KeyboardInterrupt:
        typer.echo("Interrupted.", err=True)
        raise typer.Exit(code=130) from None


if __name__ == "__main__":
    run()
