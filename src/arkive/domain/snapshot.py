"""Domain models for snapshot identity and metadata."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

CaptureMode = Literal["workspace", "untracked", "private"]
CompressionMode = Literal["gzip", "xz", "none"]


class SnapshotRecord(BaseModel):
    """Minimal snapshot index record."""

    model_config = ConfigDict(frozen=True, str_strip_whitespace=True)

    format_version: int = Field(ge=1)
    snapshot_id: str = Field(min_length=1)
    project_id: str = Field(min_length=1)
    created_at: str = Field(min_length=1)
    capture_mode: CaptureMode
    compression: CompressionMode
    payload_path: str = Field(min_length=1)
    payload_size: int = Field(ge=0)

    def payload_file(self) -> Path:
        """Return the payload file path."""
        return Path(self.payload_path)


class SnapshotCreateResult(BaseModel):
    """Result returned by snapshot creation workflows."""

    model_config = ConfigDict(frozen=True)

    snapshot_id: str
    payload_path: str
    payload_size: int
    created_at: str
    capture_mode: CaptureMode
    compression: CompressionMode


class SnapshotListItem(BaseModel):
    """Structured item used by presenters and serializers."""

    model_config = ConfigDict(frozen=True)

    snapshot_id: str
    created_at: str
    capture_mode: CaptureMode
    compression: CompressionMode
    payload_size: int


class SnapshotInspectResult(BaseModel):
    """Structured snapshot inspection result."""

    model_config = ConfigDict(frozen=True)

    record: SnapshotRecord
    manifest: dict[str, Any]
