---
type: edge/assigned
extends: edge
id: e:assigned:sre:monitor:r
name: SRE is Responsible for Monitor
description: RACI assignment - SRE is Responsible for monitoring services
tags:
  - edge
  - assigned
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
source: v:actor:role:sre
target: v:property:responsibility:monitor
source_type: vertex/actor/role
target_type: vertex/property/responsibility
orientation: directed
raci_type: R
---

# SRE is Responsible for Monitor

## Relationship

The SRE role is **Responsible** for the Monitor Services responsibility.

## RACI

- **Type:** Responsible (R)
- **Meaning:** SREs perform the monitoring and incident response work

## Edge Properties

- **Source:** SRE (Role)
- **Target:** Monitor Services (Responsibility)
- **Direction:** Role → Responsibility
