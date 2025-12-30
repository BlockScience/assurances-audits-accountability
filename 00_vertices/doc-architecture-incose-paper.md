---
type: vertex/doc
extends: doc
id: v:doc:architecture-incose-paper
name: Architecture Document - INCOSE Paper Assurance Framework
description: 4-layer SE architecture for the document assurance framework demonstrated in the INCOSE IS 2026 paper
tags:
  - vertex
  - doc
  - architecture
version: 1.0.0
created: 2025-12-30T12:00:00Z
modified: 2025-12-30T12:00:00Z
system_name: Document Assurance Framework
scope: A framework for verifying, validating, and assuring LLM-assisted documents using typed simplicial complexes with human accountability
stakeholders:
  - Cognizant Engineers
  - Technical Authorities
  - Document Authors
  - Quality Assurance Personnel
  - Systems Engineers
dependencies: []
---

# Architecture Document - INCOSE Paper Assurance Framework

**This architecture document describes the Document Assurance Framework using the four-layer SE framework (Conceptual, Functional, Logical, Physical) aligned with the INCOSE SE Handbook and V-model lifecycle.**

## Overview

The Document Assurance Framework addresses a critical gap in LLM-augmented systems engineering: how to maintain human accountability and quality assurance for machine-generated documents. As AI tools increasingly assist with documentation tasks, cognizant engineers and other authorities need mechanisms to verify structural compliance, validate fitness-for-purpose, and trace accountability to named humans.

This architecture document describes the framework at four abstraction levels, each mapping to a corresponding evaluation level in the V-model. The framework is self-demonstrating: it was used to develop itself, and this very document is an instance of what it describes.

## V-Model Summary

| Layer | Left Side (Idealized) | ← Evaluation → | Right Side (Realized) |
|-------|----------------------|----------------|----------------------|
| **Conceptual** | ConOps: Stakeholder need for requirements traceability and human accountability for machine-generated documents | Paper submitted for review | Acceptance Testing: Paper accepted at INCOSE IS 2026 = stakeholder acceptance |
| **Functional** | Functional Architecture: Automated verification, validation assistance, accountability preservation | Paper passes author's final checks | System Testing: Complete assurance audit passes with 100% coverage |
| **Logical** | Logical Architecture: Coupling edges, assurance triangles, typed document system | Documents being produced and assured | Integration Testing: Assurance faces close properly, cross-references resolve |
| **Physical** | Physical Architecture: Python scripts, Claude Code, git repository, GitHub Actions | Software implementations tested | Unit Testing: Individual scripts pass pytest, templates verify correctly |

## Conceptual Layer

### Problem Statement (ConOps)

Cognizant engineers and other technical authorities face a growing challenge: AI systems can draft documents rapidly, but cannot bear responsibility for their fitness-for-purpose. This creates an accountability gap where documents may be produced efficiently but without the human judgment necessary for engineering decisions.

**Stakeholder Needs:**

1. **Requirements Traceability**: Engineers need to trace document requirements through verification and validation to understand what standards a document claims to meet
2. **Human Accountability**: Authorities need named human approvers for qualitative assessments, not diffused responsibility to "the AI"
3. **Automated Verification**: Teams need deterministic structural checks that can run without human intervention
4. **Quality Assessment**: Organizations need systematic approaches to evaluate fitness-for-purpose beyond structural compliance
5. **Audit Trail**: Compliance officers need traceable records of who approved what, when, and on what basis

**Operational Context:**

The framework operates in engineering environments where:
- Documents are authored collaboratively between humans and LLMs
- Structural compliance can be checked automatically
- Quality assessment requires human judgment
- Accountability must trace to named individuals
- Document relationships form complex networks

### Acceptance Criteria

The framework is accepted when:

1. **Self-Demonstration**: The INCOSE paper itself is produced using the framework, with complete assurance infrastructure
2. **Community Acceptance**: Paper accepted at INCOSE IS 2026, indicating SE community finds the approach valuable
3. **Stakeholder Validation**: Named human (mzargham) attests to fitness-for-purpose of all assured documents
4. **Traceability**: All document assurance edges trace to boundary complex root, demonstrating closed system
5. **Coverage**: Assurance audit shows 100% vertex coverage with no unassured documents

