---
type: edge/has-role
extends: edge
id: e:has-role:admin:admin
name: Has Role - admin signer holds admin role
description: Bootstrap admin signer holds the admin role
source: v:signer:admin
target: v:role:admin
source_type: vertex/signer
target_type: vertex/role
orientation: directed
granted_by: genesis
granted_date: 2026-01-13T00:00:00Z
tags:
  - edge
  - has-role
  - rbac
  - foundation
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Has Role - admin signer holds admin role

This edge establishes that the bootstrap admin signer holds the admin role.

## RBAC Relationship

**Source:** `v:signer:admin` (the actor)
**Target:** `v:role:admin` (the role)

This is a NIST RBAC User Assignment (UA) edge.

## Genesis Context

This role assignment is part of the foundation bootstrap:

- Created at system initialization
- Grants admin role to placeholder signer
- Actual username populated during `aaa init`
