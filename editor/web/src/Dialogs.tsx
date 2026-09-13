// Create / Rename / Delete dialogs with previews.
import React, { useMemo, useState } from 'react'
import { api } from './api'
import type { Meta, RecordData, RenamePlan } from './types'

// ── create ──────────────────────────────────────────────────────────────────

export function CreateDialog({ meta, stems, onClose, onCreated }:
  { meta: Meta; stems: string[]; onClose: () => void; onCreated: (path: string) => void }) {
  const [scaffold, setScaffold] = useState('perk')
  const [name, setName] = useState('')
  const [folder, setFolder] = useState('')
  const [err, setErr] = useState('')
  const [busy, setBusy] = useState(false)

  const scaffoldDef = meta.scaffolds.find((s) => s.key === scaffold)
  const effectiveName = useMemo(() => {
    const prefix = scaffoldDef?.namePrefix ?? ''
    return prefix && !name.startsWith(prefix) ? prefix + name : name
  }, [name, scaffoldDef])

  const folderOptions = useMemo(() => {
    if (!scaffoldDef) return []
    const f = scaffoldDef.defaultFolder
    if (f.startsWith('Perks')) return meta.folders.perks
    if (f.startsWith('Spells')) return meta.folders.spells
    if (f.startsWith('Actions')) return meta.folders.actions
    if (f.startsWith('Rules')) return meta.folders.rules
    return meta.folders.all
  }, [scaffoldDef, meta])

  const dupWarning = useMemo(
    () => (effectiveName && stems.includes(effectiveName)
      ? `A file named '${effectiveName}' already exists — duplicates are forbidden.` : ''),
    [effectiveName, stems])

  const create = async () => {
    setBusy(true); setErr('')
    try {
      const rec = await api.create({ scaffold, name, folder: folder || scaffoldDef!.defaultFolder })
      onCreated(rec.path)
    } catch (e) {
      setErr(String(e))
    } finally {
      setBusy(false)
    }
  }

  return (
    <div className="overlay" onClick={(e) => e.target === e.currentTarget && onClose()}>
      <div className="dialog">
        <h2>New from template</h2>
        <div className="row">
          <label>Template</label>
          <select value={scaffold} onChange={(e) => setScaffold(e.target.value)}>
            {meta.scaffolds.map((s) => <option key={s.key} value={s.key}>{s.label}</option>)}
          </select>
        </div>
        <div className="row">
          <label>Name</label>
          <input value={name} onChange={(e) => setName(e.target.value)}
            placeholder={scaffoldDef?.namePrefix ? `${scaffoldDef.namePrefix}…` : 'Name'} autoFocus />
          <span className="faint" style={{ whiteSpace: 'nowrap' }}>→ {effectiveName || '…'}.md</span>
        </div>
        <div className="row">
          <label>Folder</label>
          <select value={folder || scaffoldDef?.defaultFolder || ''} onChange={(e) => setFolder(e.target.value)}>
            {(folderOptions.length ? folderOptions : [scaffoldDef?.defaultFolder ?? '']).map((f) => (
              <option key={f} value={f}>{f}</option>
            ))}
          </select>
        </div>
        {dupWarning && <div className="err">{dupWarning}</div>}
        {err && <div className="err">{err}</div>}
        <div className="actions">
          <button onClick={onClose}>Cancel</button>
          <button className="primary" onClick={create} disabled={!name.trim() || !!dupWarning || busy}>
            {busy ? 'Creating…' : 'Create'}
          </button>
        </div>
      </div>
    </div>
  )
}

// ── rename / move ───────────────────────────────────────────────────────────

