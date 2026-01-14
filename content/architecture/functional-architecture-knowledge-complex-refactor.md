---
type: vertex/doc
extends: doc
id: v:doc:functional-architecture-knowledge-complex-refactor
name: Functional Architecture - Knowledge Complex Framework Refactor
description: System functions, inputs/outputs, and function-criterion matrix for the knowledge complex framework refactor
tags:
  - vertex
  - doc
  - functional-architecture
version: 0.2.0
created: 2026-01-11T00:00:00Z
modified: 2026-01-12T00:00:00Z
system_name: Knowledge Complex Framework
scope: Internal-first deployment enabling systematic documentation with verification, validation, and assurance for BlockScience client work
conceptual_architecture_ref: v:doc:conceptual-architecture-knowledge-complex-refactor
function_count: 31
---

# Functional Architecture - Knowledge Complex Framework Refactor

## Purpose

This functional architecture defines what the knowledge complex framework must DO to meet the acceptance criteria established in the conceptual architecture. The document specifies 31 technology-agnostic functions organized into 6 functional areas, with clear inputs and outputs for each function. The Function-Criterion Matrix traces how these functions address the 12 acceptance criteria, forming the foundation for subsequent logical and physical architecture documents.

## Overview

The knowledge complex framework transforms how BlockScience manages knowledge-intensive work products. The conceptual architecture established 12 acceptance criteria addressing operator productivity (AC1, AC4), verification quality (AC2, AC3), approval process (AC5, AC6, AC10), workflow configuration (AC7, AC8), strategic goals (AC9, AC11), and runbook execution support (AC12).

This functional architecture translates those criteria into system behaviors organized by usage pattern:

1. **Document Authoring (F1-F4)**: Functions supporting operators in creating documents quickly
2. **Quality Assurance (F5-F9)**: Functions ensuring document structural compliance and quality scoring
3. **Knowledge Navigation (F10-F12)**: Functions enabling discovery and reuse of prior work
4. **Approval & Accountability (F13-F18)**: Functions supporting the approval workflow and effectiveness tracking
5. **Configuration & Meta (F19-F24)**: Functions enabling workflow builders to create new document types
6. **Runbook Management (F25-F31)**: Functions enabling runbook authoring, validation, and execution

Each function is specified with inputs, outputs, and behavior—without reference to implementation technology. The Function-Criterion Matrix shows how functions combine to achieve acceptance criteria.

## Conceptual Architecture Reference

[[conceptual-architecture-knowledge-complex-refactor]]

### Acceptance Criteria Summary

| ID | Criterion | Target |
|----|-----------|--------|
| AC1 | Document creation time | <30 minutes for standard document types |
| AC2 | Verification feedback speed | <3 seconds |
| AC3 | Verification accuracy | <5% false negatives, <5% false positives |
| AC4 | Search effectiveness | <5 minutes to find usable reference |
| AC5 | Approval efficiency | <15 minutes for standard documents |
| AC6 | Approval confidence | >90% report "confident" or "very confident" |
| AC7 | Effectiveness visibility | 100% of runbooks include performance criteria |
| AC8 | Workflow builder productivity | <2 hours for new Runbook including new types |
| AC9 | Self-demonstration | 100% of framework docs verified and assured |
| AC10 | Evaluation usefulness | >90% of approvers report evaluation scores useful |
| AC11 | Client demonstration capability | At least 3 document types with production examples |
| AC12 | Runbook execution support | 100% of runbook executions show current step, next step, and I/O requirements |

## Functional Architecture

### Function Table

