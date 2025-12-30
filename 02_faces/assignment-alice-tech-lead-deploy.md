---
type: face/assignment
extends: face
id: f:assignment:alice:tech-lead:deploy
name: Alice Tech Lead Deploy Assignment
description: RACI assignment face - Alice as Tech Lead is Accountable for Deploy
tags:
  - face
  - assignment
  - raci
  - organization
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
vertices:
  - v:actor:staff:alice
  - v:actor:role:tech-lead
  - v:property:responsibility:deploy
edges:
  - e:holds-role:alice:tech-lead
  - e:assigned:tech-lead:deploy:a
  - e:accountable:alice:deploy
orientation: oriented
raci_type: A
---

# Alice Tech Lead Deploy Assignment

## Face Structure

This assignment face captures the RACI relationship:
- **Staff:** Alice
- **Role:** Tech Lead
- **Responsibility:** Deploy to Production
- **RACI Type:** Accountable (A)

## Boundary Edges

1. `e:holds-role:alice:tech-lead` - Alice holds the Tech Lead role
2. `e:assigned:tech-lead:deploy:a` - Tech Lead is Accountable for Deploy
3. `e:accountable:alice:deploy` - Alice is accountable for Deploy

## Constraint

Alice is **Accountable** for Deploy through her Tech Lead role. This is the single-A for this responsibility.
