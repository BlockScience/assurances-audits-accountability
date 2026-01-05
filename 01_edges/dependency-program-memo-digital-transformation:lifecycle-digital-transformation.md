---
type: edge/dependency
extends: edge
id: e:dependency:program-memo-digital-transformation:lifecycle-digital-transformation
name: Dependency - Program Memo requires Lifecycle
description: Program memo depends on lifecycle for How We're Building It section
source: v:doc:program-memo-digital-transformation
target: v:doc:lifecycle-digital-transformation
source_type: vertex/doc
target_type: vertex/doc
orientation: directed
dependency_type: process_source
required: true
tags:
  - edge
  - dependency
  - program-development
version: 1.0.0
created: 2026-01-05T12:00:00Z
modified: 2026-01-05T12:00:00Z
---

# Dependency - Program Memo requires Lifecycle

**The program memo for digital transformation depends on the lifecycle document for the How We're Building It section.**

## Dependency Relationship

**Dependent:** `v:doc:program-memo-digital-transformation` (Program Memo - Digital Transformation Program)
**Dependency:** `v:doc:lifecycle-digital-transformation` (Lifecycle - Digital Transformation Program)
**Relationship:** Program memo requires lifecycle (process source)

**Usage:** The program memo's How We're Building It section synthesizes development approach, key phases, and quality assurance strategy from the lifecycle document.

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Field/Subsection** | `lifecycle_ref` in program memo metadata |
| **Required** | Yes - lifecycle MUST exist before program memo |
| **Cardinality** | One lifecycle per program memo document |

### Consistency Checks Enabled

| Check | Description |
|-------|-------------|
| C1.1 | Development approach must reflect lifecycle V-model structure |
| C1.2 | Phase groups must align with lifecycle phases |
| C1.3 | Quality assurance summary must reflect lifecycle V&V distinction |

---

**Note:** This dependency is part of the program development documentation chain: Field Survey → Architecture → Lifecycle → Program Plan → Program Memo.
