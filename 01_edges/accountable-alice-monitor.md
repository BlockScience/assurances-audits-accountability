---
type: edge/accountable
extends: edge
id: e:accountable:alice:monitor
name: Alice is accountable for Monitor
description: Direct accountability relationship - Alice is accountable for monitoring
tags:
  - edge
  - accountable
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:actor:staff:alice
target: v:property:responsibility:monitor
source_type: vertex/actor/staff
target_type: vertex/property/responsibility
orientation: directed
---

# Alice is accountable for Monitor

## Relationship

Alice is directly accountable for the Monitor responsibility (through her Tech Lead role).

## Edge Properties

- **Type:** Accountability
- **Source:** Alice (Staff)
- **Target:** Monitor Services (Responsibility)
