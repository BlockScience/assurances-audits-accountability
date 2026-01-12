---
type: vertex/guidance
extends: doc
id: v:guidance:branch-review
name: Guidance for Branch Review Documents
description: Quality criteria and best practices for creating excellent branch review documents
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-01-12T00:00:00Z
modified: 2025-01-12T00:00:00Z
dependencies: []
criteria:
  - clarity
  - completeness
  - context-alignment
  - objectivity
  - actionability
  - traceability
rubric: validation-assessment
---

# Guidance for Branch Review Documents

**This guidance defines quality criteria and best practices for creating excellent branch review documents.**

## Purpose Statement

While the spec-for-branch-review defines what structural elements must be present, this guidance helps authors assess **how well** a branch review serves its stated purpose. Great branch reviews are clear, complete, well-contextualized, objective, actionable, and traceable.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating branch review documents by providing:
- Quality assessment criteria for evaluating reviews
- Best practices for systematic branch analysis
- Common pitfalls and solutions
- Section-by-section authoring advice
- Workflow recommendations for conducting reviews

### Best Use Cases

Use this guidance when:
- Creating a new branch review document
- Reviewing an existing branch review for quality
- Teaching others how to conduct effective branch reviews
- Establishing branch review standards for your organization
- Evaluating whether a review adequately addresses its stated purpose

## Quality Criteria

### 1. Clarity

**Excellent:**
- Assertions are precise and unambiguous
- Technical terms defined or contextually clear
- Observations distinguished from interpretations
- No contradictory statements
- Confidence levels appropriately justified

**Good:**
- Generally clear with minor ambiguities
- Most terms understandable in context
- Assertions mostly distinguishable from observations
- Confidence levels present but not always justified

**Needs Improvement:**
- Vague assertions ("the code is good", "seems reasonable")
- Undefined jargon or acronyms
- Observations and assertions conflated
- Missing or arbitrary confidence levels

### 2. Completeness

**Excellent:**
- All significant changes in the branch addressed
- Change inventory covers all modified files
- Each stated key question is answered
- Assertions cover all evaluation criteria
- Gaps explicitly acknowledged if present

**Good:**
- Major changes addressed
- Most files inventoried
- Key questions mostly answered
- Some evaluation criteria addressed

**Needs Improvement:**
- Significant changes overlooked
- Incomplete file inventory
- Key questions unanswered
- Evaluation criteria ignored

### 3. Context Alignment

**Excellent:**
- Analysis clearly matches stated review purpose
- Evaluation criteria appropriate for review type
- Scope boundaries respected throughout
- Perspective consistently applied
- Key questions directly inform assertions

**Good:**
- Analysis generally aligned with purpose
- Most evaluation criteria relevant
- Scope mostly respected
- Some perspective drift

**Needs Improvement:**
- Analysis disconnected from stated purpose
- Inappropriate evaluation criteria
- Scope creep or inconsistent boundaries
- Perspective unclear or shifting

### 4. Objectivity

**Excellent:**
- Observations based on verifiable evidence
- Assertions clearly marked with confidence levels
- Counter-evidence acknowledged when present
- Personal opinions separated from factual claims
- Multiple interpretations considered where relevant

**Good:**
- Most claims supported by evidence
- Confidence levels assigned
- Generally balanced perspective
- Some opinion/fact mixing

**Needs Improvement:**
- Unsupported assertions
- Missing confidence levels
- One-sided analysis
- Opinion presented as fact

### 5. Actionability

**Excellent:**
- Primary recommendation is clear and specific
- Each recommendation includes rationale
- Recommendations are implementable
- Conditional recommendations well-specified
- Priority ordering reflects importance

**Good:**
- Recommendations present and understandable
- Most include rationale
- Generally implementable
- Some priority indication

**Needs Improvement:**
- Vague recommendations ("improve the code")
- Missing rationale
- Impractical suggestions
- No prioritization

### 6. Traceability

**Excellent:**
- Every assertion linked to specific evidence
- Evidence references specific files, commits, or sections
- Change inventory supports assertions made
- Patterns cite multiple instances
- Gaps and concerns tied to specific observations

**Good:**
- Most assertions have evidence
- Evidence generally specific
- Reasonable connection to inventory
- Some patterns supported

**Needs Improvement:**
- Unsupported assertions
- Vague evidence references
- Disconnect from change inventory
- Patterns claimed without instances

## Section-by-Section Guidance

### Review Purpose

**Purpose:** Establish why this review matters and what questions it answers

