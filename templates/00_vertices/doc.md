---
type: template/vertex/doc
extends: vertex
id: template:vertex:doc
name: Doc Type Template
description: Base type for documents (concrete, instantiable)
instantiable: true
tags:
  - template
  - vertex
  - doc
version: 1.0.0
created: 2025-12-27T15:00:00Z
modified: 2025-12-27T15:00:00Z
---

# Doc Type Template

**Concrete vertex type for documents.**

Docs are the base type for all document vertices in the knowledge complex. They can be directly instantiated or extended by specs and guidances.

## Type Hierarchy

```
vertex (abstract)
└── doc (concrete) ← YOU ARE HERE
    ├── spec (concrete)
    └── guidance (concrete)
```

## Inheritance

- **Extends:** `vertex`
- **Extended by:** `spec`, `guidance`
- **Instantiable:** Yes (docs can be created directly)

## Required Frontmatter Fields

Inherits all vertex fields, plus:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `vertex/doc` or subtype |
| `extends` | string | Must be `doc` (or parent for subtypes) |
| `tags` | array | Must include `[vertex, doc]` at minimum |

## Tag Requirements

The `tags` array MUST include the full inheritance chain:

```yaml
tags:
  - vertex    # base type
  - doc       # this type
```

For subtypes (spec, guidance), additional tags required:

```yaml
# For spec:
tags:
  - vertex
  - doc
  - spec

# For guidance:
tags:
  - vertex
  - doc
  - guidance
```

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `sections` | array | Section structure (for compositional docs) |
| `author` | string | Document author |
| `format` | string | Content format (markdown, yaml, etc.) |

## Body Content

Doc bodies should contain:
- Substantive content of the document
- Structured information following any specified schema
- Cross-references to related documents

## Purpose

Docs serve as vertices in assurance triangles and can be:
1. **Standalone documents** - Instantiated as `vertex/doc`
2. **Specifications** - Extended as `vertex/spec`
3. **Guidances** - Extended as `vertex/guidance`

## Relationship to Assurance Pattern

Docs participate in the assurance pattern:
- A **child doc** is verified against a **parent spec**
- A **child doc** is validated against a **parent guidance**
- The **parent spec** and **parent guidance** are coupled
- These three relationships form an **assurance face**

## Subtypes

- **spec** - Defines structural requirements and schemas
- **guidance** - Defines quality criteria and best practices

## Example Instance

```yaml
---
type: vertex/doc
extends: doc
id: v:doc:example-readme
name: Example README Document
tags:
  - vertex
  - doc
version: 1.0.0
created: 2025-01-15T10:00:00Z
modified: 2025-01-15T10:00:00Z
---

# Example README

This is a standalone document that is not a specification or guidance.

## Content

General documentation content here.
```

## Example Subtype (Spec)

```yaml
---
type: vertex/spec
extends: doc
id: v:spec:api-spec
name: API Specification
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-01-15T10:00:00Z
modified: 2025-01-15T10:00:00Z
---

# API Specification

Defines the structure and requirements for API endpoints.
```

## Validation Rules

1. **Type Format:** `type` must be `vertex/doc` or `vertex/<subtype>` where subtype extends doc
2. **Tag Chain:** Tags must include `vertex` and `doc`
3. **Instantiability:** Can be directly instantiated (unlike base `vertex`)
4. **Assurance Participation:** Docs can be child_doc in assurance faces
5. **Subtype Constraint:** Specs and guidances must extend from doc