| ID  | Name                              | Area                      | Inputs                                               | Outputs                                       |
| --- | --------------------------------- | ------------------------- | ---------------------------------------------------- | --------------------------------------------- |
| F1  | Template Retrieval                | Document Authoring        | Document type identifier                             | Template, spec reference, guidance reference  |
| F2  | Prior Work Discovery              | Document Authoring        | Document type, keywords, scope                       | Ranked document list, relevance scores        |
| F3  | Draft Generation                  | Document Authoring        | Template, parameters, prior work refs                | Draft document with placeholders filled       |
| F4  | Context Parameter Injection       | Document Authoring        | Draft document, parameter values                     | Document with parameters resolved             |
| F5  | Frontmatter Verification          | Quality Assurance         | Document                                             | Field presence/type results                   |
| F6  | Section Structure Verification    | Quality Assurance         | Document, specification                              | Section check results                         |
| F7  | Count Consistency Verification    | Quality Assurance         | Document                                             | Count match results                           |
| F8  | Reference Resolution Verification | Quality Assurance         | Document, knowledge complex                          | Reference validity results                    |
| F9  | Guidance-Based Evaluation         | Quality Assurance         | Document, guidance                                   | Per-criterion scores, suggestions             |
| F10 | Full-Text Search                  | Knowledge Navigation      | Query, scope constraints                             | Matching documents, snippets                  |
| F11 | Graph Traversal                   | Knowledge Navigation      | Starting vertex, relationship types, depth           | Connected vertices, paths                     |
| F12 | Backlink Discovery                | Knowledge Navigation      | Target document                                      | Referencing documents, relationship types     |
| F13 | Approval Request Initiation       | Approval & Accountability | Document, requestor, approver                        | Request record, notification                  |
| F14 | Verification Status Presentation  | Approval & Accountability | Document, verification results                       | Formatted summary for approver                |
| F15 | Evaluation Score Presentation     | Approval & Accountability | Document, evaluation scores                          | Formatted summary highlighting gaps           |
| F16 | Validation Edge Creation          | Approval & Accountability | Document, guidance, approver, assessment             | Validation edge, accountability record        |
| F17 | Runbook Step Tracking             | Approval & Accountability | Runbook, current step, context                       | Step status, I/O document refs                |
| F18 | Performance Metrics Collection    | Approval & Accountability | Runbook execution, timing data                       | Metrics record, effectiveness indicators      |
| F19 | Specification Authoring           | Configuration & Meta      | Type definition, structural requirements             | Spec document                                 |
| F20 | Guidance Authoring                | Configuration & Meta      | Type definition, quality criteria                    | Guidance document                             |
| F21 | Template Authoring                | Configuration & Meta      | Spec, guidance, boilerplate                          | Template document                             |
| F22 | Coupling Edge Creation            | Configuration & Meta      | Spec, guidance                                       | Coupling edge document                        |
| F23 | Verification Edge Creation        | Configuration & Meta      | Document, spec, verification results                 | Verification edge document                    |
| F24 | Assurance Face Construction       | Configuration & Meta      | Target, verification edge, validation edge, coupling | Assurance face, audit record                  |
| F25 | Runbook Retrieval                 | Runbook Management        | Task type, keywords                                  | Matching runbooks, applicability scores       |
| F26 | Runbook Module Authoring          | Runbook Management        | Module definition, input types, output types         | Module document                               |
| F27 | Runbook Assembly                  | Runbook Management        | Module list, ordering, effectiveness metrics         | Runbook document                              |
| F28 | Runbook I/O Validation            | Runbook Management        | Runbook                                              | Chaining validity results, type match results |
| F29 | Runbook Execution Instantiation   | Runbook Management        | Runbook, operator, context                           | Execution record, initial step                |
| F30 | Runbook Step Context Presentation | Runbook Management        | Execution, current step                              | Step requirements, I/O types, next steps      |
| F31 | Runbook Execution Completion      | Runbook Management        | Execution, final outputs                             | Completion record, deliverable references     |

### Functional Area 1: Document Authoring

#### F1: Template Retrieval

**Purpose:** Provide operators with the correct starting point for document creation.

**Inputs:**
- Document type identifier: String identifying the document type (e.g., "field-survey", "conceptual-architecture")

**Outputs:**
- Template document: The boilerplate template for this document type
- Spec reference: Link to the specification governing this document type
- Guidance reference: Link to the guidance for quality assessment

**Behavior:** Given a document type identifier, retrieves the associated template from the registry. Returns the template along with references to its governing spec and guidance documents. If the document type is not found, returns an error indicating unknown type.

#### F2: Prior Work Discovery

**Purpose:** Help operators find relevant existing documents to inform their work.

**Inputs:**
- Document type: Type of document being created (optional filter)
- Topic keywords: Search terms describing the subject matter
- Scope constraints: Limits on search (e.g., project, date range, author)

**Outputs:**
- Ranked document list: Documents matching the criteria, ordered by relevance
- Relevance scores: Numeric scores indicating match quality

**Behavior:** Searches the knowledge complex for documents matching the criteria. Combines full-text matching with type filtering and scope constraints. Returns results ranked by relevance, considering recency, relationship proximity, and keyword match quality.

#### F3: Draft Generation

**Purpose:** Create an initial document draft from template and context.

**Inputs:**
- Template: The document template from F1
- Context parameters: Values for template placeholders (system name, scope, dates)
- Prior work references: Documents to inform content (from F2)

**Outputs:**
- Draft document: A new document with template structure and parameters filled

**Behavior:** Instantiates the template with provided parameters. Fills standard placeholders (dates, identifiers, references). Preserves template structure while replacing placeholder content. The draft is ready for operator editing and content addition.

#### F4: Context Parameter Injection

**Purpose:** Resolve remaining parameters in a draft document.

**Inputs:**
- Draft document: Document with unresolved placeholders
- Parameter values: Map of parameter names to values (dates, names, IDs)

**Outputs:**
- Document with parameters resolved: All placeholders replaced with actual values

**Behavior:** Scans document for placeholder patterns. Replaces each placeholder with its corresponding value from the parameter map. Reports any unresolved placeholders as warnings. Validates that required parameters are provided.

### Functional Area 2: Quality Assurance

#### F5: Frontmatter Verification

**Purpose:** Verify that document frontmatter conforms to specification requirements.

