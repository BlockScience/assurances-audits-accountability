---
type: edge/assigned
extends: edge
id: e:assigned:tech-lead:deploy:a
name: Tech Lead is Accountable for Deploy
description: RACI assignment - Tech Lead is Accountable for deployment responsibility
tags:
  - edge
  - assigned
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:actor:role:tech-lead
target: v:property:responsibility:deploy
source_type: vertex/actor/role
target_type: vertex/property/responsibility
orientation: directed
raci_type: A
---

# Tech Lead is Accountable for Deploy

## Relationship

The Tech Lead role is **Accountable** for the Deploy to Production responsibility.

## RACI

- **Type:** Accountable (A)
- **Meaning:** The Tech Lead is ultimately answerable for deployment decisions
- **Single A Rule:** This is the only Accountable assignment for deploy

## Edge Properties

- **Source:** Tech Lead (Role)
- **Target:** Deploy to Production (Responsibility)
- **Direction:** Role → Responsibility
