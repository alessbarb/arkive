"""CLI command for project initialization."""

from __future__ import annotations

from pathlib import Path

from arkive.cli.helpers.arguments import REPO_PATH_ARGUMENT
from arkive.cli.helpers.io import echo_lines
from arkive.services.init_service import run_init


def init_command(path: Path = REPO_PATH_ARGUMENT) -> None:
    """Initialize arkive for a repository."""
    result = run_init(path)

    echo_lines(
        [
            "Initialized project",
            f"Repository:   {result.repo_root}",
            f"Project ID:   {result.project_id}",
            f"Project slug: {result.project_slug}",
            f".ark dir:     {result.ark_dir}",
            f"Vault:        {result.vault_dir}",
        ]
    )
