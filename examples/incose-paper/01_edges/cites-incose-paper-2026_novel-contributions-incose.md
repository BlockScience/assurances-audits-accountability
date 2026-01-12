---
type: edge/dependency
extends: edge
id: e:cites:incose-paper-2026:novel-contributions-incose
name: Cites - INCOSE Paper uses Novel Contributions Document
description: The INCOSE paper leverages content from the novel contributions document
source: v:doc:incose-paper-2026
target: v:doc:novel-contributions-incose-paper
source_type: vertex/doc
target_type: vertex/doc
orientation: directed
dependency_type: reference
required: true
tags:
  - edge
  - dependency
  - citation
version: 1.0.0
created: 2025-12-30T23:30:00Z
modified: 2025-12-30T23:30:00Z
---

# Cites - INCOSE Paper uses Novel Contributions Document

This edge records that the INCOSE Paper 2026 cites and leverages content from the Novel Contributions document.

## Dependency Relationship

**Dependent:** `v:doc:incose-paper-2026` (INCOSE Paper 2026)
**Dependency:** `v:doc:novel-contributions-incose-paper` (Novel Contributions Document)
**Relationship:** Paper cites/uses novel contributions content

**Usage:** The paper's contributions and claims sections are derived from and reference the novel contributions document.

## Dependency Usage

- **Section:** Contributions / Key Claims section of the paper
- **Content:** Novel contributions, differentiation from prior work
- **Required:** Yes - articulates what's new
- **Cardinality:** One novel contributions document

## Compositional Justification

The novel contributions document provides the detailed articulation of what's new that the paper presents. This citation relationship connects the paper to its core claims.

---

**Note:** This citation edge connects concrete document instances, establishing the paper's reliance on its supporting material.