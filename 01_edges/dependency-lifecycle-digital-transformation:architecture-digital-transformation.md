---
type: edge/dependency
extends: edge
id: e:dependency:lifecycle-digital-transformation:architecture-digital-transformation
name: Dependency - Lifecycle requires Architecture
description: Lifecycle document depends on architecture for system definition and V-model alignment
source: v:doc:lifecycle-digital-transformation
target: v:doc:architecture-digital-transformation
source_type: vertex/doc
target_type: vertex/doc
orientation: directed
dependency_type: architectural_foundation
required: true
tags:
  - edge
  - dependency
  - program-development
version: 1.0.0
created: 2026-01-05T12:00:00Z
modified: 2026-01-05T12:00:00Z
---

# Dependency - Lifecycle requires Architecture

**The lifecycle document for digital transformation depends on the architecture document for V-model alignment and system definition.**

## Dependency Relationship

**Dependent:** `v:doc:lifecycle-digital-transformation` (Lifecycle - Digital Transformation Program)
**Dependency:** `v:doc:architecture-digital-transformation` (Architecture - Digital Transformation Program)
**Relationship:** Lifecycle requires architecture (architectural foundation)

**Usage:** The lifecycle document's phases, verification criteria, and validation requirements are derived from the architecture's V-model layers. The lifecycle operationalizes the architecture through phases that correspond to architecture layers.

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Field/Subsection** | `architecture_ref` in lifecycle metadata |
| **Required** | Yes - architecture MUST exist before lifecycle |
| **Cardinality** | One architecture per lifecycle document |

### Consistency Checks Enabled

| Check | Description |
|-------|-------------|
| C1.1 | Design phases must map to architecture's conceptual/functional/logical/physical layers |
| C1.2 | Evaluation phases must correspond to architecture's testing criteria |
| C1.3 | Acceptance criteria must trace to architecture's conceptual layer criteria |
| C1.4 | Gate criteria must align with architecture layer boundaries |

---

**Note:** This dependency is part of the program development documentation chain: Field Survey → Architecture → Lifecycle → Program Plan → Program Memo.
