---
type: edge/dependency
extends: edge
id: e:dependency:program-plan-digital-transformation:lifecycle-digital-transformation
name: Dependency - Program Plan requires Lifecycle
description: Program plan depends on lifecycle for execution phases and V&V strategy
source: v:doc:program-plan-digital-transformation
target: v:doc:lifecycle-digital-transformation
source_type: vertex/doc
target_type: vertex/doc
orientation: directed
dependency_type: execution_framework
required: true
tags:
  - edge
  - dependency
  - program-development
version: 1.0.0
created: 2026-01-05T12:00:00Z
modified: 2026-01-05T12:00:00Z
---

# Dependency - Program Plan requires Lifecycle

**The program plan for digital transformation depends on the lifecycle document for execution phases and verification/validation strategy.**

## Dependency Relationship

**Dependent:** `v:doc:program-plan-digital-transformation` (Program Plan - Digital Transformation Program)
**Dependency:** `v:doc:lifecycle-digital-transformation` (Lifecycle - Digital Transformation Program)
**Relationship:** Program plan requires lifecycle (execution framework)

**Usage:** The program plan's execution approach, phase structure, and V&V strategy are derived from the lifecycle document. The lifecycle defines how to build it; the program plan equips the lifecycle with teams, timelines, and resources.

## Dependency Usage

| Aspect | Detail |
|--------|--------|
| **Field/Subsection** | `lifecycle_ref` in program plan metadata |
| **Required** | Yes - lifecycle MUST exist before program plan |
| **Cardinality** | One lifecycle per program plan document |

### Consistency Checks Enabled

| Check | Description |
|-------|-------------|
| C1.1 | Execution phases must align with lifecycle phases |
| C1.2 | Milestones must map to lifecycle gates |
| C1.3 | V&V strategy must reflect lifecycle verification/validation distinction |
| C1.4 | Phase durations must be realistic given lifecycle requirements |

---

**Note:** This dependency is part of the program development documentation chain: Field Survey → Architecture → Lifecycle → Program Plan → Program Memo.