**Inputs:**
- Document: The document to verify

**Outputs:**
- Field presence results: Which required fields are present/missing
- Type correctness results: Whether field values match expected types

**Behavior:** Parses YAML frontmatter from the document. Checks each required field against the document type's specification. Validates field types (string, integer, array, datetime). Returns detailed results for each field checked.

#### F6: Section Structure Verification

**Purpose:** Verify that document body structure conforms to specification.

**Inputs:**
- Document: The document to verify
- Specification: The spec defining required sections

**Outputs:**
- Section check results: Which required sections are present/missing, ordering correctness, nesting validity

**Behavior:** Parses markdown structure to identify sections by heading. Compares against specification's required sections list. Checks section ordering if spec requires specific order. Validates subsection nesting requirements.

#### F7: Count Consistency Verification

**Purpose:** Verify that frontmatter counts match actual document content.

**Inputs:**
- Document: The document to verify

**Outputs:**
- Count verification results: For each count field, whether frontmatter value matches actual count

**Behavior:** Extracts count fields from frontmatter (e.g., stakeholder_count, criterion_count, function_count). Counts actual occurrences in document body (subsections, table rows, definitions). Reports matches and mismatches with actual values.

#### F8: Reference Resolution Verification

**Purpose:** Verify that document references resolve to valid targets.

**Inputs:**
- Document: The document to verify
- Knowledge complex: The graph of all documents and relationships

**Outputs:**
- Reference verification results: For each reference, whether target exists
- Broken link report: List of unresolved references with locations

**Behavior:** Extracts all references from document (Obsidian links, ID references, path references). Checks each reference against the knowledge complex. Reports broken links with their location in the document. Distinguishes between internal (same repo) and external references.

#### F9: Guidance-Based Evaluation

**Purpose:** Score document quality against guidance criteria.

**Inputs:**
- Document: The document to evaluate
- Guidance document: The guidance defining quality criteria

**Outputs:**
- Per-criterion scores: Score (Excellent/Good/Needs Improvement) for each criterion
- Overall rating: Aggregate assessment
- Improvement suggestions: Specific recommendations for criteria below "Good"

**Behavior:** Extracts quality criteria from guidance document. Evaluates document against each criterion. Assigns scores based on criteria definitions. Generates specific suggestions for improvement. This function supports but does not replace human validation judgment.

### Functional Area 3: Knowledge Navigation

#### F10: Full-Text Search

**Purpose:** Find documents containing specific content.

**Inputs:**
- Query string: Search terms (supports phrases, operators)
- Scope constraints: Limits on search (document types, paths, date ranges)

**Outputs:**
- Matching documents: Documents containing query terms
- Snippets: Context around matches within each document
- Relevance ranking: Order by match quality

**Behavior:** Performs full-text search across document content. Supports phrase matching, boolean operators, and wildcards. Filters results by scope constraints. Returns snippets showing match context. Ranks results by relevance considering term frequency, position, and recency.

#### F11: Graph Traversal

**Purpose:** Navigate relationships in the knowledge complex.

**Inputs:**
- Starting vertex: Document to start from
- Relationship types: Types of edges to follow (dependencies, references, assurance)
- Depth limit: Maximum traversal depth

**Outputs:**
- Connected vertices: Documents reachable via specified relationships
- Traversal paths: The relationship chains connecting start to each result

**Behavior:** Starting from the given vertex, follows edges of specified types. Collects reachable vertices up to depth limit. Records the path taken to reach each vertex. Handles cycles by tracking visited vertices. Returns both vertices and the paths that reach them.

#### F12: Backlink Discovery

**Purpose:** Find documents that reference a target document.

**Inputs:**
- Target document: The document to find references to

**Outputs:**
- Referencing documents: Documents that link to the target
- Relationship types: The type of each reference (dependency, citation, assurance)

**Behavior:** Searches all documents in the knowledge complex for references to the target. Identifies reference type from context (frontmatter dependency, body link, edge relationship). Returns referencing documents grouped by relationship type. Supports understanding document impact and dependencies.

### Functional Area 4: Approval & Accountability

#### F13: Approval Request Initiation

**Purpose:** Formally request approval for a document.

**Inputs:**
- Document: The document requiring approval
- Requestor identity: Person requesting approval
- Approver identity: Person being asked to approve

**Outputs:**
- Request record: Timestamped record of the request
- Notification: Alert to the approver about pending request

**Behavior:** Creates a formal record of the approval request. Validates that verification has passed before allowing request. Records requestor, approver, document, and timestamp. Triggers notification to approver. Tracks request status (pending, approved, rejected, withdrawn).

#### F14: Verification Status Presentation

**Purpose:** Present verification results in approver-friendly format.

**Inputs:**
- Document: The document under review
- Verification results: Results from F5-F8

**Outputs:**
- Formatted summary: Clear presentation of verification status
- Pass/fail indication: Overall verification outcome
- Detail availability: Link to full verification details if needed

