// Vault-wide issues page (from the imported consistency checker) and the
// session changes panel.
import React, { useEffect, useState } from 'react'
import { api } from './api'
import type { CheckResults, SessionData } from './types'

export function IssuesPage({ onNavigate }: { onNavigate: (hash: string) => void }) {
  const [res, setRes] = useState<CheckResults | null>(null)
  const [minSev, setMinSev] = useState('low')
  const [err, setErr] = useState('')

  const load = (force = false) => api.checks(force).then(setRes).catch((e) => setErr(String(e)))
  useEffect(() => { load() }, [])

  if (err) return <div className="err">{err}</div>
  if (!res) return <div className="loading">Running tools/consistency_check.py over the vault…</div>

  const go = (file: string) => onNavigate(`#/record?path=${encodeURIComponent(file)}`)
  const sevRank: Record<string, number> = { high: 0, medium: 1, low: 2 }
  const sevOk = (s: string) => sevRank[s] <= sevRank[minSev]

  const group = (title: string, count: number, body: React.ReactNode) =>
    count > 0 ? (
      <div className="issuegroup">
        <h2>{title} <span className="cnt">— {count}</span></h2>
        {body}
      </div>
    ) : null

  const legacyBySev = res.legacy.filter((l) => sevOk(l.severity))

  return (
    <div className="issuespage">
      <div style={{ display: 'flex', gap: 10, alignItems: 'center', marginBottom: 16 }}>
        <h1 style={{ margin: 0 }}>Vault issues</h1>
        <span className="faint">{res.fileCount} files scanned</span>
        <label className="muted">min severity
          <select value={minSev} onChange={(e) => setMinSev(e.target.value)} style={{ marginLeft: 6 }}>
            <option value="high">high</option>
            <option value="medium">medium</option>
            <option value="low">low</option>
          </select>
        </label>
        <button onClick={() => load(true)}>Re-run</button>
      </div>
      {res.staleChecks.length > 0 && (
        <div className="panel" style={{ borderColor: 'var(--warn)' }}>
          <h2>Known-stale checks (kept for parity with the pipeline)</h2>
          {res.staleChecks.map((s) => <div key={s} className="muted">• {s}</div>)}
        </div>
      )}
      {res.exemptFiles && Object.keys(res.exemptFiles).length > 0 && (
        <div className="panel">
          <h2>Exempt from checks ({Object.keys(res.exemptFiles).length})</h2>
          {Object.entries(res.exemptFiles).map(([file, reason]) => (
            <div key={file} className="muted">• {file} <span className="faint">— {reason}</span></div>
          ))}
        </div>
      )}

      {group('Legacy / grid drift', legacyBySev.length,
        legacyBySev.map((l, i) => (
          <div className="issueline" key={i}>
            <span className={`sev ${l.severity}`}>{l.severity}</span>
            <span className="file" onClick={() => go(l.file)}>{l.file}:{l.line}</span>
            <span>{l.label}</span>
            <span className="snippet">{l.snippet}</span>
          </div>
        )))}

      {group('Broken embeds', res.brokenEmbeds.length,
        res.brokenEmbeds.map((e, i) => (
          <div className="issueline" key={i}>
            <span className="sev high">high</span>
            <span className="file" onClick={() => go(e.file)}>{e.file}:{e.line}</span>
            <span>→ {e.target}</span>
          </div>
        )))}

      {group('Broken links', res.brokenLinks.length,
        res.brokenLinks.map((l, i) => (
          <div className="issueline" key={i}>
            <span className="sev high">high</span>
            <span className="file" onClick={() => go(l.file)}>{l.file}:{l.line}</span>
            <span>→ {l.target}</span>
          </div>
        )))}

      {group('Links into Deprecated/UNEDITED', res.deprecatedRefs.length,
        res.deprecatedRefs.map((d, i) => (
          <div className="issueline" key={i}>
            <span className="sev medium">med</span>
            <span className="file" onClick={() => go(d.file)}>{d.file}:{d.line}</span>
            <span>→ {d.target}</span>
          </div>
        )))}

      {group('Duplicate filenames', res.duplicates.length,
        res.duplicates.map((d, i) => (
          <div key={i}>
            <div className="issueline">
              <span className="sev high">high</span><span>{d.name}</span>
            </div>
            {d.paths.map((p) => <div className="issueline" key={p}><span className="file" onClick={() => go(p)}>{p}</span></div>)}
          </div>
        )))}

      {group('Perk template violations', res.perkViolations.length,
        res.perkViolations.map((v, i) => (
          <div className="issueline" key={i}>
            <span className="sev high">high</span>
            <span className="file" onClick={() => go(v.file)}>{v.file}</span>
            <span>{v.issues.join('; ')}</span>
          </div>
        )))}

      {group('Spell template violations', res.spellViolations.length,
        res.spellViolations.map((v, i) => (
          <div className="issueline" key={i}>
            {v.issues.some((s) => res.staleChecks.includes(s))
              ? <span className="sev low">stale</span> : <span className="sev high">high</span>}
            <span className="file" onClick={() => go(v.file)}>{v.file}</span>
            <span>{v.issues.filter((s) => !res.staleChecks.includes(s)).join('; ') || '(only stale checks)'}</span>
          </div>
        )))}

      {group('Old attribute codes', res.deprecatedAttr.length,
        res.deprecatedAttr.map((h, i) => (
          <div className="issueline" key={i}>
            <span className="sev medium">med</span>
            <span className="file" onClick={() => go(h.file)}>{h.file}:{h.line}</span>
            <span>{h.label}</span>
            <span className="snippet">{h.snippet}</span>
          </div>
        )))}

      {group('Editor extras (quirks, empty stubs)', res.editorExtras.length,
        res.editorExtras.map((h, i) => (
          <div className="issueline" key={i}>
            <span className={`sev ${h.severity}`}>{h.severity}</span>
            <span className="file" onClick={() => go(h.file)}>{h.file}{h.line ? `:${h.line}` : ''}</span>
            <span>{h.label}</span>
          </div>
        )))}
    </div>
  )
}

export function SessionPanel({ onNavigate }: { onNavigate: (hash: string) => void }) {
  const [data, setData] = useState<SessionData | null>(null)
  useEffect(() => { api.session().then(setData) }, [])
  if (!data) return <div className="loading">Loading session…</div>

  return (
    <div>
      <h1 style={{ fontSize: 18, marginTop: 0 }}>This session</h1>
      <div className="panel">
        <h2>Editor writes ({data.writes.length})</h2>
        <div className="sessionlist">
          {data.writes.length === 0 && <div className="faint">Nothing written yet this session.</div>}
          {data.writes.slice().reverse().map((w, i) => (
            <div className="w" key={i}>
              <span className="action">{w.action}</span>
              <a onClick={() => onNavigate(`#/record?path=${encodeURIComponent('source/content/' + w.path.replace(/^source\/content\//, ''))}`)}
                style={{ cursor: 'pointer' }}>{w.path}</a>
              <span className="at">{w.at}</span>
            </div>
          ))}
        </div>
      </div>
      <div className="panel">
        <h2>git status (source/content)</h2>
        <div className="sessionlist">
          {data.gitStatus.length === 0 && <div className="faint">Clean — nothing modified vs git.</div>}
          {data.gitStatus.map((s, i) => (
            <div className="w" key={i}>
              <span className="action">{s.status}</span>
              <span>{s.path}</span>
            </div>
          ))}
        </div>
        <div className="faint" style={{ marginTop: 10 }}>
          The editor never commits — review with git and commit from your usual tooling.
        </div>
      </div>
    </div>
  )
}
