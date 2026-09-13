// Record view: structured form + section editors + issues + refs + raw/diff.
import React, { useEffect, useMemo, useState } from 'react'
import { api } from './api'
import type { Issue, Meta, RecordData, Refs, TreeNode } from './types'
import { ApCostEditor, AttributesEditor, buildSavePayload, CostEditor, fieldRemover, FieldWidget, GrantsEditor, OtherFieldsPanel, RequirementsEditor, stripVolatile, TagPicker } from './fields'

interface Props {
  path: string
  meta: Meta
  stems: string[]
  skills: string[]
  onNavigate: (hash: string) => void
  onSaved: () => void
  onRenameRequest: (r: RecordData) => void
  onDeleteRequest: (r: RecordData) => void
}

type Tab = 'form' | 'raw' | 'diff' | 'relations'

export function RecordView({ path, meta, stems, skills, onNavigate, onSaved, onRenameRequest, onDeleteRequest }: Props) {
  const [record, setRecord] = useState<RecordData | null>(null)
  const [orig, setOrig] = useState<RecordData | null>(null)
  const [tab, setTab] = useState<Tab>('form')
  const [saving, setSaving] = useState(false)
  const [saveErr, setSaveErr] = useState('')
  const [refs, setRefs] = useState<Refs | null>(null)
  const [tree, setTree] = useState<{ field: string; tree: TreeNode } | null>(null)
  const [raw, setRaw] = useState('')
  const [diff, setDiff] = useState('')

  useEffect(() => {
    setTab('form'); setSaveErr(''); setRefs(null); setTree(null)
    api.record(path).then((r) => { setRecord(r); setOrig(JSON.parse(JSON.stringify(r))) })
      .catch((e) => setSaveErr(String(e)))
  }, [path])

  if (!record || !orig) {
    return <div className="loading">Loading {path}… {saveErr && <span className="err">{saveErr}</span>}</div>
  }

  const dirty = JSON.stringify(stripVolatile(record)) !== JSON.stringify(stripVolatile(orig))

  // ── field mutators ──
  const setHeader = (name: string, value: string) =>
    setRecord({ ...record, headerFields: { ...record.headerFields, [name]: value } })
  const setLoose = (name: string, value: string) =>
    setRecord({ ...record, looseFields: { ...record.looseFields, [name]: value } })
  const setSection = (title: string, body: string) =>
    setRecord({ ...record, sections: record.sections.map((s) => (s.title === title ? { ...s, body } : s)) })
  const setIntro = (intro: string) => setRecord({ ...record, intro })
  const setGrants = (g: RecordData['grants']) => setRecord({ ...record, grants: g })

  // ── save ──
  const toggleDraft = async () => {
    setSaving(true); setSaveErr('')
    try {
      const saved = await api.save({ path: record.path, draft: !record.draft })
      setRecord(saved); setOrig(JSON.parse(JSON.stringify(saved)))
      onSaved()
    } catch (e) { setSaveErr(String(e)) } finally { setSaving(false) }
  }

  const save = async () => {
    setSaving(true); setSaveErr('')
    try {
      const saved = await api.save(buildSavePayload(record, orig))
      setRecord(saved)
      setOrig(JSON.parse(JSON.stringify(saved)))
      onSaved()
    } catch (e) {
      setSaveErr(String(e))
    } finally {
      setSaving(false)
    }
  }

  // ── tabs ──
  const loadRaw = () => api.raw(record.path).then((r) => setRaw(r.text))
  const loadDiff = () => api.diff(record.path).then((r) => setDiff(r.diff))
  const loadRefs = () => api.refs(record.stem).then(setRefs)
  const loadTree = () => api.tree(record.stem).then(setTree)

  const embeddables = stems.filter((s) => s.startsWith('Ability - ') || s.startsWith('Effect - '))
  const typeLabel = `${record.type}${record.subtype ? ' · ' + record.subtype : ''}`

  return (
    <div>
      <div className="record-head">
        <h1>{record.stem}</h1>
        <span className="pill type">{typeLabel}</span>
        {record.draft && <span className="pill" title="hidden from the published site">draft</span>}
        <span className="path">{record.path}</span>
        <div className="record-actions">
          {dirty && <span className="dirtydot" title="unsaved changes" />}
          <button onClick={() => onNavigate(`#/browse?type=${record.type}`)}>← Browser</button>
          <button onClick={toggleDraft} disabled={saving}>{record.draft ? 'Unmark draft' : 'Mark draft'}</button>
          <button onClick={() => onRenameRequest(record)}>Rename / Move…</button>
          <button className="danger" onClick={() => onDeleteRequest(record)}>Delete…</button>
          <button className="primary" onClick={save} disabled={saving || !dirty}>
            {saving ? 'Saving…' : 'Save'}
          </button>
        </div>
      </div>
      {saveErr && <div className="err">{saveErr}</div>}
      {dirty && <div className="savednote" style={{ color: 'var(--warn)', marginBottom: 8 }}>● unsaved changes (only the header block + sections you edited will be rewritten)</div>}

      <div style={{ display: 'flex', gap: 6, marginBottom: 14 }}>
        {(['form', 'raw', 'diff', 'relations'] as Tab[]).map((t) => (
          <button key={t} className={tab === t ? 'primary' : ''} onClick={() => {
            setTab(t)
            if (t === 'raw') loadRaw()
            if (t === 'diff') loadDiff()
            if (t === 'relations') { loadRefs(); loadTree() }
          }}>{t}</button>
        ))}
      </div>

      {tab === 'form' && (
        <>
          {(record.issues?.length ?? 0) > 0 && (
            <div className="panel issues">
              <h2>Issues ({record.issues!.length})</h2>
              {record.issues!.map((iss: Issue, i: number) => (
                <div className="issue" key={i}>
                  <span className={`sev ${iss.severity}`}>{iss.severity}</span>
                  <span>{iss.label}{iss.detail ? <span className="muted"> — {iss.detail}</span> : null}</span>
                </div>
              ))}
            </div>
          )}

          {record.schema.fields.length > 0 && (
            <div className="panel">
              <h2>Primary fields</h2>
              <div className="formgrid paircols">
                {(() => {
                  const fs = record.schema.fields
                  const nodes: React.ReactNode[] = []
                  const cell = (f: (typeof fs)[number], span2: boolean) => (
                    <React.Fragment key={f.name}>
                      <div className="lbl">{f.label}{!f.optional && <span className="req"> *</span>}</div>
                      <div className={span2 ? 'span2' : undefined}>
                        <FieldWidget name={f.name} kind={f.kind} value={record.headerFields[f.name] ?? ''}
                          onChange={(v) => setHeader(f.name, v)}
                          meta={meta} stems={stems} skills={skills} />
                      </div>
                    </React.Fragment>
                  )
                  for (let i = 0; i < fs.length;) {
                    if (fs[i].half && fs[i + 1]?.half) {
                      nodes.push(cell(fs[i], false), cell(fs[i + 1], false))
                      i += 2
                    } else {
                      nodes.push(cell(fs[i], true))
                      i += 1
                    }
                  }
                  return nodes
                })()}
              </div>
            </div>
          )}

          {/* every parsed field the schema doesn't cover — never invisible */}
          <OtherFieldsPanel record={record} orig={orig} meta={meta}
            setHeader={setHeader} setLoose={setLoose}
            onRemove={fieldRemover(setRecord, setHeader, setLoose)} />

          {record.grants !== null || ['perk'].includes(record.type) ? (
            <div className="panel">
              <h2>Grants</h2>
              <GrantsEditor grants={record.grants} onChange={setGrants} embeddables={embeddables}
                meta={meta} skills={skills} onNavigate={onNavigate}
                rawBody={record.sections.find((s) => ['grants', 'grants by stage'].includes(s.title.toLowerCase()))?.body} />
            </div>
          ) : null}

          {(record.intro.trim() || ['ability', 'effect', 'action', 'condition', 'mechanic'].includes(record.type)) && (
            <div className="panel">
              <h2>Body (text before sections)</h2>
              <textarea rows={4} value={record.intro} onChange={(e) => setIntro(e.target.value)} />
            </div>
          )}

          <div className="panel">
            <h2>Sections</h2>
            {record.type === 'perk' &&
              record.sections.some((s) => ['grants', 'grants by stage'].includes(s.title.toLowerCase())) && (
                <div className="faint" style={{ marginBottom: 10 }}>
                  ## Grants is managed in the Grants panel above — it is not shown twice here.
                </div>
              )}
            <div className="sectioned">
              {record.sections
                .filter((s) => !(record.type === 'perk' && ['grants', 'grants by stage'].includes(s.title.toLowerCase())))
                .map((s) => (
                  <div className="sec" key={s.title}>
                    <h4>{'#'.repeat(s.level)} {s.title}</h4>
                    <textarea rows={s.title === 'Short Description' ? 2 : 6} value={s.body}
                      onChange={(e) => setSection(s.title, e.target.value)} />
                  </div>
                ))}
              {record.sections.length === 0 && <div className="faint">No sections in this file.</div>}
            </div>
          </div>
        </>
      )}

      {tab === 'raw' && <pre className="raw">{raw}</pre>}
      {tab === 'diff' && (diff ? <pre className="diff">{diff}</pre> : <div className="empty">No changes vs git HEAD.</div>)}

      {tab === 'relations' && (
        <>
          <div className="panel">
            <h2>Who references this ({record.stem})</h2>
            {!refs ? <div className="faint">Loading…</div> : (
              <div className="reflist">
                <div className="muted">Embedded by ({refs.embedders.length}):</div>
                {refs.embedders.map((p) => <a key={p} onClick={() => onNavigate(`#/record?path=${encodeURIComponent(p)}`)}>{p}</a>)}
                {refs.embedders.length === 0 && <div className="faint">nobody</div>}
                <div className="muted" style={{ marginTop: 8 }}>Linked by ({refs.linkers.length}):</div>
                {refs.linkers.map((p) => <a key={p} onClick={() => onNavigate(`#/record?path=${encodeURIComponent(p)}`)}>{p}</a>)}
                {refs.linkers.length === 0 && <div className="faint">nobody</div>}
                {refs.requirers.length > 0 && (
                  <>
                    <div className="muted" style={{ marginTop: 8 }}>Required by ({refs.requirers.length}):</div>
                    {refs.requirers.map((p) => <a key={p} onClick={() => onNavigate(`#/record?path=${encodeURIComponent(p)}`)}>{p}</a>)}
                  </>
                )}
              </div>
            )}
          </div>
          {tree && (
            <div className="panel">
              <h2>{tree.field} chain</h2>
              <div className="tree"><TreeNodeView node={tree.tree} onNavigate={onNavigate} /></div>
            </div>
          )}
        </>
      )}
    </div>
  )
}

function TreeNodeView({ node, onNavigate, depth = 0 }: { node: TreeNode; onNavigate: (h: string) => void; depth?: number }) {  return (
    <div className="node">
      <a onClick={() => onNavigate(`#/record?path=${encodeURIComponent(node.path)}`)}>{node.name}</a>{' '}
      <span className="t">({node.type})</span>
      {node.children.length > 0 && (
        <ul>
          {node.children.map((c, i) => <li key={i}><TreeNodeView node={c} onNavigate={onNavigate} depth={depth + 1} /></li>)}
        </ul>
      )}
    </div>
  )
}

