"""Configuration defaults."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from arkive.constants import DEFAULT_CONFIG


def get_default_config_payload() -> dict[str, Any]:
    """Return a deep copy of the default project config payload."""
    return deepcopy(DEFAULT_CONFIG)
