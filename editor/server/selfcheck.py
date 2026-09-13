"""Model-span reassembly — the round-trip self check.

Concatenating the parsed model's region slices must reproduce the original
text byte-for-byte; used by the test suite and GET /api/selftest.
"""
from __future__ import annotations

from .vault import ParsedFile


def reassemble(parsed: ParsedFile) -> str:
    text = parsed.text
    pieces: list[tuple[int, int]] = []
    fm_end = 0
    if parsed.frontmatter:
        fm_end = len(parsed.frontmatter)
        pieces.append((0, fm_end))
    block_start = parsed.header_block[0] if parsed.header_block else parsed.intro_start
    if block_start > fm_end:
        pieces.append((fm_end, block_start))
    if parsed.header_block:
        pieces.append(parsed.header_block)
        if parsed.intro_start > parsed.header_block[1]:
            pieces.append((parsed.header_block[1], parsed.intro_start))
    if parsed.intro_end > parsed.intro_start:
        pieces.append((parsed.intro_start, parsed.intro_end))
    for s in parsed.sections:
        pieces.append((s.heading.start, s.end))

    out = []
    cursor = 0
    for s, e in pieces:
        if s < cursor:
            raise ValueError(f"overlapping/unsorted regions at {s} < {cursor} in {parsed.rel}")
        if s > cursor:
            out.append(text[cursor:s])
        out.append(text[s:e])
        cursor = e
    if cursor < len(text):
        out.append(text[cursor:])
    return "".join(out)
