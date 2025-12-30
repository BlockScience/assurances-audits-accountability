---
type: edge/responsible
extends: edge
id: e:responsible:bob:deploy
name: Bob is responsible for Deploy
description: Direct responsibility relationship - Bob executes deployment
tags:
  - edge
  - responsible
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:actor:staff:bob
target: v:property:responsibility:deploy
source_type: vertex/actor/staff
target_type: vertex/property/responsibility
orientation: directed
---

# Bob is responsible for Deploy

## Relationship

Bob is directly responsible for executing the Deploy responsibility (through his SRE role).

## Edge Properties

- **Type:** Responsibility
- **Source:** Bob (Staff)
- **Target:** Deploy to Production (Responsibility)
