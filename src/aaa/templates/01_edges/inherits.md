---
type: template/edge/inherits
extends: edge
id: template:edge:inherits
name: Inherits Edge Template
description: Tracks type inheritance/extension relationships (domain specialization, not assurance)
instantiable: true
tags:
  - template
  - edge
  - inherits
version: 1.0.0
created: 2025-12-27T17:00:00Z
modified: 2025-12-27T17:00:00Z
---

# Inherits Edge Template

**Tracks that one document type inherits/extends from another (domain specialization).**

## Type Hierarchy

```
edge (abstract)
└── inherits (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `edge`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all edge fields, plus inherits-specific constraints:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `edge/inherits` |
| `extends` | string | Must be `edge` |
| `id` | string | Unique identifier (format: `e:inherits:<child>:<parent>`) |
| `name` | string | Human-readable edge name |
| `description` | string | Clear explanation of the inheritance relationship |
| `source` | string | Child vertex ID (the type that extends) |
| `target` | string | Parent vertex ID (the type being extended) |
| `source_type` | string | Type of source vertex (must match source's type field) |
| `target_type` | string | Type of target vertex (must match target's type field) |
| `orientation` | string | Must be `directed` |
| `inheritance_type` | string | Type of inheritance (see below) |
| `inherited_fields` | array | Optional: List of fields child inherits from parent |
| `added_fields` | array | Optional: List of new fields added by child |
| `tags` | array | Must include `[edge, inherits]` |
| `version` | string | Semantic version |
| `created` | datetime | ISO 8601 creation timestamp |
| `modified` | datetime | ISO 8601 last modification timestamp |

## Tag Requirements

The `tags` array MUST include the full inheritance chain:

```yaml
tags:
  - edge        # base type
  - inherits    # concrete type
```

## Endpoint Constraints

### Source Vertex (Child - the one that extends)
- **Role:** The more specific type (e.g., `v:spec:assurance_audit`)
- **Type Constraint:** Must be same document class as target
- **Direction:** Inherits FROM target (target → source in inheritance flow)

### Target Vertex (Parent - the one being extended)
- **Role:** The more general type (e.g., `v:spec:chart`)
- **Type Constraint:** Must be same document class as source
- **Direction:** Extended BY source

### Type Consistency Rule
Both vertices MUST be the same document class:
- Spec → Spec: `vertex/spec` → `vertex/spec`
- Guidance → Guidance: `vertex/guidance` → `vertex/guidance`
- Chart → Chart: `vertex/chart` → `vertex/chart`
- etc.

**Invalid:** Spec inheriting from Guidance, or any cross-class inheritance

## Orientation

Inherits edges are **directed** - inheritance flows from parent to child:
- Arrow points from child TO parent: `child --inherits--> parent`
- Child extends parent (child is more specific)
- Parent is extended by child (parent is more general)

## Inheritance Type

The `inheritance_type` field MUST be one of:

- **`domain_specialization`** (most common): Child is a specialized version of parent in the same domain
  - Example: `assurance_audit` extends `chart` (audit charts are specialized charts)
- **`type_extension`**: Child adds capabilities to parent type
- **`implementation`**: Child implements parent's abstract requirements

## Relationship to Assurance DAG

**CRITICAL:** Inherits edges are **separate from the assurance DAG**.

```
Domain Inheritance Graph (inherits edges):
  v:spec:assurance_audit --inherits--> v:spec:chart --inherits--> v:spec:spec

Assurance DAG (verification edges):
  v:spec:assurance_audit --verifies--> v:spec:spec
  v:spec:chart --verifies--> v:spec:spec
```

**Inherits edges** explain domain modeling: "what extends what"
**Verification edges** prove assurance: "what verifies against what"

A spec that extends another spec still verifies against `v:spec:spec` (not against its parent spec).

## Validation Rules

1. **Direction Consistency:** Source MUST be more specific than target (child extends parent)
2. **Type Consistency:** Both source and target MUST be same document class
3. **Acyclic:** Inheritance graph MUST be a DAG (no cycles)
4. **Single Inheritance:** Each vertex has at most one inherits edge (no multiple inheritance)
5. **Separate from Assurance:** Inherits edges MUST NOT be confused with verification edges

## Required Sections

All inherits edges MUST include these markdown sections:

### 1. Inheritance Relationship

**Required heading:** `# Inheritance Relationship` or `## Inheritance Relationship`

**Must document:**
- Child (source) vertex identification
- Parent (target) vertex identification
- Inheritance direction explanation
- Relationship to assurance DAG (clarify separation)

**Example:**
```markdown
## Inheritance Relationship

**Child:** `v:spec:assurance_audit` (Specification for Assurance Audit Documents)
**Parent:** `v:spec:chart` (Specification for Chart Documents)
**Relationship:** assurance_audit extends chart (domain specialization)

**Assurance Note:** This inheritance edge tracks domain specialization and is separate from the assurance DAG. For assurance, SAA verifies against v:spec:spec (because SAA is a spec), not against v:spec:chart.
```

### 2. Inherited Structure

**Required heading:** `# Inherited Structure` or `## Inherited Structure`

**Must document:**
- List of inherited fields/properties
- List of added/new fields unique to child
- Any overridden fields (if applicable)

### 3. Semantic Justification

**Required heading:** `# Semantic Justification` or `## Semantic Justification`

**Must explain:**
- Domain rationale (why child is a specialization of parent)
- Use case explanation
- How this differs from assurance relationships

## Role in Type System

Inherits edges provide:
- **Explainability:** Why does this type have these fields?
- **Type Hierarchies:** Visualization of domain specialization
- **Field Provenance:** Understanding what's inherited vs. added
- **Documentation:** Clear inheritance relationships

They do NOT provide:
- **Assurance:** That's the role of verification/validation edges
- **Quality Guarantees:** Inheriting structure doesn't guarantee quality
- **Verification:** Child still verifies against base type spec (e.g., all specs verify against spec-for-spec)

## Common Patterns

### Pattern 1: Spec Inheritance
```yaml
source: v:spec:assurance_audit  # child (more specific)
target: v:spec:chart            # parent (more general)
source_type: vertex/spec
target_type: vertex/spec
inheritance_type: domain_specialization
```

### Pattern 2: Guidance Inheritance
```yaml
source: v:guidance:assurance_audit  # child
target: v:guidance:chart            # parent
source_type: vertex/guidance
target_type: vertex/guidance
inheritance_type: domain_specialization
```

### Pattern 3: Parallel Inheritance
Often specs and guidances inherit in parallel:
- `e:inherits:assurance_audit:chart` (spec → spec)
- `e:inherits:assurance_audit-guidance:chart-guidance` (guidance → guidance)

## Examples

See:
- [01_edges/inherits-assurance_audit:chart.md](../../01_edges/inherits-assurance_audit:chart.md)
- [01_edges/inherits-assurance_audit-guidance:chart-guidance.md](../../01_edges/inherits-assurance_audit-guidance:chart-guidance.md)

## Notes

- Inherits edges are for **explainability and documentation**
- They help answer "why does this type have these fields?"
- They are NOT part of assurance computation
- Visualization tools should render these separately from assurance edges
- Keep inheritance hierarchies shallow (prefer composition over deep inheritance)

---

**Template Version:** 1.0.0
**Template Status:** Active
**Last Modified:** 2025-12-27
