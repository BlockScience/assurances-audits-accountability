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

## Qualification

**Signer:** [[b0-root]]
**Guidance:** [[guidance-for-guidance]]

## Semantics

This is a boundary qualification edge where the root vertex is axiomatically qualified to sign documents that conform to guidance-for-guidance. As the genesis anchor of the system, root's qualification is foundational and requires no external justification.
