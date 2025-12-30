---
type: template/edge/verification
extends: edge
id: template:edge:verification
name: Verification Edge Template
description: Connects a document to the spec it must satisfy (structural compliance)
instantiable: true
tags:
  - template
  - edge
  - verification
version: 1.0.0
created: 2025-12-27T16:30:00Z
modified: 2025-12-27T16:30:00Z
---

# Verification Edge Template

**Connects a document to the specification it must satisfy for structural compliance.**

Verification edges represent the relationship "this document is verified against this spec" - meaning the document's structure has been checked against the spec's requirements.

## Type Hierarchy

```
edge (abstract)
└── verification (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `edge`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all edge fields, plus verification-specific constraints:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `edge/verification` |
| `extends` | string | Must be `edge` |
| `id` | string | Unique identifier (format: `e:verification:<child>:<parent-spec>`) |
| `name` | string | Human-readable edge name |
| `source` | string | Child document ID (any doc type) |
| `target` | string | Parent spec ID (format: `v:spec:<name>`) |
| `source_type` | string | Must be `vertex/doc` or subtype |
| `target_type` | string | Must be `vertex/spec` |
| `orientation` | string | Must be `directed` (child → spec) |
| `tags` | array | Must include `[edge, verification]` |
| `version` | string | Semantic version |
| `created` | datetime | ISO 8601 creation timestamp |
| `modified` | datetime | ISO 8601 last modification timestamp |

## Tag Requirements

The `tags` array MUST include the full inheritance chain:

```yaml
tags:
  - edge           # base type
  - verification   # concrete type
```

## Endpoint Constraints

### Source Vertex (Child Document)
- **Type:** MUST be `vertex/doc` or subtype (`vertex/spec`, `vertex/guidance`)
- **Role:** The document being verified
- **Constraint:** Must satisfy the target spec's structural requirements

### Target Vertex (Parent Spec)
- **Type:** MUST be `vertex/spec`
- **ID Format:** `v:spec:<name>`
- **Role:** Defines the structural requirements the child must meet

## Orientation

Verification edges are **directed** from child to spec:
- **Direction:** child_doc → parent_spec
- **Meaning:** "This child document claims to satisfy this spec's requirements"
- **Verification:** Can be checked deterministically (pass/fail)

## Body Content Requirements

The markdown body MUST contain the output of the verification tool that confirms structural compliance.

### Required Section: Verification Output

```markdown
## Verification Output

\`\`\`
[Output from verification tool showing compliance check]
\`\`\`

## Verification Status

- **Status:** Pass | Fail
- **Date:** [ISO 8601 timestamp]
- **Tool:** [Verification tool identifier and version]
```

### Optional Sections

- **Non-Compliance Issues:** If verification fails, list specific issues
- **Verification Notes:** Additional context or observations

## Role in Assurance Pattern

Verification edges form one side of the assurance triangle:

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

The verification edge connects:
- Child document (any doc)
- Parent spec (structural requirements)

Together with a validation edge and coupling edge, this forms an **assurance face**.

## Verification vs. Validation

| Aspect | Verification | Validation |
|--------|--------------|------------|
| **Checks** | Structure, required fields, data types | Quality, clarity, fitness-for-purpose |
| **Method** | Deterministic, automated | Qualitative, expert judgment |
| **Result** | Pass/Fail | Quality level (Excellent/Good/Poor) |
| **Edge Type** | `verification` | `validation` |
| **Target** | Spec | Guidance |

## Tool Integration

Verification edges SHOULD be created automatically by verification tools. The body content comes from tool output.

Example workflow:
```bash
# Run verification
python scripts/verify_spec.py 00_vertices/my-doc.md v:spec:doc

# If pass, tool creates verification edge with output in body
```

## Example Instance

```yaml
---
type: edge/verification
extends: edge
id: e:verification:spec-guidance:spec-spec
name: Verification - Spec-for-Guidance verifies against Spec-for-Spec
source: v:spec:guidance
target: v:spec:spec
source_type: vertex/spec
target_type: vertex/spec
orientation: directed
tags:
  - edge
  - verification
version: 1.0.0
created: 2025-01-15T10:00:00Z
modified: 2025-01-15T10:00:00Z
---

# Verification - Spec-for-Guidance verifies against Spec-for-Spec

This verification edge confirms that spec-for-guidance satisfies the structural requirements defined in spec-for-spec.

## Verification Output

\`\`\`
Verification Result: PASS

Checked against: v:spec:spec (Specification for Specifications)
Document: v:spec:guidance (Specification for Guidance Documents)

Required Fields:
✓ type: vertex/spec
✓ extends: doc
✓ id: v:spec:guidance
✓ name: present
✓ tags: [vertex, doc, spec]
✓ version: 1.0.0
✓ created: 2025-01-15T10:00:00Z
✓ modified: 2025-01-15T10:00:00Z

Required Body Sections:
✓ Purpose
✓ Required Frontmatter Fields
✓ Required Body Sections
✓ Schema Definition

All structural requirements satisfied.
\`\`\`

## Verification Status

- **Status:** Pass
- **Date:** 2025-01-15T10:00:00Z
- **Tool:** verify_spec.py v0.1.0
```

## Validation Rules

1. **Type Format:** `type` must be `edge/verification`
2. **Source Type:** Source must be a doc (`vertex/doc` or subtype)
3. **Target Type:** Target must be a spec (`vertex/spec`)
4. **Orientation:** Must be `directed`
5. **Tag Chain:** Tags must include `[edge, verification]`
6. **Body Content:** Must include verification output
7. **Assurance:** Should participate in an assurance face with validation edge and coupling edge

## Boundary Complex

The four foundational verification edges in the boundary complex:

1. **e:verification:spec-spec:spec-spec** - spec-for-spec verifies against itself
2. **e:verification:spec-guidance:spec-spec** - spec-for-guidance verifies against spec-for-spec
3. **e:verification:guidance-spec:spec-guidance** - guidance-for-spec verifies against spec-for-guidance
4. **e:verification:guidance-guidance:spec-guidance** - guidance-for-guidance verifies against spec-for-guidance

These demonstrate the self-referential property of the knowledge complex.
