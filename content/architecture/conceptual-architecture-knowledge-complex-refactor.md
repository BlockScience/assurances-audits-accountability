---
type: vertex/doc
extends: doc
id: v:doc:conceptual-architecture-knowledge-complex-refactor
name: Conceptual Architecture - Knowledge Complex Framework Refactor
description: Stakeholder needs, acceptance criteria, and stakeholder-criterion matrix for the knowledge complex framework refactor
tags:
  - vertex
  - doc
  - conceptual-architecture
version: 0.2.0
created: 2026-01-11T00:00:00Z
modified: 2026-01-12T00:00:00Z
system_name: Knowledge Complex Framework
scope: Internal-first deployment enabling systematic documentation with verification, validation, and assurance for BlockScience client work
field_survey_ref: v:doc:field-survey-knowledge-complex-refactor
stakeholder_count: 4
criterion_count: 12
stakeholders:
  - A3
  - A4
  - A5
  - A6
---

# Conceptual Architecture - Knowledge Complex Framework Refactor

## Purpose

This conceptual architecture establishes who the primary stakeholders are for the knowledge complex framework refactor, what each stakeholder needs, and how acceptance will be evaluated. The document creates a stakeholder-criterion matrix that traces stakeholder needs to measurable acceptance criteria, forming the foundation for subsequent functional, logical, and physical architecture documents.

## Overview

The knowledge complex framework transforms how BlockScience manages knowledge-intensive work products. Built on typed simplicial complexes, the framework provides systematic verification, validation, and assurance of documents—but currently exists as a working prototype requiring significant expertise to use.

This conceptual architecture addresses the internal-first deployment: BlockScience using the framework for client engagements before external productization. The field survey identified six actors across three layers (Platform, Configuration, Execution). For this initial deployment, we focus on four stakeholders critical to internal adoption:

- **Operators (A3)** and **Approvers (A4)** as primary users in the Execution layer
- **Workflow Builders (A5)** who configure the system
- **Infrastructure Builders (A6)** who develop and maintain the platform

The key pain points driving this architecture are: documentation chaos (scattered, inconsistent documents), knowledge capture (institutional knowledge not systematized), and client deliverable quality (need to produce demonstrably assured work products). Success requires demonstrating both effectiveness (outcomes meet expectations) and compliance (processes were followed).

### Workflows and Runbooks

Throughout this architecture, we distinguish between **workflows** and **runbooks**:

- **Workflow**: The end user's conception of a work practice—how they think about the sequence of activities needed to produce a deliverable. Workflows are informal, understood through experience and institutional knowledge.

- **Runbook**: A formally defined, typed representation within the knowledge complex that documents a workflow and facilitates its compliant, effective execution. Runbooks are first-class objects in the system with defined structure: ordered modules (steps), typed inputs and outputs, chaining constraints between modules, and effectiveness metrics.

The framework transforms implicit workflows into explicit runbooks. When operators "follow a workflow," they are executing a runbook. When workflow builders "create workflows," they are authoring runbooks. This distinction matters because:

1. **Runbooks are verifiable**: The system can check that runbook structure is valid (modules chain correctly, I/O types match)
2. **Runbooks enable tracking**: Step-by-step execution can be monitored and measured
3. **Runbooks support assurance**: Each module's outputs can be verified and validated before proceeding
4. **Runbooks capture knowledge**: The runbook itself is a document that can be searched, reused, and improved

## Field Survey Reference

[[field-survey-knowledge-complex-refactor]]

### Stakeholders Used

| ID  | Name                    | Type         | Role in This Architecture                                                                                  |
| --- | ----------------------- | ------------ | ---------------------------------------------------------------------------------------------------------- |
| A3  | Operators               | Role         | Primary hands-on users who produce documents and follow workflows; success depends on their daily adoption |
| A4  | Approvers               | Role         | Domain experts who sign off on deliverables; must trust the system and efficiently review work             |
| A5  | Workflow Builders       | Role         | Configure document types, templates, and runbooks; enable operators and approvers to succeed               |
| A6  | Infrastructure Builders | Organization | BlockScience team developing the core framework; must deliver usable tooling                               |

