"""Archive construction for snapshot payloads."""

from __future__ import annotations

import fnmatch
import tarfile
from collections.abc import Iterable
from pathlib import Path
from typing import Literal

from arkive.constants import DEFAULT_EXCLUDES
from arkive.errors import SnapshotError

TarWriteMode = Literal["w", "w:gz", "w:xz"]


def _should_exclude(relative_path: str, name: str, patterns: Iterable[str]) -> bool:
    parts = relative_path.split("/") if relative_path else [name]

    for pattern in patterns:
        if fnmatch.fnmatch(name, pattern):
            return True
        if fnmatch.fnmatch(relative_path, pattern):
            return True
        if any(fnmatch.fnmatch(part, pattern) for part in parts):
            return True

    return False


def _tar_mode(compression: str) -> TarWriteMode:
    mapping: dict[str, TarWriteMode] = {
        "gzip": "w:gz",
        "xz": "w:xz",
        "none": "w",
    }

    try:
        return mapping[compression]
    except KeyError as exc:
        raise SnapshotError(f"Unsupported compression mode: {compression}") from exc


def create_archive(
    source_dir: Path,
    target_file: Path,
    compression: str,
    exclude_patterns: list[str] | None = None,
) -> None:
    """Create a snapshot archive from a directory."""
    patterns = exclude_patterns or list(DEFAULT_EXCLUDES)

    try:
        with tarfile.open(name=target_file, mode=_tar_mode(compression)) as tar:
            root_info = tar.gettarinfo(str(source_dir), arcname=source_dir.name)
            tar.addfile(root_info)

            for path in sorted(source_dir.rglob("*")):
                relative = path.relative_to(source_dir).as_posix()

                if _should_exclude(relative, path.name, patterns):
                    continue

                arcname = f"{source_dir.name}/{relative}"

                if path.is_dir():
                    tar_info = tar.gettarinfo(str(path), arcname=arcname)
                    tar.addfile(tar_info)
                    continue

                if path.is_file():
                    tar_info = tar.gettarinfo(str(path), arcname=arcname)
                    with path.open("rb") as handle:
                        tar.addfile(tar_info, handle)
    except (tarfile.TarError, OSError) as exc:
        raise SnapshotError("Failed to create archive") from exc


def extract_archive(archive_file: Path, destination_dir: Path) -> None:
    """Extract an archive into a destination directory."""
    try:
        with tarfile.open(archive_file, "r:*") as tar:
            tar.extractall(path=destination_dir, filter="data")
    except (tarfile.TarError, OSError) as exc:
        raise SnapshotError("Failed to extract archive") from exc
