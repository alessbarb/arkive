"""Masking helpers for sensitive output."""

from __future__ import annotations


def mask_value(value: str, visible_prefix: int = 2, visible_suffix: int = 2) -> str:
    """Mask a value while keeping a small prefix and suffix visible."""
    if not value:
        return ""

    if len(value) <= visible_prefix + visible_suffix:
        return "*" * len(value)

    prefix = value[:visible_prefix]
    suffix = value[-visible_suffix:]
    middle = "*" * (len(value) - visible_prefix - visible_suffix)
    return f"{prefix}{middle}{suffix}"