**Stakeholder Selection Rationale:** For internal-first deployment, we focus on the actors directly involved in producing and approving work products (A3, A4) and those who enable them (A5, A6). Regulators (A1) and Compliance Officers (A2) are important for the full product vision but are not primary stakeholders for internal adoption. Their needs will be addressed in subsequent architecture iterations.

## Problem Statement (ConOps)

### Operational Context

BlockScience produces complex deliverables for clients: research reports, system designs, technical specifications, audit findings, and strategic recommendations. Team members work across time zones, often on multiple projects simultaneously. Deliverables must meet both internal quality standards and client expectations.

**Current state (problems):**
- Documents live in scattered locations (Google Drive, local folders, email)
- Documents do not have standard formats and associated quality criteria
- It is difficult to explain or demonstrate to a client what they will get as output from a contract
- Quality assurance depends on individual expertise and memory
- Prior work is hard to find; institutional knowledge walks out the door
- No systematic way to verify documents meet specifications
- Sign-off is informal; accountability unclear
- Demonstrating work quality to clients requires manual effort

**Desired state (with framework):**
- Documents live in version-controlled repositories with consistent structure
- Common document types are standardized and have measurable quality criteria
- It is possible to give clients example deliverables to help close contracts
- Quality assurance is systematic: verification against specs, validation against guidance
- Prior work is searchable and reusable through knowledge graph navigation
- Documents can be verified automatically against type specifications
- Sign-off creates an audit trail with clear accountability
- Work quality is demonstrable through assurance charts and audit reports

**Daily workflow:**
1. Operator receives task, finds relevant templates and prior work
2. Operator drafts document with LLM assistance, following runbook
3. Operator runs verification to check structural compliance with document type spec
4. Operator run evaluation to score alignment with guidance coupled with document type spec
5. Operator requests approval from appropriate Approver
6. Approver reviews document, document dependencies, document type guidance, and evaluation against that guidance.
7. Approver makes changes (or requests changes from operator) before signing validation edge attesting to quality
8. Assurance face is created, closing the quality loop
9. Output document may be used as input to the next stage in the runbook
10. When runbook is complete, work product is delivered with traceable dependencies and quality assurance.

### Stakeholder Needs

#### A3: Operator Needs

- **N3.1**: Find relevant templates and prior work quickly (not waste time searching)
- **N3.2**: Create documents that conform to specifications without understanding the underlying framework
- **N3.3**: Get immediate feedback when documents have structural problems
- **N3.4**: Receive guidance on what "good" looks like for each document type
- **N3.5**: Work with familiar tools (IDE, markdown, git) rather than learning new systems
- **N3.6**: Find and start the appropriate runbook for a given task
- **N3.7**: Know which step of a runbook they're on and what comes next
- **N3.8**: Understand what inputs are required for a runbook step and what outputs are expected

#### A4: Approver Needs

- **N4.1**: Know that documents are ready for review before they're submitted (verification passed)
- **N4.2**: Understand what they're attesting to when they sign off
- **N4.3**: Review documents efficiently without excessive context-switching
- **N4.4**: Trust that the verification infrastructure catches structural problems
- **N4.5**: See both compliance evidence (process followed) and effectiveness evidence (outcomes met expectations)
- **N4.6**: See runbook execution context when reviewing step outputs (what step, what runbook, what prior steps)

#### A5: Workflow Builder Needs

- **N5.1**: Configure document types and templates without deep mathematical expertise
- **N5.2**: Create runbooks that operators can follow consistently
- **N5.3**: Access reusable components (types, templates, runbooks) from a registry
- **N5.4**: Test workflows before deploying them to operators
- **N5.5**: Define effectiveness metrics that approvers can evaluate
- **N5.6**: Define runbook modules with typed inputs and outputs
- **N5.7**: Chain modules together with correct I/O type matching
- **N5.8**: Validate runbook structure before deployment (modules chain correctly, no orphans)

