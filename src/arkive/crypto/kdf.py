"""Key derivation helpers."""

from __future__ import annotations

import os

from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

from arkive.errors import CryptoError


def generate_salt(size: int = 16) -> bytes:
    """Generate a cryptographic salt."""
    if size <= 0:
        raise CryptoError("Salt size must be greater than zero")
    return os.urandom(size)


def derive_key_from_passphrase(passphrase: str, salt: bytes, length: int = 32) -> bytes:
    """Derive an encryption key from a passphrase."""
    if not passphrase:
        raise CryptoError("Passphrase cannot be empty")
    if not salt:
        raise CryptoError("Salt cannot be empty")

    try:
        kdf = Scrypt(
            salt=salt,
            length=length,
            n=2**15,
            r=8,
            p=1,
        )
        return kdf.derive(passphrase.encode("utf-8"))
    except Exception as exc:  # pragma: no cover
        raise CryptoError("Failed to derive encryption key") from exc
