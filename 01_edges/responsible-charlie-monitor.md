---
type: edge/responsible
extends: edge
id: e:responsible:charlie:monitor
name: Charlie is responsible for Monitor
description: Direct responsibility relationship - Charlie executes monitoring
tags:
  - edge
  - responsible
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:actor:staff:charlie
target: v:property:responsibility:monitor
source_type: vertex/actor/staff
target_type: vertex/property/responsibility
orientation: directed
---

# Charlie is responsible for Monitor

## Relationship

Charlie is directly responsible for executing the Monitor responsibility (through her SRE role).

## Edge Properties

- **Type:** Responsibility
- **Source:** Charlie (Staff)
- **Target:** Monitor Services (Responsibility)
