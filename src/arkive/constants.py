"""Project-wide constants."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

# -----------------------------------------
# App identity
# -----------------------------------------

APP_NAME = "arkive"

try:
    APP_VERSION = version("arkive")
except PackageNotFoundError:
    APP_VERSION = "0.0.0-dev"

# -----------------------------------------
# Paths / structure
# -----------------------------------------

ARK_DIR_NAME = ".ark"
BINDING_FILE_NAME = "binding.json"
CONFIG_FILE_NAME = "config.json"
INDEX_FILE_NAME = "index.json"

VAULT_DIR_NAME = "vault"
SNAPSHOTS_DIR_NAME = "snapshots"
METADATA_DIR_NAME = "metadata"

FORMAT_VERSION = 1
DEFAULT_CAPTURE_MODE = "workspace"
DEFAULT_COMPRESSION = "gzip"

DEFAULT_EXCLUDES: tuple[str, ...] = (
    ".git",
    ".ark",
    "__pycache__",
    "*.pyc",
    ".venv",
    "node_modules",
)

DEFAULT_CONFIG = {
    "format_version": FORMAT_VERSION,
    "capture": {
        "mode": DEFAULT_CAPTURE_MODE,
        "compression": DEFAULT_COMPRESSION,
        "exclude_patterns": list(DEFAULT_EXCLUDES),
        "include_patterns": [],
    },
    "encryption": {
        "kdf": "scrypt",
        "cipher": "aes-256-gcm",
    },
}


def get_default_data_dir() -> Path:
    """Return the default application data directory."""
    return Path.home() / ".local" / "share" / APP_NAME


def get_default_vault_root() -> Path:
    """Return the default vault root directory."""
    return get_default_data_dir() / VAULT_DIR_NAME
