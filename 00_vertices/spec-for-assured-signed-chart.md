---
type: vertex/spec
extends: doc
id: v:spec:assured_signed_chart
name: Specification for Assured Signed Chart Documents
description: Defines what makes a valid assured-signed chart - complete assurance with explicit signature accountability
tags:
  - vertex
  - doc
  - spec
  - assurance
  - signature
version: 1.0.0
created: 2025-12-30T00:00:00Z
modified: 2025-12-30T00:00:00Z
dependencies:
  - v:spec:assurance_audit
  - v:spec:signature
  - v:spec:signer
---

# Specification for Assured Signed Chart Documents

**This specification defines the structure and requirements for assured-signed chart documents in the knowledge complex.**

## Purpose

Assured-signed charts are **accountability-complete** charts that extend assurance audits with explicit signature faces. Where assurance audit charts verify that every document is assured (has verification + validation + coupling), assured-signed charts additionally require that every document has an explicit **signature face** with a qualified signer.

This creates the complete accountability picture:
- **Assurance** = Structural correctness (verification) + Quality sufficiency (validation)
- **Signature** = Human accountability (signer + qualification + attestation)

The key structural property is that **assurance and signature faces share the validation edge as a common boundary**, creating a topologically connected accountability network.

## Inheritance

```
doc → chart → assurance_audit → assured_signed
```

Assured-signed documents:
- MUST satisfy all requirements of spec-for-charts
- MUST satisfy all requirements of spec-for-assurance-audits
- MUST satisfy additional signature requirements defined below

## Required Frontmatter Fields

### Type Declaration

| Field | Type | Requirement | Value |
|-------|------|-------------|-------|
| `type` | string | REQUIRED | Must be `chart/assured_signed` |
| `extends` | string | REQUIRED | Must be `chart` |

### Inherited from spec-for-assurance-audits

All assurance audit fields remain required:
- `audit_date`, `auditor`, `audit_status`, `audit_coverage`
- `assurance_requirements` object

### Signature Requirements

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `signature_requirements` | object | REQUIRED | Container for signature requirements |
| `signature_requirements.all_docs_signed` | boolean | REQUIRED | Must be `true` for PASS status |
| `signature_requirements.signers` | array[string] | REQUIRED | List of signer vertex IDs |
| `signature_requirements.signature_method` | enum | REQUIRED | One of: `individual`, `collective`, `delegated` |

### Common Boundary Property

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `common_boundaries` | array[object] | REQUIRED | Shared edges between assurance and signature faces |
| `common_boundaries[].validation_edge` | string | REQUIRED | The shared validation edge ID |
| `common_boundaries[].assurance_face` | string | REQUIRED | The assurance face ID |
| `common_boundaries[].signature_face` | string | REQUIRED | The signature face ID |

### Element Extensions

The `elements` object must include:

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `elements.signers` | array[string] | REQUIRED | Signer vertex IDs (v:signer:*) |
| `elements.qualifies_edges` | array[string] | REQUIRED | Qualifies edge IDs (e:qualifies:*) |
| `elements.signs_edges` | array[string] | REQUIRED | Signs edge IDs (e:signs:*) |
| `elements.signature_faces` | array[string] | REQUIRED | Signature face IDs (f:signature:*) |

## Required Sections

All assured-signed chart documents MUST include the following markdown sections in addition to those required by spec-for-assurance-audits:

### 1. Signature Network

**Purpose:** Document the signature structure

**Required Subsections:**
- **Signers** - Table of all signers with their qualifications
- **Qualification Status** - For each signer, which guidances they're qualified for
- **Signature Status** - For each document, which signer signed it
- **Common Boundaries** - For each document, the shared validation edge

**Format:**
```markdown
## Signature Network

### Signers

| Signer ID | Name | GitHub | Qualified For |
|-----------|------|--------|---------------|
| v:signer:<username> | <name> | <username> | [list of guidance IDs] |

### Signature Coverage

| Document | Assurance Face | Signature Face | Signer | Shared Edge |
|----------|----------------|----------------|--------|-------------|
| <doc-id> | <assurance-id> | <signature-id> | <signer-id> | <validation-edge-id> |
```

