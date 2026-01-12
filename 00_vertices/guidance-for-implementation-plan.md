---
type: vertex/guidance
extends: doc
id: v:guidance:implementation-plan
name: Guidance for Implementation Plan Documents
description: Quality criteria and best practices for creating effective implementation plans that guide human-AI collaboration through development tasks
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-01-12T00:00:00Z
modified: 2025-01-12T00:00:00Z
dependencies: []
criteria:
  - objective-clarity
  - step-granularity
  - capability-accuracy
  - verification-coverage
  - rollback-completeness
  - actionability
---

# Guidance for Implementation Plan Documents

**This guidance helps authors create high-quality implementation plans that effectively guide human-AI collaboration through single-use development tasks.**

## Purpose

While spec-for-implementation-plan defines what structural elements must be present, this guidance helps authors assess **how well** an implementation plan serves its purpose. Great implementation plans enable practitioners and AI assistants to confidently execute development tasks, know exactly what to do at each step, and recover gracefully from failures.

## Document Overview

### What This Guidance Covers

Implementation plans are single-use execution guides with:

1. **Objective:** Clear goal, motivation, and measurable success criteria
2. **Prerequisites:** What must be true before starting
3. **Steps:** Ordered actions with capability hints for human vs. AI execution
4. **Verification:** How to confirm the plan succeeded
5. **Rollback:** How to recover if something goes wrong

This guidance supports authors in creating implementation plans that:

- Clearly establish what needs to be done and why
- Correctly attribute execution to humans, AI, or both
- Provide verifiable completion criteria for every step
- Enable recovery from any failure point
- Are actionable without additional research

### Best Use Cases

1. **Repository Refactors:** Restructuring code or documentation
2. **Feature Implementation:** Adding new functionality
3. **Bug Fixes:** Complex debugging requiring multiple steps
4. **Migrations:** Moving between systems, versions, or patterns
5. **Infrastructure Changes:** CI/CD, tooling, or environment updates
6. **Documentation Tasks:** Creating or updating doc sets

### When NOT to Use

- When the task is trivial (just do it)
- When creating reusable workflows (use a runbook instead)
- When documenting a process for multiple practitioners (use a runbook)
- When the "plan" has only one step

## Quality Criteria

### 1. Objective Clarity

**Excellent:**

- Goal is a single, specific sentence that describes what changes
- Motivation clearly explains the problem being solved or opportunity
- Success criteria are objectively measurable (not subjective)
- A reader can determine if the plan succeeded by checking the criteria
- Goal, motivation, and criteria are aligned and consistent

**Good:**

- Goal and motivation are clear
- Success criteria are present and mostly measurable
- General alignment between sections

**Needs Improvement:**

- Vague goal ("improve the system", "make it better")
- Missing or unclear motivation
- Success criteria are subjective ("ensure quality", "make it fast")
- Criteria don't actually prove goal was achieved
- Misalignment between stated goal and criteria

### 2. Step Granularity

**Excellent:**

- Each step accomplishes exactly one logical unit of work
- Steps are small enough to verify individually
- Steps are large enough to be meaningful (not micro-tasks)
- Dependencies between steps are accurate and complete
- A failed step can be retried without affecting other steps
- Total step count is appropriate for task complexity (not over-engineered)

**Good:**

- Steps are mostly appropriate size
- Dependencies are documented
- Most steps can be verified individually

**Needs Improvement:**

- Steps are too large (multiple logical units combined)
- Steps are too small (micromanagement, excessive overhead)
- Dependencies missing or incorrect
- Failure in one step cascades unpredictably
- Plan has 20 steps for a simple task

### 3. Capability Accuracy

**Excellent:**

- Every step has a capability hint that correctly indicates who/what executes
- `automatable` steps truly can be fully automated by Claude
- `human-judgment` steps genuinely require human decision-making
- `verification-only` steps don't require modifications
- `pair-programming` steps benefit from real-time collaboration
- `human-only` steps cannot be delegated to AI (credentials, external access)
- No steps are mis-attributed to avoid work or responsibility

**Good:**

- Capability hints are present and mostly accurate
- Clear rationale for most attributions
- No obviously wrong attributions

**Needs Improvement:**

- `automatable` steps that require judgment calls
- `human-only` steps that could clearly be automated
- Missing capability hints
- Hints chosen to shift responsibility inappropriately
- No clear rationale for why a hint was chosen

### 4. Verification Coverage

**Excellent:**

- Every step has at least one verification criterion
- Verifications are objectively checkable (commands, assertions, checklists)
- Verification criteria prove the step actually succeeded (not just ran)
- Final verification checklist traces back to success criteria
- Automated checks catch common failure modes
- Manual verification catches semantic/quality issues

**Good:**

