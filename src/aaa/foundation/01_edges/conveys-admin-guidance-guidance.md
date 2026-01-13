---
type: edge/conveys
extends: edge
id: e:conveys:admin:guidance-guidance
name: Conveys - admin role conveys authority for guidance-guidance
description: Admin role conveys authority to validate against guidance-for-guidance
source: v:role:admin
target: v:guidance:guidance
source_type: vertex/role
target_type: vertex/guidance
orientation: directed
tags:
  - edge
  - conveys
  - rbac
  - foundation
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Conveys - admin role conveys authority for guidance-guidance

This edge establishes that the admin role conveys authority to validate against guidance-for-guidance.

## RBAC Relationship

**Source:** `v:role:admin` (the role)
**Target:** `v:guidance:guidance` (the guidance/permission)

This is a NIST RBAC Permission Assignment (PA) edge.

## Authorization Chain

Combined with `e:has-role:admin:admin`, this enables:
- Admin signer holds admin role
- Admin role conveys authority for guidance-guidance
- Therefore admin signer can validate guidance docs
