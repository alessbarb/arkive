"""Time helpers."""

from __future__ import annotations

from datetime import datetime, timezone


def utc_now() -> datetime:
    """Return the current UTC datetime."""
    return datetime.now(timezone.utc)


def utc_now_iso() -> str:
    """Return the current UTC datetime in ISO-8601 format."""
    return utc_now().isoformat()


def utc_now_compact() -> str:
    """Return a compact UTC timestamp suitable for snapshot identifiers."""
    return utc_now().strftime("%Y%m%d-%H%M%S")
