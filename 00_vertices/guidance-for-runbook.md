---
type: vertex/guidance
extends: doc
id: v:guidance:runbook
name: Guidance for Runbook Documents
description: Quality criteria and best practices for creating effective runbooks that guide humans through multi-step workflows
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-01-04T16:00:00Z
modified: 2025-01-04T16:00:00Z
dependencies: []
criteria:
  - context-clarity
  - dependency-accuracy
  - actionability
  - consistency-checking
  - maintenance-completeness
  - troubleshooting-utility
---

# Guidance for Runbook Documents

**This guidance helps authors create high-quality runbooks that effectively guide practitioners through multi-step workflows to accomplish their goals and maintain artifact currency over time.**

## Purpose

While spec-for-runbook defines what structural elements must be present, this guidance helps authors assess **how well** a runbook serves its purpose. Great runbooks enable practitioners to confidently navigate complex workflows, know exactly what to do at each step, verify consistency with earlier artifacts, and maintain the artifact set over its lifetime.

## Document Overview

### What This Guidance Covers

Runbooks are human-activity guides with three parts:

1. **Context (Why, What, Who):** Problem being solved, artifacts produced, roles/skills required
2. **Workflow (How):** Ordered steps with dependencies, parallelization, consistency checkpoints
3. **Maintenance (Revisions & Reassurance):** How to update documents, propagate changes, and re-assure

This guidance supports authors in creating runbooks that:

- Clearly establish purpose, scope, and audience
- Show dependencies and parallelization opportunities
- Provide actionable, referenced steps
- Verify consistency with earlier artifacts
- Support ongoing maintenance and re-assurance

### Best Use Cases

1. **Multi-Document Workflows:** Creating related document sets (Architecture → Lifecycle → Program Plan → Program Memo)
2. **System Prompt Development:** Building AI configurations (Purpose → Persona → Protocol → System Prompt)
3. **Document Type Creation:** Establishing new types (Spec → Guidance → Coupling → Assurance)
4. **Onboarding Workflows:** Walking new practitioners through complex processes
5. **Cross-Functional Activities:** Coordinating work spanning multiple roles

### When NOT to Use

- When describing how a single document type is developed (use a lifecycle document)
- When documenting tool usage without a workflow context (use tool documentation)
- When the "workflow" is a single step (just do it)

## Quality Criteria

### 1. Context Clarity

**Excellent:**

- Why clearly states the problem being solved and value delivered
- What explicitly lists all artifacts with types and descriptions
- Who identifies specific roles with responsibilities and required skills
- Roles/skills in body match frontmatter exactly
- A newcomer could determine if this runbook is for them

**Good:**

- Why, What, Who sections present and understandable
- Artifacts listed with types
- Roles mentioned with general skills

**Needs Improvement:**

- Vague problem statement ("improve the system")
- Artifacts listed without types or descriptions
- Generic audience ("anyone who needs to...")
- Mismatch between frontmatter and body

### 2. Dependency Accuracy

**Excellent:**

- Mermaid diagram accurately shows all step dependencies
- Parallel steps are clearly marked (both in diagram and table)
- Summary table includes "Depends On" column
- Diagram uses subgraphs to group related phases
- Practitioner can determine execution order at a glance

**Good:**

- Diagram shows major dependencies
- Parallelization mentioned
- Table includes dependencies

**Needs Improvement:**

- Diagram doesn't match actual step dependencies
- Parallelization opportunities not identified
- No way to determine which steps can run concurrently
- Sequential-only presentation when parallelism is possible

### 3. Actionability

**Excellent:**

- Every activity can be performed without additional research
- Commands and tool invocations are copy-paste ready
- Specific file paths, document names, and references provided
- No ambiguous verbs ("ensure", "verify appropriately")
- Tools and References section points to exact documents with context

**Good:**

- Most activities are clear and executable
- References to specific documents
- Generally actionable with occasional interpretation

**Needs Improvement:**

- Activities are vague ("create the document")
- Generic tool references ("use the verification tools")
- Requires significant interpretation to execute
- Practitioner must figure out "how" on their own

### 4. Consistency Checking

**Excellent:**

- Every step with dependencies includes Consistency Checks
- Checks verify alignment with specific elements of prior artifacts
- Checks are actionable (not just "ensure consistency")
- Misalignment detection and resolution documented
- Cross-references are bidirectional where appropriate

**Good:**

- Consistency checks present for dependent steps
- Checks reference prior artifacts
- Generally verifiable

**Needs Improvement:**

- Missing consistency checks for dependent steps
- Vague checks ("make sure it aligns")
- No guidance on detecting or resolving misalignment
- Assumes prior artifacts never need updating

### 5. Maintenance Completeness

**Excellent:**

