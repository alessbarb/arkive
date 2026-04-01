"""Restore domain models."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class RestoreResult(BaseModel):
    """Structured restore result."""

    model_config = ConfigDict(frozen=True)

    snapshot_id: str
    destination_dir: str
    restored: bool
