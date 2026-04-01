"""Vault-related domain models."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class VaultLayout(BaseModel):
    """Structured vault layout description."""

    model_config = ConfigDict(frozen=True)

    vault_dir: str
    snapshots_dir: str
    metadata_dir: str
    index_file: str
