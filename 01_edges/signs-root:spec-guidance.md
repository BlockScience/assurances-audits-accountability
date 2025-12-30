---
type: edge/signs
extends: edge
id: e:signs:root:spec-guidance
name: Signs - Root attests spec-for-guidance assurance
description: Bootstrap signing edge where root anchors the spec-for-guidance assurance
source: b0:root
target: v:spec:guidance
source_type: vertex/b0
target_type: vertex/spec
orientation: directed
signing_date: 2025-12-27T00:00:00Z
commit_hash: genesis
qualifies_edge: e:qualifies:root:guidance-spec
tags:
  - edge
  - signs
  - boundary
  - genesis
version: 1.0.0
created: 2025-12-27T00:00:00Z
modified: 2025-12-30T00:00:00Z
---

# Signs - Root attests spec-for-guidance assurance

## Signing Event

**Signer:** [[b0-root]]
**Document:** [[spec-for-guidance]]
**Date:** 2025-12-27T00:00:00Z

## Semantics

This is a boundary signing edge where the root vertex serves as the bootstrap authority for the spec-for-guidance assurance.