## Functional Layer

### Functional Architecture

The system performs three primary functions and several supporting functions:

| Function | Inputs | Outputs | Description |
|----------|--------|---------|-------------|
| **F1: Verify Document** | Document, Specification | Pass/Fail + Details | Check document structure against spec requirements |
| **F2: Validate Document** | Document, Guidance, Human Judgment | Quality Assessment | Evaluate document fitness-for-purpose against criteria |
| **F3: Assure Document** | Verification Result, Validation Result, Coupling | Assurance Attestation | Combine edges into assurance triangle with accountability |
| **F4: Couple Spec-Guidance** | Specification, Guidance | Coupling Edge | Link spec and guidance for same document type |
| **F5: Audit Assurance** | Chart of Documents | Audit Report | Analyze completeness and topology of assurance network |
| **F6: Trace to Root** | Any Document | Path to Root | Verify document connects to boundary complex foundation |

### System Testing Criteria

The functional architecture is validated when:

1. **Verification Function**: Script processes document and returns deterministic pass/fail with specific check results
2. **Validation Function**: Assessment includes quality levels for each criterion with human approver signature
3. **Assurance Function**: Face document correctly references all three bounding edges with coherence assessment
4. **Coupling Function**: Edge correctly links paired spec and guidance with appropriate types
5. **Audit Function**: Report shows vertex count, edge count, face count, coverage percentage, and Euler characteristic
6. **Trace Function**: Every vertex in chart has valid path to boundary complex root

## Logical Layer

### Logical Architecture

The design-independent component structure uses typed simplicial complexes:

| Component | Responsibility | Interfaces |
|-----------|---------------|------------|
| **Document Store** | Persist and retrieve typed documents | Create, Read, Update, Query by type/id |
| **Type System** | Enforce document type constraints | Validate type, Check inheritance, Resolve extends |
| **Verification Service** | Execute structural checks | Input: (document, spec), Output: verification result |
| **Validation Service** | Coordinate quality assessment | Input: (document, guidance, human), Output: validation result |
| **Assurance Service** | Combine edges into faces | Input: (verification, validation, coupling), Output: assurance face |
| **Topology Analyzer** | Compute simplicial complex properties | Input: chart, Output: Euler characteristic, boundary analysis |
| **Accountability Tracker** | Record human approvals | Input: (document, human, action), Output: accountability record |

### Component Interactions

```
Document Store ←→ Type System (type validation on all operations)
        ↓
Verification Service ←→ Type System (load specs by type)
        ↓
Validation Service ←→ Accountability Tracker (require human for validation)
        ↓
Assurance Service ←→ Verification + Validation + Coupling (triangle assembly)
        ↓
Topology Analyzer ←→ Document Store (load charts and compute properties)
```

### Integration Testing Criteria

Component integration is verified when:

1. **Type Resolution**: Document Store correctly resolves `extends` chains through Type System
2. **Verification Pipeline**: Verification Service loads spec from Document Store via Type System
3. **Validation Pipeline**: Validation Service records approver via Accountability Tracker
4. **Assurance Assembly**: Assurance Service correctly identifies all three bounding edges
5. **Topological Analysis**: Topology Analyzer computes correct Euler characteristic (χ = V - E + F)
6. **Cross-Reference Integrity**: All document references resolve to existing documents

## Physical Layer

### Physical Architecture

Specific implementation choices for each logical component:

