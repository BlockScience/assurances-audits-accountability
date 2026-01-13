---
type: edge/signs
extends: edge
id: e:signs:admin:ontology-base
name: Signs - admin signs ontology-base
description: Admin signer signs the ontology-base validation
source: v:signer:admin
target: v:ontology:base
source_type: vertex/signer
target_type: vertex/ontology
orientation: directed
signing_date: 2026-01-13T00:00:00Z
commit_hash: foundation
tags:
  - edge
  - signs
  - foundation
version: 1.0.0
created: 2026-01-13T00:00:00Z
modified: 2026-01-13T00:00:00Z
---

# Signs - admin signs ontology-base

This edge records that the admin signer has signed the ontology-base validation.

## Signing Relationship

**Source:** `v:signer:admin` (the signer)
**Target:** `v:ontology:base` (the document)

## Accountability

- **Signer:** Admin (placeholder, replaced during aaa init)
- **Date:** 2026-01-13
- **Commit:** foundation (bootstrap)