- When to Revisit covers all realistic triggers
- Change Propagation shows exactly which artifacts need review when each changes
- Regression Testing uses specs and guidance, not just verification
- Re-Assurance Protocol distinguishes minor/moderate/major changes
- Currency Tracking provides template for ongoing maintenance

**Good:**

- Major maintenance scenarios covered
- Change propagation documented
- Re-assurance mentioned

**Needs Improvement:**

- Maintenance section is perfunctory
- No change propagation guidance
- No regression testing steps
- Re-assurance not addressed
- Workflow appears to be "run once and forget"

### 6. Troubleshooting Utility

**Excellent:**

- Common problems are ones practitioners actually encounter
- Solutions are specific and actionable
- Problems reference specific steps where they occur
- Covers both process errors and tool failures
- Practitioner can self-recover from most issues

**Good:**

- Major problems documented
- Solutions are generally helpful
- Most practitioners can self-recover

**Needs Improvement:**

- Generic problems ("something goes wrong")
- Vague solutions ("try again")
- Missing common failure modes
- Practitioner cannot recover without external help

## Section-by-Section Guidance

### Context Section

**Purpose:** Establish why this workflow exists, what it produces, and who should execute it

**Tips:**

- Why should articulate the problem from the practitioner's perspective
- What should list every artifact with its document type
- Who should match `target_roles` and `required_skills` in frontmatter exactly
- Include time estimate to set expectations

**Anti-patterns:**

- ❌ Vague problem statement: "This helps with program documentation"
- ❌ Missing artifact types: "Produces an architecture and a plan"
- ❌ Generic audience: "Engineers and managers"

**Preferred:**

- ✅ Specific problem: "Transforms an idea into a fully documented, communicable program plan"
- ✅ Typed artifacts: "Architecture (v:doc:architecture), Lifecycle (v:doc:lifecycle)"
- ✅ Specific roles: "Systems Engineer (4-layer architecture expertise), Program Manager (stakeholder coordination)"

### Workflow Overview Section

**Purpose:** Provide visual orientation showing dependencies and parallelization

**Tips:**

- Use subgraphs in Mermaid to group related steps
- Show dependencies with solid arrows, optional dependencies with dashed
- Explicitly mark parallel groups in both diagram and table
- Summary table should have "Depends On" column

**Anti-patterns:**

- ❌ Linear diagram when parallelism is possible
- ❌ Missing dependency arrows
- ❌ Diagram that doesn't match step descriptions

**Preferred:**

- ✅ Subgraphs grouping phases with clear dependency arrows
- ✅ Parallel steps explicitly marked with notes
- ✅ Summary table showing inputs, outputs, and dependencies

### Step Definitions

**Purpose:** Guide practitioners through each step with precision

**Tips:**

- Goal should be one sentence stating what this step accomplishes
- Inputs should list specific artifacts needed (not vague references)
- Activities should be numbered, imperative, and actionable
- Tools and References should point to exact documents with context
- Consistency Checks required for steps that depend on earlier artifacts
- Checkpoint should be objectively verifiable

**Anti-patterns:**

- ❌ Vague goals: "Prepare the documentation"
- ❌ Generic activities: "Review the requirements"
- ❌ Missing consistency checks for dependent steps
- ❌ Subjective checkpoints: "Ensure quality is acceptable"

**Preferred:**

- ✅ Clear goal: "Create the architecture document defining system structure across four layers"
- ✅ Specific activities: "Run `python scripts/verify_template_based.py arch.md --templates templates`"
- ✅ Explicit consistency checks: "[ ] Architecture references match lifecycle phase names"
- ✅ Objective checkpoint: "Architecture document passes verification with 0 errors"

### Maintenance Section

**Purpose:** Enable ongoing currency, traceability, and accountability after initial completion

**Tips:**

- When to Revisit should cover realistic triggers (scope changes, stakeholder feedback, errors found)
- Change Propagation should be a matrix showing dependencies
- Regression Testing should use both verification (specs) and validation (guidance)
- Re-Assurance Protocol should distinguish change severity levels
- Currency Tracking provides a template practitioners can copy

**Anti-patterns:**

- ❌ Treating the workflow as "run once and done"
- ❌ Vague triggers: "When things change"
- ❌ Missing propagation guidance
- ❌ No regression testing steps

**Preferred:**

- ✅ Specific triggers: "When architecture scope changes, Steps 2-4 must be reviewed"
- ✅ Clear propagation: "If Architecture changes → review Lifecycle phases → update Program Plan milestones"
- ✅ Testable regression: "Re-run verification on all affected documents; re-validate if scope changed"
- ✅ Severity-based re-assurance: "Major changes require full re-assurance with updated faces"

## Workflow Guidance

### Recommended Authoring Sequence

1. **Define the Goal and Scope** (20 min)
   - What artifacts are produced?
   - What problem does this solve?
   - Who are the target roles?