### 2. Local Constraints

**Purpose:** Document the topological coupling between assurance and signature faces

**Required Content:**
- Common boundary diagram showing shared validation edges
- Constraint verification that all pairs share exactly one edge
- List of all (assurance_face, signature_face, shared_edge) triples

**Format:**
```markdown
## Local Constraints

### Common Boundary Property

For each assured document, its assurance face and signature face MUST share exactly one edge: the validation edge.

```
Assurance Face: (doc, spec, guidance)
  - verification: doc → spec
  - validation: doc → guidance  ← SHARED
  - coupling: spec ↔ guidance

Signature Face: (doc, guidance, signer)
  - validation: doc → guidance  ← SHARED
  - signs: signer → doc
  - qualifies: signer → guidance
```

### Constraint Verification

| Document | Assurance Face | Signature Face | Shared Edge | Valid |
|----------|----------------|----------------|-------------|-------|
| <doc-id> | <assurance-id> | <signature-id> | <edge-id> | ✓/✗ |
```

### 3. Dependency Acknowledgment

**Purpose:** Document all dependencies and their assurance status

**Required Content:**
- Dependency graph showing which documents depend on which
- Assurance status of each dependency
- Signature status of each dependency
- Any external dependencies (not in chart)

**Format:**
```markdown
## Dependency Acknowledgment

### Dependency Graph

| Document | Depends On | Dependency Type | Assured | Signed |
|----------|------------|-----------------|---------|--------|
| <doc-id> | <dep-id> | <type> | ✓/✗ | ✓/✗ |

### External Dependencies

| External | Type | Status | Notes |
|----------|------|--------|-------|
| <ext-ref> | <type> | <status> | <notes> |

### Root Anchoring

All assurance chains trace to: [list boundary complex root faces]
```

## Hard Requirements (MUST)

### Inherited from spec-for-assurance-audits

All assurance audit requirements remain in force:
1. Complete assurance coverage
2. Root anchored
3. Valid triangles
4. Structural checks
5. Quality assessments
6. Documentation
7. Audit trail

### Additional Signature Requirements

| ID | Requirement |
|----|-------------|
| SIG-1 | Every document vertex in the chart MUST have exactly one signature face |
| SIG-2 | Every signature face MUST share its validation edge with an assurance face |
| SIG-3 | Every signer MUST have valid qualifies edges for all guidances they sign against |
| SIG-4 | Qualifies edges MUST be valid (non-expired) at signing time |
| SIG-5 | Signs edges MUST reference the commit hash of the signing event |
| SIG-6 | All signers MUST have verified GitHub usernames |
| SIG-7 | Common boundaries MUST be explicitly documented |
| SIG-8 | Dependencies MUST be acknowledged with assurance/signature status |

### Structural Constraints

| ID | Constraint |
|----|------------|
| STR-1 | For each document D with assurance face A and signature face S: |
|       | - A.vertices ∩ S.vertices = {D, guidance} |
|       | - A.edges ∩ S.edges = {validation_edge} |
| STR-2 | The validation edge in both faces MUST be the same edge (same ID) |
| STR-3 | The signer in S MUST be qualified for the guidance in S |

## Audit Status Definitions

### PASS (Assured and Signed)

**Criteria:**
- All assurance audit PASS criteria met
- All documents have valid signature faces
- All signers qualified at signing time
- All common boundaries verified
- All dependencies acknowledged

### PARTIAL (Partially Signed)

**Criteria:**
- Assurance audit PASS or PARTIAL
- Some documents have signature faces
- Some signatures or qualifications pending

### FAIL (Signature Incomplete)

**Criteria:**
- Missing signature faces for documented vertices
- Invalid qualifies edges (expired or missing)
- Common boundary violations
- Unacknowledged dependencies

## Validation Rules

### Signature Face Validation

For each document D in the chart:

```
ASSERT: EXISTS signature_face WHERE D IN signature_face.vertices
ASSERT: signature_face.validation_edge == assurance_face.validation_edge
ASSERT: signature_face.signer HAS qualifies_edge TO signature_face.guidance
ASSERT: qualifies_edge.valid_at(signature_face.signing_date)
```

