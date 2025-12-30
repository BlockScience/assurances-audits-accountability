---
type: face/assignment
extends: face
id: f:assignment:bob:sre:monitor
name: Bob SRE Monitor Assignment
description: RACI assignment face - Bob as SRE is Responsible for Monitor
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
  - v:property:responsibility:monitor
edges:
  - e:holds-role:bob:sre
  - e:assigned:sre:monitor:r
  - e:responsible:bob:monitor
orientation: oriented
raci_type: R
---

# Bob SRE Monitor Assignment

## Face Structure

This assignment face captures the RACI relationship:
- **Staff:** Bob
- **Role:** SRE
- **Responsibility:** Monitor Services
- **RACI Type:** Responsible (R)

## Boundary Edges

1. `e:holds-role:bob:sre` - Bob holds the SRE role
2. `e:assigned:sre:monitor:r` - SRE is Responsible for Monitor

## Constraint

Bob is **Responsible** for executing Monitor through his SRE role.
