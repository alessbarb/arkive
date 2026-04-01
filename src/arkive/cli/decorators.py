"""CLI decorators placeholder."""

from __future__ import annotations

from collections.abc import Callable
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def passthrough(command: Callable[P, R]) -> Callable[P, R]:
    """Return the command unchanged.

    Placeholder for future CLI decoration hooks.
    """
    return command
