---
type: template/chart/assured_signed
extends: chart
id: template:chart:assured_signed
name: Assured Signed Chart Template
description: Complete accountability chart with assurance and signature coverage
instantiable: true
tags:
  - template
  - chart
  - assurance
  - signature
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
---

# Assured Signed Chart Template

**Complete accountability chart combining assurance (verification + validation) with signatures (human attestation).**

Assured-signed charts extend assurance audits by adding explicit signature faces for every document. The key structural property is that assurance and signature faces share the validation edge as a common boundary.

## Type Hierarchy

```
doc (abstract)
└── chart (concrete)
    └── assurance_audit (concrete)
        └── assured_signed (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `chart` (via `assurance_audit`)
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

### From chart

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `chart/assured_signed` |
| `extends` | string | Must be `chart` |
| `id` | string | Format: `c:assured-signed:<name>` |
| `constructed_by` | string | Constructor identity |
| `construction_method` | string | `manual`, `assisted`, `automated` |
| `construction_date` | datetime | When constructed |
| `purpose` | string | Why this chart exists |
| `scope` | string | What is included/excluded |
| `elements` | object | Vertices, edges, faces |

### From assurance_audit

| Field | Type | Description |
|-------|------|-------------|
| `audit_date` | datetime | When audit was performed |
| `auditor` | string | Who performed audit |
| `audit_status` | string | `PASS`, `PARTIAL`, `FAIL` |
| `audit_coverage` | string | Coverage description |
| `assurance_requirements` | object | Assurance constraints |

### Signature-specific

| Field | Type | Description |
|-------|------|-------------|
| `signature_requirements` | object | Signature constraints |
| `signature_requirements.all_docs_signed` | boolean | All docs have signatures |
| `signature_requirements.signers` | array | List of signer IDs |
| `signature_requirements.signature_method` | string | `individual`, `collective`, `delegated` |
| `common_boundaries` | array | Shared edge documentation |

### Extended Elements

| Field | Type | Description |
|-------|------|-------------|
| `elements.signers` | array | Signer vertex IDs |
| `elements.qualifies_edges` | array | Qualifies edge IDs |
| `elements.signs_edges` | array | Signs edge IDs |
| `elements.signature_faces` | array | Signature face IDs |

## Tag Requirements

```yaml
tags:
  - chart
  - assurance_audit
  - assured_signed
```

## Required Body Sections

### From chart

- Chart Overview
- Why This Chart Exists
- What This Chart Contains
- How This Chart Was Constructed
- Element Tables (Vertices, Edges, Faces)
- Chart Properties
- Verification

### From assurance_audit

- Assurance Audit Results
- Audit Trail

### Signature-specific

- **Signature Network** - Signers, qualifications, coverage
- **Local Constraints** - Common boundary documentation
- **Dependency Acknowledgment** - Dependency status tracking

## Key Structural Property

```
                    doc
                   / | \
                  /  |  \
         verification | validation (SHARED EDGE)
               /     |     \
           spec    signs   guidance
              \      |      /
          coupling   |  qualifies
                 \   |   /
                  signer

Assurance Face: (doc, spec, guidance)
  Edges: verification, validation, coupling

Signature Face: (doc, guidance, signer)
  Edges: validation, signs, qualifies

SHARED: The validation edge appears in both faces
```

## Example Instance

```yaml
---
type: chart/assured_signed
extends: chart
id: c:assured-signed:incose-paper
name: Assured Signed INCOSE Paper Chart
description: Complete accountability for INCOSE self-demonstration

# Chart construction
constructed_by: claude-opus-4-5-20251101
construction_method: assisted
construction_date: 2025-12-30T00:00:00Z
purpose: Demonstrate complete accountability for self-demonstrating paper
scope: INCOSE paper with all dependencies, assurance, and signatures

# Assurance audit fields
audit_date: 2025-12-30T00:00:00Z
auditor: claude-opus-4-5-20251101
audit_status: PASS
audit_coverage: 100% (8/8 vertices assured)
assurance_requirements:
  all_vertices_assured: true
  assurance_method: mixed
  minimum_assurance_level: ASSURED

# Signature fields
signature_requirements:
  all_docs_signed: true
  signers:
    - v:signer:mzargham
  signature_method: individual