#### A6: Infrastructure Builder Needs

- **N6.1**: Maintain clean abstractions over the mathematical foundations
- **N6.2**: Use the framework to document the framework itself (self-demonstration)
- **N6.3**: Develop tooling that is testable and maintainable
- **N6.4**: Support multiple deployment contexts (internal, client, open-source)
- **N6.5**: Gather feedback from operators and approvers to improve the system

## Acceptance Criteria

| ID   | Criterion                       | Measurement                                              | Target                                                                         |
| ---- | ------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------ |
| AC1  | Document creation time          | Time from task receipt to draft completion               | <30 minutes for standard document types                                        |
| AC2  | Verification feedback speed     | Time from save to verification result                    | <3 seconds                                                                     |
| AC3  | Verification accuracy           | False positive/negative rate for structural errors       | <5% false negatives, <5% false positives                                       |
| AC4  | Search effectiveness            | Time to find relevant prior work                         | <5 minutes to find usable reference                                            |
| AC5  | Approval efficiency             | Time for approver to complete review                     | <15 minutes for standard documents                                             |
| AC6  | Approval confidence             | Approver-reported confidence in sign-off                 | >90% report "confident" or "very confident"                                    |
| AC7  | Effectiveness visibility        | Approvers can see effectiveness metrics                  | 100% of runbooks include performance criteria                                  |
| AC8  | Workflow builder productivity   | Time to create new Runbook, requiring new document types | <2 hours for new Runbook including new types with spec, guidance, and template |
| AC9  | Self-demonstration              | Framework documents pass own verification                | 100% of framework docs verified and assured                                    |
| AC10 | Evaluation usefulness           | Evaluation scores help identify quality gaps             | >90% of approvers report evaluation scores are useful for review               |
| AC11 | Client demonstration capability | Ability to show example deliverables during sales        | At least 3 document types have production-quality examples available           |
| AC12 | Runbook execution support       | System guides operators through runbook steps            | 100% of runbook executions show current step, next step, and I/O requirements  |

### Criterion Definitions

#### AC1: Document Creation Time

Operators should be able to produce a draft document quickly using templates, prior work references, and LLM assistance. The 30-minute target assumes standard document types (not novel research); complex documents may take longer but should benefit from reusable components.

#### AC2: Verification Feedback Speed

Verification must be fast enough to integrate into the editing workflow. If verification takes too long, operators will skip it or batch it at the end, losing the benefit of immediate feedback. The 3-second target enables verification on every save.

#### AC3: Verification Accuracy

Verification must be reliable. False negatives (missing real errors) erode trust in assured documents. False positives (flagging non-errors) create friction and cause operators to ignore warnings. Both error types are equally costly: missed errors undermine assurance while false alarms train operators to ignore the system.

#### AC4: Search Effectiveness

Finding prior work is critical for knowledge reuse and reducing rework. The 5-minute target assumes the operator knows roughly what they're looking for. Graph navigation, backlinks, and full-text search should combine to make discovery tractable.

#### AC5: Approval Efficiency

Approvers have limited time; review processes must be efficient. The 15-minute target assumes verification has already passed and the approver is reviewing quality, not catching structural errors. Documents requiring extensive revision should return to operators.

#### AC6: Approval Confidence

Approvers must feel confident in their sign-off. If approvers sign reluctantly or feel uncertain, the assurance system provides false comfort. The 90% target reflects the high bar required: nearly all approvers should feel confident, not just a majority. Self-reported confidence captures the subjective experience that objective metrics may miss.

#### AC7: Effectiveness Visibility

Demonstrating effectiveness (not just compliance) requires explicit metrics in runbooks. Every runbook should define what "effective" means for that workflow, enabling approvers to attest to outcomes, not just process adherence.

