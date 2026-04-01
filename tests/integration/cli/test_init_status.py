from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from tests.support.cli import app


def test_init_then_status(runner: CliRunner, repo_dir: Path) -> None:
    init_result = runner.invoke(app, ["init", str(repo_dir)])
    assert init_result.exit_code == 0
    assert "Initialized project" in init_result.stdout
    assert "Project ID:" in init_result.stdout

    status_result = runner.invoke(app, ["status", str(repo_dir)])
    assert status_result.exit_code == 0
    assert "Repository:" in status_result.stdout
    assert "Initialized:  yes" in status_result.stdout
    assert "Snapshots:    0" in status_result.stdout


def test_status_uninitialized_repo(runner: CliRunner, repo_dir: Path) -> None:
    status_result = runner.invoke(app, ["status", str(repo_dir)])
    assert status_result.exit_code == 0
    assert "Initialized:  no" in status_result.stdout
