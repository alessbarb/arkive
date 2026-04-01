"""Status domain models."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class StatusResult(BaseModel):
    """Structured repository status."""

    model_config = ConfigDict(frozen=True)

    repo_root: str
    initialized: bool
    project_id: str | None
    project_slug: str | None
    ark_dir: str | None
    vault_dir: str | None
    snapshots_dir: str | None
    snapshot_count: int
    capture_mode: str | None
    compression: str | None
