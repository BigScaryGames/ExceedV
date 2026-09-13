// App shell: hash routing, sidebar (types + filters), topbar, content area.
import React, { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { api } from './api'
import type { IndexRow, Meta, RecordData } from './types'
import { Browser, setFilterHost } from './Browser'
import { RecordView } from './RecordView'
import { CreateDialog, DeleteDialog, RenameDialog } from './Dialogs'
import { IssuesPage, SessionPanel } from './Pages'
import { RulebookView, Reader } from './RulebookView'

type Route =
  | { view: 'browse'; type: string }
  | { view: 'record'; path: string }
  | { view: 'issues' }
  | { view: 'session' }
  | { view: 'rulebook' }
  | { view: 'read'; path: string }

function parseHash(): Route {
  const h = window.location.hash || '#/browse?type=perk'
  const [pathPart, queryPart] = h.replace(/^#\//, '').split('?')
  const params = new URLSearchParams(queryPart ?? '')
  if (pathPart === 'record') return { view: 'record', path: params.get('path') ?? '' }
  if (pathPart === 'issues') return { view: 'issues' }
  if (pathPart === 'session') return { view: 'session' }
  if (pathPart === 'rulebook') return { view: 'rulebook' }
  if (pathPart === 'read') return { view: 'read', path: params.get('path') ?? 'Rules/Rulebook.md' }
  return { view: 'browse', type: params.get('type') ?? 'perk' }
}

const TYPE_LABELS: [string, string][] = [
  ['perk', 'Perks'],
  ['spell', 'Spells'],
  ['ability', 'Abilities'],
  ['effect', 'Effects'],
  ['action', 'Actions'],
  ['condition', 'Conditions'],
  ['mechanic', 'Mechanics'],
  ['rule', 'Rules'],
  ['doc', 'Docs'],
  ['template', 'Templates'],
]

export default function App() {
  const [route, setRoute] = useState<Route>(parseHash)
  const [meta, setMeta] = useState<Meta | null>(null)
  const [rows, setRows] = useState<IndexRow[]>([])
  const [loading, setLoading] = useState(false)
  const [query, setQuery] = useState('')
  const [showCreate, setShowCreate] = useState(false)
  const [renameTarget, setRenameTarget] = useState<RecordData | null>(null)
  const [deleteTarget, setDeleteTarget] = useState<RecordData | null>(null)
  const [issueCount, setIssueCount] = useState<number | null>(null)
  const filterRef = useRef<HTMLDivElement>(null)

  const navigate = useCallback((hash: string) => {
    window.location.hash = hash
    setRoute(parseHash())
  }, [])

  useEffect(() => {
    const onHash = () => setRoute(parseHash())
    window.addEventListener('hashchange', onHash)
    return () => window.removeEventListener('hashchange', onHash)
  }, [])

  useEffect(() => { setFilterHost(filterRef.current) }, [route])

  const loadIndex = useCallback((type?: string) => {
    setLoading(true)
    api.index(type, undefined).then(setRows).finally(() => setLoading(false))
  }, [])

  const loadMeta = useCallback(() => api.meta().then(setMeta), [])

  const refreshIssueCount = useCallback(() => {
    api.checks().then((r) => {
      // count = high-severity signals only (broken links/embeds, duplicates,
      // perk violations, non-stale spell violations)
      setIssueCount(r.brokenEmbeds.length + r.brokenLinks.length + r.duplicates.length
        + r.perkViolations.length
        + r.spellViolations.filter((v) => v.issues.some((s) => !r.staleChecks.includes(s))).length)
    }).catch(() => setIssueCount(null))
  }, [])

  useEffect(() => {
    if (!meta) { loadMeta(); refreshIssueCount() }
    if (route.view === 'browse' && (rows.length === 0 || rows[0]?.type !== route.type)) loadIndex(route.type)
  }, [route, meta, rows, loadIndex, loadMeta, refreshIssueCount])

  const stems = useMemo(() => rows.map((r) => r.stem).sort(), [rows])
  const allStems = useRef<string[]>([])
  useEffect(() => { api.index().then((r) => { allStems.current = r.map((x) => x.stem).sort() }) }, [])

  const skills = useMemo(() => {
    const pool = new Set<string>()
    rows.forEach((r) => {
      const req = r.requirements ?? ''
      req.split(',').forEach((part) => {
        const m = part.trim().match(/^([A-Z][a-z]+(?:\/[A-Z][a-z]+)*)\s+\d/)
        if (m) m[1].split('/').forEach((s) => pool.add(s))
      })
    })
    return [...pool].sort()
  }, [rows])

  if (!meta) return <div className="loading">Connecting to the vault server…</div>

  return (
    <div className="app">
      <datalist id="all-stems">{allStems.current.map((s) => <option key={s} value={s} />)}</datalist>
      <datalist id="skill-names">{skills.map((s) => <option key={s} value={s} />)}</datalist>

      <div className="topbar">
        <span className="logo">⚙ Exceed Vault Editor</span>
        <input className="search" placeholder="Search vault… (name, requirements; goes to Browser)"
          value={route.view === 'browse' ? query : ''}
          onChange={(e) => {
            setQuery(e.target.value)
            if (route.view !== 'browse') navigate(`#/browse?type=${route.view === 'record' ? 'perk' : 'perk'}`)
          }}
          onKeyDown={(e) => e.key === 'Enter' && route.view !== 'browse' && navigate('#/browse?type=perk')} />
        <div className="spacer" />
        <button className="primary" onClick={() => setShowCreate(true)}>+ New…</button>
        <button onClick={() => navigate('#/rulebook')}>Rulebook</button>
        <button onClick={() => navigate('#/issues')}>
          Issues{issueCount !== null && issueCount > 0 && <span className="badge">{issueCount}</span>}
        </button>
        <button onClick={() => navigate('#/session')}>Session</button>
      </div>

      <div className="main">
        {route.view !== 'issues' && route.view !== 'session' && route.view !== 'rulebook' && route.view !== 'read' && (
          <div className="sidebar">
            <h3>Types</h3>
            <div className="typelist">
              {TYPE_LABELS.map(([t, label]) => (
                <button key={t} className={route.view === 'browse' && route.type === t ? 'active' : ''}
                  onClick={() => navigate(`#/browse?type=${t}`)}>
                  <span>{label}</span>
                  <span className="count">{meta.typeCounts[t] ?? 0}</span>
                </button>
              ))}
            </div>
            <div ref={filterRef} />
          </div>
        )}

        <div className="content">
          {route.view === 'browse' && (
            <Browser
              rows={rows} meta={meta} type={route.type}
              onNavigate={navigate}
              onTypeChange={(t) => { loadIndex(t); navigate(`#/browse?type=${t}`) }}
              query={query} onQueryChange={setQuery}
              loading={loading}
            />
          )}
          {route.view === 'record' && route.path && (
            <RecordView
              path={route.path} meta={meta} stems={allStems.current.length ? allStems.current : stems}
              skills={skills}
              onNavigate={navigate}
              onSaved={() => { loadIndex(); refreshIssueCount() }}
              onRenameRequest={setRenameTarget}
              onDeleteRequest={setDeleteTarget}
            />
          )}
          {route.view === 'issues' && <IssuesPage onNavigate={navigate} />}
          {route.view === 'session' && <SessionPanel onNavigate={navigate} />}
          {route.view === 'rulebook' && <RulebookView onNavigate={navigate} />}
          {route.view === 'read' && route.path && <Reader path={route.path} depth={0} onNavigate={navigate} />}
        </div>
      </div>

      {showCreate && (
        <CreateDialog
          meta={meta} stems={allStems.current}
          onClose={() => setShowCreate(false)}
          onCreated={(path) => { setShowCreate(false); loadIndex(); refreshIssueCount(); navigate(`#/record?path=${encodeURIComponent(path)}`) }}
        />
      )}
      {renameTarget && (
        <RenameDialog
          record={renameTarget} meta={meta}
          onClose={() => setRenameTarget(null)}
          onDone={(newPath) => { setRenameTarget(null); loadIndex(); refreshIssueCount(); navigate(`#/record?path=${encodeURIComponent(newPath)}`) }}
        />
      )}
      {deleteTarget && (
        <DeleteDialog
          record={deleteTarget}
          onClose={() => setDeleteTarget(null)}
          onDone={() => { setDeleteTarget(null); loadIndex(); refreshIssueCount(); navigate('#/browse?type=perk') }}
        />
      )}
    </div>
  )
}