- Most steps have verification
- Final checklist covers main success criteria
- Mix of automated and manual checks

**Needs Improvement:**

- Steps without verification criteria
- Vague verifications ("check it worked", "ensure quality")
- Final checklist doesn't prove success criteria are met
- Only automated OR only manual checks
- Verification that something ran but not that it succeeded

### 5. Rollback Completeness

**Excellent:**

- Rollback trigger is specific and actionable
- Rollback steps can restore the system from any point in the plan
- Rollback steps are in reverse dependency order
- Post-rollback verification proves system is restored
- Rollback is actually possible (data loss, external changes considered)
- Recovery path is tested or clearly testable

**Good:**

- Rollback trigger defined
- Most failure cases covered
- Post-rollback verification present

**Needs Improvement:**

- No rollback trigger criteria
- Rollback only works from final step (not intermediate failures)
- Rollback steps would leave system in undefined state
- No post-rollback verification
- Claims rollback is possible when it isn't (irreversible changes)

### 6. Actionability

**Excellent:**

- Every action can be executed without additional research
- Commands are copy-paste ready with actual values
- File paths are explicit (not "the config file")
- No ambiguous verbs ("ensure", "verify appropriately", "handle")
- Inputs list specific artifacts with locations
- Outputs describe concrete deliverables
- A new practitioner could execute the plan successfully

**Good:**

- Most actions are clear and executable
- Key commands and paths provided
- Generally actionable with occasional interpretation

**Needs Improvement:**

- Actions require research to understand ("update the settings")
- Missing file paths, commands, or specific values
- Heavy use of ambiguous language
- Assumes context not documented in the plan
- Practitioner would need to ask many questions to proceed

## Section-by-Section Guidance

### Objective Section

**Purpose:** Establish what we're doing and why it matters

**Tips:**

- Goal should be achievable in the estimated effort time
- Motivation should explain both the problem AND the value of solving it
- Success criteria should be the minimum set that proves goal is met
- Each criterion should be independently verifiable

**Anti-patterns:**

- Vague goal: "Refactor the codebase"
- Missing motivation: Jumping straight to what without why
- Unmeasurable criteria: "Code is cleaner"
- Too many criteria: 10+ criteria for a simple task

**Preferred:**

- Specific goal: "Add input validation using zod to all user service endpoints"
- Clear motivation: "Current endpoints accept unvalidated input, creating security and data integrity risks"
- Measurable criteria: "All endpoints return 400 with error message for invalid input"

### Capability Hints Taxonomy Section

**Purpose:** Define the vocabulary for collaboration

**Tips:**

- Use the 6 standard hints unless you need domain-specific additions
- If adding custom hints, document them clearly in this section
- Hints should reflect reality, not wishful thinking about AI capabilities

**Anti-patterns:**

