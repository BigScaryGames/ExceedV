"""Vault scanner and lossless markdown parser.

Parses every .md file under source/content into a structured model:
fields (bold **Name:** lines), sections (## headings), intro body, embeds
and wikilinks — all with char spans into the original text so the
serializer can splice edits surgically without touching anything else.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VAULT_ROOT = REPO_ROOT / "source" / "content"

BOM = "\ufeff"

# A field line: optional tiny junk prefix (e.g. the stray "1" in
# "1**Requirements:**"), then **Name:** (colon inside the bold, the universal
# vault format) and the rest of the line as value. Bold terms without a
# colon ("**1. Dancing** (...)") are prose, not fields.
FIELD_RE = re.compile(r"^(?P<pre>.{0,4}?)\*\*(?P<name>[^*:\n]+?):\*\*[ \t]*(?P<value>.*?)[ \t]*$")

HEADING_RE = re.compile(r"^(?P<level>#{1,6})[ \t]+(?P<title>.*?)[ \t]*$")

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.S)

# Same shapes as tools/consistency_check.py (EMBED_RE / LINK_RE).
EMBED_RE = re.compile(r"!\[\[([^\]|#]+?)(?:[#|][^\]]*)?\]\]")
LINK_RE = re.compile(r"(?<!\!)\[\[([^\]|#]+?)(?:[#|][^\]]*)?\]\]")

GRANTS_TITLES = {"grants", "grants by stage"}
STAGE_RE = re.compile(r"\*\*Stage\s*(\d+):?\*\*", re.I)


def clean_target(t: str) -> str:
    """Strip escaping/whitespace from a link target ([[A\|A]] -> A)."""
    return t.strip().rstrip("\\").strip()


@dataclass
class Line:
    start: int          # offset of first char of the line
    end: int            # offset of last char of the content (exclusive of EOL)
    eol_start: int      # offset where the EOL sequence begins (== end if none)
    end_with_eol: int   # offset just past the EOL (== end if none)
    content: str


@dataclass
class Field:
    name: str           # "Requirements"
    value: str          # "Martial 2" (trailing whitespace stripped)
    raw: str            # the full original line content (no EOL)
    line: Line
    line_no: int
    in_header_block: bool = False


@dataclass
class Section:
    title: str          # "Grants" (no ##)
    level: int
    heading: Line       # the heading line
    body_start: int     # offset just past the heading line's EOL
    end: int            # offset where the next heading starts (or EOF)


@dataclass
class ParsedFile:
    rel: str            # posix path relative to vault root
    stem: str
    text: str           # decoded original text (no BOM)
    bom: bool
    eol: str            # dominant EOL: "\n" or "\r\n"
    frontmatter: str | None
    fields: list[Field]
    sections: list[Section]
    intro_start: int
    intro_end: int
    header_block: tuple[int, int] | None   # span of the leading field block

    # -- convenience accessors ------------------------------------------------
    def field(self, name: str) -> Field | None:
        wanted = name.strip().lower()
        for f in self.fields:
            if f.name.strip().lower() == wanted:
                return f
        return None

    def field_value(self, name: str) -> str | None:
        f = self.field(name)
        return f.value if f else None

    def section(self, title: str) -> Section | None:
        wanted = title.strip().lower()
        for s in self.sections:
            if s.title.strip().lower() == wanted:
                return s
        return None

    def section_body(self, title: str) -> str | None:
        s = self.section(title)
        return self.text[s.body_start:s.end] if s else None

    @property
    def intro(self) -> str:
        return self.text[self.intro_start:self.intro_end]

    def header_field_names(self) -> list[str]:
        if not self.header_block:
            return []
        s, e = self.header_block
        return [f.name for f in self.fields if s <= f.line.start < e]

    def header_field(self, name: str) -> Field | None:
        wanted = name.strip().lower()
        for f in self.fields:
            if f.in_header_block and f.name.strip().lower() == wanted:
                return f
        return None

    def grants(self) -> dict | None:
        """{'mode': 'simple'|'staged', 'stages': {n: [targets]}|None,
            'embeds': [targets]} for the Grants / Grants by Stage section."""
        sec = None
        for s in self.sections:
            if s.title.strip().lower() in GRANTS_TITLES:
                sec = s
                break
        if sec is None:
            return None
        body = self.text[sec.body_start:sec.end]
        staged: dict[int, list[str]] = {}
        for m in STAGE_RE.finditer(body):
            stage_no = int(m.group(1))
            # embeds on the same stage line (up to the next stage or EOL)
            line_end = body.find("\n", m.end())
            if line_end == -1:
                line_end = len(body)
            chunk = body[m.end():line_end]
            staged[stage_no] = [clean_target(e.group(1)) for e in EMBED_RE.finditer(chunk)]
        embeds = [clean_target(m.group(1)) for m in EMBED_RE.finditer(body)]
        if staged and len(embeds) >= len(staged):
            return {"mode": "staged", "title": sec.title, "stages": staged, "embeds": embeds}
        return {"mode": "simple", "title": sec.title, "stages": None, "embeds": embeds}

    def links_and_embeds(self) -> tuple[list[dict], list[dict]]:
        """All wikilinks and embeds with char offsets (for rename rewrites)."""
        links, embeds = [], []
        for m in LINK_RE.finditer(self.text):
            links.append({"target": clean_target(m.group(1)), "raw": m.group(0),
                          "start": m.start(), "end": m.end()})
        for m in EMBED_RE.finditer(self.text):
            embeds.append({"target": clean_target(m.group(1)), "raw": m.group(0),
                           "start": m.start(), "end": m.end()})
        return links, embeds


def _split_lines(text: str) -> list[Line]:
    lines: list[Line] = []
    pos = 0
    n = len(text)
    while pos < n:
        nl = text.find("\n", pos)
        if nl == -1:
            content = text[pos:n]
            end, eol_start, past = n, n, n
            if content.endswith("\r"):
                content = content[:-1]
                end, eol_start = n - 1, n - 1
            lines.append(Line(pos, end, eol_start, past, content))
            break
        eol_start = nl
        if nl > pos and text[nl - 1] == "\r":
            end = nl - 1
            content = text[pos:end]
        else:
            end = nl
            content = text[pos:nl]
        lines.append(Line(pos, end, eol_start, nl + 1, content))
        pos = nl + 1
    return lines


def parse_text(text: str, rel: str = "", stem: str = "") -> ParsedFile:
    bom = text.startswith(BOM)
    if bom:
        text = text[1:]

    eol = "\r\n" if "\r\n" in text else "\n"
    lines = _split_lines(text)

    frontmatter = None
    fm_end = 0
    fm = FRONTMATTER_RE.match(text)
    if fm:
        frontmatter = fm.group(0)
        fm_end = fm.end()

    fields: list[Field] = []
    sections: list[Section] = []

    in_fence = False
    first_heading_start: int | None = None
    field_line_idxs: list[int] = []
    header_field_idxs: list[int] = []

    # Header block scan state: from the top we may pass frontmatter, blanks
    # and H1 lines; once field lines start, blanks and more field lines may
    # follow; any other line ends the block.
    block_started = False
    block_open = True
    block_start_idx: int | None = None
    block_end_idx: int | None = None

    for idx, ln in enumerate(lines):
        if ln.start < fm_end:
            continue
        stripped = ln.content.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            block_open = False
            continue
        if in_fence:
            block_open = False
            continue

        hm = HEADING_RE.match(ln.content)
        if hm:
            level = len(hm.group("level"))
            if block_started:
                block_open = False
            elif level == 1 and not fields:
                # H1 title line before any field line does not break the
                # leading scan (spell template shape); deeper headings do
                continue
            else:
                block_open = False
            if first_heading_start is None:
                first_heading_start = ln.start
            sections.append(Section(hm.group("title"), level,
                                    ln, ln.end_with_eol, len(text)))
            continue

        fm2 = FIELD_RE.match(ln.content)
        if fm2 and not stripped.startswith("|"):
            f = Field(name=fm2.group("name").strip(), value=fm2.group("value"),
                      raw=ln.content, line=ln, line_no=idx + 1)
            fields.append(f)
            field_line_idxs.append(idx)
            if block_open:
                if not block_started:
                    block_started = True
                    block_start_idx = idx
                block_end_idx = idx
                header_field_idxs.append(idx)
            continue

        if stripped == "":
            continue  # blanks neither start nor close the block

        block_open = False

    # mark header fields
    for f in fields:
        f.in_header_block = f.line_no - 1 in header_field_idxs

    # section bodies end where the next heading begins
    for i, s in enumerate(sections):
        s.end = sections[i + 1].heading.start if i + 1 < len(sections) else len(text)

    if first_heading_start is None:
        first_heading_start = len(text)

    # intro: after the header block (or frontmatter / file start) up to the
    # first heading. If there is no header block, intro starts after
    # frontmatter (body-first files like effects).
    if block_end_idx is not None:
        intro_start = lines[block_end_idx].end_with_eol
    else:
        intro_start = fm_end
    intro_end = first_heading_start
    if intro_end < intro_start:
        intro_end = intro_start

    header_block = None
    if block_start_idx is not None and block_end_idx is not None:
        header_block = (lines[block_start_idx].start, lines[block_end_idx].end)

    return ParsedFile(
        rel=rel, stem=stem or Path(rel).stem, text=text, bom=bom, eol=eol,
        frontmatter=frontmatter, fields=fields, sections=sections,
        intro_start=intro_start, intro_end=intro_end, header_block=header_block,
    )


class Vault:
    """Scans the vault and caches parsed files (mtime-invalidated)."""

    def __init__(self, root: Path = VAULT_ROOT):
        self.root = Path(root)
        self._cache: dict[str, tuple[float, int, ParsedFile]] = {}

    # -- filesystem ------------------------------------------------------------
    def scan(self) -> list[str]:
        rels = []
        for dp, dns, fns in os.walk(self.root):
            dns[:] = [d for d in dns if not d.startswith(".")]
            for fn in fns:
                if fn.endswith(".md"):
                    p = Path(dp) / fn
                    rels.append(p.relative_to(self.root).as_posix())
        rels.sort()
        return rels

    def abs_path(self, rel: str) -> Path:
        return (self.root / rel).resolve()

    def is_inside(self, rel: str) -> bool:
        try:
            p = self.abs_path(rel)
            p.relative_to(self.root.resolve())
        except ValueError:
            return False
        return p.suffix == ".md" and p.is_file()

    def read_text(self, rel: str) -> str:
        data = self.abs_path(rel).read_bytes()
        return data.decode("utf-8", errors="surrogateescape")

    def write_text(self, rel: str, text: str) -> None:
        p = self.abs_path(rel)
        data = text.encode("utf-8", errors="surrogateescape")
        tmp = p.parent / (p.name + ".tmp~")
        tmp.parent.mkdir(parents=True, exist_ok=True)
        tmp.write_bytes(data)
        os.replace(tmp, p)

    def get(self, rel: str) -> ParsedFile:
        p = self.abs_path(rel)
        st = p.stat()
        cached = self._cache.get(rel)
        if cached and cached[0] == st.st_mtime_ns and cached[1] == st.st_size:
            return cached[2]
        text = self.read_text(rel)
        parsed = parse_text(text, rel=rel, stem=p.stem)
        self._cache[rel] = (st.st_mtime_ns, st.st_size, parsed)
        return parsed

    def invalidate(self, rel: str) -> None:
        self._cache.pop(rel, None)

    # -- indexes ---------------------------------------------------------------
    def stem_index(self) -> dict[str, list[str]]:
        idx: dict[str, list[str]] = {}
        for rel in self.scan():
            idx.setdefault(Path(rel).stem, []).append(rel)
        return idx

    def resolve_stem(self, target: str) -> str | None:
        """Obsidian-style stem resolution over non-empty vault files."""
        t = target.strip()
        if t.startswith("http"):
            return None
        normalized = t.replace("\\", "/").replace("source/content/", "")
        if normalized.endswith(".md"):
            normalized = normalized[:-3]
        all_rels = set(self.scan())
        # exact relative path
        if normalized + ".md" in all_rels:
            return normalized + ".md"
        # bare stem (Obsidian resolves to the shortest matching path)
        stem = Path(normalized).name
        idx = self.stem_index()
        if stem in idx:
            non_empty = [r for r in idx[stem] if self.abs_path(r).stat().st_size > 0]
            pool = non_empty or list(idx[stem])
            pool.sort(key=lambda r: (r.count("/"), r))
            return pool[0]
        return None