2. **Map Dependencies** (30 min)
   - List steps in rough order
   - Identify which steps depend on which prior outputs
   - Mark parallelization opportunities

3. **Draw the Dependency Diagram** (20 min)
   - Create Mermaid diagram with subgraphs
   - Add dependency arrows
   - Mark parallel groups

4. **Write Step Details** (60-90 min)
   - For each step: Goal, Inputs, Activities, Tools, Outputs, Consistency Checks, Checkpoint
   - Be specific and actionable
   - Include actual commands and document references

5. **Document Maintenance** (30 min)
   - What triggers revisiting?
   - How do changes propagate?
   - What regression tests apply?
   - When is re-assurance needed?

6. **Add Prerequisites and Completion** (20 min)
   - Write entry criteria
   - Write exit checklist
   - Ensure artifacts map between these

7. **Add Troubleshooting** (20 min)
   - What can go wrong at each step?
   - What are common practitioner mistakes?
   - How do you recover?

8. **Test the Runbook** (variable)
   - Walk through with a practitioner
   - Note where they get stuck
   - Refine based on real usage

**Total estimated time:** 4-5 hours for initial runbook, plus testing

### Quality Checkpoints

- **After step 2:** Can you trace dependencies from start to all artifacts?
- **After step 4:** Could a practitioner execute each step without asking questions?
- **After step 5:** Is maintenance realistic and actionable?
- **After step 8:** Did a real practitioner complete the workflow successfully?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Vague Context** | "For engineers who need documentation" | Specify exact roles, skills, and problem being solved |
| **Missing Dependencies** | Steps assume inputs that weren't produced | Draw dependency diagram first; trace outputs-to-inputs |
| **No Parallelization** | Everything shown as sequential | Analyze which steps truly depend on each other |
| **Missing Consistency Checks** | Later steps don't verify alignment | Add checks for every step that references earlier artifacts |
| **Perfunctory Maintenance** | "Update as needed" | Specify triggers, propagation paths, regression tests |
| **Untestable Checkpoints** | "Ensure quality" | Replace with verification commands or specific checklists |
| **Generic Troubleshooting** | "Fix the issue" | Document specific recovery actions for specific failures |

## Best Practices

1. **Start with Dependencies** - Map what depends on what before writing steps
2. **Be Ruthlessly Specific** - "Run this command" beats "verify the document"
3. **Check Consistency Explicitly** - Every dependent step should verify alignment
4. **Plan for Maintenance** - Workflows don't end at first completion
5. **Test with Real Practitioners** - Runbooks are for humans; humans should validate them
6. **Show Parallelism** - Help teams work efficiently by marking concurrent opportunities
7. **Document the Unhappy Path** - Troubleshooting is as important as the happy path
8. **Version Control Runbooks** - Workflows evolve; track changes
9. **Match Frontmatter to Body** - Roles and skills must be consistent
10. **Include Re-Assurance Protocol** - Changes require systematic re-verification

## Validation vs. Verification

**Verification** (deterministic, against spec-for-runbook):

- Are Context, Prerequisites, Workflow Overview, Steps, Decision Points, Completion, Troubleshooting, Maintenance sections present?
- Does Context include Why, What, Who?
- Is there a Mermaid dependency diagram?
- Are parallelization opportunities documented?
- Do dependent steps include Consistency Checks?
- Is Maintenance section complete with all subsections?

**Validation** (qualitative, against this guidance):

- Is context clear about problem, artifacts, and audience?
- Does the dependency diagram accurately reflect step relationships?
- Are activities actionable without additional research?
- Do consistency checks verify alignment with specific prior elements?
- Is maintenance realistic and complete?
- Can practitioners self-recover using troubleshooting?

This guidance document supports **validation** - assessing fitness-for-purpose.

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

- **Context Clarity:** Clear purpose statement, specific audience (runbook authors)
- **Dependency Accuracy:** Quality criteria trace to section guidance
- **Actionability:** Specific tips, anti-patterns with ❌/✅ markers
- **Consistency Checking:** References spec-for-runbook throughout
- **Maintenance Completeness:** Workflow guidance with checkpoints
- **Troubleshooting Utility:** Common issues table with specific solutions

## Document Metadata

| Property | Value |
|----------|-------|
| Specification | [[spec-for-runbook]] |
| Guidance Version | 1.0.0 |
| Specification Version | 1.0.0 |
| Terminology | RUNBOOK = human-activity guide; LIFECYCLE = engineering object development |
| Target Users | Authors creating procedural guides for multi-step workflows |

---

**Note:** This guidance is coupled with [[spec-for-runbook]] via a coupling edge. Together they enable assurance of runbook documents that guide practitioners through complex workflows while maintaining artifact currency, traceability, and accountability.
