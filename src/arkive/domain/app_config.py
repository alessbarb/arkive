"""Application-level config models."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class AppConfig(BaseModel):
    """Minimal application configuration model."""

    model_config = ConfigDict(frozen=True)

    app_name: str
    version: str
