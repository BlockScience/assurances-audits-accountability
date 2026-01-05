---
type: vertex/guidance
extends: doc
id: v:guidance:lifecycle
name: Guidance for Lifecycle Documents
description: Quality criteria and best practices for creating excellent engineering lifecycle documentation aligned with the V-model
tags:
  - vertex
  - doc
  - guidance
version: 2.0.0
created: 2025-12-30T18:00:00Z
modified: 2025-01-04T20:00:00Z
criteria:
  - v-model-alignment
  - architecture-traceability
  - phase-completeness
  - operations-coverage
  - decommissioning-readiness
  - gate-rigor
dependencies:
  - v:guidance:architecture
---

# Guidance for Lifecycle Documents

**This guidance defines quality criteria and best practices for creating excellent engineering lifecycle documents that transform architectures into operational systems through the V-model.**

## Purpose

While spec-for-lifecycle defines what structural elements must be present, this guidance helps authors assess **how well** a lifecycle document serves its purpose. Great lifecycle documents clearly stage the engineering process from architecture through operations, maintain traceability across all phases, and provide actionable guidance for delivering systems that stakeholders will accept.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating lifecycle documents by providing:

- Quality assessment criteria for V-model aligned engineering processes
- Best practices for design-to-evaluation traceability
- Common pitfalls in lifecycle documentation
- Section-by-section authoring recommendations
- Workflow for creating lifecycle documents

### Best Use Cases

Use this guidance when:

- Creating a lifecycle for a new system architecture
- Reviewing existing lifecycle documentation for V-model alignment
- Ensuring operations and decommissioning are adequately addressed
- Evaluating whether a lifecycle can successfully deliver an operational system

## Quality Criteria

### 1. V-Model Alignment

**Definition:** How well does the lifecycle reflect the V-model's design-evaluation symmetry?

| Level | Indicators |
|-------|------------|
| **Excellent** | Clear mapping between each design phase and its evaluation counterpart; Unit↔Physical, Integration↔Logical, System↔Functional, Acceptance↔Conceptual explicitly documented; V-model diagram shows symmetric structure |
| **Good** | Design and evaluation phases present; mapping implied but not always explicit; V-model structure recognizable |
| **Needs Improvement** | Design phases listed without evaluation counterparts; no V-model visualization; testing phases disconnected from design |

### 2. Architecture Traceability

**Definition:** How well does the lifecycle trace to and implement its referenced architecture?

| Level | Indicators |
|-------|------------|
| **Excellent** | Architecture explicitly referenced in frontmatter and introduction; all four layers summarized with evaluation mapping; key requirements identified and traced through phases; traceability matrix complete |
| **Good** | Architecture referenced; most layers addressed; some traceability gaps |
| **Needs Improvement** | Architecture mentioned vaguely; layers not systematically addressed; traceability unclear or missing |

### 3. Phase Completeness

**Definition:** Does each phase have all required elements with sufficient detail?

| Level | Indicators |
|-------|------------|
| **Excellent** | Every phase has Goal, Inputs, Process, Outputs, and Gate; process steps are numbered and actionable; gates have explicit pass/fail criteria; failure paths documented |
| **Good** | Most phases complete; some gaps in process detail or gate criteria |
| **Needs Improvement** | Phases missing components; vague goals; no gate criteria; only happy path documented |

### 4. Operations Coverage

**Definition:** How thoroughly does the lifecycle address post-acceptance operations?

| Level | Indicators |
|-------|------------|
| **Excellent** | Deployment process detailed; monitoring metrics with targets and thresholds; all four maintenance types addressed (corrective, adaptive, perfective, preventive); change management process defined |
| **Good** | Operations addressed; monitoring mentioned; maintenance types partially covered |
| **Needs Improvement** | Operations superficial or missing; no monitoring metrics; maintenance not addressed |

### 5. Decommissioning Readiness

**Definition:** Does the lifecycle address end-of-life considerations?

