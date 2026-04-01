"""Interactive passphrase prompts."""

from __future__ import annotations

import getpass

from arkive.crypto.passphrase import validate_passphrase
from arkive.errors import CryptoError


def prompt_passphrase(confirm: bool = False) -> str:
    """Prompt for a passphrase."""
    first = validate_passphrase(getpass.getpass("Passphrase: "))

    if not confirm:
        return first

    second = validate_passphrase(getpass.getpass("Confirm passphrase: "))
    if first != second:
        raise CryptoError("Passphrases do not match")

    return first
