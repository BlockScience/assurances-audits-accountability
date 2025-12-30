---
type: face/assignment
extends: face
id: f:assignment:dana:senior-developer:build
name: Dana Senior Developer Build Assignment
description: RACI assignment face - Dana as Senior Developer is Accountable for Build
tags:
  - face
  - assignment
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
vertices:
  - v:actor:staff:dana
  - v:actor:role:senior-developer
  - v:property:responsibility:build
edges:
  - e:holds-role:dana:senior-developer
  - e:assigned:senior-developer:build:a
  - e:accountable:dana:build
orientation: oriented
raci_type: A
---

# Dana Senior Developer Build Assignment

## Face Structure

This assignment face captures the RACI relationship:
- **Staff:** Dana
- **Role:** Senior Developer
- **Responsibility:** Build Application
- **RACI Type:** Accountable (A)

## Boundary Edges

1. `e:holds-role:dana:senior-developer` - Dana holds the Senior Developer role
2. `e:assigned:senior-developer:build:a` - Senior Developer is Accountable for Build

## Constraint

Dana is **Accountable** for Build through her Senior Developer role. This is the single-A for this responsibility.
