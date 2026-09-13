"""Session change tracking: files written this session + live git status.

The editor never commits; it only shows what changed.
"""
from __future__ import annotations

import subprocess
import threading
from pathlib import Path

from .vault import REPO_ROOT

_lock = threading.Lock()
_written: list[dict] = []  # [{path, action, at}]


def record_write(rel: str, action: str) -> None:
    import datetime
    with _lock:
        _written.append({"path": rel, "action": action,
                         "at": datetime.datetime.now().isoformat(timespec="seconds")})


def session_writes() -> list[dict]:
    with _lock:
        return list(_written)


def git_status() -> list[dict]:
    """git status --porcelain for source/content only."""
    try:
        out = subprocess.run(
            ["git", "status", "--porcelain", "--", "source/content"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=15,
        ).stdout
    except Exception:
        return []
    entries = []
    for line in out.splitlines():
        if not line.strip():
            continue
        status = line[:2].strip() or "??"
        path = line[3:].strip().strip('"')
        entries.append({"status": status, "path": path})
    return entries


def git_diff_for(rel: str) -> str:
    """Unified diff of one vault file (vs HEAD), '' if clean."""
    spec = f":./source/content/{rel}"
    try:
        return subprocess.run(
            ["git", "diff", "HEAD", "--", spec],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=15,
        ).stdout
    except Exception:
        return ""
