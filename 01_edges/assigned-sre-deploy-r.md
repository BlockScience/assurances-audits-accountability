---
type: edge/assigned
extends: edge
id: e:assigned:sre:deploy:r
name: SRE is Responsible for Deploy
description: RACI assignment - SRE is Responsible for executing deployments
tags:
  - edge
  - assigned
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:actor:role:sre
target: v:property:responsibility:deploy
source_type: vertex/actor/role
target_type: vertex/property/responsibility
orientation: directed
raci_type: R
---

# SRE is Responsible for Deploy

## Relationship

The SRE role is **Responsible** for the Deploy to Production responsibility.

## RACI

- **Type:** Responsible (R)
- **Meaning:** SREs execute the actual deployment work
- **Note:** Multiple SREs share this responsibility

## Edge Properties

- **Source:** SRE (Role)
- **Target:** Deploy to Production (Responsibility)
- **Direction:** Role → Responsibility
