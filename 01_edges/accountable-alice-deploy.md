---
type: edge/accountable
extends: edge
id: e:accountable:alice:deploy
name: Alice is accountable for Deploy
description: Direct accountability relationship - Alice is accountable for deployment
tags:
  - edge
  - accountable
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:actor:staff:alice
target: v:property:responsibility:deploy
source_type: vertex/actor/staff
target_type: vertex/property/responsibility
orientation: directed
---

# Alice is accountable for Deploy

## Relationship

Alice is directly accountable for the Deploy responsibility (through her Tech Lead role).

## Edge Properties

- **Type:** Accountability
- **Source:** Alice (Staff)
- **Target:** Deploy to Production (Responsibility)