| Level | Indicators |
|-------|------------|
| **Excellent** | Multiple decommissioning triggers identified; process steps cover stakeholder notification, data preservation, service transition, resource cleanup, documentation archival; post-decommissioning state defined |
| **Good** | Decommissioning triggers listed; basic process documented |
| **Needs Improvement** | Decommissioning absent or perfunctory; no triggers; no preservation considerations |

### 6. Gate Rigor

**Definition:** Are verification and validation gates well-defined and actionable?

| Level | Indicators |
|-------|------------|
| **Excellent** | Clear distinction between verification (automated) and validation (human); explicit pass/fail criteria for every gate; acceptance testing requires named stakeholder sign-off; failure paths lead to specific remediation |
| **Good** | Gates present with criteria; verification/validation mostly distinguished |
| **Needs Improvement** | Gates vague ("ensure quality"); verification/validation conflated; no failure handling |

## Section-by-Section Guidance

### Introduction

**Purpose:** Orient reader to the system and V-model context

**Tips:**

- Reference the architecture document in the first paragraph
- State what system this lifecycle delivers
- Explain the V-model alignment explicitly
- Identify stakeholders who will perform acceptance

**Anti-patterns:**

- ❌ Generic introduction not tied to specific architecture
- ❌ No mention of V-model or engineering process
- ❌ Stakeholders unnamed or vague

**Preferred:**

- ✅ "This lifecycle implements [[architecture-xyz]] to deliver the ABC system"
- ✅ "Following the V-model, design phases on the left produce artifacts validated by testing phases on the right"

### Architecture Foundation

**Purpose:** Establish the architecture this lifecycle implements

**Tips:**

- Use the 4-layer summary table format
- Map each layer to its evaluation counterpart
- Extract key requirements that drive the lifecycle
- Reference actual architecture sections

**Anti-patterns:**

- ❌ Summarizing architecture without layer structure
- ❌ Missing the layer-to-evaluation mapping
- ❌ Vague requirements ("meet user needs")

**Preferred:**

- ✅ Four-row table with Conceptual/Functional/Logical/Physical
- ✅ Each row shows layer description AND evaluation phase
- ✅ Key requirements are specific and traceable

### V-Model Overview

**Purpose:** Visualize the complete lifecycle structure

**Tips:**

- Use Mermaid flowchart with subgraphs for Design, Implementation, Evaluation, Operations
- Show the flow from ConOps through Decommissioning
- Color-code phases by type (design, implementation, evaluation, operations)
- Keep readable—not too many nodes

**Anti-patterns:**

- ❌ Linear flowchart without V-model structure
- ❌ Missing operations/decommissioning phases
- ❌ No visual distinction between phase types

**Preferred:**

- ✅ Four subgraphs: Design (left), Implementation (bottom), Evaluation (right), Operations (post-acceptance)
- ✅ Color coding: design phases, implementation, evaluation phases, operations phases

### Design Phases

**Purpose:** Define the left side of the V (requirements → design)

**Tips:**

- Three phases: ConOps→Functional, Functional→Logical, Logical→Physical
- Each phase transforms one architecture layer to the next
- Maintain traceability artifacts (function-to-need, component-to-function, etc.)
- Verification gates check design completeness

**Anti-patterns:**

- ❌ Combining multiple transitions in one phase
- ❌ No traceability artifacts
- ❌ Skipping directly from ConOps to Physical

**Preferred:**

- ✅ Each phase has explicit transformation goal
- ✅ Outputs include traceability artifacts
- ✅ Gates verify layer completeness before proceeding

### Implementation Phase

**Purpose:** Define the transition from design to realized system

**Tips:**

- Takes physical architecture as input
- Produces implemented components ready for testing
- Include implementation standards and practices
- Verification gate ensures implementation matches specs

**Anti-patterns:**

- ❌ Vague implementation ("build the system")
- ❌ No verification of implementation correctness

**Preferred:**

- ✅ Specific implementation activities
- ✅ Clear criteria for implementation completeness

### Evaluation Phases

**Purpose:** Define the right side of the V (testing → acceptance)

**Tips:**