**Behavior:** Aggregates results from all verification functions. Presents overall pass/fail status prominently. Summarizes individual check results. Highlights any failures or warnings. Provides access to detailed results for investigation.

#### F15: Evaluation Score Presentation

**Purpose:** Present evaluation scores highlighting areas needing attention.

**Inputs:**
- Document: The document under review
- Evaluation scores: Results from F9

**Outputs:**
- Formatted summary: Clear presentation of evaluation scores
- Gap highlighting: Visual emphasis on criteria below "Good"
- Improvement suggestions: Actionable recommendations

**Behavior:** Presents evaluation scores in scannable format. Uses visual indicators (color, icons) to highlight quality levels. Groups suggestions by criterion. Prioritizes most impactful improvements. Enables approver to focus review on areas needing attention.

#### F16: Validation Edge Creation

**Purpose:** Create formal record of human validation approval.

**Inputs:**
- Document: The document being validated
- Guidance: The guidance used for validation
- Approver identity: Person signing the validation
- Assessment: The validation judgment and rationale

**Outputs:**
- Validation edge document: Formal edge connecting document to guidance
- Accountability record: Timestamped record with approver signature

**Behavior:** Creates a validation edge document conforming to spec-for-validation. Records the approver's identity, assessment date, and rationale. Requires explicit approver action (not automatic). Links document to guidance through the validation edge. Creates immutable accountability record.

#### F17: Runbook Step Tracking

**Purpose:** Track progress through runbook execution.

**Inputs:**
- Runbook: The runbook being executed
- Current step: Which step is active
- Operator context: Who is executing, when started

**Outputs:**
- Step status: Current step state (not started, in progress, completed, blocked)
- Input/output document references: Documents consumed and produced by step

**Behavior:** Tracks runbook execution state. Records step transitions with timestamps. Links documents produced/consumed at each step. Identifies dependencies between steps. Enables resumption of interrupted executions.

#### F18: Performance Metrics Collection

**Purpose:** Collect effectiveness metrics during runbook execution.

**Inputs:**
- Runbook execution: The execution being measured
- Step completions: Records of completed steps
- Timing data: Duration of each step and overall execution

**Outputs:**
- Metrics record: Collected performance measurements
- Effectiveness indicators: Comparison to runbook's defined success criteria

**Behavior:** Collects timing data for each step. Aggregates into overall execution metrics. Compares against runbook's performance criteria. Records any effectiveness indicators defined in runbook. Supports approver attestation to effectiveness (not just compliance).

### Functional Area 5: Configuration & Meta

#### F19: Specification Authoring

**Purpose:** Create specification documents for new document types.

**Inputs:**
- Type definition: Name, purpose, and identity of new document type
- Structural requirements: Required fields, sections, constraints

**Outputs:**
- Spec document: Specification conforming to spec-for-spec

**Behavior:** Generates specification document structure. Populates required sections (frontmatter requirements, body sections, type constraints). Validates against spec-for-spec requirements. Ensures spec is complete and internally consistent.

#### F20: Guidance Authoring

**Purpose:** Create guidance documents for new document types.

**Inputs:**
- Type definition: Name, purpose, and identity of document type
- Quality criteria: Criteria for evaluating document quality

**Outputs:**
- Guidance document: Guidance conforming to spec-for-guidance

**Behavior:** Generates guidance document structure. Populates quality criteria with Excellent/Good/Needs Improvement levels. Validates against spec-for-guidance requirements. Ensures guidance is actionable and assessable.

#### F21: Template Authoring

**Purpose:** Create template documents for new document types.

**Inputs:**
- Spec: The specification for the document type
- Guidance: The guidance for the document type
- Boilerplate content: Standard content to include

**Outputs:**
- Template document: Usable starting point for new documents

**Behavior:** Generates template with all required frontmatter fields as placeholders. Creates body structure matching spec's required sections. Includes guidance references for each section. Adds boilerplate content where appropriate. Validates template instantiation produces valid documents.

#### F22: Coupling Edge Creation

**Purpose:** Create coupling edge connecting spec and guidance.

**Inputs:**
- Spec: Specification document
- Guidance: Guidance document

**Outputs:**
- Coupling edge document: Edge connecting spec and guidance

**Behavior:** Creates coupling edge conforming to spec-for-coupling. Validates spec and guidance govern same document type. Records semantic alignment between spec requirements and guidance criteria. Enables complete assurance triangles for documents of this type.

#### F23: Verification Edge Creation

**Purpose:** Create verification edge recording structural compliance.

**Inputs:**
- Document: The verified document
- Spec: The specification verified against
- Verification results: Results from F5-F8

**Outputs:**
- Verification edge document: Edge connecting document to spec

**Behavior:** Creates verification edge conforming to spec-for-verification. Records verification method (automated), verifier (script), and results. Links document to its governing specification. Provides permanent record of structural compliance.

#### F24: Assurance Face Construction

**Purpose:** Construct complete assurance face closing the assurance triangle.

