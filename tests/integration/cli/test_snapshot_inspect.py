from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from tests.support.cli import app


def _extract_snapshot_id(output: str) -> str:
    for line in output.splitlines():
        if line.startswith("Snapshot ID:"):
            return line.split(":", 1)[1].strip()
    raise AssertionError("Snapshot ID not found in output")


def test_snapshot_inspect(runner: CliRunner, repo_dir: Path) -> None:
    assert runner.invoke(app, ["init", str(repo_dir)]).exit_code == 0

    create_result = runner.invoke(
        app,
        ["snapshot", "create", str(repo_dir)],
        input="secret-passphrase\n",
    )
    assert create_result.exit_code == 0
    snapshot_id = _extract_snapshot_id(create_result.stdout)

    inspect_result = runner.invoke(app, ["snapshot", "inspect", snapshot_id, str(repo_dir)])
    assert inspect_result.exit_code == 0
    assert "Snapshot record:" in inspect_result.stdout
    assert "Manifest:" in inspect_result.stdout
    assert snapshot_id in inspect_result.stdout