#### AC8: Workflow Builder Productivity

Workflow builders must be able to create new runbooks efficiently, including any new document types the runbook requires. A runbook defines an end-to-end workflow; creating one may require defining new document types (each with spec, guidance, and template). The 2-hour target for a complete new runbook assumes familiarity with the framework and access to reference examples. If runbook creation takes days, the system won't adapt to organizational needs.

#### AC9: Self-Demonstration

The framework should eat its own cooking. If framework documents don't pass verification or lack assurance, why should users trust the system for their documents? 100% compliance demonstrates both capability and commitment.

#### AC10: Evaluation Usefulness

Evaluation scores (step 4 in the workflow) provide a quantitative assessment of document alignment with guidance. These scores help approvers identify specific areas needing attention before sign-off. The 90% target reflects that evaluation must be genuinely useful, not just available—nearly all approvers should find the scores helpful for focusing their review. If evaluation scores are not useful, approvers must read guidance manually and assess quality from scratch—defeating the purpose of systematic quality assessment.

#### AC11: Client Demonstration Capability

Before signing contracts, clients often want to see what deliverables will look like. Having production-quality example documents (not templates, but actual completed work) demonstrates the framework's output quality and helps set client expectations. The target of 3 document types ensures coverage of common deliverable categories.

#### AC12: Runbook Execution Support

Runbooks define multi-step workflows. Operators need to know where they are in a runbook, what the current step requires as input, what output it should produce, and what comes next. The system should present this context clearly during execution. The 100% target reflects that this is essential—every runbook execution should provide this guidance, not just some. Without execution support, operators revert to reading runbook definitions manually, losing the benefit of systematic workflow guidance.

## Stakeholder-Criterion Matrix

### Matrix View

|    | AC1 | AC2 | AC3 | AC4 | AC5 | AC6 | AC7 | AC8 | AC9 | AC10 | AC11 | AC12 |
|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|------|
| A3 |  X  |  X  |  X  |  X  |     |     |     |     |     |  X   |      |  X   |
| A4 |     |     |  X  |     |  X  |  X  |  X  |     |     |  X   |      |  X   |
| A5 |  X  |  X  |  X  |     |     |     |  X  |  X  |     |  X   |  X   |  X   |
| A6 |     |  X  |  X  |  X  |     |     |     |  X  |  X  |  X   |  X   |  X   |

### Relationship Details

| Stakeholder | Criterion | Role | Rationale |
|-------------|-----------|------|-----------|
| A3 | AC1 | Primary Beneficiary | Fast document creation directly benefits operator productivity |
| A3 | AC2 | Primary User | Operators experience verification feedback during editing |
| A3 | AC3 | Affected Party | Unreliable verification wastes operator time on false positives or missed errors |
| A3 | AC4 | Primary Beneficiary | Operators need to find prior work to avoid reinventing solutions |
| A4 | AC3 | Affected Party | Approvers depend on verification accuracy to trust pre-review checks |
| A4 | AC5 | Primary Beneficiary | Efficient review directly benefits approver productivity |
| A4 | AC6 | Primary User | Approvers experience confidence (or lack thereof) during sign-off |
| A4 | AC7 | Primary Beneficiary | Effectiveness visibility enables approvers to attest to outcomes |
| A5 | AC1 | Accountable | Workflow builders create templates and runbooks that determine creation time |
| A5 | AC2 | Accountable | Workflow builders configure verification that determines feedback speed |
| A5 | AC3 | Accountable | Workflow builders define specs that determine verification accuracy |
| A5 | AC7 | Accountable | Workflow builders define effectiveness metrics in runbooks |
| A5 | AC8 | Primary Beneficiary | Workflow builder productivity directly benefits from efficient type creation |
| A6 | AC2 | Accountable | Infrastructure builders implement verification engine performance |
| A6 | AC3 | Accountable | Infrastructure builders implement verification algorithm accuracy |
| A6 | AC4 | Accountable | Infrastructure builders implement search and navigation features |
| A6 | AC8 | Accountable | Infrastructure builders provide APIs and tools for type creation |
| A6 | AC9 | Accountable | Infrastructure builders responsible for framework self-demonstration |
| A3 | AC10 | Primary User | Operators run evaluation and see scores before requesting approval |
| A4 | AC10 | Primary Beneficiary | Evaluation scores help approvers focus review on areas needing attention |
| A5 | AC10 | Accountable | Workflow builders define guidance criteria that evaluation scores against |
| A6 | AC10 | Accountable | Infrastructure builders implement evaluation scoring engine |
| A5 | AC11 | Accountable | Workflow builders create and maintain example deliverables |
| A6 | AC11 | Accountable | Infrastructure builders ensure framework supports example document workflows |
| A3 | AC12 | Primary Beneficiary | Operators benefit from clear step-by-step guidance during runbook execution |
| A4 | AC12 | Primary Beneficiary | Approvers benefit from seeing execution context when reviewing step outputs |
| A5 | AC12 | Accountable | Workflow builders define runbooks that execution support presents |
| A6 | AC12 | Accountable | Infrastructure builders implement runbook execution presentation |

