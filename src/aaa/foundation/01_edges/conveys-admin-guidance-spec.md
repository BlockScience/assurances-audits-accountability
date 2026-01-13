---
type: edge/conveys
extends: edge
id: e:conveys:admin:guidance-spec
name: Conveys - admin role conveys authority for guidance-spec
description: Admin role conveys authority to validate against guidance-for-spec
source: v:role:admin
target: v:guidance:spec
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

# Conveys - admin role conveys authority for guidance-spec

This edge establishes that the admin role conveys authority to validate against guidance-for-spec.

## RBAC Relationship

**Source:** `v:role:admin` (the role)
**Target:** `v:guidance:spec` (the guidance/permission)

This is a NIST RBAC Permission Assignment (PA) edge.

## Authorization Chain

Combined with `e:has-role:admin:admin`, this enables:
- Admin signer holds admin role
- Admin role conveys authority for guidance-spec
- Therefore admin signer can validate specs
