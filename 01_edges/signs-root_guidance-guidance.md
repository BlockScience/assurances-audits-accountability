---
type: edge/signs
extends: edge
id: e:signs:root:guidance-guidance
name: Signs - Root attests guidance-for-guidance assurance
description: Bootstrap signing edge where root anchors the guidance-for-guidance assurance
source: b0:root
target: v:guidance:guidance
source_type: vertex/b0
target_type: vertex/guidance
orientation: directed
signing_date: 2025-12-27T00:00:00Z
commit_hash: genesis
qualifies_edge: e:qualifies:root:guidance-guidance
tags:
  - edge
  - signs
  - boundary
  - genesis
version: 1.0.0
created: 2025-12-27T00:00:00Z
modified: 2025-12-30T00:00:00Z
---

# Signs - Root attests guidance-for-guidance assurance

## Signing Event

**Signer:** [[b0-root]]
**Document:** [[guidance-for-guidance]]
**Date:** 2025-12-27T00:00:00Z

## Semantics

This is a boundary signing edge where the root vertex serves as the bootstrap authority for the foundational guidance-for-guidance assurance. Root's signing role represents the axiomatic acceptance of the boundary complex at system genesis.