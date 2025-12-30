---
type: edge/assigned
extends: edge
id: e:assigned:developer:build:r
name: Developer is Responsible for Build
description: RACI assignment - Developer is Responsible for executing builds
tags:
  - edge
  - assigned
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:actor:role:developer
target: v:property:responsibility:build
source_type: vertex/actor/role
target_type: vertex/property/responsibility
orientation: directed
raci_type: R
---

# Developer is Responsible for Build

## Relationship

The Developer role is **Responsible** for the Build Application responsibility.

## RACI

- **Type:** Responsible (R)
- **Meaning:** Developers execute the actual build work

## Edge Properties

- **Source:** Developer (Role)
- **Target:** Build Application (Responsibility)
- **Direction:** Role → Responsibility
