// Entity browser: type tabs in the sidebar, filterable data table.
import React, { useMemo, useState } from 'react'
import type { IndexRow, Meta } from './types'

export interface BrowserProps {
  rows: IndexRow[]
  meta: Meta
  type: string
  onNavigate: (hash: string) => void
  onTypeChange: (type: string) => void
  query: string
  onQueryChange: (q: string) => void
  loading: boolean
}

type SortKey = 'name' | 'folder' | 'cost' | 'tier' | 'apCost' | 'attributes'

export function Browser({ rows, meta, type, onNavigate, onTypeChange, query, onQueryChange, loading }: BrowserProps) {
  const [folder, setFolder] = useState('')
  const [tag, setTag] = useState('')
  const [attr, setAttr] = useState('')
  const [hasEmbeds, setHasEmbeds] = useState('')
  const [sort, setSort] = useState<SortKey>('name')
  const [desc, setDesc] = useState(false)

  const typePrefix: Record<string, string> = {
    perk: 'Perks/', spell: 'Spells/', ability: 'Actions/', effect: 'Rules/Effects/',
    action: 'Actions/', condition: 'Rules/References/Conditions', mechanic: 'Rules/',
    rule: 'Rules/', template: '', doc: '',
  }

  const folders = useMemo(() => {
    const pool = new Set(rows.map((r) => r.folder))
    return [...pool].filter((f) => (typePrefix[type] ? f.startsWith(typePrefix[type]) : true)).sort()
  }, [rows, type])

  const tags = useMemo(() => {
    const pool = new Set<string>()
    rows.forEach((r) => r.tags.forEach((t) => pool.add(t)))
    return [...pool].sort()
  }, [rows])

  const filtered = useMemo(() => {
    let out = rows
    if (folder) out = out.filter((r) => r.folder === folder || r.folder.startsWith(folder + '/'))
    if (tag) out = out.filter((r) => r.tags.includes(tag))
    if (attr) out = out.filter((r) => r.attrCodes.includes(attr))
    if (hasEmbeds === 'yes') out = out.filter((r) => r.grantCount > 0)
    if (hasEmbeds === 'no') out = out.filter((r) => r.grantCount === 0)
    const get = (r: IndexRow): string | number => {
      switch (sort) {
        case 'name': return r.stem.toLowerCase()
        case 'folder': return r.folder
        case 'cost': return parseInt(r.cost) || 0
        case 'tier': return parseInt(r.tier) || 0
        case 'apCost': return parseInt(r.apCost) || 0
        case 'attributes': return r.attributes
      }
    }
    return [...out].sort((a, b) => {
      const va = get(a), vb = get(b)
      const cmp = typeof va === 'number' && typeof vb === 'number' ? va - vb : String(va).localeCompare(String(vb))
      return desc ? -cmp : cmp
    })
  }, [rows, folder, tag, attr, hasEmbeds, sort, desc])

  const columns = useMemo(() => {
    const sample = filtered[0] ?? rows.find((r) => r.type === type)
    return sample ? Object.keys(sample.columns).filter((c) => c !== 'Tags') : []
  }, [filtered, rows, type])

  const th = (key: SortKey, label: string) => (
    <th onClick={() => { if (sort === key) setDesc(!desc); else { setSort(key); setDesc(false) } }}>
      {label}{sort === key ? (desc ? ' ↓' : ' ↑') : ''}
    </th>
  )

  const typeCounts = meta.typeCounts
  const categoryOf = (r: IndexRow): string =>
    meta.categoryTags.find((c) => r.tags.includes(c)) ?? 'Uncategorized'

  const renderTable = (rs: IndexRow[]) => (
    <table className="grid">
      <thead>
        <tr>
          {th('name', 'Name')}
          {th('folder', 'Folder')}
          {columns.map((c) => <th key={c}>{c}</th>)}
          <th>Tags</th>
        </tr>
      </thead>
      <tbody>
        {rs.map((r) => (
          <tr key={r.path} onClick={() => onNavigate(`#/record?path=${encodeURIComponent(r.path)}`)}>
            <td className="name">{r.stem}
              {r.subtype && <span className="pill sub">{r.subtype}</span>}
              {r.leveled && <span className="pill">leveled</span>}
            </td>
            <td className="mono faint">{r.folder}</td>
            {columns.map((c) => {
              const v = r.columns[c]
              return <td key={c} className="mono">{typeof v === 'number' ? (v || '—') : (v || '—')}</td>
            })}
            <td>{r.tags.slice(0, 3).map((t) => <span key={t} className="pill tag">{t}</span>)}
              {r.tags.length > 3 && <span className="faint"> +{r.tags.length - 3}</span>}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )

  // Mechanics are organized into areas by their category tag
  // (#Combat / #Core / #Downtime / #Magic / #Social).
  const grouped = type === 'mechanic' ? (() => {
    const order = [...meta.categoryTags, 'Uncategorized']
    return order
      .map((cat) => ({ cat, rows: filtered.filter((r) => categoryOf(r) === cat) }))
      .filter((g) => g.rows.length > 0)
  })() : null

  return (
    <>
      <div style={{ display: 'flex', gap: 10, alignItems: 'center', marginBottom: 12, flexWrap: 'wrap' }}>
        <input className="search" placeholder="Filter by name / requirements / columns…" value={query}
          onChange={(e) => onQueryChange(e.target.value)} style={{ width: 320 }} />
        <span className="faint">{filtered.length} / {rows.length} records</span>
        <button className="small" onClick={() => { setFolder(''); setTag(''); setAttr(''); setHasEmbeds('') }}>Reset filters</button>
      </div>

      {loading ? <div className="loading">Scanning vault…</div> : grouped ? (
        grouped.map((g) => (
          <div key={g.cat} style={{ marginBottom: 22 }}>
            <h3 style={{ margin: '14px 0 6px', color: 'var(--dim)', fontSize: 13, textTransform: 'uppercase', letterSpacing: '1px' }}>
              {g.cat} <span className="faint" style={{ textTransform: 'none' }}>— {g.rows.length}</span>
            </h3>
            {renderTable(g.rows)}
          </div>
        ))
      ) : renderTable(filtered)}
      {!loading && filtered.length === 0 && <div className="empty">No records match.</div>}

      {/* sidebar filter mount (rendered into sidebar via portal-less prop drilling) */}
      <SidebarFilters meta={meta} type={type} folders={folders} tags={tags}
        folder={folder} tag={tag} attr={attr} hasEmbeds={hasEmbeds}
        setFolder={setFolder} setTag={setTag} setAttr={setAttr} setHasEmbeds={setHasEmbeds} />
    </>
  )
}

import { createPortal } from 'react-dom'

// Simple approach: filters live in a DOM node the App places in the sidebar.
let filterHost: HTMLElement | null = null
export function setFilterHost(el: HTMLElement | null) { filterHost = el }

function SidebarFilters(props: {
  meta: Meta; type: string; folders: string[]; tags: string[]
  folder: string; tag: string; attr: string; hasEmbeds: string
  setFolder: (v: string) => void; setTag: (v: string) => void; setAttr: (v: string) => void; setHasEmbeds: (v: string) => void
}) {
  const { meta, folders, tags, folder, tag, attr, hasEmbeds,
    setFolder, setTag, setAttr, setHasEmbeds } = props
  const content = (
    <div className="filterbox">
      <h3>Filters</h3>
      <label>Folder
        <select value={folder} onChange={(e) => setFolder(e.target.value)}>
          <option value="">all</option>
          {folders.map((f) => <option key={f} value={f}>{f}</option>)}
        </select>
      </label>
      <label>Tag
        <select value={tag} onChange={(e) => setTag(e.target.value)}>
          <option value="">all</option>
          {tags.map((t) => <option key={t} value={t}>{t}</option>)}
        </select>
      </label>
      <label>Attribute
        <select value={attr} onChange={(e) => setAttr(e.target.value)}>
          <option value="">any</option>
          {meta.attributeCodes.map((a) => <option key={a} value={a}>{a}</option>)}
        </select>
      </label>
      <label>Grants
        <select value={hasEmbeds} onChange={(e) => setHasEmbeds(e.target.value)}>
          <option value="">any</option>
          <option value="yes">has embeds</option>
          <option value="no">no embeds</option>
        </select>
      </label>
      <div className="faint" style={{ marginTop: 6 }}>{props.type} view</div>
    </div>
  )
  return filterHost ? createPortal(content, filterHost) : null
}
