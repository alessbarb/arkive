"""Small JSON I/O helpers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from arkive.errors import RepositoryError


def read_json_file(path: Path) -> Any:
    """Read JSON content from a file."""
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError as exc:
        raise RepositoryError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RepositoryError(f"Invalid JSON file: {path}") from exc
    except OSError as exc:
        raise RepositoryError(f"Failed to read file: {path}") from exc


def write_json_file(path: Path, payload: Any) -> None:
    """Write JSON content to a file."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="\n") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
    except OSError as exc:
        raise RepositoryError(f"Failed to write file: {path}") from exc