- Four phases: Unit, Integration, System, Acceptance
- Each phase validates against its corresponding architecture layer
- Unit→Physical, Integration→Logical, System→Functional, Acceptance→Conceptual
- Acceptance requires stakeholder sign-off (human validation)

**Anti-patterns:**

- ❌ Testing phases not mapped to architecture layers
- ❌ Acceptance testing without stakeholder involvement
- ❌ No distinction between verification and validation

**Preferred:**

- ✅ Each test phase explicitly references its architecture layer
- ✅ Acceptance includes "Stakeholder sign-off" as output
- ✅ Acceptance gate is a Validation Gate (human), others are Verification Gates

### Operations Phase

**Purpose:** Define post-acceptance system operations

**Tips:**

- Deployment: specific steps to go live
- Monitoring: metrics, targets, thresholds, alert handling
- Maintenance: all four types with triggers and processes
- Change management: how changes flow back through V-model

**Anti-patterns:**

- ❌ "Deploy to production" without details
- ❌ Monitoring without metrics
- ❌ Only corrective maintenance addressed

**Preferred:**

- ✅ Deployment checklist or process
- ✅ Monitoring table with specific metrics and thresholds
- ✅ Four maintenance types: corrective, adaptive, perfective, preventive
- ✅ Change management references V-model phases

### Decommissioning

**Purpose:** Define when and how the system ends

**Tips:**

- Multiple triggers (technology obsolescence, business change, replacement system, etc.)
- Process covers all aspects: notification, data, transition, cleanup, archive
- Post-decommissioning state is clear

**Anti-patterns:**

- ❌ Single trigger ("when no longer needed")
- ❌ No data preservation consideration
- ❌ Missing stakeholder communication

**Preferred:**

- ✅ 3-5 specific decommissioning triggers
- ✅ 5-step process covering all aspects
- ✅ Clear post-decommissioning documentation location

### Traceability Matrix

**Purpose:** Summarize lifecycle-to-architecture mapping with concrete artifacts

**Tips:**

- Four rows: Conceptual, Functional, Logical, Physical
- Columns: Design Phase, Implementation Artifact, Evaluation Phase
- Implementation column shows the concrete artifact produced at each layer
- Shows complete coverage of architecture with traceable deliverables

**Anti-patterns:**

- ❌ Incomplete matrix with empty cells
- ❌ Missing implementation column or using "-" placeholders
- ❌ Generic descriptions instead of concrete artifacts

**Preferred:**

- ✅ Every architecture layer mapped to design, implementation artifact, and evaluation
- ✅ Implementation artifacts show refinement progression:
  - Conceptual → Stakeholder Requirements Document
  - Functional → System-Level Functional Requirements
  - Logical → Component-level Specifications
  - Physical → Implementation (code, hardware, etc.)
- ✅ Clear traceability from stakeholder needs through to unit-tested implementation

## Workflow Guidance

### Recommended Authoring Sequence

1. **Review Architecture** (30-45 min)
   - Read the referenced architecture document
   - Identify the four layers and key requirements
   - Note stakeholders for acceptance

2. **Draft V-Model Overview** (30 min)
   - Create the Mermaid diagram first
   - Establish the phase structure
   - Validate completeness (design, implementation, evaluation, operations, decommissioning)

3. **Write Architecture Foundation** (20-30 min)
   - Summarize each layer
   - Map to evaluation phases
   - Extract key requirements

4. **Define Design Phases** (45-60 min)
   - Three phases with full structure
   - Include traceability outputs
   - Define verification gates

5. **Define Implementation Phase** (20-30 min)
   - Implementation process
   - Verification gate

6. **Define Evaluation Phases** (45-60 min)
   - Four phases with full structure
   - Map each to architecture layer
   - Acceptance testing includes stakeholder sign-off

7. **Define Operations Phase** (30-45 min)
   - Deployment process
   - Monitoring metrics
   - Four maintenance types
   - Change management

8. **Define Decommissioning** (20-30 min)
   - Triggers
   - Process
   - Post-decommissioning state