# Common boundaries
common_boundaries:
  - validation_edge: e:validation:incose-paper-spec:guidance-spec
    assurance_face: f:assurance:incose-paper-spec
    signature_face: f:signature:incose-paper-spec:mzargham

# Elements
elements:
  vertices:
    - v:spec:incose-paper
    - v:guidance:incose-paper
    - v:doc:incose-paper-2026
    - v:signer:mzargham
  edges:
    - e:coupling:incose-paper
    - e:verification:incose-paper-spec:spec-spec
    - e:validation:incose-paper-spec:guidance-spec
    - e:qualifies:mzargham:guidance-spec
    - e:signs:mzargham:spec-incose-paper
  faces:
    - f:assurance:incose-paper-spec
    - f:signature:incose-paper-spec:mzargham
  signers:
    - v:signer:mzargham
  qualifies_edges:
    - e:qualifies:mzargham:guidance-spec
  signs_edges:
    - e:signs:mzargham:spec-incose-paper
  signature_faces:
    - f:signature:incose-paper-spec:mzargham

tags:
  - chart
  - assurance_audit
  - assured_signed
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
---

# Assured Signed INCOSE Paper Chart

This chart demonstrates complete accountability for the INCOSE self-demonstration paper.

## Why This Chart Exists

**Motivation:** Provide complete accountability evidence for the self-demonstrating paper.

**Context:** The INCOSE paper claims documents can be systematically assured AND signed. This chart proves that claim.

**Intended Use:** Primary demonstration artifact showing assurance + signature coverage.

## What This Chart Contains

### Scope Definition

**Included:**
- INCOSE paper spec, guidance, and content
- All assurance faces for these documents
- All signature faces with signer qualification
- Common boundary documentation

**Excluded:**
- Boundary complex (assumed as foundation)
- Other document types

### Element Summary

**Vertices:** 4 (3 docs + 1 signer)
**Edges:** 5+ (coupling, verification, validation, qualifies, signs)
**Faces:** 2+ (assurance + signature per document)

## Signature Network

### Signers

| Signer ID | Name | GitHub | Qualified For |
|-----------|------|--------|---------------|
| v:signer:mzargham | Michael Zargham | mzargham | v:guidance:spec, v:guidance:guidance |

### Signature Coverage

| Document | Assurance Face | Signature Face | Signer | Shared Edge |
|----------|----------------|----------------|--------|-------------|
| v:spec:incose-paper | f:assurance:incose-paper-spec | f:signature:incose-paper-spec:mzargham | v:signer:mzargham | e:validation:incose-paper-spec:guidance-spec |

## Local Constraints

### Common Boundary Property

For each document, assurance and signature faces share the validation edge:

| Document | Assurance Face | Signature Face | Shared Edge | Valid |
|----------|----------------|----------------|-------------|-------|
| v:spec:incose-paper | f:assurance:... | f:signature:... | e:validation:... | ✓ |

## Dependency Acknowledgment

### Root Anchoring

All chains trace to:
- b2:spec-spec
- b2:guidance-guidance

## Assurance Audit Results

**Status:** PASS
**Coverage:** 100%

## Accountability Statement

Constructed with LLM assistance, approved by mzargham.

**Signed:** mzargham
**Date:** 2025-12-30
```

## Validation Rules

1. **Type Format:** `type` must be `chart/assured_signed`
2. **Assurance Coverage:** All assurance_audit requirements must be met
3. **Signature Coverage:** Every document must have a signature face
4. **Common Boundaries:** Every (assurance, signature) pair must share validation edge
5. **Signer Qualifications:** All signers must have valid qualifies edges
6. **Required Sections:** Must include Signature Network, Local Constraints, Dependency Acknowledgment
7. **Element Arrays:** Must include signers, qualifies_edges, signs_edges, signature_faces

## Usage Notes

### When to Use

Use assured_signed charts when you need:
- Complete accountability (not just quality assurance)
- Explicit human responsibility attribution
- Audit-ready documentation
- Self-demonstration evidence

### Common Boundary Verification

For each document D:
```
VERIFY: assurance_face.validation_edge == signature_face.validation_edge
```

This ensures the topological coupling between quality assurance and accountability.
