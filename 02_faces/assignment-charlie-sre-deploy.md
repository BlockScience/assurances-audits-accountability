---
type: face/assignment
extends: face
id: f:assignment:charlie:sre:deploy
name: Charlie SRE Deploy Assignment
description: RACI assignment face - Charlie as SRE is Responsible for Deploy
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
  - v:property:responsibility:deploy
edges:
  - e:holds-role:charlie:sre
  - e:assigned:sre:deploy:r
  - e:responsible:charlie:deploy
orientation: oriented
raci_type: R
---

# Charlie SRE Deploy Assignment

## Face Structure

This assignment face captures the RACI relationship:
- **Staff:** Charlie
- **Role:** SRE
- **Responsibility:** Deploy to Production
- **RACI Type:** Responsible (R)

## Boundary Edges

1. `e:holds-role:charlie:sre` - Charlie holds the SRE role
2. `e:assigned:sre:deploy:r` - SRE is Responsible for Deploy

## Constraint

Charlie is **Responsible** for executing Deploy through her SRE role.