- Omitting the taxonomy section (readers won't know what hints mean)
- Creating unnecessary custom hints
- Defining hints inconsistently with their actual meaning

**Preferred:**

- Include the full 6-hint table
- Add custom hints only when the standard set doesn't cover a case
- Ensure hint definitions match how they're used in steps

### Steps Section

**Purpose:** Guide execution with clarity and verification

**Tips:**

- Each step should have a clear verb in its name (Create, Update, Verify, Configure)
- Description should explain what AND why (briefly)
- Actions should be numbered and use imperative verbs
- Verification should prove success, not just completion
- Dependencies should form a directed acyclic graph (no cycles)

**Anti-patterns:**

- Step names that don't describe actions: "Step 3: Configuration"
- Descriptions that just repeat the name
- Actions that require interpretation: "Set up the environment"
- Subjective verifications: "Ensure it looks correct"

**Preferred:**

- Clear step name: "Step 3: Configure Database Connection"
- Informative description: "Set up connection pooling to improve performance under load"
- Specific action: "Edit `config/database.yml` and set `pool_size: 10`"
- Objective verification: "Run `rails db:migrate` - expect 0 errors"

### Verification Checklist Section

**Purpose:** Confirm the plan achieved its goal

**Tips:**

- Automated checks should run without human judgment
- Manual verification catches what automation misses (semantic correctness)
- Each success criterion should trace to at least one verification item
- Documentation updates prevent knowledge rot

**Anti-patterns:**

- All automated, no manual (misses semantic issues)
- All manual, no automated (misses regressions)
- Verification items that don't trace to success criteria
- Missing documentation updates

**Preferred:**

- Balanced: automated for structural, manual for semantic
- Clear traceability: "Success criterion 1 verified by: automated check 1, manual check 2"
- Explicit documentation requirements

### Rollback Plan Section

**Purpose:** Enable recovery from failures

**Tips:**

- Rollback trigger should be specific (not "if something goes wrong")
- Steps should restore system to pre-plan state
- Consider data loss, external system changes, side effects
- Post-rollback verification proves recovery worked

**Anti-patterns:**

- Vague trigger: "If the plan fails"
- Incomplete rollback: Only handles final step failure
- Ignoring irreversible changes: "Just revert the commits" (what about database?)
- No verification: "System should be restored"

**Preferred:**

- Specific trigger: "If tests fail after Step 3 OR deployment health check fails"
- Complete rollback: Steps for recovering from each phase
- Honest about limitations: "Note: External API changes cannot be reverted"
- Verified recovery: "Run full test suite; all tests pass"

## Workflow Guidance

### Recommended Authoring Sequence

1. **Define the Goal** (10 min)
   - What specific change are you making?
   - Why does it matter?

2. **Write Success Criteria** (10 min)
   - How will you know you succeeded?
   - What's the minimum set of checkable criteria?

3. **Identify Steps** (15 min)
   - What logical units of work are needed?
   - What are the dependencies between them?

4. **Assign Capability Hints** (10 min)
   - For each step, who/what should execute it?
   - Be honest about AI capabilities

5. **Write Step Details** (30-60 min)
   - Description, inputs, actions, outputs, verification
   - Make actions specific and copy-paste ready

6. **Create Verification Checklist** (15 min)
   - Map success criteria to specific checks
   - Balance automated and manual

7. **Write Rollback Plan** (15 min)
   - What triggers rollback?
   - How to recover from each phase?

8. **Review Prerequisites** (10 min)
   - What must be true before starting?
   - Entry checklist items

**Total estimated time:** 2-3 hours for a typical implementation plan

### Quality Checkpoints

- **After step 2:** Can success be objectively verified?
- **After step 4:** Are capability attributions realistic?
- **After step 5:** Could someone execute each step without asking questions?
- **After step 6:** Does verification prove success criteria are met?
- **After step 7:** Can you recover from any failure point?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Vague Goal** | "Improve performance" | Specify what changes: "Reduce API latency to <100ms p95" |
| **Unmeasurable Criteria** | "Code is cleaner" | Use objective measures: "All functions <50 lines" |
| **Wrong Capability Hint** | `automatable` for judgment calls | Be honest: use `human-judgment` or `pair-programming` |
| **No Step Verification** | "Do the thing, move on" | Add objective check for each step |
| **Useless Rollback** | "Revert changes" | Specify exact commands and verify recovery |
| **Unactionable Steps** | "Configure the system" | List specific files, values, commands |

## Best Practices

1. **Start with Success Criteria** - Define done before defining how
2. **Be Honest About Capabilities** - Mis-attributed hints waste time
3. **One Logical Unit Per Step** - Easier to verify and rollback
4. **Commands Over Prose** - Copy-paste beats interpretation
5. **Verify Success, Not Completion** - Running isn't the same as working
6. **Plan for Failure** - Rollback is as important as the happy path
7. **Update Status** - Move plan through lifecycle (draft → approved → in-progress → completed)
8. **Archive Don't Delete** - Completed plans are documentation
9. **Keep Plans Focused** - One task per plan; create multiple plans if needed
10. **Test the Plan** - Walk through mentally before executing

## Validation vs. Verification

**Verification** (deterministic, against spec-for-implementation-plan):

- Are all required frontmatter fields present?
- Is status one of the defined enum values?
- Does the Capability Hints Taxonomy section exist?
- Are there at least 2 steps with required fields?
- Does every step have a capability hint?
- Is there a rollback plan with trigger, steps, and verification?

**Validation** (qualitative, against this guidance):

- Is the objective clear and measurable?
- Are steps appropriately granular?
- Are capability hints accurately assigned?
- Does verification prove success?
- Is rollback actually possible?
- Are actions executable without research?

This guidance document supports **validation** - assessing fitness-for-purpose.

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

- **Objective Clarity:** Clear purpose statement, specific audience (plan authors)
- **Step Granularity:** Authoring sequence with appropriate steps
- **Capability Accuracy:** Quality criteria accurately describe what to assess
- **Verification Coverage:** Checkpoints and common issues provide verification
- **Rollback Completeness:** Common issues show recovery from problems
- **Actionability:** Specific anti-patterns and preferred patterns

## Document Metadata

| Property | Value |
|----------|-------|
| Specification | [[spec-for-implementation-plan]] |
| Guidance Version | 1.0.0 |
| Specification Version | 1.0.0 |
| Terminology | IMPLEMENTATION PLAN = single-use execution guide; RUNBOOK = reusable workflow |
| Target Users | Authors creating execution guides for human-AI development tasks |

---

**Note:** This guidance is coupled with [[spec-for-implementation-plan]] via a coupling edge. Together they enable assurance of implementation plan documents that guide human-AI collaboration through single-use development tasks.
