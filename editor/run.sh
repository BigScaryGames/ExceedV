#!/usr/bin/env bash
# Exceed Vault Editor — one-shot launcher.
# Builds the web UI if needed, creates the venv if needed, serves on
# http://127.0.0.1:8787 (localhost only).
set -euo pipefail
cd "$(dirname "$0")/.."

# ── python venv + deps ──────────────────────────────────────────────────────
if [ ! -x editor/.venv/bin/python ]; then
    echo "· creating editor/.venv"
    python3 -m venv editor/.venv
    editor/.venv/bin/pip install -q -r editor/server/requirements.txt
fi
if ! editor/.venv/bin/python -c "import fastapi, uvicorn" 2>/dev/null; then
    editor/.venv/bin/pip install -q -r editor/server/requirements.txt
fi

# ── web build (skip with EXCEED_EDITOR_DEV=1 to use vite dev server) ────────
if [ "${EXCEED_EDITOR_DEV:-0}" != "1" ] && [ ! -f editor/web/dist/index.html ]; then
    echo "· building web UI (first run only)"
    (cd editor/web && npm install && npm run build)
fi

echo "· editor running at http://127.0.0.1:8787  (Ctrl-C to stop)"
exec editor/.venv/bin/python -m editor.server
