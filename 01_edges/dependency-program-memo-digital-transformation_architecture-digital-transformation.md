---
type: edge/dependency
extends: edge
id: e:dependency:program-memo-digital-transformation:architecture-digital-transformation
name: Dependency - Program Memo requires Architecture
description: Program memo depends on architecture for What We're Building section
source: v:doc:program-memo-digital-transformation
target: v:doc:architecture-digital-transformation
source_type: vertex/doc
target_type: vertex/doc
orientation: directed
dependency_type: technical_source
required: true
tags:
  - edge
  - dependency
  - program-development
version: 1.0.0
created: 2026-01-05T12:00:00Z
modified: 2026-01-05T12:00:00Z
---

# Dependency - Program Memo requires Architecture

**The program memo for digital transformation depends on the architecture document for the What We're Building section.**

## Dependency Relationship

**Dependent:** `v:doc:program-memo-digital-transformation` (Program Memo - Digital Transformation Program)
**Dependency:** `v:doc:architecture-digital-transformation` (Architecture - Digital Transformation Program)
**Relationship:** Program memo requires architecture (technical source)

**Usage:** The program memo's What We're Building section synthesizes goal state, key components, and success criteria from the architecture document's conceptual and logical layers.

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Field/Subsection** | `architecture_ref` in program memo metadata |
| **Required** | Yes - architecture MUST exist before program memo |
| **Cardinality** | One architecture per program memo document |

### Consistency Checks Enabled

| Check | Description |
|-------|-------------|
| C1.1 | Goal state must align with architecture conceptual layer |
| C1.2 | Key components must be traceable to architecture logical layer |
| C1.3 | Success criteria must reflect architecture acceptance criteria |

---

**Note:** This dependency is part of the program development documentation chain: Field Survey → Architecture → Lifecycle → Program Plan → Program Memo.