**Inputs:**
- Target document: The document being assured
- Verification edge: The verification edge for this document
- Validation edge: The validation edge for this document
- Coupling edge: The coupling edge for the spec-guidance pair

**Outputs:**
- Assurance face document: Face closing the assurance triangle
- Audit record: Complete audit trail of assurance process

**Behavior:** Creates assurance face conforming to spec-for-assurance. Validates all three edges form a proper triangle. Records assurance method, assurer, and human approver. Produces audit record linking all components. Marks document as fully assured.

### Functional Area 6: Runbook Management

#### F25: Runbook Retrieval

**Purpose:** Help operators find the appropriate runbook for a given task.

**Inputs:**
- Task type: The kind of work to be done (e.g., "client audit", "system design")
- Keywords: Terms describing the task context

**Outputs:**
- Matching runbooks: Runbooks applicable to the task type
- Applicability scores: How well each runbook matches the task

**Behavior:** Searches the runbook registry for runbooks matching the task type and keywords. Ranks results by applicability considering task type match, keyword relevance, and recency. Returns runbooks with descriptions and expected outputs. If no exact match, suggests closest alternatives.

#### F26: Runbook Module Authoring

**Purpose:** Create module (step) definitions for runbooks with typed inputs and outputs.

**Inputs:**
- Module definition: Name, purpose, description of the step
- Input types: Document types required as inputs to this module
- Output types: Document types produced by this module

**Outputs:**
- Module document: Module definition conforming to module spec

**Behavior:** Creates a module document with typed I/O declarations. Validates input and output types exist in the type registry. Records the transformation this module performs. Enables the module to be composed into runbooks. Module is a first-class vertex in the knowledge complex.

#### F27: Runbook Assembly

**Purpose:** Compose modules into a complete runbook with ordering and effectiveness metrics.

**Inputs:**
- Module list: Ordered list of modules comprising the runbook
- Ordering constraints: Precedence relationships between modules
- Effectiveness metrics: Criteria for evaluating runbook success

**Outputs:**
- Runbook document: Complete runbook conforming to runbook spec

**Behavior:** Assembles modules into a runbook structure. Creates `precedes` edges between modules based on ordering. Validates the module sequence forms a directed acyclic graph. Records effectiveness metrics for later evaluation. The runbook becomes a chart (subcomplex) in the knowledge complex.

#### F28: Runbook I/O Validation

**Purpose:** Validate that runbook module I/O types chain correctly.

**Inputs:**
- Runbook: The runbook to validate

**Outputs:**
- Chaining validity results: Whether output types of each module match input types of successor modules
- Type match results: Specific matches and mismatches between modules

**Behavior:** For each pair of adjacent modules in the runbook sequence, verifies that the output types of the predecessor are compatible with the input types of the successor. Reports any type mismatches that would break the chain. Ensures the runbook can be executed without type errors. This is a structural verification, not a runtime check.

#### F29: Runbook Execution Instantiation

**Purpose:** Start a new execution of a runbook, creating the execution context.

**Inputs:**
- Runbook: The runbook to execute
- Operator: Person starting the execution
- Context: Initial parameters and inputs for the execution

**Outputs:**
- Execution record: Timestamped record of the execution start
- Initial step: The first module to execute

**Behavior:** Creates an execution instance from the runbook definition. Records operator, start time, and initial context. Identifies the first module (entry point) in the runbook. Creates references to any input documents provided. Sets execution state to "in progress."

#### F30: Runbook Step Context Presentation

**Purpose:** Present the current step's requirements and context to the operator.

**Inputs:**
- Execution: The active runbook execution
- Current step: The module currently being executed

**Outputs:**
- Step requirements: What the step requires (inputs, guidance, spec)
- I/O types: Expected input and output document types for this step
- Next steps: What comes after this step completes

**Behavior:** Retrieves the module definition for the current step. Presents input requirements (document types needed), output expectations (document types to produce), and applicable guidance. Shows progress through the runbook (which steps completed, which remain). Identifies any blocking dependencies. Enables operator to understand exactly what is needed.

#### F31: Runbook Execution Completion

**Purpose:** Mark a runbook execution as complete and record final deliverables.

**Inputs:**
- Execution: The runbook execution being completed
- Final outputs: Documents produced as final deliverables

**Outputs:**
- Completion record: Timestamped record of completion with metrics
- Deliverable references: Links to all output documents from the execution

**Behavior:** Validates all required steps have been completed. Collects final output documents as deliverables. Calculates execution metrics (total time, step times). Compares metrics against runbook's effectiveness criteria. Creates completion record with full audit trail. Updates execution state to "completed."

## Function-Criterion Matrix

### Matrix View

