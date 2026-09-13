// Thin fetch wrapper over the editor's JSON API.

async function req<T>(url: string, init?: RequestInit): Promise<T> {
  const res = await fetch(url, init)
  if (!res.ok) {
    let detail = res.statusText
    try {
      const body = await res.json()
      detail = body.detail ?? JSON.stringify(body)
    } catch { /* keep statusText */ }
    throw new Error(`${res.status}: ${detail}`)
  }
  return res.json()
}

export const api = {
  meta: () => req<import('./types').Meta>('/api/meta'),
  index: (type?: string, q?: string, fullText?: boolean) => {
    const p = new URLSearchParams()
    if (type) p.set('type', type)
    if (q) p.set('q', q)
    if (fullText) p.set('fullText', 'true')
    const qs = p.toString()
    return req<import('./types').IndexRow[]>(`/api/index${qs ? `?${qs}` : ''}`)
  },
  record: (path: string) => req<import('./types').RecordData>(`/api/record?path=${encodeURIComponent(path)}`),
  raw: (path: string) => req<{ path: string; text: string }>(`/api/raw?path=${encodeURIComponent(path)}`),
  read: (path: string) => req<import('./types').ReadData>(`/api/read?path=${encodeURIComponent(path)}`),
  rulebook: () => req<import('./types').RulebookData>('/api/rulebook'),
  resolve: (stem: string) => req<string>(`/api/resolve?stem=${encodeURIComponent(stem)}`),
  diff: (path: string) => req<{ path: string; diff: string }>(`/api/diff?path=${encodeURIComponent(path)}`),
  save: (body: object) => req<import('./types').RecordData>('/api/record', {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  }),
  create: (body: object) => req<import('./types').RecordData>('/api/create', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  }),
  rename: (body: object) => req<import('./types').RenamePlan & { preview: boolean; result?: object }>('/api/rename', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  }),
  delete: (body: object) => req<{ preview: boolean; file: string; inboundReferences: { file: string; line: number; reference: string }[] }>('/api/delete', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  }),
  checks: (force = false) => req<import('./types').CheckResults>(`/api/checks${force ? '?force=true' : ''}`),
  refs: (stem: string) => req<import('./types').Refs>(`/api/refs?stem=${encodeURIComponent(stem)}`),
  tree: (stem: string) => req<{ root: string; field: string; tree: import('./types').TreeNode }>(`/api/tree?stem=${encodeURIComponent(stem)}`),
  session: () => req<import('./types').SessionData>('/api/session'),
  selftest: () => req<{ files: number; failures: string[]; ok: boolean }>('/api/selftest'),
}
