"""Adapters package."""

from arkive.adapters.filesystem import path_exists
from arkive.adapters.git import is_git_repository
from arkive.adapters.input import normalize_text_input

__all__ = [
    "is_git_repository",
    "normalize_text_input",
    "path_exists",
]
