from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from tests.support.cli import app


def test_snapshot_list_after_create(runner: CliRunner, repo_dir: Path) -> None:
    assert runner.invoke(app, ["init", str(repo_dir)]).exit_code == 0

    create_result = runner.invoke(
        app,
        ["snapshot", "create", str(repo_dir)],
        input="secret-passphrase\n",
    )
    assert create_result.exit_code == 0

    list_result = runner.invoke(app, ["snapshot", "list", str(repo_dir)])
    assert list_result.exit_code == 0
    assert "No snapshots found." not in list_result.stdout
    assert "workspace" in list_result.stdout
