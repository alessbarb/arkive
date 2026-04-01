from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def repo_dir(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    (repo / "README.md").write_text("# Test repo\n", encoding="utf-8")
    (repo / "notes.txt").write_text("private local note\n", encoding="utf-8")
    return repo


@pytest.fixture
def restore_dir(tmp_path: Path) -> Path:
    target = tmp_path / "restore"
    target.mkdir()
    return target


@pytest.fixture
def test_passphrase() -> str:
    return "test-passphrase"


@pytest.fixture(autouse=True)
def patch_getpass(monkeypatch: pytest.MonkeyPatch, test_passphrase: str) -> None:
    """Patch interactive passphrase prompts during tests only."""
    import getpass

    monkeypatch.setattr(getpass, "getpass", lambda _prompt="": test_passphrase)
