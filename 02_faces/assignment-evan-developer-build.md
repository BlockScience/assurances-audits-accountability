---
type: face/assignment
extends: face
id: f:assignment:evan:developer:build
name: Evan Developer Build Assignment
description: RACI assignment face - Evan as Developer is Responsible for Build
tags:
  - face
  - assignment
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
vertices:
  - v:actor:staff:evan
  - v:actor:role:developer
  - v:property:responsibility:build
edges:
  - e:holds-role:evan:developer
  - e:assigned:developer:build:r
  - e:responsible:evan:build
orientation: oriented
raci_type: R
---

# Evan Developer Build Assignment

## Face Structure

This assignment face captures the RACI relationship:
- **Staff:** Evan
- **Role:** Developer
- **Responsibility:** Build Application
- **RACI Type:** Responsible (R)

## Boundary Edges

1. `e:holds-role:evan:developer` - Evan holds the Developer role
2. `e:assigned:developer:build:r` - Developer is Responsible for Build

## Constraint

Evan is **Responsible** for executing Build through his Developer role.
