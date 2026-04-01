"""Application error hierarchy for arkive."""

from __future__ import annotations


class ArkiveError(Exception):
    """Base application error."""


class UsageError(ArkiveError):
    """Raised for invalid user input or invalid local state."""


class ConfigurationError(ArkiveError):
    """Raised when configuration or binding state is invalid."""


class RepositoryError(ArkiveError):
    """Raised for persistence and repository access failures."""


class SnapshotError(ArkiveError):
    """Raised for snapshot lifecycle failures."""


class RestoreError(ArkiveError):
    """Raised for restore lifecycle failures."""


class CryptoError(ArkiveError):
    """Raised for encryption or passphrase handling failures."""
