"""Claude Code adapter.

Claude Code is treated as a local coding agent. Authentication remains in the
user's Claude Code installation; no credentials are stored by Merge.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path


def execute(prompt: str, repo_root: Path) -> str:
    command = os.getenv("CLAUDE_CODE_COMMAND", "claude")
    result = subprocess.run(
        [command, "-p", prompt],
        cwd=repo_root,
        text=True,
        capture_output=True,
        timeout=1800,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Claude Code failed with exit code {result.returncode}: {result.stderr.strip()}"
        )
    return result.stdout
