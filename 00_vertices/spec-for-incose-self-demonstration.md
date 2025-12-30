---
type: vertex/spec
extends: spec-for-incose-paper
id: v:spec:incose-self-demonstration
name: Specification for INCOSE Self-Demonstrating Paper
description: Extended specification for INCOSE papers that demonstrate their framework by being instances of it, requiring consistency with architecture, lifecycle, literature review, and novel contributions documents
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-30T21:00:00Z
modified: 2025-12-30T21:00:00Z
dependencies:
  - v:spec:incose-paper
---

# Specification for INCOSE Self-Demonstrating Paper

## Purpose

This specification **extends** `spec-for-incose-paper` with additional requirements for papers that demonstrate their framework by being instances of it. Self-demonstrating papers must maintain consistency and completeness relative to four supporting documents that exist at time of production:

1. **Architecture Document** - Defines the framework's conceptual, functional, logical, and physical layers
2. **Lifecycle Document** - Describes the engineering process used to produce assured documents
3. **Literature Review** - Provides the scholarly foundation and citation catalog
4. **Novel Contributions Document** - Articulates what is new and differentiating

This specification ensures the paper accurately reflects, cites, and is consistent with these authoritative supporting documents.

---

## Inheritance

This specification inherits ALL requirements from `spec-for-incose-paper` v2.0.0. A document conforming to this specification MUST also conform to the parent specification.

**Parent Requirements Remain in Force:**
- Word limit ≤7,000 words
- All required sections (Abstract through References)
- AI disclosure requirements
- Anonymization requirements
- INCOSE template format
- All structural constraints

This specification adds additional requirements for self-demonstrating papers.

---

## Required Supporting Documents

### Supporting Document Inventory

A self-demonstrating paper MUST have the following documents available at time of production:

| Document Type | Spec | Expected ID Pattern | Purpose |
|---------------|------|---------------------|---------|
| **Architecture** | `spec-for-architecture` | `v:doc:architecture-*` | Technical framework definition |
| **Lifecycle** | `spec-for-lifecycle` | `v:doc:lifecycle-*` | Engineering process description |
| **Literature Review** | `spec-for-incose-literature-review` | `v:doc:literature-review-*` | Scholarly foundation |
| **Novel Contributions** | `spec-for-novel-contributions` | `v:doc:novel-contributions-*` | Differentiation articulation |

### Supporting Document Status

| Requirement | Description |
|-------------|-------------|
| Existence | All four supporting documents MUST exist |
| Assurance Status | Supporting documents SHOULD be assured (verified and validated) before paper finalization |
| Accessibility | Supporting documents MUST be accessible to authors during paper production |

---

## Consistency Requirements

### C1: Architecture Consistency

The paper MUST be consistent with its architecture document.

| Check | Requirement | Location in Paper |
|-------|-------------|-------------------|
| C1.1 | All four architecture layers (Conceptual, Functional, Logical, Physical) MUST be referenced or reflected | Methodology |
| C1.2 | V-model mapping from architecture MUST be consistent with paper's V&V discussion | Background, Methodology |
| C1.3 | Stakeholder needs from architecture MUST align with problem statement in paper | Introduction |
| C1.4 | Physical implementation choices in architecture MUST match tooling described | Methodology, Results |
| C1.5 | Functional requirements in architecture MUST map to demonstrated capabilities | Results |

### C2: Lifecycle Consistency

The paper MUST be consistent with its lifecycle document.

| Check | Requirement | Location in Paper |
|-------|-------------|-------------------|
| C2.1 | Paper MUST follow the lifecycle phases described in the lifecycle document | Implicit in structure |
| C2.2 | Lifecycle phases referenced in paper MUST match lifecycle document terminology | Methodology |
| C2.3 | If paper describes its own production process, it MUST match lifecycle document | Results, Discussion |
| C2.4 | Foundation/boundary complex assumptions MUST be consistent between documents | Background, Methodology |

### C3: Literature Review Consistency

The paper MUST be consistent with its literature review document.

| Check | Requirement | Location in Paper |
|-------|-------------|-------------------|
| C3.1 | All citations in paper MUST appear in literature review catalog (or be explicitly new) | References |
| C3.2 | Gap analysis from literature review MUST align with paper's contribution claims | Background, Introduction |
| C3.3 | Thematic organization in literature review SHOULD inform Background structure | Background |
| C3.4 | Positioning statement from literature review MUST be consistent with paper's positioning | Introduction, Background |
| C3.5 | Citation count in paper SHOULD be ≥ literature review theme count × 2 | References |

