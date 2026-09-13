// Structured field widgets driven by the schema field "kind".
import React, { useEffect, useMemo, useState } from 'react'
import { api } from './api'
import type { Grants, Meta, RecordData } from './types'

// ── shared: volatile-strip + save payload builder ───────────────────────────

export function stripVolatile(r: RecordData): RecordData {
  const { issues: _i, changed: _c, ...rest } = r
  return rest as RecordData
}

export function buildSavePayload(record: RecordData, orig: RecordData): Record<string, unknown> {
  const headerFields: Record<string, string> = {}
  for (const f of record.schema.fields) {
    if (f.name in record.headerFields) headerFields[f.name] = record.headerFields[f.name]
  }
  for (const [k, v] of Object.entries(record.headerFields)) {
    if (!(k in headerFields)) headerFields[k] = v
  }
  const looseFields: Record<string, string> = {}
  for (const [k, v] of Object.entries(record.looseFields)) {
    if (orig.looseFields[k] !== v) looseFields[k] = v
  }
  const sectionBodies: Record<string, string> = {}
  for (const s of record.sections) {
    const o = orig.sections.find((x) => x.title === s.title)
    if (!o || o.body !== s.body) sectionBodies[s.title] = s.body
  }
  const grantsChanged = JSON.stringify(record.grants) !== JSON.stringify(orig.grants)
  const introChanged = record.intro !== orig.intro
  return {
    path: record.path,
    headerFields,
    ...(Object.keys(looseFields).length ? { looseFields } : {}),
    ...(Object.keys(sectionBodies).length ? { sectionBodies } : {}),
    ...(grantsChanged && record.grants ? { grants: record.grants } : {}),
    ...(introChanged ? { intro: record.intro } : {}),
  }
}

// ── one widget switch used by schema fields and "other fields" alike ────────

export function FieldWidget({ name, kind, value, onChange, meta, stems, skills }:
  { name: string; kind: string; value: string; onChange: (v: string) => void
    meta: Meta; stems: string[]; skills: string[] }) {
  if (kind === 'requirements') {
    return <RequirementsEditor value={value} onChange={onChange} stems={stems} skills={skills} />
  }
  if (kind === 'attributes') {
    return <AttributesEditor value={value} onChange={onChange} codes={meta.attributeCodes} />
  }
  if (kind === 'cost') return <CostEditor value={value} onChange={onChange} />
  if (kind === 'apcost') return <ApCostEditor value={value} onChange={onChange} />
  if (kind.startsWith('tags:')) {
    const vocabKey = kind.split(':')[1] as 'perk' | 'mechanic' | 'spell'
    return <TagPicker value={value} onChange={onChange} vocab={meta.tagVocab[vocabKey] ?? []} />
  }
  if (kind === 'number') {
    return <input type="number" value={value} style={{ width: 100 }} onChange={(e) => onChange(e.target.value)} />
  }
  return <input style={{ width: '100%' }} value={value} onChange={(e) => onChange(e.target.value)} />
}

// ── requirements token editor ───────────────────────────────────────────────

export interface ReqToken { kind: string; text: string }

const REQ_KINDS = [
  { key: 'tier', label: 'Tier' },
  { key: 'skill', label: 'Skill' },
  { key: 'perk', label: 'Perk' },
  { key: 'attr', label: 'Attr' },
  { key: 'text', label: 'Free' },
]

export function parseRequirements(value: string): ReqToken[] {
  if (!value || value.trim() === '-' || value.trim() === '') return []
  return value.split(',').map((part) => {
    const t = part.trim()
    const m = t.match(/^\[\[([^\]]+)\]\](.*)$/)
    if (m) return { kind: 'perk', text: `[[${m[1]}]]${m[2].trim() ? ' ' + m[2].trim() : ''}` }
    if (/^Tier\s+\d+$/i.test(t)) return { kind: 'tier', text: t }
    if (/^(PR|WL|CH|WT|MG|EN|AG|DX|WI)\s*\d+$/i.test(t)) return { kind: 'attr', text: t }
    if (/^[A-Z][a-z]+(\/[A-Z][a-z]+)*\s+\d+(\/\s*\d+)?( or .+)?/.test(t)) return { kind: 'skill', text: t }
    return { kind: 'text', text: t }
  }).filter((tok) => tok.text)
}

