---
type: face/assignment
extends: face
id: f:assignment:charlie:sre:monitor
name: Charlie SRE Monitor Assignment
description: RACI assignment face - Charlie as SRE is Responsible for Monitor
tags:
  - face
  - assignment
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
vertices:
  - v:actor:staff:charlie
  - v:actor:role:sre
  - v:property:responsibility:monitor
edges:
  - e:holds-role:charlie:sre
  - e:assigned:sre:monitor:r
  - e:responsible:charlie:monitor
orientation: oriented
raci_type: R
---

# Charlie SRE Monitor Assignment

## Face Structure

This assignment face captures the RACI relationship:
- **Staff:** Charlie
- **Role:** SRE
- **Responsibility:** Monitor Services
- **RACI Type:** Responsible (R)

## Boundary Edges

1. `e:holds-role:charlie:sre` - Charlie holds the SRE role
2. `e:assigned:sre:monitor:r` - SRE is Responsible for Monitor

## Constraint

Charlie is **Responsible** for executing Monitor through her SRE role.