|      | AC1 | AC2 | AC3 | AC4 | AC5 | AC6 | AC7 | AC8 | AC9 | AC10 | AC11 | AC12 |
|------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|------|
| F1   |  X  |     |     |     |     |     |     |     |     |      |      |      |
| F2   |  X  |     |     |  X  |     |     |     |     |     |      |      |      |
| F3   |  X  |     |     |     |     |     |     |     |     |      |  X   |      |
| F4   |  X  |     |     |     |     |     |     |     |     |      |      |      |
| F5   |     |  X  |  X  |     |     |     |     |     |     |      |      |      |
| F6   |     |  X  |  X  |     |     |     |     |     |     |      |      |      |
| F7   |     |  X  |  X  |     |     |     |     |     |     |      |      |      |
| F8   |     |     |  X  |     |     |     |     |     |  X  |      |      |      |
| F9   |     |     |     |     |     |     |     |     |     |  X   |      |      |
| F10  |     |     |     |  X  |     |     |     |     |     |      |      |      |
| F11  |     |     |     |  X  |     |     |     |     |     |      |      |      |
| F12  |     |     |     |  X  |     |     |     |     |     |      |      |      |
| F13  |     |     |     |     |  X  |     |     |     |     |      |      |      |
| F14  |     |     |     |     |  X  |  X  |     |     |     |      |      |      |
| F15  |     |     |     |     |  X  |  X  |     |     |     |  X   |      |      |
| F16  |     |     |     |     |     |  X  |     |     |     |      |      |      |
| F17  |     |     |     |     |     |     |  X  |     |     |      |      |  X   |
| F18  |     |     |     |     |     |     |  X  |     |     |      |      |      |
| F19  |     |     |     |     |     |     |     |  X  |     |      |      |      |
| F20  |     |     |     |     |     |     |     |  X  |     |      |      |      |
| F21  |     |     |     |     |     |     |     |  X  |     |      |      |      |
| F22  |     |     |     |     |     |     |     |  X  |  X  |      |      |      |
| F23  |     |     |     |     |     |     |     |     |  X  |      |      |      |
| F24  |     |     |     |     |     |     |     |     |  X  |      |  X   |      |
| F25  |     |     |     |  X  |     |     |     |     |     |      |      |  X   |
| F26  |     |     |     |     |     |     |     |  X  |     |      |      |      |
| F27  |     |     |     |     |     |     |  X  |  X  |     |      |      |      |
| F28  |     |     |  X  |     |     |     |     |  X  |     |      |      |      |
| F29  |     |     |     |     |     |     |     |     |     |      |      |  X   |
| F30  |     |     |     |     |     |     |     |     |     |      |      |  X   |
| F31  |     |     |     |     |     |     |  X  |     |     |      |      |  X   |

### Relationship Details

| Function | Criterion | Contribution Type | Rationale |
|----------|-----------|-------------------|-----------|
| F1 | AC1 | Primary Contributor | Template retrieval is first step enabling fast document creation |
| F2 | AC1 | Supporting | Prior work discovery reduces creation time through reuse |
| F2 | AC4 | Primary Contributor | Prior work discovery directly addresses search effectiveness |
| F3 | AC1 | Primary Contributor | Draft generation automates initial document creation |
| F3 | AC11 | Supporting | Draft generation produces documents that can become production examples |
| F4 | AC1 | Supporting | Parameter injection completes automated draft setup |
| F5 | AC2 | Primary Contributor | Frontmatter verification contributes to fast feedback |
| F5 | AC3 | Primary Contributor | Frontmatter verification catches structural errors |
| F6 | AC2 | Primary Contributor | Section verification contributes to fast feedback |
| F6 | AC3 | Primary Contributor | Section verification catches structural errors |
| F7 | AC2 | Primary Contributor | Count verification contributes to fast feedback |
| F7 | AC3 | Primary Contributor | Count verification catches consistency errors |
| F8 | AC3 | Primary Contributor | Reference verification catches broken links |
| F8 | AC9 | Supporting | Reference verification enables self-demonstration |
| F9 | AC10 | Primary Contributor | Evaluation scoring directly addresses evaluation usefulness |
| F10 | AC4 | Primary Contributor | Full-text search directly addresses search effectiveness |
| F11 | AC4 | Supporting | Graph traversal enables relationship-based discovery |
| F12 | AC4 | Supporting | Backlink discovery enables contextual discovery |
| F13 | AC5 | Primary Contributor | Request initiation starts efficient approval workflow |
| F14 | AC5 | Supporting | Verification presentation enables efficient review |
| F14 | AC6 | Primary Contributor | Verification presentation builds approver confidence |
| F15 | AC5 | Supporting | Evaluation presentation enables efficient review |
| F15 | AC6 | Primary Contributor | Evaluation presentation builds approver confidence |
| F15 | AC10 | Supporting | Evaluation presentation makes scores useful to approvers |
| F16 | AC6 | Primary Contributor | Validation edge creation formalizes confident approval |
| F17 | AC7 | Primary Contributor | Step tracking enables effectiveness visibility in runbooks |
| F18 | AC7 | Primary Contributor | Metrics collection captures effectiveness data |
| F19 | AC8 | Primary Contributor | Spec authoring is part of type creation workflow |
| F20 | AC8 | Primary Contributor | Guidance authoring is part of type creation workflow |
| F21 | AC8 | Primary Contributor | Template authoring is part of type creation workflow |
| F22 | AC8 | Supporting | Coupling edge completes type configuration |
| F22 | AC9 | Primary Contributor | Coupling edge enables assurance infrastructure |
| F23 | AC9 | Primary Contributor | Verification edge is part of assurance triangle |
| F24 | AC9 | Primary Contributor | Assurance face completes self-demonstration |
| F24 | AC11 | Primary Contributor | Assured documents become production examples |
| F25 | AC4 | Supporting | Runbook retrieval helps operators find relevant workflows |
| F25 | AC12 | Primary Contributor | Runbook retrieval is entry point for execution support |
| F26 | AC8 | Primary Contributor | Module authoring is part of runbook creation workflow |
| F27 | AC7 | Primary Contributor | Runbook assembly includes effectiveness metrics definition |
| F27 | AC8 | Primary Contributor | Runbook assembly is part of runbook creation workflow |
| F28 | AC3 | Supporting | I/O validation catches structural errors in runbooks |
| F28 | AC8 | Supporting | I/O validation ensures runbook quality before deployment |
| F29 | AC12 | Primary Contributor | Execution instantiation starts guided runbook execution |
| F30 | AC12 | Primary Contributor | Step context presentation is core execution guidance |
| F31 | AC7 | Supporting | Execution completion records effectiveness metrics |
| F31 | AC12 | Primary Contributor | Execution completion finalizes guided workflow |

