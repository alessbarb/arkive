"""Domain models for project identity and binding."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class ProjectBinding(BaseModel):
    """Repository-local binding between a project and its vault."""

    model_config = ConfigDict(frozen=True, str_strip_whitespace=True)

    format_version: int = Field(ge=1)
    project_id: str = Field(min_length=1)
    project_slug: str = Field(min_length=1)
    source_dir: str = Field(min_length=1)
    ark_dir: str = Field(min_length=1)
    vault_dir: str = Field(min_length=1)
    snapshots_dir: str = Field(min_length=1)
    metadata_dir: str = Field(min_length=1)

    @property
    def source_path(self) -> Path:
        """Return the bound repository path."""
        return Path(self.source_dir)

    @property
    def ark_path(self) -> Path:
        """Return the repository-local ark directory."""
        return Path(self.ark_dir)

    @property
    def vault_path(self) -> Path:
        """Return the bound vault directory."""
        return Path(self.vault_dir)

    @property
    def snapshots_path(self) -> Path:
        """Return the bound snapshots directory."""
        return Path(self.snapshots_dir)

    @property
    def metadata_path(self) -> Path:
        """Return the bound metadata directory."""
        return Path(self.metadata_dir)


class ProjectConfig(BaseModel):
    """Repository-local project configuration."""

    model_config = ConfigDict(frozen=True)

    format_version: int = Field(ge=1)
    capture: dict[str, Any]
    encryption: dict[str, Any]
