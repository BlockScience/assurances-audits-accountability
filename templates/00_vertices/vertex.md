---
type: template/vertex
extends: null
id: template:vertex
name: Vertex Type Template
description: Base type for all 0-simplices (vertices)
instantiable: false
tags:
  - template
  - vertex
version: 1.0.0
created: 2025-12-27T15:00:00Z
modified: 2025-12-27T15:00:00Z
---

# Vertex Type Template

**Base type for all 0-simplices in the knowledge complex.**

## Type Hierarchy

```
vertex (base, abstract)
├── doc (concrete)
│   ├── spec (concrete)
│   └── guidance (concrete)
├── actor (concrete)
│   ├── individual (concrete)
│   │   └── staff (concrete)
│   └── group (concrete)
│       └── team (concrete)
└── property (concrete)
    └── role (concrete)
```

## Required Frontmatter Fields

All vertices MUST include:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Element type (format: `vertex/<subtype>`) |
| `extends` | string\|null | Parent type (null for base vertex) |
| `id` | string | Unique identifier (format: `v:<domain>:<name>`) |
| `name` | string | Human-readable name |
| `tags` | array | Full inheritance chain (must include 'vertex') |
| `version` | string | Semantic version |
| `created` | datetime | Creation timestamp (ISO 8601) |
| `modified` | datetime | Last modification timestamp (ISO 8601) |

## Tag Requirements

The `tags` array MUST include:
- `vertex` (always present for all vertex types)
- All parent types in the inheritance chain

Example for a `staff` vertex:
```yaml
tags:
  - vertex      # base type
  - actor       # parent of individual
  - individual  # parent of staff
  - staff       # concrete type
```

## Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `description` | string | Brief description of this vertex |
| `status` | string | Lifecycle status (e.g., active, deprecated) |

## Body Content

The markdown body should describe:
- Purpose of this vertex
- Domain-specific properties
- Relationships to other elements
- Usage examples

## Subtypes

This base type can be extended by:
- **doc** - Documents (specs, guidances)
- **actor** - Entities with agency (individuals, groups)
- **property** - Attributes or capabilities (roles)

## Instantiability

**Abstract:** Base `vertex` type is not directly instantiable. Use concrete subtypes.

## Example Instance

```yaml
---
type: vertex/vertex
extends: null
id: v:example:myvertex
name: Example Vertex
tags:
  - vertex
version: 1.0.0
created: 2025-01-15T10:00:00Z
modified: 2025-01-15T10:00:00Z
---

# Example Vertex

Description of this vertex's purpose and properties.
```

## Validation Rules

1. **Type Format:** `type` must start with `vertex/`
2. **ID Format:** `id` must start with `v:`
3. **Tag Presence:** `vertex` tag must be present
4. **Extends Validity:** If not null, `extends` must reference a valid vertex type
5. **Tag Chain:** Tags must include full inheritance chain from base to concrete type