export function serializeRequirements(tokens: ReqToken[]): string {
  if (tokens.length === 0) return '-'
  return tokens.map((t) => t.text.trim()).filter(Boolean).join(', ')
}

export function RequirementsEditor({ value, onChange, stems, skills }:
  { value: string; onChange: (v: string) => void; stems: string[]; skills: string[] }) {
  const tokens = useMemo(() => parseRequirements(value), [value])
  const [adding, setAdding] = useState<string | null>(null)
  const [draft, setDraft] = useState('')

  const update = (next: ReqToken[]) => onChange(serializeRequirements(next))
  const setToken = (i: number, text: string) =>
    update(tokens.map((t, j) => (i === j ? { ...t, text } : t)))
  const remove = (i: number) => update(tokens.filter((_, j) => j !== i))

  const addToken = () => {
    if (!draft.trim()) { setAdding(null); return }
    let text = draft.trim()
    if (adding === 'perk') text = `[[${text.replace(/^\[\[|\]\]$/g, '')}]]`
    update([...tokens, { kind: adding ?? 'text', text }])
    setDraft('')
    setAdding(null)
  }

  return (
    <div>
      <div className="tokenlist">
        {tokens.map((t, i) => (
          <span className="token" key={i}>
            <span className="kind">{t.kind}</span>
            <input value={t.text} onChange={(e) => setToken(i, e.target.value)}
              list={t.kind === 'perk' ? 'all-stems' : t.kind === 'skill' ? 'skill-names' : undefined}
              style={{ width: Math.max(60, t.text.length * 8) }} />
            <a className="x" onClick={() => remove(i)}>✕</a>
          </span>
        ))}
        <span className="token adder" onClick={() => { setAdding(null); update([]) }}>clear</span>
      </div>
      <div style={{ marginTop: 8, display: 'flex', gap: 6, flexWrap: 'wrap' }}>
        {REQ_KINDS.map((k) => (
          <button key={k.key} className="small" onClick={() => { setAdding(k.key); setDraft('') }}>
            + {k.label}
          </button>
        ))}
      </div>
      {adding && (
        <div className="fieldrow" style={{ marginTop: 8 }}>
          {adding === 'tier' ? (
            <select value={draft} onChange={(e) => setDraft(e.target.value)} autoFocus>
              <option value="">Tier…</option>
              {[1, 2, 3, 4, 5].map((n) => <option key={n} value={`Tier ${n}`}>Tier {n}</option>)}
            </select>
          ) : adding === 'attr' ? (
            <select value={draft} onChange={(e) => setDraft(e.target.value)} autoFocus>
              <option value="">Attribute…</option>
              {['PR', 'WL', 'CH', 'WT', 'MG', 'EN', 'AG', 'DX'].map((a) =>
                [1, 2, 3, 4].map((n) => <option key={`${a}${n}`} value={`${a} ${n}`}>{a} {n}</option>))}
            </select>
          ) : (
            <input className="grow" autoFocus value={draft}
              list={adding === 'perk' ? 'all-stems' : adding === 'skill' ? 'skill-names' : undefined}
              placeholder={adding === 'perk' ? 'Perk name…' : adding === 'skill' ? 'e.g. Medicine 2' : 'Free text…'}
              onChange={(e) => setDraft(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && addToken()} />
          )}
          <button className="small primary" onClick={addToken} disabled={!draft.trim()}>Add</button>
          <button className="small" onClick={() => setAdding(null)}>Cancel</button>
        </div>
      )}
    </div>
  )
}

// ── attributes ──────────────────────────────────────────────────────────────

export function AttributesEditor({ value, onChange, codes }:
  { value: string; onChange: (v: string) => void; codes: string[] }) {
  const parts = (value || '').trim() === '-' || !value ? [] : value.trim().split('/').map((s) => s.trim()).filter(Boolean)
  const a = parts[0] ?? ''
  const b = parts[1] ?? ''
  const opt = (v: string) => <option value={v}>{v || '—'}</option>
  const set = (first: string, second: string) => {
    const out = [first, second].filter(Boolean).join('/')
    onChange(out || '-')
  }
  const warning = parts.some((p) => p === 'WI')
  return (
    <div>
      <div className="fieldrow">
        <select value={a} onChange={(e) => set(e.target.value, e.target.value && b && e.target.value === b ? '' : b)}>
          {opt('')}{codes.map(opt)}
        </select>
        <span className="faint">/</span>
        <select value={b} onChange={(e) => set(a, e.target.value)}>
          {opt('')}{codes.map(opt)}
        </select>
        <span className="faint">("—" for none)</span>
      </div>
      {warning && <div className="err">WI is a known typo for WT — pick WT.</div>}
    </div>
  )
}

// ── cost ────────────────────────────────────────────────────────────────────

export function CostEditor({ value, onChange }: { value: string; onChange: (v: string) => void }) {
  const v = (value ?? '').trim()
  const xp = v.match(/^(\d+)\s*XP$/i)
  const variable = v.startsWith('Variable')
  const mode = xp ? 'xp' : variable ? 'variable' : v === '-' || v === '' ? 'none' : v === 'TBD' ? 'tbd' : 'custom'
  const [num, setNum] = useState(xp ? xp[1] : '5')
  const [formula, setFormula] = useState(variable ? v.replace(/^Variable\s*\(?/, '').replace(/\)$/, '') : 'Max_Wounds × level')
  const [custom, setCustom] = useState(v)

  const setMode = (m: string) => {
    if (m === 'xp') onChange(`${num} XP`)
    else if (m === 'variable') onChange(`Variable (${formula})`)
    else if (m === 'none') onChange('-')
    else if (m === 'tbd') onChange('TBD')
    else onChange(custom)
  }

  return (
    <div className="fieldrow">
      <select value={mode} onChange={(e) => setMode(e.target.value)}>
        <option value="xp">XP</option>
        <option value="variable">Variable</option>
        <option value="none">—</option>
        <option value="tbd">TBD</option>
        <option value="custom">Custom</option>
      </select>
      {mode === 'xp' && (
        <span className="fieldrow">
          <input type="number" min={1} style={{ width: 80 }} value={num}
            onChange={(e) => { setNum(e.target.value); onChange(`${e.target.value} XP`) }} /> XP
        </span>
      )}
      {mode === 'variable' && (
        <input className="grow" value={formula}
          onChange={(e) => { setFormula(e.target.value); onChange(`Variable (${e.target.value})`) }}
          placeholder="formula" />
      )}
      {mode === 'custom' && (
        <input className="grow" value={custom} onChange={(e) => { setCustom(e.target.value); onChange(e.target.value) }} />
      )}
    </div>
  )
}

// ── tag picker ──────────────────────────────────────────────────────────────

export function TagPicker({ value, onChange, vocab, allowCustom = true, collapsible = true }:
  { value: string; onChange: (v: string) => void; vocab: string[]; allowCustom?: boolean; collapsible?: boolean }) {
  const selected = (value ?? '').trim() === '-' ? [] : (value ?? '').split(/\s+/).filter((t) => t.startsWith('#'))
  const [custom, setCustom] = useState('')
  const [expanded, setExpanded] = useState(!collapsible)

  const toggle = (tag: string) => {
    const next = selected.includes(tag) ? selected.filter((t) => t !== tag) : [...selected, tag]
    onChange(next.join(' ') || '-')
  }
  const addCustom = () => {
    const t = custom.trim().startsWith('#') ? custom.trim() : `#${custom.trim()}`
    if (t !== '#' && !selected.includes(t)) onChange([...selected, t].join(' '))
    setCustom('')
  }
  const extras = selected.filter((t) => !vocab.includes(t))
  const unselected = vocab.filter((t) => !selected.includes(t))

  return (
    <div>
      <div className="tagpick">
        {selected.map((tag) => (
          <span key={tag} className={`tagchip${vocab.includes(tag) ? ' on' : ' custom on'}`} onClick={() => toggle(tag)}>{tag}</span>
        ))}
        {selected.length === 0 && <span className="faint">no tags</span>}
        {collapsible && unselected.length > 0 && (
          <button className="small ghost" onClick={() => setExpanded(!expanded)}>
            {expanded ? '▾ hide vocabulary' : `▸ vocabulary (${unselected.length})`}
          </button>
        )}
      </div>
      {expanded && unselected.length > 0 && (
        <div className="tagpick" style={{ marginTop: 6, paddingTop: 6, borderTop: '1px solid var(--line)' }}>
          {unselected.map((tag) => (
            <span key={tag} className="tagchip" onClick={() => toggle(tag)}>{tag}</span>
          ))}
        </div>
      )}
      {allowCustom && (
        <div className="fieldrow" style={{ marginTop: 8 }}>
          <input style={{ width: 160 }} value={custom} placeholder="#custom"
            onChange={(e) => setCustom(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && addCustom()} />
          <button className="small" onClick={addCustom} disabled={!custom.trim()}>Add</button>
        </div>
      )}
    </div>
  )
}

// ── "other fields" panel: every parsed field the schema doesn't cover,
//    plus fields newly added in this session ─────────────────────────────────

const ADDABLE_FIELDS = ['Trigger', 'Effect', 'Roll', 'Limit Cost', 'Duration',
  'Prerequisites', 'Progression', 'XP Cost', 'Base Target/Range', 'Traits']

export function OtherFieldsPanel({ record, meta, setHeader, setLoose, title = 'Other fields' }:
  { record: RecordData; meta: Meta
    setHeader: (name: string, v: string) => void; setLoose: (name: string, v: string) => void
    title?: string }) {
  const schemaNames = new Set(record.schema.fields.map((f) => f.name.toLowerCase()))
  const parsedNames = new Set(record.fields.map((f) => f.name.toLowerCase()))

  const items = record.fields
    .filter((f) => !schemaNames.has(f.name.toLowerCase()))
    // fields inside a section body are edited in that section's textarea —
    // their single place (no duplication like Limit Cost inside ## Effect)
    .filter((f) => !f.inSection)
    .map((f) => ({
      name: f.name, line: f.line as number, inHeader: f.inHeader,
      value: f.inHeader
        ? (record.headerFields[f.name] ?? f.value)
        : (record.looseFields[f.name] ?? f.value),
    }))
  // fields added via "+ Add field" that aren't in the file yet
  for (const [name, value] of Object.entries(record.looseFields)) {
    if (!parsedNames.has(name.toLowerCase()) && !schemaNames.has(name.toLowerCase())) {
      items.push({ name, line: -1, inHeader: false, value })
    }
  }
  if (items.length === 0 && ADDABLE_FIELDS.length === 0) return null

  const present = new Set([...record.fields.map((f) => f.name.toLowerCase()),
    ...Object.keys(record.headerFields).map((k) => k.toLowerCase()),
    ...Object.keys(record.looseFields).map((k) => k.toLowerCase())])
  const addable = ADDABLE_FIELDS.filter((n) => !present.has(n.toLowerCase()))

  return <OtherFieldsPanelInner items={items} addable={addable} meta={meta}
    setHeader={setHeader} setLoose={setLoose} title={title} />
}

function OtherFieldsPanelInner({ items, addable, meta, setHeader, setLoose, title }: {
  items: { name: string; line: number; inHeader: boolean; value: string }[]
  addable: string[]; meta: Meta
  setHeader: (name: string, v: string) => void; setLoose: (name: string, v: string) => void
  title: string
}) {
  const [adding, setAdding] = useState('')
  const kindFor = (name: string): string => {
    const n = name.toLowerCase()
    if (n === 'tags' || n === 'traits') return 'tags:mechanic'
    if (n === 'requirements') return 'requirements'
    if (n === 'attributes') return 'attributes'
    if (n === 'cost') return 'cost'
    if (n === 'ap cost') return 'apcost'
    if (n === 'tier') return 'number'
    return 'text'
  }
  return (
    <div className="panel">
      <h2>{title}</h2>
      <div className="formgrid">
        {items.map((f, i) => {
          const dup = items.some((g, j) => j !== i && g.name.toLowerCase() === f.name.toLowerCase())
          return (
            <React.Fragment key={`${f.name}-${f.line}`}>
              <div className="lbl">{f.name}{dup && <span className="faint"> (line {f.line})</span>}</div>
              <div>
                <FieldWidget name={f.name} kind={kindFor(f.name)} value={f.value}
                  onChange={(v) => (f.inHeader ? setHeader(f.name, v) : setLoose(f.name, v))}
                  meta={meta} stems={[]} skills={[]} />
              </div>
            </React.Fragment>
          )
        })}
      </div>
      {addable.length > 0 && (
        <div className="fieldrow" style={{ marginTop: 10 }}>
          <span className="faint">add field:</span>
          <select value={adding} onChange={(e) => setAdding(e.target.value)}>
            <option value="">choose…</option>
            {addable.map((n) => <option key={n} value={n}>{n}</option>)}
          </select>
          <button className="small" onClick={() => { setLoose(adding, ''); setAdding('') }} disabled={!adding}>
            + Add
          </button>
          <span className="faint">creates a **Name:** line in the file on save</span>
        </div>
      )}
    </div>
  )
}

// ── grants editor ───────────────────────────────────────────────────────────

// Inline editor for one granted ability/effect — edit it without leaving
// the perk view.
export function InlineGrantEditor({ target, meta, stems, skills, onNavigate }:
  { target: string; meta: Meta; stems: string[]; skills: string[]; onNavigate: (h: string) => void }) {
  const [record, setRecord] = useState<RecordData | null>(null)
  const [orig, setOrig] = useState<RecordData | null>(null)
  const [err, setErr] = useState('')
  const [savedNote, setSavedNote] = useState('')
  const [busy, setBusy] = useState(false)

  useEffect(() => {
    setRecord(null); setErr(''); setSavedNote('')
    api.resolve(target)
      .then((p) => api.record(p))
      .then((r) => { setRecord(r); setOrig(JSON.parse(JSON.stringify(r))) })
      .catch((e) => setErr(String(e)))
  }, [target])

  if (err) return <div className="err">{err}</div>
  if (!record || !orig) return <div className="faint">Loading {target}…</div>

  const dirty = JSON.stringify(stripVolatile(record)) !== JSON.stringify(stripVolatile(orig))
  const setHeader = (name: string, value: string) =>
    setRecord({ ...record, headerFields: { ...record.headerFields, [name]: value } })
  const setLoose = (name: string, value: string) =>
    setRecord({ ...record, looseFields: { ...record.looseFields, [name]: value } })
  const setSection = (title: string, body: string) =>
    setRecord({ ...record, sections: record.sections.map((s) => (s.title === title ? { ...s, body } : s)) })
  const setIntro = (intro: string) => setRecord({ ...record, intro })

  const save = async () => {
    setBusy(true); setErr(''); setSavedNote('')
    try {
      const saved = await api.save(buildSavePayload(record, orig))
      setRecord(saved); setOrig(JSON.parse(JSON.stringify(saved)))
      setSavedNote('saved ✓')
    } catch (e) { setErr(String(e)) } finally { setBusy(false) }
  }

  const schemaNames = new Set(record.schema.fields.map((f) => f.name.toLowerCase()))
  void schemaNames

  return (
    <div className="inlinegrant">
      <div className="fieldrow" style={{ marginBottom: 8 }}>
        <span className="pill type">{record.type}</span>
        <span className="faint">{record.path}</span>
        {dirty && <span className="dirtydot" title="unsaved changes" />}
        <span style={{ flex: 1 }} />
        {savedNote && <span className="savednote">{savedNote}</span>}
        <button className="small" onClick={() => onNavigate(`#/record?path=${encodeURIComponent(record.path)}`)}>open full ↗</button>
        <button className="small primary" onClick={save} disabled={busy || !dirty}>{busy ? 'Saving…' : 'Save'}</button>
      </div>
      {err && <div className="err">{err}</div>}
      {record.schema.fields.length > 0 && (
        <div className="formgrid">
          {record.schema.fields.map((f) => (
            <React.Fragment key={f.name}>
              <div className="lbl">{f.label}</div>
              <div>
                <FieldWidget name={f.name} kind={f.kind} value={record.headerFields[f.name] ?? ''}
                  onChange={(v) => setHeader(f.name, v)} meta={meta} stems={stems} skills={skills} />
              </div>
            </React.Fragment>
          ))}
        </div>
      )}
      <OtherFieldsPanel record={record} meta={meta} setHeader={setHeader} setLoose={setLoose} title="Other fields" />
      {record.intro.trim() !== '' && (
        <div style={{ marginTop: 8 }}>
          <div className="lbl faint">body</div>
          <textarea rows={3} value={record.intro} onChange={(e) => setIntro(e.target.value)} />
        </div>
      )}
      {record.sections.map((s) => (
        <div key={s.title} style={{ marginTop: 8 }}>
          <div className="lbl faint">## {s.title}</div>
          <textarea rows={Math.min(6, Math.max(2, s.body.split('\n').length))} value={s.body}
            onChange={(e) => setSection(s.title, e.target.value)} />
        </div>
      ))}
    </div>
  )
}

export function GrantsEditor({ grants, onChange, embeddables, meta, skills, onNavigate, rawBody }:
  { grants: Grants | null; onChange: (g: Grants) => void; embeddables: string[]
    meta?: Meta; skills?: string[]; onNavigate?: (h: string) => void; rawBody?: string }) {
  const g: Grants = grants ?? { mode: 'simple', title: 'Grants', stages: null, embeds: [] }
  const [adding, setAdding] = useState('')
  const [custom, setCustom] = useState('')
  const [editing, setEditing] = useState<string | null>(null)

  // non-embed content in the raw section would be lost on regen — surface it
  const strayLines = (rawBody ?? '').split('\n').filter((l) => {
    const t = l.trim()
    if (t === '' || t.startsWith('![')) return false
    if (/^-\s*\*\*Stage \d+:\*\*/i.test(t)) return false
    if (/^\*\*Stage \d+:\*\*/i.test(t)) return false
    return true
  })

  const setEmbeds = (embeds: string[]) => onChange({ ...g, mode: 'simple', embeds })
  const move = (i: number, dir: -1 | 1) => {
    const j = i + dir
    if (j < 0 || j >= g.embeds.length) return
    const next = [...g.embeds]
    ;[next[i], next[j]] = [next[j], next[i]]
    setEmbeds(next)
  }

  const addEmbed = (target: string) => {
    if (!target) return
    if (g.mode === 'simple') setEmbeds([...g.embeds, target])
    else {
      const stages = { ...(g.stages ?? {}) }
      const keys = Object.keys(stages).map(Number).sort((a, b) => a - b)
      const last = keys.length ? keys[keys.length - 1] : 0
      stages[String(last + 1)] = [target]
      onChange({ ...g, mode: 'staged', stages })
    }
    setAdding('')
    setCustom('')
  }

  return (
    <div>
      <div className="fieldrow" style={{ marginBottom: 10 }}>
        <select value={g.mode} onChange={(e) => {
          if (e.target.value === 'simple') onChange({ ...g, mode: 'simple', stages: null, embeds: g.embeds })
          else onChange({ ...g, mode: 'staged', title: 'Grants by Stage', stages: g.stages ?? { '1': g.embeds } })
        }}>
          <option value="simple">Simple (single grant list)</option>
          <option value="staged">Staged (Grants by Stage — leveled perks)</option>
        </select>
        {strayLines.length > 0 && (
          <span className="pill bad" title={`Saving grants will drop this text:\n${strayLines.join('\n')}`}>
            {strayLines.length} stray line(s) in section
          </span>
        )}
      </div>

      {g.mode === 'simple' ? (
        <div className="grantlist">
          {g.embeds.map((e, i) => (
            <div className="grantwrap" key={i}>
              <div className="grantrow">
                <span className="ord">#{i + 1}</span>
                <span className={`pill ${e.startsWith('Ability - ') ? 'good' : 'tag'}`}>
                  {e.startsWith('Ability - ') ? 'ability' : 'effect'}
                </span>
                <span className="grow">{e}</span>
                {onNavigate && meta && (
                  <button className="small" onClick={() => setEditing(editing === e ? null : e)}>
                    {editing === e ? 'close' : 'edit inline'}
                  </button>
                )}
                <button className="small" onClick={() => move(i, -1)} disabled={i === 0}>↑</button>
                <button className="small" onClick={() => move(i, 1)} disabled={i === g.embeds.length - 1}>↓</button>
                <button className="small danger" onClick={() => setEmbeds(g.embeds.filter((_, j) => j !== i))}>✕</button>
              </div>
              {editing === e && onNavigate && meta && (
                <InlineGrantEditor target={e} meta={meta}
                  stems={[]} skills={skills ?? []} onNavigate={onNavigate} />
              )}
            </div>
          ))}
          {g.embeds.length === 0 && <div className="faint">No embeds — this perk will fail the consistency check.</div>}
        </div>
      ) : (
        <div className="grantlist">
          {Object.keys(g.stages ?? {}).map(Number).sort((a, b) => a - b).map((n) => (
            <div className="grantrow" key={n}>
              <span className="ord">Stage {n}</span>
              <span className="grow">{(g.stages ?? {})[String(n)].join(' + ')}</span>
              <button className="small danger" onClick={() => {
                const stages = { ...(g.stages ?? {}) }
                delete stages[String(n)]
                onChange({ ...g, stages })
              }}>✕</button>
            </div>
          ))}
        </div>
      )}

      <div className="fieldrow" style={{ marginTop: 10 }}>
        <select value={adding} onChange={(e) => setAdding(e.target.value)}>
          <option value="">Add ability/effect…</option>
          <optgroup label="Abilities">
            {embeddables.filter((s) => s.startsWith('Ability - ')).map((s) => <option key={s} value={s}>{s}</option>)}
          </optgroup>
          <optgroup label="Effects">
            {embeddables.filter((s) => s.startsWith('Effect - ')).map((s) => <option key={s} value={s}>{s}</option>)}
          </optgroup>
        </select>
        <input style={{ width: 220 }} value={custom} placeholder="or type name (creates broken link)"
          onChange={(e) => setCustom(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && addEmbed(custom)} />
        <button className="small primary" onClick={() => addEmbed(adding || custom)} disabled={!(adding || custom.trim())}>Add</button>
      </div>
    </div>
  )
}

// ── AP cost ─────────────────────────────────────────────────────────────────

export function ApCostEditor({ value, onChange }: { value: string; onChange: (v: string) => void }) {
  const [custom, setCustom] = useState(value)
  const quick = ['1', '2', '3', '4', '5', 'R', '-', '+1', '+2', '+3']
  const isQuick = quick.includes((value ?? '').trim())
  return (
    <div className="fieldrow">
      {quick.map((q) => (
        <button key={q} className={`small${(value ?? '').trim() === q ? ' primary' : ''}`}
          onClick={() => { onChange(q); setCustom(q) }}>{q}</button>
      ))}
      <input style={{ width: 200 }} value={isQuick ? '' : custom} placeholder="custom (e.g. 1 minute)"
        onChange={(e) => { setCustom(e.target.value); onChange(e.target.value) }} />
    </div>
  )
}
