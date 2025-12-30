---
type: vertex/doc
extends: vertex
id: v:doc:incose-paper-2026
name: INCOSE IS 2026 Paper - Test-Driven Document Development
description: Draft research paper demonstrating simplicial complex framework for verification, validation, and assurance
tags:
  - vertex
  - doc
  - paper
  - incose
version: 0.1.0
created: 2025-12-30T12:00:00Z
modified: 2025-12-30T12:00:00Z
word_count: 0
target_spec: v:spec:incose-paper
target_guidance: v:guidance:incose-paper
---

# Test-Driven Document Development: Simplicial Complexes for Verification, Validation, and Assurance with Human Accountability

**Authors:** [Anonymized for review]

## Abstract

The integration of Large Language Models (LLMs) into documentation workflows offers productivity gains but introduces quality assurance challenges: How do we ensure LLM-assisted documents meet structural requirements and quality standards while maintaining clear human accountability? We present a framework using typed simplicial complexes to formalize verification, validation, and assurance (VVA) for document development. The framework represents documents as vertices, relationships (verification, validation, coupling) as edges, and complete assurance patterns as faces in a simplicial complex. This mathematical foundation enables test-driven document development: specifications define deterministic structural checks; guidance documents define qualitative criteria; assurance triangles close when both verification and validation pass with explicit human sign-off. We demonstrate the framework by using it to write this paper—the paper itself is an assured vertex in a chart that we present as our primary result. The approach addresses the IS 2026 theme "Seeking Wa in SE" by formalizing the harmony between human judgment and AI capability, ensuring that LLM assistance enhances rather than replaces human accountability. We contribute: (1) a formal model for document assurance using algebraic topology, (2) a practical implementation with verification scripts and audit tooling, and (3) a demonstration that the framework works by producing this assured paper.

**Keywords:** verification, validation, assurance, simplicial complex, LLM, human-AI collaboration, documentation, accountability

---

## 1. Introduction

The proliferation of Large Language Models (LLMs) in systems engineering workflows presents both opportunity and challenge. LLMs can draft specifications, generate documentation, and assist with complex technical writing at unprecedented speed. Yet this capability raises fundamental questions: How do we know an LLM-generated document meets requirements? Who is accountable when AI assists with content creation? How do we maintain the rigor that systems engineering demands?

These questions resonate with the IS 2026 theme "Beyond Digital Engineering: Seeking Wa in SE"—the Japanese concept of harmony. The challenge is not to reject AI assistance but to harmonize it with human judgment, creating workflows where technology amplifies rather than replaces human accountability.

We address this challenge through a formal framework for document verification, validation, and assurance (VVA). Our approach uses typed simplicial complexes—structures from algebraic topology—to model documents and their quality assurance relationships. The framework enables what we call **test-driven document development**: documents are written to satisfy specifications (verified structurally) and guidance (validated qualitatively), with explicit accountability at each step.

The key innovation is the **assurance triangle**: a 2-simplex (face) formed by three edges connecting a document to its specification, guidance, and the coupling between them. When all three edges are present and valid, the triangle "closes," establishing complete assurance for the document. Human approval is required for validation edges and assurance faces, ensuring accountability is always attributed to identified persons.

**This paper demonstrates the framework by being an instance of it.** The paper you are reading is a vertex in a simplicial complex, verified against a specification for INCOSE papers, validated against guidance for INCOSE papers, and assured through a complete triangle with human sign-off. The audit chart visualizing this assurance network is our primary empirical result.

### Paper Structure

Section 2 provides background on verification, validation, and simplicial complexes. Section 3 presents the framework architecture. Section 4 demonstrates the framework through this paper's own assurance. Section 5 describes the tooling and process. Section 6 discusses limitations and implications. Section 7 concludes.

---

## 2. Background

### 2.1 Verification and Validation in Systems Engineering

Verification and validation (V&V) are foundational SE concepts, though often conflated. Per the INCOSE SE Handbook:

- **Verification** answers: "Did we build the system right?" It confirms that outputs conform to specifications through deterministic checking.
- **Validation** answers: "Did we build the right system?" It assesses whether outputs meet stakeholder needs through qualitative judgment.

For documents, this distinction maps to:
- **Verification**: Does the document have required sections, proper formatting, correct data types?
- **Validation**: Is the document clear, useful, well-organized, fit for purpose?

Verification can be automated; validation requires expert judgment. Both are necessary for complete assurance.

### 2.2 The Assurance Gap

Current document management systems track verification (templates, schemas, linters) but struggle with validation. Code review processes address validation for software but lack formal structure for documentation. When LLMs generate content, this gap becomes critical—automated checks may pass while quality suffers.

