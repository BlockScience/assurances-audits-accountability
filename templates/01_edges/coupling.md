---
type: template/edge/coupling
extends: edge
id: template:edge:coupling
name: Coupling Edge Template
description: Connects a spec with its corresponding guidance document
instantiable: true
tags:
  - template
  - edge
  - coupling
version: 1.0.0
created: 2025-12-27T16:30:00Z
modified: 2025-12-27T16:30:00Z
---

# Coupling Edge Template

**Connects a specification document with its corresponding guidance document.**

## Type Hierarchy

```
edge (abstract)
└── coupling (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `edge`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all edge fields, plus coupling-specific constraints:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `edge/coupling` |
| `extends` | string | Must be `edge` |
| `id` | string | Unique identifier (format: `e:coupling:<spec-name>`) |
| `name` | string | Human-readable edge name |
| `source` | string | Spec vertex ID (format: `v:spec:<name>`) |
| `target` | string | Guidance vertex ID (format: `v:guidance:<name>`) |
| `source_type` | string | Must be `vertex/spec` |
| `target_type` | string | Must be `vertex/guidance` |
| `orientation` | string | Must be `undirected` |
| `tags` | array | Must include `[edge, coupling]` |
| `version` | string | Semantic version |
| `created` | datetime | ISO 8601 creation timestamp |
| `modified` | datetime | ISO 8601 last modification timestamp |

## Tag Requirements

The `tags` array MUST include the full inheritance chain:

```yaml
tags:
  - edge        # base type
  - coupling    # concrete type
```

## Endpoint Constraints

### Source Vertex (Spec)
- **Type:** MUST be `vertex/spec` (or subtype)
- **ID Format:** `v:spec:<name>`
- **Role:** Defines structural requirements

### Target Vertex (Guidance)
- **Type:** MUST be `vertex/guidance` (or subtype)
- **ID Format:** `v:guidance:<name>`
- **Role:** Defines quality criteria for documents satisfying the spec

### Semantic Constraint
The spec and guidance SHOULD address the same document type or domain. Typically:
- `v:spec:X` is coupled with `v:guidance:X`
- Both define requirements for the same class of documents

## Orientation

Coupling edges are **undirected** - the relationship is symmetric:
- The spec defines structure for a document type
- The guidance defines quality criteria for that same document type
- Neither is subordinate to the other

## Role in Assurance Pattern

Coupling edges form the base of assurance triangles:

```
          child_doc
           /      \
          /        \
  verification   validation
        /            \
       /              \
   parent_spec ---- parent_guidance
              coupling
```

The coupling edge ensures that:
1. Structural requirements (spec) and quality criteria (guidance) are aligned
2. Both aspects of assurance (verification and validation) are addressed
3. The assurance face can close properly

## Body Content

The markdown body should describe:
- Why this spec and guidance are coupled
- What document type they jointly govern
- How structural requirements relate to quality criteria
- Any special considerations for this coupling

## Example Instance

```yaml
---
type: edge/coupling
extends: edge
id: e:coupling:vertex
name: Coupling - Vertex Spec and Guidance
source: v:spec:vertex
target: v:guidance:vertex
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2025-01-15T10:00:00Z
modified: 2025-01-15T10:00:00Z
---

# Coupling - Vertex Spec and Guidance

This coupling connects the specification that defines vertex structure with the guidance that defines vertex quality criteria.

## Purpose

Together, these documents enable:
- **Verification:** Checking that a vertex has required fields (against spec)
- **Validation:** Assessing whether a vertex is well-designed (against guidance)

## Governed Document Type

Both documents govern vertices of all types in the knowledge complex.
```

## Validation Rules

1. **Type Format:** `type` must be `edge/coupling`
2. **Source Type:** Source must be a spec (`vertex/spec` or subtype)
3. **Target Type:** Target must be a guidance (`vertex/guidance` or subtype)
4. **Orientation:** Must be `undirected`
5. **Tag Chain:** Tags must include `[edge, coupling]`
6. **Semantic Alignment:** Source and target should govern the same document type (recommended, not enforced)

## Boundary Complex

The four foundational coupling edges form the boundary complex:

1. **e:coupling:spec** - Couples spec-for-spec with guidance-for-spec
2. **e:coupling:guidance** - Couples spec-for-guidance with guidance-for-guidance

These, along with the verification and validation edges, form the self-referential foundation of the knowledge complex.

## Face Participation

Coupling edges participate as the base of assurance faces:
- Source: parent_spec
- Target: parent_guidance
- Third vertex: child_doc (connected by verification and validation edges)

The assurance face closes when all three edges form a valid triangle.
