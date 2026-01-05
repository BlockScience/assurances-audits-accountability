---
type: edge/dependency
extends: edge
id: e:dependency:program-plan-digital-transformation:architecture-digital-transformation
name: Dependency - Program Plan requires Architecture
description: Program plan depends on architecture for scope definition and deliverables
source: v:doc:program-plan-digital-transformation
target: v:doc:architecture-digital-transformation
source_type: vertex/doc
target_type: vertex/doc
orientation: directed
dependency_type: scope_definition
required: true
tags:
  - edge
  - dependency
  - program-development
version: 1.0.0
created: 2026-01-05T12:00:00Z
modified: 2026-01-05T12:00:00Z
---

# Dependency - Program Plan requires Architecture

**The program plan for digital transformation depends on the architecture document for scope definition and deliverable specifications.**

## Dependency Relationship

**Dependent:** `v:doc:program-plan-digital-transformation` (Program Plan - Digital Transformation Program)
**Dependency:** `v:doc:architecture-digital-transformation` (Architecture - Digital Transformation Program)
**Relationship:** Program plan requires architecture (scope definition)

**Usage:** The program plan's objectives, deliverables, and acceptance criteria are derived from the architecture document. The architecture defines what is being built; the program plan defines how it will be executed.

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Field/Subsection** | `architecture_ref` in program plan metadata |
| **Required** | Yes - architecture MUST exist before program plan |
| **Cardinality** | One architecture per program plan document |

### Consistency Checks Enabled

| Check | Description |
|-------|-------------|
| C1.1 | Program objectives must trace to architecture capabilities |
| C1.2 | Deliverables must map to architecture components |
| C1.3 | Acceptance criteria must align with architecture acceptance criteria |
| C1.4 | Scope boundaries must be consistent with architecture scope |

---

**Note:** This dependency is part of the program development documentation chain: Field Survey → Architecture → Lifecycle → Program Plan → Program Memo.
