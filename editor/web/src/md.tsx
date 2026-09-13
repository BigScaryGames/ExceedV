// Minimal read-only markdown renderer for the rulebook "zoom" view.
// Covers the vault's dialect subset: headings, tables, lists, blockquotes,
// bold/italic/code/highlight inline, wikilinks, HRs. Prose fidelity, not WYSIWYG.
import React from 'react'

export function Inline({ text, onLink }: { text: string; onLink: (stem: string) => void }) {
  // split on inline tokens: `code`, **bold**, *italic*, ==highlight==, [[wikilink]]
  const parts: React.ReactNode[] = []
  const re = /(`[^`]+`|\*\*[^*]+\*\*|\*[^*\n]+\*|==[^=]+==|\[\[[^\]]+\]\])/g
  let last = 0, m: RegExpExecArray | null, k = 0
  while ((m = re.exec(text))) {
    if (m.index > last) parts.push(text.slice(last, m.index))
    const tok = m[0]
    if (tok.startsWith('`')) parts.push(<code key={k++}>{tok.slice(1, -1)}</code>)
    else if (tok.startsWith('**')) parts.push(<strong key={k++}>{tok.slice(2, -2)}</strong>)
    else if (tok.startsWith('==')) parts.push(<mark key={k++}>{tok.slice(2, -2)}</mark>)
    else if (tok.startsWith('[[')) {
      const inner = tok.slice(2, -2)
      const [target, alias] = inner.split('|')
      const clean = target.replace(/\\$/, '').replace(/\.md$/, '')
      parts.push(<a key={k++} className="wikilink" onClick={() => onLink(clean)}>{(alias ?? clean).replace('\\|', '|')}</a>)
    } else if (tok.startsWith('*')) parts.push(<em key={k++}>{tok.slice(1, -1)}</em>)
    last = m.index + tok.length
  }
  if (last < text.length) parts.push(text.slice(last))
  return <>{parts}</>
}

export function Markdown({ text, onLink, headingOffset = 0 }:
  { text: string; onLink: (stem: string) => void; headingOffset?: number }) {
  const lines = text.split('\n')
  const out: React.ReactNode[] = []
  let i = 0, key = 0

  const flushTable = () => {
    const rows: string[][] = []
    while (i < lines.length && lines[i].trim().startsWith('|')) {
      const cells = lines[i].trim().replace(/^\||\|$/g, '').split('|')
      if (!cells.every((c) => /^\s*:?-+:?\s*$/.test(c))) rows.push(cells)
      i++
    }
    const [head, ...body] = rows
    out.push(
      <table className="mdtable" key={key++}>
        <thead><tr>{head.map((c, j) => <th key={j}><Inline text={c} onLink={onLink} /></th>)}</tr></thead>
        <tbody>{body.map((r, j) => <tr key={j}>{r.map((c, l) => <td key={l}><Inline text={c} onLink={onLink} /></td>)}</tr>)}</tbody>
      </table>)
  }

  while (i < lines.length) {
    const line = lines[i]
    const t = line.trim()
    if (t.startsWith('|')) { flushTable(); continue }
    if (t === '') { i++; continue }
    const h = t.match(/^(#{1,6})\s+(.*)$/)
    if (h) {
      const level = Math.min(6, h[1].length + headingOffset)
      const Tag = `h${level}` as keyof React.JSX.IntrinsicElements
      out.push(<Tag key={key++}><Inline text={h[2]} onLink={onLink} /></Tag>)
      i++; continue
    }
    if (/^(-{3,}|\*{3,})$/.test(t)) { out.push(<hr key={key++} />); i++; continue }
    if (t.startsWith('> ')) {
      const buf: string[] = []
      while (i < lines.length && lines[i].trim().startsWith('>')) { buf.push(lines[i].trim().replace(/^>\s?/, '')); i++ }
      out.push(<blockquote key={key++}><Markdown text={buf.join('\n')} onLink={onLink} headingOffset={headingOffset + 1} /></blockquote>)
      continue
    }
    const li = t.match(/^[-*]\s+(.*)$/)
    if (li) {
      const items: string[] = []
      while (i < lines.length) {
        const m2 = lines[i].trim().match(/^[-*]\s+(.*)$/)
        if (!m2) break
        items.push(m2[1]); i++
      }
      out.push(<ul key={key++}>{items.map((it, j) => <li key={j}><Inline text={it} onLink={onLink} /></li>)}</ul>)
      continue
    }
    const ol = t.match(/^\d+[.)]\s+(.*)$/)
    if (ol) {
      const items: string[] = []
      while (i < lines.length) {
        const m2 = lines[i].trim().match(/^\d+[.)]\s+(.*)$/)
        if (!m2) break
        items.push(m2[1]); i++
      }
      out.push(<ol key={key++}>{items.map((it, j) => <li key={j}><Inline text={it} onLink={onLink} /></li>)}</ol>)
      continue
    }
    // paragraph: gather until blank/structural line
    const buf: string[] = [line]
    i++
    while (i < lines.length && lines[i].trim() !== '' && !/^(#{1,6}\s|\||[-*]\s|\d+[.)]\s|>\s)/.test(lines[i].trim())) {
      buf.push(lines[i]); i++
    }
    out.push(<p key={key++}><Inline text={buf.join('\n').replace(/\n/g, ' ')} onLink={onLink} /></p>)
  }
  return <>{out}</>
}