### Key Dependencies

1. **Operator productivity depends on Workflow Builder configuration (A3 → A5 → AC1, AC2)**: Operators experience the system through templates and runbooks that Workflow Builders create. If Workflow Builders can't efficiently create good templates (AC8), operator creation time (AC1) suffers.

2. **Approver confidence depends on verification accuracy (A4 → AC3 → AC6)**: Approvers trust verification to catch structural errors before review. If verification accuracy (AC3) is poor, approvers can't be confident (AC6) in their sign-off because they must second-guess the verification.

3. **Effectiveness demonstration depends on runbook design (A4 → A5 → AC7)**: Approvers need to see effectiveness metrics (AC7) to attest to outcomes. These metrics come from runbooks designed by Workflow Builders. If runbooks lack metrics, approvers can only attest to compliance, not effectiveness.

4. **Self-demonstration validates the entire system (A6 → AC9)**: If the framework's own documents don't pass verification (AC9), no other acceptance criterion matters—the system lacks credibility. Self-demonstration is a forcing function for quality.

5. **Search effectiveness enables knowledge reuse (A3 → AC4)**: Finding prior work (AC4) is the foundation for knowledge capture. If search is ineffective, operators reinvent solutions, institutional knowledge remains trapped, and one of the core pain points remains unaddressed.

6. **Evaluation scores bridge verification and approval (A3 → AC10 → A4)**: Operators run evaluation (step 4 in workflow) to score alignment with guidance before requesting approval. Approvers use these scores to focus their review. If evaluation is not useful (AC10), the workflow reverts to manual quality assessment.

7. **Client demonstration depends on production-quality examples (A5 → AC11)**: Closing contracts often requires showing clients what they'll get. Workflow Builders must create and maintain example deliverables that showcase framework outputs. This also serves as a forcing function for quality—examples must be excellent.

8. **Runbook execution requires well-defined modules (A3 → A5 → AC12)**: Operators can only receive step-by-step guidance (AC12) if Workflow Builders have defined runbooks with proper module structure, typed I/O, and sequencing. Poorly structured runbooks produce confusing execution guidance.

## Acceptance Testing Strategy

### Test Approach by Criterion

