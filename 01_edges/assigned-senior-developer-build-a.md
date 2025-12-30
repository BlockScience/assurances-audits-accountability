---
type: edge/assigned
extends: edge
id: e:assigned:senior-developer:build:a
name: Senior Developer is Accountable for Build
description: RACI assignment - Senior Developer is Accountable for build responsibility
tags:
  - edge
  - assigned
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:actor:role:senior-developer
target: v:property:responsibility:build
source_type: vertex/actor/role
target_type: vertex/property/responsibility
orientation: directed
raci_type: A
---

# Senior Developer is Accountable for Build

## Relationship

The Senior Developer role is **Accountable** for the Build Application responsibility.

## RACI

- **Type:** Accountable (A)
- **Meaning:** The Senior Developer is ultimately answerable for build quality
- **Single A Rule:** This is the only Accountable assignment for build

## Edge Properties

- **Source:** Senior Developer (Role)
- **Target:** Build Application (Responsibility)
- **Direction:** Role → Responsibility
