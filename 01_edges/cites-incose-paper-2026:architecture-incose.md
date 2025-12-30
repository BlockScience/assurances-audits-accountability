---
type: edge/dependency
extends: edge
id: e:cites:incose-paper-2026:architecture-incose
name: Cites - INCOSE Paper uses Architecture Document
description: The INCOSE paper leverages content from the architecture document
source: v:doc:incose-paper-2026
target: v:doc:architecture-incose-paper
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

# Cites - INCOSE Paper uses Architecture Document

This edge records that the INCOSE Paper 2026 cites and leverages content from the Architecture document.

## Dependency Relationship

**Dependent:** `v:doc:incose-paper-2026` (INCOSE Paper 2026)
**Dependency:** `v:doc:architecture-incose-paper` (Architecture Document)
**Relationship:** Paper cites/uses architecture content

**Usage:** The paper's architecture section is derived from and references the architecture document, which provides the detailed typed simplicial complex framework description.

## Dependency Usage

- **Section:** Architecture section of the paper
- **Content:** Typed simplicial complex structure, compositional patterns
- **Required:** Yes - the architecture is foundational to the paper's claims
- **Cardinality:** One architecture document

## Compositional Justification

The paper is composed from its supporting documents. The architecture document provides the detailed technical framework that the paper summarizes. This is a reference/citation relationship at the document instance level, not a type-level composition.

---

**Note:** This citation edge connects concrete document instances, establishing the paper's reliance on its supporting material.