**Tips:**
- Connect to real decisions or actions that depend on this review
- Make key questions specific and answerable
- Ensure questions can be addressed within the stated scope
- Avoid generic questions that apply to any review

**Anti-pattern:** Generic purpose
- ❌ "This review evaluates the quality of the branch"
- ✅ "This review assesses whether the architecture refactoring aligns with our documented conceptual architecture and is ready for integration"

### Review Scope

**Purpose:** Define clear boundaries for what is being reviewed

**Tips:**
- Branch information should match frontmatter exactly
- In-scope items should be specific enough to verify
- Out-of-scope items prevent scope creep
- Be explicit about what you're NOT reviewing

**Quality indicators:**
- Reader can determine if a specific change is in or out of scope
- Boundaries align with available expertise
- Scope is appropriate for review type

### Review Context

**Purpose:** Establish the lens through which changes are analyzed

**Tips:**
- Review type should match common industry terms when applicable
- Perspective should explain what knowledge/expertise informs the review
- Evaluation criteria should be specific to this review type
- Criteria should be assessable from the available information

**Example evaluation criteria:**
- Architecture review: "Consistency with documented patterns", "Separation of concerns", "Dependency direction"
- Quality audit: "Code coverage", "Error handling completeness", "Documentation currency"
- Competitive analysis: "Feature parity", "Innovation differentiation", "Integration complexity"

### Branch Overview

**Purpose:** Provide narrative context before diving into details

**Tips:**
- Summary should be readable by stakeholders unfamiliar with the codebase
- Key commits should represent significant milestones, not every commit
- Change statistics help calibrate expectations for detail
- Themes should emerge from the changes, not be imposed

**Anti-pattern:** Commit log dump
- ❌ Listing all commits without significance assessment
- ✅ Selecting 3-5 commits that represent major milestones with explanation of why they matter

### Change Inventory

**Purpose:** Systematically document what changed

**Tips:**
- Categories should reflect repository structure (vertices, edges, scripts, etc.)
- Every file in the diff should appear somewhere
- Change type should be accurate (Added/Modified/Deleted)
- Descriptions should be brief but informative

**Quality indicators:**
- Category organization makes finding changes easy
- File count matches actual diff
- Descriptions help readers understand impact without reading files

### Analysis

**Purpose:** Identify patterns, implications, and concerns

**Tips:**
- Observations should be factual (verifiable from the changes)
- Patterns should cite multiple instances as evidence
- Gaps and concerns should include severity assessment
- Implications should connect observations to broader context

**Anti-pattern:** Judgment without analysis
- ❌ "The code quality is poor"
- ✅ "5 of 12 new functions lack error handling, which may cause silent failures in production (High severity)"

### Assertions

**Purpose:** Make clear claims about the branch

**Tips:**
- Summary assertion should answer the primary key question
- Each assertion should be independently meaningful
- Confidence levels should reflect evidence strength
- Rationale should be concise but complete

**Confidence level guidelines:**
- **High:** Multiple pieces of strong evidence, no counter-evidence
- **Medium:** Some evidence supports assertion, minor uncertainty remains
- **Low:** Limited evidence, significant uncertainty, more information needed

**Example assertion:**
| ID | Assertion | Confidence | Evidence |
|----|-----------|------------|----------|
| A1 | The architecture refactoring is consistent with the documented conceptual architecture | High | All 4 architecture documents reference and implement concepts from the base ontology; dependency directions match specification |

### Recommendations

**Purpose:** Provide actionable guidance based on findings

**Tips:**
- Primary recommendation should be crystal clear (merge, reject, modify)
- Specific recommendations should be implementable
- Rationale should connect to assertions and evidence
- Conditional recommendations handle edge cases

**Quality indicators:**
- Someone could act on recommendations without further clarification
- Recommendations follow logically from assertions
- Priority ordering reflects actual importance

### Accountability

**Purpose:** Document who conducted the review and how

**Tips:**
- Reviewer should be identifiable (person, team, or system)
- Review method should describe tools and approach used
- Limitations should be honest about what the review can and cannot claim

**Review method examples:**
- "Manual code review with LLM-assisted summarization"
- "Automated static analysis combined with human architectural assessment"
- "Pair review by two senior engineers with domain expertise"

## Workflow Guidance

### Recommended Review Process

1. **Scope Definition** (10-15 min)
   - Identify branch and base
   - Define review purpose and type
   - Establish evaluation criteria
   - Document scope boundaries

