# Exceed Vault Editor

A local, data-asset-style editor for the `source/content/` Obsidian vault —
like a game engine's asset inspector, but the storage stays plain markdown.

- **Markdown is the storage.** The editor parses the vault into structured
  records and writes changes back to the same `.md` files. Obsidian, Quartz,
  the playtest app and `tools/consistency_check.py` keep working at all times.
- **Lossless round-trip.** Anything you didn't touch stays byte-identical.
  Saving regenerates only the header field block (canonicalized) plus the
  specific sections you edited. Verified by a test that round-trips every
  file in the vault byte-for-byte (`GET /api/selftest`, 554 files).
- **Write scope.** Only `.md` files under `source/content/` — enforced
  server-side. Never `.obsidian/`, `source/quartz/`, `tools/`, `docs/`.
- **No git integration.** The editor writes files and shows what changed
  this session (plus live `git status`); you commit with your own tooling.

## Run

```bash
./editor/run.sh          # first run: creates venv + builds web UI
# → http://127.0.0.1:8787  (localhost only)
```

Requirements: Python 3.10+, Node/npm (for the one-time web build).

Development mode (hot reload): `EXCEED_EDITOR_DEV=1` skip the static build,
run `cd editor/web && npm run dev` (Vite on :5178, proxies `/api` to :8787)
and `editor/.venv/bin/python -m editor.server` together.

## What you can do

- **Browser** — every record type (perks, spells, abilities, effects, actions,
  conditions, mechanics, rules) as a sortable table with filters (folder, tag,
  attribute, has-embeds) and search.
- **Record form** — structured fields per type: requirements builder (tier /
  skill / perk link / attribute / free text), attribute dropdowns, cost /
  AP-cost pickers, tag vocabularies (perk tags vs mechanic tags vs spell
  traits, kept separate per CLAUDE.md), grants editor (embed picker with
  reorder, staged "Grants by Stage" for leveled perks), prose sections as
  plain text. Live per-record issues from the consistency checker.
- **Create** — new files from templates (`+ New…`), `Ability - ` / `Effect - `
  name prefixes enforced, duplicate stems forbidden.
- **Rename / Move** — previews every `[[wikilink]]` / `![[embed]]` rewrite
  vault-wide before applying.
- **Delete** — shows what would break first.
- **Issues page** — the full `tools/consistency_check.py` suite (imported,
  not reimplemented) + editor extras (quirks, empty stubs, WI typo…).
- **Rulebook tree** — the rules reading hierarchy derived from
  `Rules/Rulebook.md` → chapter pages → hub embeds (no manifest). Read mode
  renders the book with embeds expanded inline ("zoom"); structure issues
  flag broken embeds, unwired files and drafts inside the published tree.
- **Drafts** — `draft: true` frontmatter (toggle in the record view) keeps
  dev-only files out of the published Quartz site while visible in
  Obsidian/the editor.
- **Relations** — who embeds/links/requires a record, requirement /
  prerequisite chains as trees.
- **Session** — files written this session + git status of `source/content`.
- **diff tab** — per-record `git diff` vs HEAD.

## HTTP API (also the machine surface for AI tooling)

The UI is a thin client over this API — ZCode or scripts can do everything
the editor does without the browser:

| Endpoint | What |
|---|---|
| `GET /api/index?type=perk&q=…&fullText=true` | table rows for the browser |
| `GET /api/record?path=…` | full parsed record (fields, sections, grants, issues) |
| `PUT /api/record` | surgical save: `{path, headerFields?, looseFields?, sectionBodies?, grants?, intro?}` |
| `POST /api/create` | `{scaffold, name, folder}` |
| `POST /api/rename` | `{path, newName?, newFolder?, apply?}` — omit `apply` for preview |
| `POST /api/delete` | `{path, apply?}` — omit `apply` for inbound-ref preview |
| `GET /api/checks` | full consistency results (checker + extras) |
| `GET /api/rulebook` | rules reading tree, derived from Rulebook/chapter embeds |
| `GET /api/read?path=…` | content + resolved embeds for the reader/zoom view |
| `GET /api/refs?stem=…` | reverse deps (embedders / linkers / requirers) |
| `GET /api/tree?stem=…` | requirement/prerequisite chain |
| `GET /api/session` | writes this session + git status |
| `GET /api/diff?path=…` | git diff for one file |
| `GET /api/selftest` | round-trip proof over the whole vault |
| `GET /api/meta` | attribute codes, tag vocabs, folders, scaffolds |

## Layout

```
editor/
  server/            FastAPI app
    vault.py         scanner + lossless parser (fields/sections with char spans)
    types.py         type inference (folder/prefix) + per-type schemas
    serialize.py     splice engine: header regen + surgical section edits
    records.py       parser → API JSON
    refactor.py      rename/move with vault-wide link rewrite, delete
    checks.py        imports tools/consistency_check.py + editor extras
    scaffolds.py     new-file templates
    session.py       session writes + git status (never commits)
  web/               Vite + React + TS SPA (dark, table-first)
  tests/             round-trip + API tests (586 tests, temp vault for writes)
```

## Tests

```bash
editor/.venv/bin/python -m pytest editor/tests/ -q
```

The critical gate: for every `.md` in the vault, parsing into the model and
reassembling its spans reproduces the file byte-for-byte, and an empty edit
is a no-op. If a future change breaks that, the foundation is broken.
