---
type: edge/qualifies
extends: edge
id: e:qualifies:admin:guidance-ontology
name: Qualifies - admin for guidance-ontology
description: Admin signer is qualified to validate against guidance-for-ontology
source: v:signer:admin
target: v:guidance:ontology
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

# Qualifies - admin for guidance-ontology

This edge establishes that the admin signer is qualified to validate against guidance-for-ontology.

## Qualification Relationship

**Source:** `v:signer:admin` (the signer)
**Target:** `v:guidance:ontology` (the guidance)

This qualification is derived from the RBAC chain:
- Admin signer has admin role (has-role edge)
- Admin role conveys authority for guidance-ontology (conveys edge)
- Therefore admin is qualified for guidance-ontology (this edge)

## RBAC Chain

This edge is SHARED between:
- Authorization face (proves WHY admin is qualified)
- Signature face (proves admin signed validations)
