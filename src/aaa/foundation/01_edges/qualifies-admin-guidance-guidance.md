---
type: edge/qualifies
extends: edge
id: e:qualifies:admin:guidance-guidance
name: Qualifies - admin for guidance-guidance
description: Admin signer is qualified to validate against guidance-for-guidance
source: v:signer:admin
target: v:guidance:guidance
source_type: vertex/signer
target_type: vertex/guidance
orientation: directed
credential_type: role
granted_by: v:role:admin
granted_date: 2026-01-13T00:00:00Z
tags:
  - edge
  - qualifies
  - rbac
  - foundation
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Qualifies - admin for guidance-guidance

This edge establishes that the admin signer is qualified to validate against guidance-for-guidance.

## Qualification Relationship

**Source:** `v:signer:admin` (the signer)
**Target:** `v:guidance:guidance` (the guidance)

This qualification is derived from the RBAC chain:
- Admin signer has admin role (has-role edge)
- Admin role conveys authority for guidance-guidance (conveys edge)
- Therefore admin is qualified for guidance-guidance (this edge)

## RBAC Chain

This edge is SHARED between:
- Authorization face (proves WHY admin is qualified)
- Signature face (proves admin signed validations)
