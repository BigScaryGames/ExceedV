// Shared model types mirroring the server's JSON shapes.

export type FieldType =
  | 'perk' | 'spell' | 'ability' | 'effect' | 'action'
  | 'condition' | 'mechanic' | 'rule' | 'template' | 'doc'

export interface IndexRow {
  path: string
  stem: string
  name: string
  type: FieldType
  subtype: string
  folder: string
  columns: Record<string, string | number>
  requirements: string
  attributes: string
  cost: string
  apCost: string
  tier: string
  tags: string[]
  attrCodes: string[]
  hasEmbeds: boolean
  grantCount: number
  leveled: boolean
}

export interface SchemaField {
  name: string
  kind: string
  label: string
  optional?: boolean
}

export interface Schema {
  fields: SchemaField[]
  sections: string[]
  looseFields?: string[]
  tableColumns: string[]
}

export interface SectionInfo {
  title: string
  level: number
  line: number | null
  body: string
  embeds: string[]
  links: string[]
}

export interface Issue {
  severity: 'high' | 'medium' | 'low' | string
  label: string
  detail?: string
}

export interface Grants {
  mode: 'simple' | 'staged'
  title: string
  stages: Record<string, string[]> | null
  embeds: string[]
}

export interface RecordData {
  path: string
  stem: string
  type: FieldType
  subtype: string
  folder: string
  draft?: boolean
  schema: Schema
  headerFields: Record<string, string>
  looseFields: Record<string, string>
  fields: { name: string; value: string; line: number; inHeader: boolean; inSection?: string | null }[]
  intro: string
  sections: SectionInfo[]
  grants: Grants | null
  embeds: string[]
  links: string[]
  attrCodesValid: boolean
  issues?: Issue[]
  changed?: boolean
}

export interface Meta {
  attributeCodes: string[]
  categoryTags: string[]
  tagVocab: { perk: string[]; mechanic: string[]; spell: string[] }
  headerFields: Record<string, string[]>
  folders: {
    perks: string[]
    spells: string[]
    rules: string[]
    actions: string[]
    all: string[]
  }
  scaffolds: { key: string; label: string; defaultFolder: string; namePrefix: string }[]
  typeCounts: Record<string, number>
}

export interface CheckResults {
  fileCount: number
  legacy: { file: string; line: number; label: string; severity: string; snippet: string }[]
  brokenEmbeds: { file: string; line: number; target: string; snippet: string }[]
  brokenLinks: { file: string; line: number; target: string; snippet: string }[]
  deprecatedRefs: { file: string; line: number; target: string; snippet: string }[]
  duplicates: { name: string; paths: string[] }[]
  perkViolations: { file: string; issues: string[] }[]
  spellViolations: { file: string; issues: string[] }[]
  deprecatedAttr: { file: string; line: number; label: string; snippet: string }[]
  staleChecks: string[]
  editorExtras: { file: string; line: number | null; severity: string; label: string; paths?: string[] }[]
  exemptFiles?: Record<string, string>
}

export interface Refs {
  stem: string
  embedders: string[]
  linkers: string[]
  requirers: string[]
  prerequisites: string[]
}

export interface TreeNode {
  path: string
  name: string
  type: string
  children: TreeNode[]
}

export interface SessionData {
  writes: { path: string; action: string; at: string }[]
  gitStatus: { status: string; path: string }[]
}

export interface RenamePlan {
  from: string
  to: string
  stemChanged: boolean
  folderChanged: boolean | string
  referenceChanges: { file: string; line: number; before: string; after: string }[]
}

export interface ReadData {
  path: string
  name: string
  draft: boolean
  content: string
  embeds: { target: string; path: string | null; name: string }[]
}

export interface RulebookNode {
  path: string
  name: string
  draft: boolean
  children: RulebookNode[]
  brokenEmbeds: string[]
  unwired: string[]
}

export interface RulebookData {
  root: RulebookNode | null
  drafts: string[]
  issues: { file: string; severity: string; label: string }[]
}