| Element | Technology/Tool | Purpose |
|---------|----------------|---------|
| **Document Store** | Markdown files with YAML frontmatter in git repository | Version-controlled, human-readable persistence |
| **Type System** | Python scripts parsing YAML frontmatter | Type validation and inheritance resolution |
| **Verification Service** | `verify_template_based.py` Python script | Structural compliance checking |
| **Validation Service** | Claude Code (claude-opus-4-5) with human review | LLM-assisted quality assessment with human accountability |
| **Assurance Service** | Manual document creation following templates | Face assembly with accountability statements |
| **Topology Analyzer** | `topology.py` and `audit_assurance_chart.py` Python scripts | Euler characteristic and coverage analysis |
| **Accountability Tracker** | Git commit history + `human_approver` frontmatter field | Immutable record of who approved what |
| **CI Enforcement** | GitHub Actions workflows | Automated verification on commit, approver validation |
| **Authoring Environment** | VS Code for editing, Obsidian for wiki-style navigation | Developer experience for document authors |
| **LLM Integration** | Claude Code CLI with PPP framework | AI assistance with systematic workflow |

### Technology Rationale

- **Markdown + YAML**: Human-readable, version-controllable, widely supported
- **Python**: Accessible scripting language with good YAML/markdown libraries
- **Git**: Industry-standard version control with immutable history
- **GitHub Actions**: Free CI/CD with excellent git integration
- **Claude Code**: State-of-the-art LLM with tool use for systematic workflows
- **Obsidian**: Excellent for wiki-style linked document navigation

### Unit Testing Criteria

Individual components are verified when:

1. **verify_template_based.py**: Correctly identifies missing required fields, returns structured pass/fail
2. **topology.py**: Computes correct χ for known test charts (e.g., tetrahedron χ=2)
3. **audit_assurance_chart.py**: Correctly identifies unassured vertices and coverage percentage
4. **Type parsing**: Correctly extracts frontmatter and resolves type inheritance
5. **GitHub Actions**: Workflow runs on push, fails on verification errors
6. **Template generation**: Generated documents pass verification against their specs

## Traceability Matrix

| Conceptual Need | Functional Requirement | Logical Component | Physical Element |
|-----------------|----------------------|-------------------|------------------|
| Requirements Traceability | F1: Verify Document | Verification Service | verify_template_based.py |
| Human Accountability | F2: Validate Document | Validation Service + Accountability Tracker | human_approver field + git history |
| Automated Verification | F1: Verify Document | Verification Service + Type System | Python scripts + YAML parsing |
| Quality Assessment | F2: Validate Document | Validation Service | Claude Code + human review |
| Audit Trail | F5: Audit Assurance | Topology Analyzer | audit_assurance_chart.py + git log |

## Constraints and Assumptions

### Constraints

1. **Double-Blind Review**: Implementation details cannot be linked in INCOSE submission; described without repository URLs
2. **Human Availability**: Validation requires human judgment; cannot be fully automated
3. **Git-Based**: Assumes git for version control and accountability tracking
4. **Markdown Format**: Documents must be markdown with YAML frontmatter
5. **Single Approver**: Current implementation supports one human_approver per validation; future versions may support multiple

### Assumptions

1. **LLM Capability**: Claude Code can reliably follow PPP protocols for consistent document generation
2. **Structural Sufficiency**: Specification compliance implies document structure is adequate for purpose
3. **Human Competence**: Named approvers have sufficient expertise to assess fitness-for-purpose
4. **Repository Integrity**: Git history is not tampered with post-commit
5. **Network Connectivity**: Assurance network is connected (all vertices trace to root)

## Risks and Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| LLM generates incorrect assessments | Medium | Medium | Human approver reviews all validation assessments |
| Verification script has bugs | High | Low | Unit tests for scripts; manual inspection for critical documents |
| Human approver unavailable | High | Low | Single approver (mzargham) with high availability for this project |
| Type system too rigid | Medium | Medium | Iterative spec refinement based on usage experience |
| Assurance overhead too high | Medium | Medium | Templates and LLM assistance reduce manual effort |
| Topological analysis incorrect | Low | Low | Known test cases verify Euler characteristic computation |

---

**Note:** This architecture document follows the INCOSE SE Handbook patterns for architecture description and aligns with the V-model lifecycle for verification and validation. It is verified against [[spec-for-architecture]] and validated against [[guidance-for-architecture]].
