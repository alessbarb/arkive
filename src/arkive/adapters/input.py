"""Input adapters."""

from __future__ import annotations


def normalize_text_input(value: str) -> str:
    """Normalize one text input value."""
    return value.strip()
