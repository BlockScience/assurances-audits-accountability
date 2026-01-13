---
type: edge/qualifies
extends: edge
id: e:qualifies:root:guidance-guidance
name: Qualifies - Root for guidance-for-guidance
description: Bootstrap qualification where root is axiomatically qualified to sign guidance documents
source: b0:root
target: v:guidance:guidance
source_type: vertex/b0
target_type: vertex/guidance
orientation: directed
credential_type: axiom
granted_by: genesis
granted_date: 2025-12-27T00:00:00Z
tags:
  - edge
  - qualifies
  - boundary
  - genesis
version: 1.0.0
created: 2025-12-27T00:00:00Z
modified: 2025-12-30T00:00:00Z
---

# Qualifies - Root for guidance-for-guidance

## Qualification Description

**Signer:** [[b0-root]]
**Guidance:** [[guidance-for-guidance]]
**Credential Type:** axiom

Root is axiomatically qualified to sign documents that conform to guidance-for-guidance. As the genesis anchor of the system, root's qualification is foundational and requires no external justification.

## Credential Evidence

- **Genesis Bootstrap:** Root is the foundational anchor of the knowledge complex
- **Axiomatic Authority:** Root's qualification is self-evident by construction
- **Boundary Semantics:** This edge participates in the b2 boundary faces

## Scope and Limitations

**Scope:** Root can validate any document against guidance-for-guidance.

**Limitations:** This is a bootstrap qualification that exists only to resolve the genesis circularity. In operational use, human signers with proper credentials should be used.
