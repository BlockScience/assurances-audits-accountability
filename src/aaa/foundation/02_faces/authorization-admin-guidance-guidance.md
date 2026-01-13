---
type: face/authorization
extends: face
id: f:authorization:admin:guidance-guidance
name: Authorization Face - admin for guidance-guidance
description: Proves admin's qualification for guidance-guidance via admin role
vertices:
  - v:signer:admin
  - v:role:admin
  - v:guidance:guidance
edges:
  - e:has-role:admin:admin
  - e:conveys:admin:guidance-guidance
  - e:qualifies:admin:guidance-guidance
has_role_edge: e:has-role:admin:admin
conveys_edge: e:conveys:admin:guidance-guidance
qualifies_edge: e:qualifies:admin:guidance-guidance
signer: v:signer:admin
role: v:role:admin
guidance: v:guidance:guidance
orientation: oriented
tags:
  - face
  - authorization
  - rbac
  - foundation
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Authorization Face - admin for guidance-guidance

This is an **authorization face** proving why the admin signer is qualified for guidance-guidance.

## Face Structure

**Vertices:**
1. `v:signer:admin` - The actor
2. `v:role:admin` - The role
3. `v:guidance:guidance` - The permission (guidance)

**Edges:**
1. `e:has-role:admin:admin` - User Assignment (signer → role)
2. `e:conveys:admin:guidance-guidance` - Permission Assignment (role → guidance)
3. `e:qualifies:admin:guidance-guidance` - SHARED with signature face

## NIST RBAC Pattern

This face implements the NIST RBAC permission derivation:
- User Assignment (UA): admin has admin role
- Permission Assignment (PA): admin role conveys authority for guidance-guidance
- Derived Permission: admin is qualified for guidance-guidance

The qualifies edge is shared with `f:signature:guidance-ontology`, linking the RBAC proof to the attestation.