### C4: Novel Contributions Consistency

The paper MUST be consistent with its novel contributions document.

| Check | Requirement | Location in Paper |
|-------|-------------|-------------------|
| C4.1 | All claimed contributions in paper MUST appear in novel contributions document | Abstract, Introduction, Conclusion |
| C4.2 | Novelty claims MUST NOT exceed those in novel contributions document | All sections |
| C4.3 | Differentiation from prior work MUST match novel contributions analysis | Background |
| C4.4 | Evidence cited for novelty MUST match novel contributions document | Results |

---

## Completeness Requirements

### CP1: Architecture Completeness

| Check | Requirement |
|-------|-------------|
| CP1.1 | Paper MUST cover all four architecture layers in some form |
| CP1.2 | Paper MUST NOT introduce architectural elements not in architecture document |
| CP1.3 | Paper MUST address all stakeholder needs identified in architecture |

### CP2: Lifecycle Completeness

| Check | Requirement |
|-------|-------------|
| CP2.1 | Paper's self-demonstration MUST complete all lifecycle phases |
| CP2.2 | Paper MUST reference key properties from lifecycle document |
| CP2.3 | If paper discusses assurance, it MUST align with lifecycle's assurance model |

### CP3: Literature Review Completeness

| Check | Requirement |
|-------|-------------|
| CP3.1 | Paper MUST cite at least one source from each literature review theme |
| CP3.2 | Paper MUST address all gaps identified in literature review |
| CP3.3 | Paper's Background MUST cover all themes from literature review |

### CP4: Novel Contributions Completeness

| Check | Requirement |
|-------|-------------|
| CP4.1 | Paper MUST articulate ALL contributions from novel contributions document |
| CP4.2 | Paper MUST provide evidence for EACH claimed contribution |
| CP4.3 | Paper MUST address differentiation for EACH contribution |

---

## Cross-Document Traceability

### Traceability Requirements

| Requirement | Description |
|-------------|-------------|
| T1 | Paper SHOULD include references to supporting documents (in final version) |
| T2 | Claims in paper MUST be traceable to supporting document sections |
| T3 | Terminology MUST be consistent across paper and all supporting documents |
| T4 | Figures/diagrams in paper SHOULD derive from architecture or lifecycle documents |

### Terminology Consistency

The paper MUST use consistent terminology with supporting documents:

| Term Type | Requirement |
|-----------|-------------|
| Framework components | MUST match architecture document naming |
| Process phases | MUST match lifecycle document naming |
| Prior work references | MUST match literature review categorization |
| Contribution names | MUST match novel contributions document |

---

## Self-Demonstration Requirements

### SD1: The Paper as Instance

| Check | Requirement |
|-------|-------------|
| SD1.1 | Paper MUST explicitly state it is a self-demonstrating instance |
| SD1.2 | Paper MUST exist as a vertex in an assurance chart |
| SD1.3 | Paper MUST pass its own verification criteria |
| SD1.4 | Paper MUST be validated against its own guidance criteria |

### SD2: Evidence of Self-Demonstration

| Check | Requirement | Location |
|-------|-------------|----------|
| SD2.1 | Paper MUST include audit results showing its assurance status | Results |
| SD2.2 | Paper MUST reference its own specification and guidance | Methodology |
| SD2.3 | Paper MUST describe how it was produced using the framework | Results |
| SD2.4 | Paper SHOULD include visualization of its assurance chart | Figures |

### SD3: Recursive Consistency

| Check | Requirement |
|-------|-------------|
| SD3.1 | Paper's claims about the framework MUST be verified by the paper's own existence |
| SD3.2 | Any limitation claimed in paper MUST be demonstrable in the paper itself |
| SD3.3 | The paper's assurance triangle MUST be complete before claiming "assured" status |

---

## Validation Rules

### Extended Verification Checks

In addition to parent specification checks, a self-demonstrating paper MUST pass:

