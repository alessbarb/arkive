from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from tests.support.cli import app


def _extract_snapshot_id(output: str) -> str:
    for line in output.splitlines():
        if line.startswith("Snapshot ID:"):
            return line.split(":", 1)[1].strip()
    raise AssertionError("Snapshot ID not found in output")


def test_snapshot_restore(runner: CliRunner, repo_dir: Path, restore_dir: Path) -> None:
    assert runner.invoke(app, ["init", str(repo_dir)]).exit_code == 0

    create_result = runner.invoke(app, ["snapshot", "create", str(repo_dir)])
    assert create_result.exit_code == 0
    snapshot_id = _extract_snapshot_id(create_result.stdout)

    restore_result = runner.invoke(
        app,
        ["snapshot", "restore", snapshot_id, str(restore_dir), str(repo_dir)],
    )
    assert restore_result.exit_code == 0
    assert "Snapshot restored" in restore_result.stdout

    restored_repo = restore_dir / repo_dir.name
    assert restored_repo.exists()
    assert (restored_repo / "README.md").exists()
    assert (restored_repo / "notes.txt").exists()
