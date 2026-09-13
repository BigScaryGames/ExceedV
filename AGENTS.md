# AGENTS.md — working in this repo

Skill-based fantasy TTRPG ("Exceed"). The `source/content/` folder is an
Obsidian vault that doubles as the single source of truth: it is parsed by
the Quartz site (GitHub Pages), the external playtest app
(`BigScaryGames/Exceed-Playtest-App`), and `tools/consistency_check.py`.

## Content conventions

- **`source/content/CLAUDE.md`** is the authoritative content-conventions
  doc: attribute codes (`PR WL CH WT MG EN AG DX`), perk/spell/ability/effect
  file formats, `Ability - ` / `Effect - ` naming, perk-tags vs mechanic-tags
  vs spell-traits vocabularies, folder organization. Read it before writing
  content. Filenames are global identifiers (title = filename, no H1).

## Editing content — use the vault editor, not raw file edits

`editor/` is a local web app (FastAPI + React) that edits the vault as
structured records with **lossless round-trip**: anything not edited stays
byte-identical, saves are surgical, and every write is validated against the
consistency checker.

- Start it: `./editor/run.sh` → http://127.0.0.1:8787
- Full API docs: **`editor/README.md`**
- The HTTP API under `/api/*` is the preferred surface for AI/parsers —
  don't hand-edit `.md` files when a structured endpoint exists:
  - `GET /api/index?type=perk` — list records
  - `GET /api/record?path=…` — parsed record (fields, sections, grants, issues)
  - `PUT /api/record` — surgical save (header fields / sections / grants)
  - `POST /api/create`, `POST /api/rename` (preview without `apply:true`),
    `POST /api/delete` (preview without `apply:true`)
  - `GET /api/checks` — full consistency suite (also run
    `python3 tools/consistency_check.py` directly)
  - `GET /api/selftest` — must always report `"ok": true`
- Run tests after changing editor code:
  `editor/.venv/bin/python -m pytest editor/tests/ -q`
  (includes the round-trip gate over every vault file)

## Hard rules

- Writes go to `.md` files under `source/content/` only — never
  `.obsidian/`, `.github/`, `source/quartz/`, `tools/`, `docs/`
  (the editor's API enforces this server-side).
- Never commit from tooling unless explicitly asked; the editor itself never
  commits. Show `git status` / diffs and let the user commit.
- UTF-8, LF line endings (`source/.gitattributes`), no BOM.
- After content changes, `GET /api/checks` (or the checker CLI) — the CI
  pipeline only catches hard build breaks, not convention violations.