| Rule | Check | Severity |
|------|-------|----------|
| SD-V1 | Architecture document exists and is referenced | REQUIRED |
| SD-V2 | Lifecycle document exists and is referenced | REQUIRED |
| SD-V3 | Literature review document exists | REQUIRED |
| SD-V4 | Novel contributions document exists | REQUIRED |
| SD-V5 | All C1 (architecture consistency) checks pass | REQUIRED |
| SD-V6 | All C2 (lifecycle consistency) checks pass | REQUIRED |
| SD-V7 | All C3 (literature review consistency) checks pass | REQUIRED |
| SD-V8 | All C4 (novel contributions consistency) checks pass | REQUIRED |
| SD-V9 | All CP (completeness) checks pass | REQUIRED |
| SD-V10 | All SD (self-demonstration) checks pass | REQUIRED |
| SD-V11 | Paper vertex exists in assurance chart | REQUIRED |
| SD-V12 | Paper assurance triangle is closable | REQUIRED |

### Pre-Submission Checklist (Extended)

In addition to parent specification checklist:

**Supporting Document Checks:**
- [ ] Architecture document exists and is assured
- [ ] Lifecycle document exists and is assured
- [ ] Literature review document exists and is assured
- [ ] Novel contributions document exists and is assured

**Consistency Checks:**
- [ ] All four architecture layers represented in paper
- [ ] V-model mapping consistent with architecture
- [ ] Lifecycle phases terminology matches lifecycle document
- [ ] All citations appear in literature review catalog
- [ ] Gap analysis alignment verified
- [ ] All contributions from novel contributions document included
- [ ] Novelty claims do not exceed novel contributions document

**Completeness Checks:**
- [ ] At least one citation from each literature review theme
- [ ] All gaps from literature review addressed
- [ ] All contributions articulated with evidence
- [ ] All stakeholder needs from architecture addressed

**Self-Demonstration Checks:**
- [ ] Paper explicitly states self-demonstration
- [ ] Paper exists as vertex in assurance chart
- [ ] Audit results included showing assurance status
- [ ] Assurance chart visualization included or referenced

---

## Schema Extension

### Extended Metadata Schema

```yaml
# Extends paper metadata from spec-for-incose-paper

paper:
  # All parent schema fields...

  # Self-demonstration specific
  self_demonstrating: true  # REQUIRED for this type

  supporting_documents:
    architecture:
      id: <vertex-id>           # REQUIRED
      assured: <boolean>        # RECOMMENDED: true
    lifecycle:
      id: <vertex-id>           # REQUIRED
      assured: <boolean>        # RECOMMENDED: true
    literature_review:
      id: <vertex-id>           # REQUIRED
      assured: <boolean>        # RECOMMENDED: true
    novel_contributions:
      id: <vertex-id>           # REQUIRED
      assured: <boolean>        # RECOMMENDED: true

  assurance_status:
    vertex_id: <vertex-id>      # REQUIRED
    chart_id: <chart-id>        # REQUIRED
    audit_status: <pass|fail>   # REQUIRED
    coverage: <percentage>      # REQUIRED
```

---

## Compliance Statement

A document claiming `type: vertex/doc` with target specification `v:spec:incose-self-demonstration` is **compliant** if and only if:

### Required Compliance (Parent + Extended)

1. All requirements from `spec-for-incose-paper` are satisfied
2. All four supporting documents exist
3. All consistency checks (C1-C4) pass
4. All completeness checks (CP1-CP4) pass
5. All self-demonstration checks (SD1-SD3) pass
6. Paper exists as vertex in an assurance chart
7. Paper assurance triangle is complete

### Recommended Compliance

8. All supporting documents are assured before paper finalization
9. Assurance chart visualization included in paper
10. Cross-document terminology is perfectly consistent

---

## Related Documents

| Document | Relationship | Purpose |
|----------|--------------|---------|
| `v:spec:incose-paper` | Parent specification | Base structural requirements |
| `v:guidance:incose-self-demonstration` | Coupled guidance | Quality criteria for self-demonstration |
| `v:spec:architecture` | Supporting doc spec | Architecture document requirements |
| `v:spec:lifecycle` | Supporting doc spec | Lifecycle document requirements |
| `v:spec:incose-literature-review` | Supporting doc spec | Literature review requirements |
| `v:spec:novel-contributions` | Supporting doc spec | Novel contributions requirements |

---

**Note:** This specification extends `spec-for-incose-paper` for the special case of self-demonstrating papers. The additional requirements ensure the paper is consistent with and complete relative to its supporting documents, enabling the "paper is its own proof" claim that is central to self-demonstrating frameworks.
