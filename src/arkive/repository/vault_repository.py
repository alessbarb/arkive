"""Vault layout helpers."""

from __future__ import annotations

from arkive.constants import INDEX_FILE_NAME
from arkive.domain.project import ProjectBinding
from arkive.domain.vault import VaultLayout


def build_vault_layout(binding: ProjectBinding) -> VaultLayout:
    """Build a structured vault layout description from a binding."""
    return VaultLayout(
        vault_dir=str(binding.vault_path),
        snapshots_dir=str(binding.snapshots_path),
        metadata_dir=str(binding.metadata_path),
        index_file=str(binding.vault_path / INDEX_FILE_NAME),
    )
