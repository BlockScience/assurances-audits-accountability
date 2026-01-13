---
type: face/authorization
extends: face
id: f:authorization:admin:guidance-spec
name: Authorization Face - admin for guidance-spec
description: Proves admin's qualification for guidance-spec via admin role
vertices:
  - v:signer:admin
  - v:role:admin
  - v:guidance:spec
edges:
  - e:has-role:admin:admin
  - e:conveys:admin:guidance-spec
  - e:qualifies:admin:guidance-spec
has_role_edge: e:has-role:admin:admin
conveys_edge: e:conveys:admin:guidance-spec
qualifies_edge: e:qualifies:admin:guidance-spec
signer: v:signer:admin
role: v:role:admin
guidance: v:guidance:spec
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

# Authorization Face - admin for guidance-spec

This is an **authorization face** proving why the admin signer is qualified for guidance-spec.

## Face Structure

**Vertices:**
1. `v:signer:admin` - The actor
2. `v:role:admin` - The role
3. `v:guidance:spec` - The permission (guidance)

**Edges:**
1. `e:has-role:admin:admin` - User Assignment (signer → role)
2. `e:conveys:admin:guidance-spec` - Permission Assignment (role → guidance)
3. `e:qualifies:admin:guidance-spec` - SHARED with signature face

## NIST RBAC Pattern

This face implements the NIST RBAC permission derivation:
- User Assignment (UA): admin has admin role
- Permission Assignment (PA): admin role conveys authority for guidance-spec
- Derived Permission: admin is qualified for guidance-spec

The qualifies edge is shared with `f:signature:spec-ontology`, linking the RBAC proof to the attestation.