### Key Traces

1. **Operator Document Creation Chain**: F1 (template retrieval) → F2 (prior work discovery) → F3 (draft generation) → F4 (parameter injection) enables AC1 (<30 min creation). Each function reduces time: F1 provides structure, F2 provides content references, F3 automates assembly, F4 finalizes placeholders.

2. **Verification Pipeline**: F5 (frontmatter) + F6 (sections) + F7 (counts) + F8 (references) → aggregated verification result enables AC2 (<3s) and AC3 (<5%/5% error). Functions execute in parallel for speed; all must pass for overall pass.

3. **Approver Review Chain**: F14 (verification presentation) + F15 (evaluation presentation) + F9 (scoring) → F16 (validation edge) enables AC5 (<15 min), AC6 (>90% confidence), AC10 (>90% usefulness). Presentations summarize complex results; evaluation identifies focus areas; validation formalizes approval.

4. **Knowledge Discovery Chain**: F10 (full-text) + F11 (graph traversal) + F12 (backlinks) enables AC4 (<5 min search). Multiple discovery modes (content, relationship, reverse reference) ensure operators find relevant work regardless of how they search.

5. **Type Configuration Chain**: F19 (spec) → F20 (guidance) → F21 (template) → F22 (coupling) enables AC8 (<2 hr runbook creation). Sequential creation ensures consistency; coupling enables complete assurance.

6. **Self-Demonstration Chain**: F22 (coupling) + F23 (verification edge) + F16 (validation edge) → F24 (assurance face) enables AC9 (100% framework docs assured). Triangle construction ensures all framework documents are fully assured.

7. **Effectiveness Tracking Chain**: F17 (step tracking) + F18 (metrics collection) enables AC7 (100% runbooks have performance criteria). Tracking captures what was done; metrics capture how well it was done.

8. **Runbook Authoring Chain**: F26 (module authoring) → F27 (runbook assembly) → F28 (I/O validation) enables AC8 (runbook creation). Module definition ensures typed I/O; assembly creates ordered workflow; validation ensures chaining correctness.

9. **Runbook Execution Chain**: F25 (runbook retrieval) → F29 (execution instantiation) → F30 (step context presentation) → F17 (step tracking) → F31 (execution completion) enables AC12 (execution support). Each function guides operators through the workflow with clear context and requirements.

## System Testing Strategy

### Test Approach by Function

