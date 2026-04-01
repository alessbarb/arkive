"""Repository-local project metadata access."""

from __future__ import annotations

from pathlib import Path

from arkive.constants import BINDING_FILE_NAME, CONFIG_FILE_NAME
from arkive.domain.project import ProjectBinding, ProjectConfig
from arkive.utils.jsonio import read_json_file, write_json_file
from arkive.utils.project_paths import ark_dir_for_repo


def get_ark_dir(repo_root: Path) -> Path:
    """Return the repository-local ark directory path."""
    return ark_dir_for_repo(repo_root)


def get_binding_file(repo_root: Path) -> Path:
    """Return the binding file path for a repository."""
    return get_ark_dir(repo_root) / BINDING_FILE_NAME


def get_config_file(repo_root: Path) -> Path:
    """Return the config file path for a repository."""
    return get_ark_dir(repo_root) / CONFIG_FILE_NAME


def is_initialized(repo_root: Path) -> bool:
    """Return whether the repository has an arkive binding."""
    return get_binding_file(repo_root).is_file()


def read_binding(repo_root: Path) -> ProjectBinding:
    """Read the project binding from the repository."""
    payload = read_json_file(get_binding_file(repo_root))
    return ProjectBinding.model_validate(payload)


def write_binding(repo_root: Path, binding: ProjectBinding) -> None:
    """Persist the project binding."""
    write_json_file(get_binding_file(repo_root), binding.model_dump())


def read_config(repo_root: Path) -> ProjectConfig:
    """Read the project configuration from the repository."""
    payload = read_json_file(get_config_file(repo_root))
    return ProjectConfig.model_validate(payload)


def write_config(repo_root: Path, config: ProjectConfig) -> None:
    """Persist the project configuration."""
    write_json_file(get_config_file(repo_root), config.model_dump())
