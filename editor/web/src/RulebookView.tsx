// Rulebook tree view + "zoom" reader (embeds expanded inline).
import React, { useEffect, useState } from 'react'
import { api } from './api'
import { Markdown } from './md'

interface RulebookNode {
  path: string
  name: string
  draft: boolean
  children: RulebookNode[]
  brokenEmbeds: string[]
  unwired: string[]
}
interface RulebookData {
  root: RulebookNode | null
  drafts: string[]
  issues: { file: string; severity: string; label: string }[]
}

export function RulebookView({ onNavigate }: { onNavigate: (hash: string) => void }) {
  const [data, setData] = useState<RulebookData | null>(null)
  const [open, setOpen] = useState<Record<string, boolean>>({})
  const [tab, setTab] = useState<'tree' | 'issues'>('tree')

  useEffect(() => {
    api.rulebook().then((r: RulebookData) => {
      setData(r)
      const init: Record<string, boolean> = {}
      const walk = (n: RulebookNode, d: number) => {
        if (d < 1) { init[n.path] = true; n.children.forEach((c) => walk(c, d + 1)) }
      }
      if (r.root) walk(r.root, 0)
      setOpen(init)
    })
  }, [])

  if (!data) return <div className="loading">Deriving the rulebook tree…</div>
  if (!data.root) return <div className="empty">No Rules/Rulebook.md — create the root page first.</div>

  const go = (p: string) => onNavigate(`#/record?path=${encodeURIComponent(p)}`)
  const read = (p: string) => onNavigate(`#/read?path=${encodeURIComponent(p)}`)

  const renderNode = (n: RulebookNode, depth: number) => {
    const expanded = open[n.path]
    const hasKids = n.children.length > 0
    return (
      <div className="rnode" key={n.path}>
        <div className="rrow">
          {hasKids
            ? <button className="ghost small" onClick={() => setOpen({ ...open, [n.path]: !expanded })}>{expanded ? '▾' : '▸'}</button>
            : <span className="leafdot">·</span>}
          <span className="rname" onClick={() => go(n.path)}>{n.name}</span>
          {n.draft && <span className="pill" title="draft: hidden from the published site">draft</span>}
          {n.unwired.length > 0 && <span className="pill sub" title="files in the chapter folder not embedded">{n.unwired.length} unwired</span>}
          {n.brokenEmbeds.length > 0 && <span className="pill bad">{n.brokenEmbeds.length} broken</span>}
          <span className="rrow-actions">
            <button className="ghost small" onClick={() => read(n.path)}>read</button>
            <button className="ghost small" onClick={() => go(n.path)}>edit</button>
          </span>
        </div>
        {expanded && (
          <div className="rkids">
            {n.children.map((c) => renderNode(c, depth + 1))}
            {n.unwired.map((u) => (
              <div className="rrow unwired" key={u}>
                <span className="leafdot">·</span>
                <span className="rname faint" onClick={() => go(`Rules/${n.name}/${u}`)}>{u}</span>
                <span className="pill sub">not embedded</span>
              </div>
            ))}
          </div>
        )}
      </div>
    )
  }

  return (
    <div>
      <div className="record-head">
        <h1>Rulebook</h1>
        <span className="faint">derived from Rules/Rulebook.md embeds — no manifest to maintain</span>
        <div className="record-actions">
          <button className={tab === 'tree' ? 'primary' : ''} onClick={() => setTab('tree')}>Tree</button>
          <button className={tab === 'issues' ? 'primary' : ''} onClick={() => setTab('issues')}>
            Structure issues{data.issues.length > 0 && <span className="badge">{data.issues.length}</span>}
          </button>
          <button onClick={() => read('Rules/Rulebook.md')}>Read the whole book</button>
        </div>
      </div>
      {tab === 'tree' && <div className="tree ruletree">{renderNode(data.root, 0)}</div>}
      {tab === 'issues' && (
        <div className="panel">
          <h2>Structure issues ({data.issues.length})</h2>
          {data.issues.length === 0 && <div className="faint">The tree is fully wired: no broken embeds, no unwired files, no drafts inside the published tree.</div>}
          {data.issues.map((iss, i) => (
            <div className="issue" key={i}>
              <span className={`sev ${iss.severity}`}>{iss.severity}</span>
              <span className="rname" onClick={() => go(iss.file)}>{iss.file}</span>
              <span>{iss.label}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

// ── reader ──────────────────────────────────────────────────────────────────

interface ReadData {
  path: string
  name: string
  draft: boolean
  content: string
  embeds: { target: string; path: string | null; name: string }[]
}

export function Reader({ path, depth, onNavigate }:
  { path: string; depth: number; onNavigate: (hash: string) => void }) {
  const [data, setData] = useState<ReadData | null>(null)
  const [err, setErr] = useState('')

  useEffect(() => {
    setData(null); setErr('')
    api.read(path).then(setData).catch((e) => setErr(String(e)))
  }, [path])

  if (err) return <div className="err">{err}</div>
  if (!data) return <div className="loading">Loading {path}…</div>

  const link = (stem: string) => {
    api.resolve(stem)
      .then((p) => onNavigate(`#/record?path=${encodeURIComponent(p)}`))
      .catch(() => onNavigate(`#/browse?type=rule`))
  }

  // split content into prose segments and embed slots
  const segs: ({ type: 'text'; text: string } | { type: 'embed'; index: number })[] = []
  const re = /!\[\[([^\]]+)\]\]/g
  let last = 0
  let m: RegExpExecArray | null
  let idx = 0
  while ((m = re.exec(data.content))) {
    if (m.index > last) segs.push({ type: 'text', text: data.content.slice(last, m.index) })
    segs.push({ type: 'embed', index: idx++ })
    last = m.index + m[0].length
  }
  if (last < data.content.length) segs.push({ type: 'text', text: data.content.slice(last) })

  return (
    <div className={`reader${depth === 0 ? ' root' : ''}`}>
      {depth === 0 && (
        <div className="record-head">
          <h1>{data.name}</h1>
          {data.draft && <span className="pill" title="hidden from the published site">draft</span>}
          <div className="record-actions">
            <button onClick={() => onNavigate('#/rulebook')}>← Tree</button>
            <button onClick={() => onNavigate(`#/record?path=${encodeURIComponent(path)}`)}>Edit source</button>
          </div>
        </div>
      )}
      {depth > 0 && (
        <div className="embedhead" onClick={() => onNavigate(`#/record?path=${encodeURIComponent(path)}`)}>
          {data.name}
        </div>
      )}
      {segs.map((s, i) => {
        if (s.type === 'text') {
          return <Markdown key={i} text={s.text} headingOffset={depth === 0 ? 0 : 2} onLink={link} />
        }
        const e = data.embeds[s.index]
        if (!e) return null
        if (!e.path) return <div key={i} className="embedblock broken">broken embed: {e.target}</div>
        if (depth >= 2) {
          return (
            <button key={i} className="embedmore" onClick={() => onNavigate(`#/read?path=${encodeURIComponent(e.path!)}`)}>
              ▸ {e.name}
            </button>
          )
        }
        return <EmbedLazy key={i} path={e.path} depth={depth} onNavigate={onNavigate} />
      })}
    </div>
  )
}

function EmbedLazy({ path, depth, onNavigate }: { path: string; depth: number; onNavigate: (h: string) => void }) {
  const [open, setOpen] = useState(depth < 1)
  if (!open) {
    const label = path.split('/').pop()?.replace(/\.md$/, '') ?? path
    return <button className="embedmore" onClick={() => setOpen(true)}>▸ expand {label}</button>
  }
  return (
    <div className="embedblock">
      <Reader path={path} depth={depth + 1} onNavigate={onNavigate} />
    </div>
  )
}