| Criterion | Test Type | Test Method | Success Indicator |
|-----------|-----------|-------------|-------------------|
| AC1 | Performance | Timed task completion with sample operators | 80% of trials complete in <30 minutes |
| AC2 | Performance | Automated timing of verification runs | 95th percentile <3 seconds |
| AC3 | Accuracy | Test suite with known-good and known-bad documents | False negative rate <5%, false positive rate <5% |
| AC4 | Usability | Timed search tasks with sample operators | 80% of trials find usable reference in <5 minutes |
| AC5 | Performance | Timed review tasks with sample approvers | 80% of standard reviews complete in <15 minutes |
| AC6 | Survey | Post-sign-off confidence survey | >90% report "confident" or "very confident" |
| AC7 | Inspection | Audit of runbooks for performance criteria | 100% of runbooks include explicit metrics |
| AC8 | Performance | Timed runbook creation tasks with workflow builders | 80% of trials complete new runbook (with types) in <2 hours |
| AC9 | Verification | Run verification on all framework documents | 100% pass; all have assurance faces |
| AC10 | Survey | Post-review survey of approvers about evaluation usefulness | >90% report scores are useful for focusing review |
| AC11 | Inspection | Audit of document type registry for production examples | At least 3 document types have complete, assured examples |
| AC12 | Functional | Execute runbooks, verify step/context presentation | 100% of executions show current step, next step, and I/O requirements |

## Constraints and Assumptions

### Constraints

- **C1**: Documents must remain human-readable markdown with YAML frontmatter (no binary formats)
- **C2**: Git must remain the source of truth for version control
- **C3**: Human approval is required for all validation and assurance (no fully automated trust)
- **C4**: Internal deployment must not disrupt ongoing client work
- **C5**: Initial deployment limited to BlockScience team (not external users yet)

### Assumptions

- **A1**: Team members have basic familiarity with markdown and git
- **A2**: VS Code is available and acceptable as primary IDE
- **A3**: Claude Code is available for LLM integration
- **A4**: Obsidian is acceptable for knowledge exploration
- **A5**: Team is willing to invest time in learning new workflows

## Risks and Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Learning curve deters adoption | High | Medium | Start with simple document types; provide hands-on training; pair new users with experienced ones |
| Verification too slow for workflow | Medium | Low | Profile and optimize verification engine; cache results; implement incremental verification |
| Operators bypass verification | High | Medium | Make verification automatic and non-blocking; surface results prominently; tie to approval workflow |
| Approvers rubber-stamp without reviewing | High | Medium | Require explicit attestation; track approval patterns; review effectiveness metrics |
| Runbooks lack effectiveness metrics | Medium | High | Provide templates with metric placeholders; review runbooks before deployment |

## Traceability to Field Survey

### From Actors to Stakeholder Needs

| Field Survey Actor | Conceptual Architecture Stakeholder Needs |
|--------------------|-------------------------------------------|
| A3: Operators | N3.1-N3.5 (find work, create documents, get feedback, receive guidance, use familiar tools) |
| A4: Approvers | N4.1-N4.5 (readiness, understanding, efficiency, trust, effectiveness visibility) |
| A5: Workflow Builders | N5.1-N5.5 (configure types, create runbooks, access registry, test workflows, define metrics) |
| A6: Infrastructure Builders | N6.1-N6.5 (abstractions, self-demo, maintainability, contexts, feedback) |

### Key Findings Addressed

- **Documentation chaos (from Field Survey)**: Addressed by AC1 (fast creation), AC4 (search effectiveness), and the overall framework structure
- **Knowledge capture (from Field Survey)**: Addressed by AC4 (search), AC9 (self-demonstration as example)
- **Client deliverable quality (from Field Survey)**: Addressed by AC3 (verification accuracy), AC6 (approval confidence), AC7 (effectiveness visibility), AC11 (client demonstration capability)
- **Effectiveness vs. compliance (from Field Survey)**: Addressed by AC7 (effectiveness visibility in runbooks), AC10 (evaluation usefulness)
- **Standard formats and quality criteria (from ConOps)**: Addressed by AC3 (verification accuracy), AC10 (evaluation usefulness)
- **Client demonstration during sales (from ConOps)**: Addressed by AC11 (client demonstration capability)

---

**Note:** This conceptual architecture is the first of four extended architecture documents. It establishes the stakeholder needs and acceptance criteria that flow into the functional architecture (what the system does), logical architecture (technology-agnostic components), and physical architecture (specific implementation choices).