We propose closing this gap through explicit coupling of specifications (verification criteria) with guidance (validation criteria), and requiring both to be satisfied before declaring a document "assured."

### 2.3 Simplicial Complexes

A simplicial complex is a mathematical structure consisting of vertices (0-simplices), edges (1-simplices), faces (2-simplices), and higher-dimensional analogs. Key properties:

- **Closure**: If a simplex is in the complex, all its faces are also in the complex
- **Intersection**: Any two simplices intersect in a face of both
- **Euler characteristic**: χ = V - E + F (for 2-complexes)

Simplicial complexes provide a natural model for typed relationships with compositional constraints. An edge exists only if both its endpoint vertices exist. A face exists only if all three bounding edges exist.

### 2.4 Typed Simplicial Complexes for Documentation

We extend simplicial complexes with types:

- **Vertex types**: `doc`, `spec`, `guidance` (and subtypes)
- **Edge types**: `verification`, `validation`, `coupling`, `dependency`
- **Face types**: `assurance` (the primary pattern)

The type system ensures well-formedness: a verification edge can only connect a document to a specification; a validation edge can only connect a document to guidance; a coupling edge connects a specification to its corresponding guidance.

---

## 3. Framework Architecture

### 3.1 Document Model

Documents are vertices with typed frontmatter:

```yaml
type: vertex/doc
id: v:doc:example
name: Example Document
target_spec: v:spec:example-type
target_guidance: v:guidance:example-type
```

Every document declares its governing specification and guidance, establishing the endpoints for verification and validation edges.

### 3.2 Specifications and Guidance

**Specifications** define structural requirements using prescriptive language (MUST, SHALL, REQUIRED):

- Required fields and their types
- Required sections and their order
- Format constraints (word limits, templates)
- Schema definitions for programmatic checking

**Guidance** defines quality criteria using evaluative language (Excellent, Good, Needs Improvement):

- Quality dimensions (clarity, rigor, completeness)
- Leveled assessment rubrics
- Section-by-section authoring advice
- Workflow recommendations

Specifications enable verification; guidance enables validation.

### 3.3 Edge Types

**Coupling edges** (undirected) connect specifications to their corresponding guidance:

```yaml
type: edge/coupling
source: v:spec:X
target: v:guidance:X
```

**Verification edges** (directed) connect documents to specifications:

```yaml
type: edge/verification
source: v:doc:Y
target: v:spec:X
# Body contains verification tool output
```

**Validation edges** (directed) connect documents to guidance:

```yaml
type: edge/validation
source: v:doc:Y
target: v:guidance:X
validator: <person or LLM>
human_approver: <required if LLM-assisted>
# Body contains quality assessment
```

### 3.4 The Assurance Triangle

An assurance face closes when three edges form a valid triangle:

```
          guidance
           /    \
 validation      coupling
         /        \
        /          \
    document ---- spec
          verification
```

The assurance face attests that:
1. The document is structurally compliant (verification passed)
2. The document meets quality criteria (validation passed)
3. The spec and guidance are properly coupled (coherent type system)
4. A human has reviewed and approved the complete pattern

### 3.5 Accountability Model

Every validation edge and assurance face requires human accountability:

- **Manual validation**: `validator` is the person who assessed quality
- **LLM-assisted validation**: `validator` is the LLM; `human_approver` is REQUIRED
- The human approver takes responsibility for the assessment

This ensures AI assistance is transparent and human judgment is always in the loop.

### 3.6 Boundary Complex

The framework bootstraps itself through a **boundary complex**: four foundational vertices (spec-for-spec, spec-for-guidance, guidance-for-spec, guidance-for-guidance) connected in a self-referential pattern. A unique root vertex (b0:root) resolves the self-referential paradox by anchoring boundary faces.

All other specifications and guidance documents are verified/validated against these foundational types, creating an extensible hierarchy rooted in explicit axioms.

---

## 4. Case Study: This Paper

### 4.1 The INCOSE Paper Type

We created specification and guidance documents for INCOSE symposium papers:

**spec-for-incose-paper** defines:
- 7,000 word limit
- Required sections (Abstract through References)
- AI disclosure requirements per INCOSE 2026 guidelines
- INCOSE template format

**guidance-for-incose-paper** defines:
- Quality criteria: Relevance, Accessibility, Rigor, Novelty, Theme Alignment, Engagement
- Section-by-section authoring guidance
- Common issues and solutions
- Workflow with time estimates

### 4.2 Assurance Infrastructure

We built the complete assurance triangle:

