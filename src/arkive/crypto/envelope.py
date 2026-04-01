"""Authenticated encryption envelope helpers."""

from __future__ import annotations

import base64
import json
import os
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from arkive.crypto.kdf import derive_key_from_passphrase, generate_salt
from arkive.errors import CryptoError


def encrypt_bytes(payload: bytes, passphrase: str) -> bytes:
    """Encrypt raw bytes into a JSON envelope."""
    if not passphrase:
        raise CryptoError("Passphrase cannot be empty")

    salt = generate_salt()
    key = derive_key_from_passphrase(passphrase=passphrase, salt=salt)
    nonce = os.urandom(12)

    try:
        ciphertext = AESGCM(key).encrypt(nonce, payload, None)
    except Exception as exc:  # pragma: no cover
        raise CryptoError("Failed to encrypt payload") from exc

    envelope = {
        "v": 1,
        "kdf": "scrypt",
        "cipher": "aes-256-gcm",
        "salt": base64.b64encode(salt).decode("ascii"),
        "nonce": base64.b64encode(nonce).decode("ascii"),
        "ciphertext": base64.b64encode(ciphertext).decode("ascii"),
    }
    return json.dumps(envelope, separators=(",", ":")).encode("utf-8")


def decrypt_bytes(payload: bytes, passphrase: str) -> bytes:
    """Decrypt a JSON envelope into raw bytes."""
    if not passphrase:
        raise CryptoError("Passphrase cannot be empty")

    try:
        envelope = json.loads(payload.decode("utf-8"))
        salt = base64.b64decode(envelope["salt"])
        nonce = base64.b64decode(envelope["nonce"])
        ciphertext = base64.b64decode(envelope["ciphertext"])
        key = derive_key_from_passphrase(passphrase=passphrase, salt=salt)
        return AESGCM(key).decrypt(nonce, ciphertext, None)
    except Exception as exc:  # pragma: no cover
        raise CryptoError("Failed to decrypt payload") from exc


def encrypt_file(source: Path, target: Path, passphrase: str) -> None:
    """Encrypt a file into a target path."""
    try:
        plaintext = source.read_bytes()
        encrypted = encrypt_bytes(plaintext, passphrase=passphrase)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(encrypted)
    except OSError as exc:
        raise CryptoError(f"Failed to encrypt file: {source}") from exc


def decrypt_file(source: Path, target: Path, passphrase: str) -> None:
    """Decrypt a file into a target path."""
    try:
        encrypted = source.read_bytes()
        plaintext = decrypt_bytes(encrypted, passphrase=passphrase)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(plaintext)
    except OSError as exc:
        raise CryptoError(f"Failed to decrypt file: {source}") from exc