2. **Change Collection** (15-30 min)
   - Generate diff statistics
   - Create file inventory by category
   - Identify key commits
   - Note initial observations

3. **Systematic Analysis** (30-60 min)
   - Review changes by category
   - Identify patterns across changes
   - Assess against evaluation criteria
   - Document observations and concerns

4. **Assertion Development** (20-30 min)
   - Formulate specific assertions
   - Assign confidence levels
   - Link assertions to evidence
   - Write rationale for each

5. **Recommendation Formulation** (15-20 min)
   - Determine primary recommendation
   - Develop specific action items
   - Prioritize recommendations
   - Add conditional guidance

6. **Document Assembly** (20-30 min)
   - Complete all sections per spec
   - Verify frontmatter accuracy
   - Check internal consistency
   - Add accountability information

7. **Quality Review** (15-20 min)
   - Review against this guidance
   - Verify traceability of assertions
   - Check for scope creep
   - Ensure objectivity

**Total estimated time:** 2-3 hours for a typical branch review

### Quality Checkpoints

After completing each phase:

- **After step 1:** Are the key questions specific enough to have definitive answers?
- **After step 3:** Do observations reference specific files and changes?
- **After step 4:** Could someone verify each assertion from the evidence cited?
- **After step 5:** Could someone act on each recommendation without clarification?
- **After step 7:** Does the review answer all stated key questions?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Scope Creep** | Review addresses changes outside stated scope | Explicitly mark out-of-scope observations; revise scope if needed |
| **Unsupported Assertions** | Claims without evidence references | Add specific file/commit references; adjust confidence if evidence weak |
| **Generic Observations** | "The code is good/bad" without specifics | Cite specific patterns with file locations and counts |
| **Missing Confidence** | Assertions without confidence levels | Add confidence levels; document uncertainty explicitly |
| **Vague Recommendations** | "Improve the code quality" | Specify exactly what to change and where |
| **Incomplete Inventory** | Files missing from change inventory | Cross-check against actual diff; add missing files |
| **Purpose Drift** | Analysis doesn't answer key questions | Revisit analysis through lens of stated questions |
| **Opinion as Fact** | Personal preferences stated as requirements | Distinguish "I prefer" from "the spec requires" |

## Best Practices

1. **Start with Purpose** - Define key questions before analyzing changes
2. **Be Systematic** - Review by category to ensure nothing is missed
3. **Evidence First** - Build assertions from observations, not vice versa
4. **Acknowledge Uncertainty** - Use confidence levels honestly
5. **Stay in Scope** - Resist scope creep; note out-of-scope observations separately
6. **Distinguish Fact from Opinion** - Clearly mark interpretive statements
7. **Make Actionable Recommendations** - Someone should be able to act immediately
8. **Maintain Traceability** - Every assertion should trace to evidence
9. **Consider the Audience** - Write for stakeholders who may not review the code
10. **Be Concise** - Comprehensive doesn't mean verbose
11. **Review Your Review** - Apply this guidance to your own document
12. **Document Limitations** - Be honest about what the review cannot assess

## Validation vs. Verification

**Verification** (deterministic):
- Does the document structurally comply with spec-for-branch-review?
- Are all required sections present?
- Do field counts match (commits, files, assertions)?
- Are confidence levels from the allowed set?

**Validation** (qualitative):
- Is the review clear and well-reasoned?
- Does it serve its stated purpose?
- Are assertions properly supported?
- Are recommendations actionable?

This guidance document supports **validation** - assessing fitness-for-purpose.

## Self-Consistency

This guidance document is itself an instance of type `vertex/guidance` and demonstrates the quality criteria it defines:

- Clear purpose and scope
- Quality criteria with leveled assessments
- Practical section-by-section advice
- Common issues with solutions
- Best practices enumerated
- Workflow with time estimates

## Coupling

This guidance is coupled with [[spec-for-branch-review]] via a coupling edge, forming an assurance basis for branch review documents.

| Spec Requirement | Guidance Criterion |
|------------------|-------------------|
| Key Questions (≥3) | Completeness: All key questions answered |
| Assertions with confidence | Objectivity: Confidence levels justified |
| Evidence references | Traceability: Assertions linked to evidence |
| Recommendations with rationale | Actionability: Recommendations implementable |
| Review Context sections | Context Alignment: Analysis matches purpose |
| Accountability section | Clarity: Method and limitations documented |

---

**Note:** This guidance helps reviewers create branch reviews that effectively communicate findings, support decision-making, and maintain accountability for conclusions drawn.
