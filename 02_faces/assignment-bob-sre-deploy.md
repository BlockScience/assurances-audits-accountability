---
type: face/assignment
extends: face
id: f:assignment:bob:sre:deploy
name: Bob SRE Deploy Assignment
description: RACI assignment face - Bob as SRE is Responsible for Deploy
tags:
  - face
  - assignment
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
vertices:
  - v:actor:staff:bob
  - v:actor:role:sre
  - v:property:responsibility:deploy
edges:
  - e:holds-role:bob:sre
  - e:assigned:sre:deploy:r
  - e:responsible:bob:deploy
orientation: oriented
raci_type: R
---

# Bob SRE Deploy Assignment

## Face Structure

This assignment face captures the RACI relationship:
- **Staff:** Bob
- **Role:** SRE
- **Responsibility:** Deploy to Production
- **RACI Type:** Responsible (R)

## Boundary Edges

1. `e:holds-role:bob:sre` - Bob holds the SRE role
2. `e:assigned:sre:deploy:r` - SRE is Responsible for Deploy

## Constraint

Bob is **Responsible** for executing Deploy through his SRE role.
