from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from tests.support.cli import app


def test_snapshot_create(runner: CliRunner, repo_dir: Path) -> None:
    init_result = runner.invoke(app, ["init", str(repo_dir)])
    assert init_result.exit_code == 0

    result = runner.invoke(app, ["snapshot", "create", str(repo_dir)])
    assert result.exit_code == 0
    assert "Snapshot created" in result.stdout
    assert "Snapshot ID:" in result.stdout
