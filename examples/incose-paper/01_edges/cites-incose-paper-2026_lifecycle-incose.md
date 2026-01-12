---
type: edge/dependency
extends: edge
id: e:cites:incose-paper-2026:lifecycle-incose
name: Cites - INCOSE Paper uses Lifecycle Document
description: The INCOSE paper leverages content from the lifecycle document
source: v:doc:incose-paper-2026
target: v:doc:lifecycle-incose-paper
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

# Cites - INCOSE Paper uses Lifecycle Document

This edge records that the INCOSE Paper 2026 cites and leverages content from the Lifecycle document.

## Dependency Relationship

**Dependent:** `v:doc:incose-paper-2026` (INCOSE Paper 2026)
**Dependency:** `v:doc:lifecycle-incose-paper` (Lifecycle Document)
**Relationship:** Paper cites/uses lifecycle content

**Usage:** The paper's methodology section is derived from and references the lifecycle document, which describes the test-driven document development process.

## Dependency Usage

- **Section:** Methodology/Process section of the paper
- **Content:** V-model stages, verification/validation workflow
- **Required:** Yes - the lifecycle explains how the framework is applied
- **Cardinality:** One lifecycle document

## Compositional Justification

The lifecycle document provides the detailed process description that the paper summarizes for INCOSE presentation. This citation relationship connects the paper to its methodological foundation.

---

**Note:** This citation edge connects concrete document instances, establishing the paper's reliance on its supporting material.