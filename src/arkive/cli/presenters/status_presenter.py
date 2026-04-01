"""Status presenter helpers."""

from __future__ import annotations

from arkive.domain.status import StatusResult

from .common import present_path


def render_status(result: StatusResult) -> list[str]:
    """Render repository status as terminal lines."""
    lines = [
        f"Repository:   {present_path(result.repo_root)}",
        f"Initialized:  {'yes' if result.initialized else 'no'}",
    ]

    if not result.initialized:
        return lines

    lines.extend(
        [
            f"Project ID:   {result.project_id}",
            f"Project slug: {result.project_slug}",
            f".ark dir:     {present_path(result.ark_dir or '')}",
            f"Vault:        {present_path(result.vault_dir or '')}",
            f"Snapshots:    {result.snapshot_count}",
            f"Mode:         {result.capture_mode}",
            f"Compression:  {result.compression}",
        ]
    )
    return lines