| Function | Test Type | Test Method | Success Indicator |
|----------|-----------|-------------|-------------------|
| F1 | Integration | Request templates for all known types | All types return valid template within 100ms |
| F2 | Performance | Timed searches with known relevant documents | 80% of trials find target document in <30s |
| F3 | Functional | Generate drafts, verify against specs | 100% of drafts pass structural verification |
| F4 | Functional | Inject parameters, verify resolution | 100% of placeholders resolved without error |
| F5 | Accuracy | Suite of valid/invalid frontmatter samples | <5% false positive, <5% false negative |
| F6 | Accuracy | Suite of valid/invalid section structures | <5% false positive, <5% false negative |
| F7 | Accuracy | Suite of documents with correct/incorrect counts | <5% false positive, <5% false negative |
| F8 | Accuracy | Suite of documents with valid/broken references | <5% false positive, <5% false negative |
| F9 | Correlation | Evaluate samples, compare to human assessment | 80% agreement with expert ratings |
| F10 | Performance | Timed searches for known content | 80% of trials return relevant results in <3s |
| F11 | Functional | Traverse from known start, verify reachable set | 100% accuracy against expected graph |
| F12 | Functional | Query backlinks for documents with known references | 100% of known references discovered |
| F13 | Functional | Initiate requests, verify record creation | 100% of requests create valid records |
| F14 | Usability | Approver survey on presentation clarity | >80% rate presentations as "clear" or "very clear" |
| F15 | Usability | Approver survey on evaluation usefulness | >80% rate presentations as "useful" or "very useful" |
| F16 | Functional | Create edges, verify spec compliance | 100% of edges pass spec-for-validation verification |
| F17 | Functional | Execute runbooks, verify step tracking accuracy | 100% of steps tracked correctly |
| F18 | Functional | Complete runbooks, verify metrics capture | 100% of defined metrics captured |
| F19 | Functional | Author specs, verify against spec-for-spec | 100% of specs pass verification |
| F20 | Functional | Author guidance, verify against spec-for-guidance | 100% of guidance passes verification |
| F21 | Functional | Author templates, verify instantiation produces valid docs | 100% of templates produce verifiable docs |
| F22 | Functional | Create couplings, verify spec compliance | 100% of couplings pass verification |
| F23 | Functional | Create verification edges, verify spec compliance | 100% of edges pass verification |
| F24 | Integration | Construct faces from edges, verify completeness | 100% of faces close valid triangles |
| F25 | Functional | Search for runbooks by task type, verify relevance | 80% of trials find relevant runbook in top 3 results |
| F26 | Functional | Author modules, verify against module spec | 100% of modules pass spec verification |
| F27 | Functional | Assemble runbooks, verify structure and metrics | 100% of runbooks have valid structure and metrics |
| F28 | Accuracy | Validate I/O chaining on known valid/invalid runbooks | <5% false positive, <5% false negative |
| F29 | Functional | Instantiate executions, verify record creation | 100% of instantiations create valid records |
| F30 | Usability | Operator survey on step context clarity | >80% rate context as "clear" or "very clear" |
| F31 | Functional | Complete executions, verify deliverable tracking | 100% of completions record all deliverables |

## Traceability to Conceptual Architecture

### From Criteria to Functions

| Acceptance Criterion | Primary Functions | Supporting Functions |
|---------------------|-------------------|---------------------|
| AC1: Document creation time | F1, F3 | F2, F4 |
| AC2: Verification feedback speed | F5, F6, F7 | - |
| AC3: Verification accuracy | F5, F6, F7, F8 | F28 |
| AC4: Search effectiveness | F2, F10 | F11, F12, F25 |
| AC5: Approval efficiency | F13 | F14, F15 |
| AC6: Approval confidence | F14, F15, F16 | - |
| AC7: Effectiveness visibility | F17, F18, F27 | F31 |
| AC8: Workflow builder productivity | F19, F20, F21, F26, F27 | F22, F28 |
| AC9: Self-demonstration | F8, F22, F23, F24 | - |
| AC10: Evaluation usefulness | F9 | F15 |
| AC11: Client demonstration | F3, F24 | - |
| AC12: Runbook execution support | F25, F29, F30, F31 | F17 |

### Coverage Analysis

All 12 acceptance criteria are addressed by at least one function:
- **Complete coverage**: Every criterion has at least one primary function
- **Depth**: Most criteria have supporting functions that contribute
- **Balance**: Functions distribute across criteria without excessive concentration

### Stakeholder Function Usage

| Stakeholder | Primary Functions | Rationale |
|-------------|------------------|-----------|
| A3 (Operators) | F1-F4, F10-F12, F25, F29-F31 | Document creation, search, and runbook execution |
| A4 (Approvers) | F14-F16 | Review and approval workflow |
| A5 (Workflow Builders) | F19-F22, F26-F28 | Type configuration and runbook authoring |
| A6 (Infrastructure Builders) | F5-F9, F23-F24 | Verification infrastructure and assurance |

## Constraints and Assumptions

### Constraints

- **C1**: Functions must be technology-agnostic (no implementation dependencies)
- **C2**: Verification functions (F5-F8) must be deterministic and automated
- **C3**: Validation (F16) requires human judgment—cannot be fully automated
- **C4**: All functions must complete within reasonable time bounds (see test criteria)
- **C5**: Functions must preserve document immutability where required

### Assumptions

- **A1**: A registry of document types and templates exists
- **A2**: The knowledge complex provides a queryable graph interface
- **A3**: User identity is authenticated before approval functions
- **A4**: Guidance documents define scorable quality criteria
- **A5**: Runbooks define performance metrics for effectiveness

---

**Note:** This functional architecture is the second of four extended architecture documents. It establishes system functions that flow into the [[logical-architecture-knowledge-complex-refactor]] (components that implement functions) and [[physical-architecture-knowledge-complex-refactor]] (technologies that realize components).
