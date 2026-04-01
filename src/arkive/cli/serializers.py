"""CLI serialization helpers."""

from __future__ import annotations

import json
from typing import Any


def to_pretty_json(payload: Any) -> str:
    """Serialize a payload to pretty JSON."""
    return json.dumps(payload, indent=2, sort_keys=True)
