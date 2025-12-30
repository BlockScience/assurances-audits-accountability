---
type: edge/assigned
extends: edge
id: e:assigned:tech-lead:monitor:a
name: Tech Lead is Accountable for Monitor
description: RACI assignment - Tech Lead is Accountable for monitoring responsibility
tags:
  - edge
  - assigned
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:actor:role:tech-lead
target: v:property:responsibility:monitor
source_type: vertex/actor/role
target_type: vertex/property/responsibility
orientation: directed
raci_type: A
---

# Tech Lead is Accountable for Monitor

## Relationship

The Tech Lead role is **Accountable** for the Monitor Services responsibility.

## RACI

- **Type:** Accountable (A)
- **Meaning:** The Tech Lead is ultimately answerable for monitoring quality
- **Single A Rule:** This is the only Accountable assignment for monitor

## Edge Properties

- **Source:** Tech Lead (Role)
- **Target:** Monitor Services (Responsibility)
- **Direction:** Role → Responsibility
