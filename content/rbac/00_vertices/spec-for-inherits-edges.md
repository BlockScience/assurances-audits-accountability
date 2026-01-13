---
type: vertex/spec
extends: doc
id: v:spec:inherits
name: Specification for Inherits Edges
description: Defines structure and semantics for inherits edges that track type inheritance relationships
version: 1.0.0
created: 2025-12-27T17:00:00Z
modified: 2025-12-27T17:00:00Z
dependencies: []
tags:
  - vertex
  - spec
  - doc
  - edge-type
  - inheritance
---

# Specification for Inherits Edges

## Purpose

This specification defines the structure, semantics, and requirements for `edge/inherits` edges, which track type inheritance relationships in the knowledge complex. Inherits edges are **separate from the assurance DAG** and exist to provide explainability about domain specialization.

## Document Overview

**What this spec defines:** Structure for edges that represent "X extends Y" relationships

**Scope:** Type inheritance tracking (domain specialization, not assurance)

**Target audience:** Documentation authors, automation tools, assurance systems

## Type Definition

```yaml
type: edge/inherits
extends: edge
```

## Required Frontmatter Fields

All inherits edges MUST include these frontmatter fields:

### Core Identity Fields

1. **type** (string, required): Must be `edge/inherits`
2. **extends** (string, required): Must be `edge`
3. **id** (string, required): Edge identifier following pattern `e:inherits:<child>:<parent>`
   - Example: `e:inherits:assurance_audit:chart`
4. **name** (string, required): Human-readable name
5. **description** (string, required): Clear explanation of the inheritance relationship

### Relationship Fields

6. **source** (vertex ID, required): The child type (the one that extends/inherits)
   - Example: `v:spec:assurance_audit` (SAA inherits from SC)
7. **target** (vertex ID, required): The parent type (the one being extended from)
   - Example: `v:spec:chart` (SAA extends SC)
8. **source_type** (vertex type, required): Type of source vertex
   - Must match the `type` field from source vertex
9. **target_type** (vertex type, required): Type of target vertex
   - Must match the `type` field from target vertex
10. **orientation** (string, required): Must be `directed`
    - Inheritance flows from parent to child (target → source)

### Inheritance Semantics Fields

11. **inheritance_type** (string, required): Type of inheritance
    - Values: `domain_specialization`, `type_extension`, `implementation`
    - Most common: `domain_specialization` (e.g., chart → assurance_audit)
12. **inherited_fields** (list of strings, optional): Fields that child inherits from parent
13. **added_fields** (list of strings, optional): New fields added by child

### Metadata Fields

14. **version** (string, required): Semantic version (e.g., "1.0.0")
15. **created** (ISO 8601 timestamp, required)
16. **modified** (ISO 8601 timestamp, required)
17. **tags** (list, required): Must include `edge`, `inherits`

## Required Sections

### 1. Inheritance Relationship

**Required heading:** `# Inheritance Relationship` or `## Inheritance Relationship`

**Purpose:** Clearly state what inherits from what

**Must include:**
- Source (child) vertex identification
- Target (parent) vertex identification
- Inheritance direction explanation
- Relationship to assurance DAG (clarify these are separate)

**Example:**
```markdown
## Inheritance Relationship

**Child:** `v:spec:assurance_audit` (Specification for Assurance Audit Documents)
**Parent:** `v:spec:chart` (Specification for Chart Documents)
**Relationship:** assurance_audit extends chart (domain specialization)

**Assurance Note:** This inheritance edge tracks domain specialization. For assurance purposes, SAA still verifies against v:spec:spec (because SAA is a spec), not against v:spec:chart.
```

### 2. Inherited Structure

**Required heading:** `# Inherited Structure` or `## Inherited Structure`

**Purpose:** Document what the child inherits from parent

**Must include:**
- List of inherited fields/properties
- List of added/new fields unique to child
- Any overridden fields

### 3. Semantic Justification

**Required heading:** `# Semantic Justification` or `## Semantic Justification`

**Purpose:** Explain why this inheritance makes sense

**Must include:**
- Domain rationale (why child is a specialization of parent)
- Use case explanation
- How this differs from assurance relationships

## Validation Rules

1. **Direction Consistency:** Source must be more specific than target (child extends parent)
2. **Type Consistency:** Both source and target must be same document class
   - Spec can only extend spec: `v:spec:X` → `v:spec:Y`
   - Guidance can only extend guidance: `v:guidance:X` → `v:guidance:Y`
   - Charts can only extend charts, etc.
3. **Acyclic:** Inheritance graph must be a DAG (no cycles)
4. **Single Inheritance:** Each vertex has at most one inherits edge (no multiple inheritance)
5. **Separate from Assurance:** Inherits edges MUST NOT be confused with verification edges

## Relationship to Assurance DAG

**CRITICAL DISTINCTION:**

- **Inherits edges** track domain specialization (e.g., assurance_audit extends chart)
- **Verification edges** track assurance (e.g., SAA verifies against SS because SAA is a spec)

These are **two separate graph structures**:

```
Domain Inheritance Graph (inherits edges):
  v:spec:assurance_audit --inherits--> v:spec:chart --inherits--> v:spec:spec

Assurance DAG (verification edges):
  v:spec:assurance_audit --verifies--> v:spec:spec
  v:spec:chart --verifies--> v:spec:spec
```

The inheritance graph explains "what extends what" for domain modeling.
The assurance DAG explains "what verifies against what" for quality assurance.

## Examples

### Example 1: Spec Inheritance

```yaml
---
type: edge/inherits
extends: edge
id: e:inherits:assurance_audit:chart
name: Inherits - Assurance Audit extends Chart
description: Assurance audit specs inherit structure from chart specs (domain specialization)
source: v:spec:assurance_audit
target: v:spec:chart
source_type: vertex/spec
target_type: vertex/spec
orientation: directed
inheritance_type: domain_specialization
inherited_fields:
  - elements (vertices, edges, faces)
  - topology (euler_characteristic)
  - constructed_by
  - construction_method
added_fields:
  - audit_targets
  - audit_date
  - auditor
  - audit_status
  - assurance_requirements
---
```

### Example 2: Guidance Inheritance

```yaml
---
type: edge/inherits
extends: edge
id: e:inherits:assurance_audit-guidance:chart-guidance
name: Inherits - Guidance for Assurance Audits extends Guidance for Charts
description: Assurance audit guidances inherit from chart guidances (domain specialization)
source: v:guidance:assurance_audit
target: v:guidance:chart
source_type: vertex/guidance
target_type: vertex/guidance
orientation: directed
inheritance_type: domain_specialization
---
```

## Notes

- Inherits edges provide **explainability** but are not part of the assurance computation
- They help answer "why does this type have these fields?" without conflating with "is this type properly assured?"
- Visualization tools should render these separately from assurance edges

---

**Version:** 1.0.0
**Status:** Active
**Last Modified:** 2025-12-27