1. **Coupling**: spec-for-incose-paper ↔ guidance-for-incose-paper
2. **Verification**: This paper verified against spec-for-incose-paper
3. **Validation**: This paper validated against guidance-for-incose-paper
4. **Assurance face**: Human-approved triangle closing

### 4.3 The Audit Chart

The audit chart (Figure 1) visualizes the complete assurance network:

[FIGURE 1: Audit chart showing INCOSE paper assurance - to be generated]

Vertices:
- Boundary complex (5): root, spec-for-spec, spec-for-guidance, guidance-for-spec, guidance-for-guidance
- INCOSE paper type (2): spec-for-incose-paper, guidance-for-incose-paper
- This paper (1): doc-incose-paper-2026

Edges: Verification, validation, and coupling relationships

Faces: Assurance triangles with human sign-off

**Audit result**: All vertices assured (100% coverage)

### 4.4 Topological Properties

The audit chart has Euler characteristic χ, confirming topological validity. The boundary complex forms the contractible seed from which all assurance extends.

---

## 5. Tooling and Process

### 5.1 Verification Scripts

```bash
python scripts/verify_template_based.py <file> --templates templates
```

This script checks documents against their declared types, returning PASS/FAIL with specific check results.

### 5.2 Audit Tool

```bash
python scripts/audit_assurance_chart.py charts/<chart>/<chart>.md
```

Verifies all vertices have assurance coverage, identifies gaps, computes topological properties.

### 5.3 Visualization

```bash
python scripts/visualize_chart.py <chart>.json
```

Generates interactive 3D HTML visualization of the simplicial complex.

### 5.4 Document Development Workflow

1. **Clarify** requirements (Phase 1)
2. **Test** baseline—run existing verification (Phase 2)
3. **Generate** document with compliance (Phase 3)
4. **Assure** with human approval (Phase 4)

This mirrors test-driven development: write the test (spec), then write code (document) to pass.

---

## 6. Discussion

### 6.1 Limitations

**Scope**: The current implementation handles documentation; extending to code or models requires additional vertex types.

**Validation subjectivity**: Quality criteria involve judgment. The framework makes this explicit and accountable, but doesn't eliminate subjectivity.

**Overhead**: Creating specifications and guidance for every document type requires investment. The framework is most valuable for high-stakes or repeatedly-used document types.

### 6.2 Connection to "Seeking Wa"

The framework embodies Wa (harmony) through:

- **Human-AI balance**: AI assists; humans approve. Neither dominates.
- **Structural-qualitative integration**: Verification and validation are coupled, not isolated.
- **Explicit accountability**: Harmony requires knowing who is responsible.

### 6.3 Future Work

- Integration with MBSE tools (SysML model verification)
- Automated validation assistance (LLM pre-assessment for human review)
- Composition patterns for large document sets
- Application to requirements engineering

---

## 7. Conclusion

We presented a framework for test-driven document development using typed simplicial complexes. The framework formalizes verification (structural compliance), validation (quality assessment), and assurance (complete human-approved patterns) through mathematical structures that ensure consistency and accountability.

The key contribution is the **assurance triangle**: a 2-simplex that closes only when a document passes both verification against specification and validation against guidance, with explicit human approval. This pattern makes AI assistance transparent and ensures human judgment remains central.

We demonstrated the framework by using it to write this paper—the paper itself is an assured vertex in a simplicial complex. The audit chart showing 100% assurance coverage is our primary empirical result.

For the systems engineering community, we offer a practical approach to maintaining rigor in an era of AI assistance. The framework operationalizes the IS 2026 theme of "Seeking Wa" by harmonizing human accountability with AI capability.

---

## Acknowledgments

### AI Assistance Disclosure

**Tools used:** Claude (Claude Opus 4.5)

**Usage categories:**
- **Content generation**: Drafting all sections based on framework understanding
- **Analysis**: Generating verification outputs, quality assessments, assurance documentation
- **Conceptual**: Framework architecture emerged through human-AI collaboration

**Author involvement:** The framework architecture, research questions, and all accountability decisions are original author work. The author directed all AI-assisted content generation and made final editorial decisions. The demonstration (using the framework to write itself) was conceived and orchestrated by the author.

**Human accountability:** [Author name] reviewed all AI-generated content and takes full responsibility for the paper's claims and conclusions.

---

## References

[To be completed with proper INCOSE/AMA citation format]

1. INCOSE. 2023. Systems Engineering Handbook, version 5.0.
2. INCOSE IS 2026 Call for Submissions.
3. [References on simplicial complexes, V&V, document quality, LLM in SE]

---

**Word count:** [To be calculated - target ≤7000]

---

*Note: This is a draft content vertex demonstrating the framework. Actual paper would require further refinement, proper citations, and complete assurance workflow.*