9. **Complete Traceability Matrix** (15 min)
   - Verify complete coverage

10. **Review for Quality** (30 min)
    - Check against this guidance's criteria
    - Verify V-model diagram matches content

**Total estimated time:** 5-7 hours for a comprehensive lifecycle document

### Quality Checkpoints

- **After step 2:** Does the V-model diagram show symmetric design-evaluation structure?
- **After step 4:** Are all three design transitions covered with traceability?
- **After step 6:** Does each evaluation phase map to its architecture layer?
- **After step 7:** Are all four maintenance types addressed?
- **After step 9:** Is the traceability matrix complete?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Missing V-model structure** | Lifecycle is linear without design-evaluation mapping | Restructure with explicit left side (design) and right side (evaluation) phases |
| **Disconnected testing** | Test phases don't reference architecture layers | Add explicit "validates against [layer]" to each test phase |
| **No operations content** | Lifecycle ends at acceptance | Add Operations section with deployment, monitoring, maintenance |
| **Perfunctory decommissioning** | "Decommission when obsolete" | Expand with specific triggers, process steps, data considerations |
| **Vague gates** | "Verify the design" | Specify criteria: "All functions trace to needs; coverage ≥95%" |
| **Missing stakeholder sign-off** | Acceptance without human approval | Add "Stakeholder sign-off" as required output with named approver |
| **No traceability artifacts** | Phases don't produce traceability | Add outputs like "function-to-need traceability matrix" |
| **Architecture not referenced** | Lifecycle floats without foundation | Add architecture_ref to frontmatter; summarize in Architecture Foundation |

## Best Practices

1. **Start with the Architecture** - Read and understand the architecture before designing the lifecycle
2. **Visualize First** - Create the V-model diagram early to establish structure
3. **Trace Everything** - Every evaluation phase should reference its corresponding design phase
4. **Name Your Stakeholders** - Acceptance testing requires named human approvers
5. **Think Beyond Acceptance** - Operations and decommissioning are part of the lifecycle
6. **Define Metrics** - Monitoring needs specific metrics, not just "monitor the system"
7. **Plan for Change** - Change management should reference how changes flow through V-model
8. **Consider End-of-Life** - Multiple decommissioning triggers show mature thinking
9. **Gate with Criteria** - Every gate needs explicit pass/fail criteria
10. **Maintain Symmetry** - The V-model's power is in design-evaluation correspondence

## Validation vs. Verification

**Verification** (deterministic, against spec-for-lifecycle):

- Are all required sections present?
- Is the architecture reference in frontmatter?
- Are three design phases and four evaluation phases defined?
- Is there a V-model diagram?
- Are operations and decommissioning sections present?

**Validation** (qualitative, against this guidance):

- Is V-model alignment clear and correct?
- Is architecture traceability complete?
- Are phases comprehensive with actionable content?
- Is operations coverage thorough?
- Is decommissioning realistic?
- Are gates rigorous with explicit criteria?

This guidance document supports **validation** - assessing fitness-for-purpose.

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

- **V-Model Alignment:** Criteria map to lifecycle phases (design, evaluation, operations)
- **Architecture Traceability:** References spec-for-lifecycle explicitly
- **Phase Completeness:** Each section has purpose, tips, anti-patterns, preferred
- **Operations Coverage:** Workflow includes quality checkpoints and maintenance guidance
- **Decommissioning Readiness:** Addresses common issues including end-of-life
- **Gate Rigor:** Clear distinction between verification and validation criteria

## Document Metadata

| Property | Value |
|----------|-------|
| Specification | [[spec-for-lifecycle]] |
| Guidance Version | 2.0.0 |
| Specification Version | 2.0.0 |
| Terminology | VERIFICATION = structural compliance; VALIDATION = quality assessment |
| Target Users | Systems engineers creating engineering lifecycle documentation |

---

**Note:** This guidance is coupled with [[spec-for-lifecycle]] via a coupling edge, supporting the assurance of engineering lifecycle documentation that delivers systems from architecture through operations.