### Common Boundary Validation

For each (assurance_face, signature_face) pair:

```
ASSERT: |assurance_face.edges ∩ signature_face.edges| == 1
ASSERT: shared_edge.type == "edge/validation"
```

### Dependency Validation

For each document D:

```
ASSERT: D.dependencies ALL IN chart.elements.vertices OR acknowledged_external
ASSERT: D.dependencies ALL (assured AND signed) OR acknowledged_exception
```

## Quality Criteria

### Excellent Assured-Signed Chart

- 100% assurance coverage (from assurance_audit)
- 100% signature coverage
- All qualifies edges current (no expired credentials)
- All common boundaries verified
- All dependencies assured and signed
- Clear accountability chain
- Visualizable signature network

### Good Assured-Signed Chart

- ≥90% assurance coverage
- ≥90% signature coverage
- Most qualifies edges current
- Common boundaries mostly verified
- Most dependencies acknowledged

### Adequate Assured-Signed Chart

- ≥75% assurance coverage
- ≥75% signature coverage
- Critical documents signed
- Common boundary property documented
- Key dependencies acknowledged

### Poor Assured-Signed Chart

- <75% coverage
- Missing signature faces
- Unverified common boundaries
- Unacknowledged dependencies
- Unclear accountability

## Schema Summary

```yaml
# Type declaration
type: chart/assured_signed
extends: chart

# Inherited from assurance_audit
audit_date: <ISO8601>
auditor: <string>
audit_status: PASS | PARTIAL | FAIL
audit_coverage: <string>
assurance_requirements:
  all_vertices_assured: <boolean>
  assurance_method: standard | boundary | mixed
  minimum_assurance_level: ASSURED | VERIFIED | VALIDATED

# Signature-specific
signature_requirements:
  all_docs_signed: <boolean>
  signers: [<signer-ids>]
  signature_method: individual | collective | delegated

# Common boundary documentation
common_boundaries:
  - validation_edge: <edge-id>
    assurance_face: <face-id>
    signature_face: <face-id>

# Extended elements
elements:
  vertices: [...]
  edges: [...]
  faces: [...]  # includes both assurance and signature faces
  signers: [<signer-ids>]
  qualifies_edges: [<qualifies-edge-ids>]
  signs_edges: [<signs-edge-ids>]
  signature_faces: [<signature-face-ids>]

# Required body sections (in addition to assurance_audit sections)
## Signature Network
  ### Signers
  ### Signature Coverage
## Local Constraints
  ### Common Boundary Property
  ### Constraint Verification
## Dependency Acknowledgment
  ### Dependency Graph
  ### External Dependencies
  ### Root Anchoring
```

## Compliance

A document claiming `type: chart/assured_signed` is compliant with this specification if and only if:

### Inherited Compliance

1. All requirements from spec-for-charts are satisfied
2. All requirements from spec-for-assurance-audits are satisfied

### Signature Compliance

3. Every document has exactly one signature face
4. All signature faces share validation edge with corresponding assurance face
5. All signers have valid qualifies edges
6. All signing events recorded with commit hash
7. Common boundaries explicitly documented
8. All dependencies acknowledged

### Documentation Compliance

9. Signature Network section present with required tables
10. Local Constraints section present with common boundary verification
11. Dependency Acknowledgment section present

## Related Specifications

| Spec | Relationship | Purpose |
|------|--------------|---------|
| v:spec:chart | Grandparent | Base chart requirements |
| v:spec:assurance_audit | Parent | Assurance audit requirements |
| v:spec:signature | Referenced | Signature face structure |
| v:spec:signer | Referenced | Signer vertex requirements |
| v:spec:qualifies | Referenced | Qualification edge requirements |
| v:spec:signs | Referenced | Signing edge requirements |

---

**Note:** Assured-signed charts represent the complete accountability picture for a document network. By requiring both assurance faces (structural + quality) and signature faces (human accountability), and by documenting their shared boundaries, these charts provide full traceability from document content to human responsibility.