export function RenameDialog({ record, meta, onClose, onDone }:
  { record: RecordData; meta: Meta; onClose: () => void; onDone: (newPath: string) => void }) {
  const [newName, setNewName] = useState(record.stem)
  const [newFolder, setNewFolder] = useState(record.folder)
  const [plan, setPlan] = useState<(RenamePlan & { preview: boolean }) | null>(null)
  const [err, setErr] = useState('')
  const [busy, setBusy] = useState(false)

  const preview = async () => {
    setErr(''); setBusy(true)
    try {
      const p = await api.rename({ path: record.path, newName, newFolder })
      setPlan(p)
    } catch (e) {
      setErr(String(e))
    } finally {
      setBusy(false)
    }
  }

  const apply = async () => {
    setErr(''); setBusy(true)
    try {
      await api.rename({ path: record.path, newName, newFolder, apply: true })
      onDone(plan!.to)
    } catch (e) {
      setErr(String(e))
    } finally {
      setBusy(false)
    }
  }

  const folderOptions = record.path.startsWith('Perks') ? meta.folders.perks
    : record.path.startsWith('Spells') ? meta.folders.spells
      : record.path.startsWith('Actions') ? meta.folders.actions
        : record.path.startsWith('Rules') ? meta.folders.rules : meta.folders.all

  return (
    <div className="overlay" onClick={(e) => e.target === e.currentTarget && onClose()}>
      <div className="dialog">
        <h2>Rename / move {record.stem}</h2>
        <div className="row">
          <label>New name</label>
          <input value={newName} onChange={(e) => { setNewName(e.target.value); setPlan(null) }} autoFocus />
        </div>
        <div className="row">
          <label>Folder</label>
          <select value={newFolder} onChange={(e) => { setNewFolder(e.target.value); setPlan(null) }}>
            {[...new Set([record.folder, ...folderOptions])].map((f) => (
              <option key={f} value={f}>{f}</option>
            ))}
          </select>
        </div>
        {err && <div className="err">{err}</div>}
        {plan && (
          <div>
            <h3 style={{ fontSize: 13 }}>Preview — {plan.referenceChanges.length} reference(s) will be updated:</h3>
            {plan.referenceChanges.slice(0, 100).map((c, i) => (
              <div className="changeitem" key={i}>
                <span className="file">{c.file}:{c.line}</span><br />
                <span className="before">{c.before}</span> → <span className="after">{c.after}</span>
              </div>
            ))}
            {plan.referenceChanges.length > 100 && <div className="faint">… +{plan.referenceChanges.length - 100} more</div>}
            {plan.referenceChanges.length === 0 && <div className="faint">No references point at this file.</div>}
          </div>
        )}
        <div className="actions">
          <button onClick={onClose}>Cancel</button>
          {!plan && <button onClick={preview} disabled={busy}>Preview changes</button>}
          {plan && <button className="primary" onClick={apply} disabled={busy}>{busy ? 'Applying…' : 'Apply rename'}</button>}
        </div>
      </div>
    </div>
  )
}

// ── delete ──────────────────────────────────────────────────────────────────

export function DeleteDialog({ record, onClose, onDone }:
  { record: RecordData; onClose: () => void; onDone: () => void }) {
  const [inbound, setInbound] = useState<{ file: string; line: number; reference: string }[] | null>(null)
  const [busy, setBusy] = useState(false)
  const [err, setErr] = useState('')

  React.useEffect(() => {
    api.delete({ path: record.path }).then((r) => setInbound(r.inboundReferences)).catch((e) => setErr(String(e)))
  }, [record.path])

  const del = async () => {
    setBusy(true); setErr('')
    try {
      await api.delete({ path: record.path, apply: true })
      onDone()
    } catch (e) {
      setErr(String(e))
    } finally {
      setBusy(false)
    }
  }

  return (
    <div className="overlay" onClick={(e) => e.target === e.currentTarget && onClose()}>
      <div className="dialog">
        <h2>Delete {record.path}?</h2>
        {err && <div className="err">{err}</div>}
        {inbound === null ? <div className="faint">Checking inbound references…</div> : (
          <>
            {inbound.length > 0 ? (
              <div>
                <div className="err">{inbound.length} reference(s) will break (they are NOT updated):</div>
                {inbound.slice(0, 50).map((i, k) => (
                  <div className="changeitem" key={k}>
                    <span className="file">{i.file}:{i.line}</span> — {i.reference}
                  </div>
                ))}
              </div>
            ) : <div className="muted">No other file references this one.</div>}
            <div className="faint" style={{ marginTop: 10 }}>Deletable via git if you change your mind.</div>
          </>
        )}
        <div className="actions">
          <button onClick={onClose}>Cancel</button>
          <button className="danger" onClick={del} disabled={busy || inbound === null}>Delete file</button>
        </div>
      </div>
    </div>
  )
}
