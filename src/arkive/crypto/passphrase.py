"""Passphrase validation helpers."""

from __future__ import annotations

from arkive.errors import CryptoError


def validate_passphrase(passphrase: str) -> str:
    """Validate and normalize a passphrase."""
    normalized = passphrase.strip()
    if not normalized:
        raise CryptoError("Passphrase cannot be empty")
    return normalized
