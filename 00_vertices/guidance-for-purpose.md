---
type: vertex/guidance
extends: doc
id: v:guidance:purpose
name: Guidance for Purpose Documents
description: Quality criteria and best practices for creating excellent purpose documents defining problems solved, objectives, deliverables, constraints, and success criteria
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-27T22:00:00Z
modified: 2025-12-27T22:00:00Z
dependencies: []
---

# Guidance for Purpose Documents

**This guidance defines quality criteria and best practices for creating excellent purpose documents.**

## Purpose

While [[spec-for-purpose]] defines what structural elements must be present, this guidance helps authors assess **how well** a purpose defines the problem being solved and value being delivered. Great purposes are specific, user-centered, measurable, and focused. **Purpose is the anchor of PPP design - design it FIRST.**

## Document Overview

### What This Guidance Covers

This guidance supports authors creating purpose documents by providing:
- Quality assessment criteria for purposes
- Best practices for defining problems, objectives, and success
- Common pitfalls and solutions
- Section-by-section authoring advice
- Workflow recommendations for purpose creation

### Best Use Cases

Use this guidance when:
- Starting a new AI model design in the PPP framework (design Purpose FIRST)
- Reviewing an existing purpose for clarity and focus
- Teaching others how to define valuable AI purposes
- Evaluating whether a purpose addresses real user needs
- Preventing scope creep through clear constraints

## Quality Criteria

### 1. Problem Specificity

**Excellent:**
- Problem statement is specific and concrete
- Focuses on user need, not AI capability
- Clear and direct
- Uses format: "help users [solve specific problem]"

**Good:**
- Problem is reasonably clear
- User-focused
- Understandable

**Needs Improvement:**
- Problem is vague ("help with stuff")
- Feature-focused instead of problem-focused
- Unclear what user challenge is being addressed

### 2. Objectives Quality

**Excellent:**
- Lists 3-6 specific, measurable objectives
- Uses strong action verbs (analyzing, extracting, generating, validating)
- Each objective directly addresses the problem
- Objectives are realistic and achievable

**Good:**
- Objectives are stated
- Mostly measurable
- Generally address problem

**Needs Improvement:**
- Too few (< 3) or too many (> 6) objectives
- Vague objectives ("help users")
- Objectives don't address the stated problem
- Unmeasurable or unrealistic

### 3. Deliverable Concreteness

**Excellent:**
- Names specific, concrete artifacts or outcomes
- **Specifies deliverable types by referencing specs** (e.g., "chart document conforming to [[spec-for-charts]]")
- Examples: "template.yaml specification", "compliance report conforming to [[spec-for-assurance-audits]]", "step-by-step guidance"
- At least 2 deliverables listed with explicit types
- Deliverables align with objectives
- Creates new spec if no existing spec covers the deliverable type

**Good:**
- Deliverables are stated
- Reasonably concrete
- Some alignment with objectives
- Some type specification

**Needs Improvement:**
- Deliverables are vague ("useful outputs")
- No specific artifacts named
- No type specifications or spec references
- Doesn't align with objectives

### 4. Constraint Clarity

**Excellent:**
- Explicitly defines what is OUT of scope
- Lists 3+ clear boundaries
- Prevents scope creep
- Manages expectations realistically
- Examples: "only analyzes provided documents", "requires minimum 2 examples"

**Good:**
- Some constraints stated
- Boundaries generally clear
- Most scope defined

**Needs Improvement:**
- No constraints or boundaries stated
- Scope is unlimited or unclear
- Likely to experience scope creep

### 5. Success Measurability

**Excellent:**
- Success criteria are verifiable, not purely subjective
- Mixes quality, completeness, usability, and outcome measures
- Uses format: "Your work is successful when:" + bulleted list
- Clear how to know it worked

**Good:**
- Success criteria are stated
- Mostly measurable
- Some mix of measures

**Needs Improvement:**
- Success is unmeasurable ("users are happy")
- Purely subjective criteria
- No clear way to verify success

### 6. User-Centeredness

**Excellent:**
- Entire purpose addresses real user needs
- Problem is stated from user perspective
- Value to user is clear
- Avoids feature lists in favor of problem-solving

**Good:**
- Generally user-focused
- User value is present
- Some user perspective

**Needs Improvement:**
- Feature-focused ("AI can do X, Y, Z") instead of problem-focused
- User value unclear
- Describes AI capabilities instead of user problems solved

### 7. Obsidian Compatibility

**Excellent:**
- Links to related persona and protocol documents when applicable
- Uses consistent ID format (`v:purpose:<name>`)
- Tags properly included in frontmatter

**Good:**
- Basic linking present
- ID format correct

**Needs Improvement:**
- No cross-references where appropriate
- ID format inconsistent

## Section-by-Section Guidance

### Problem Statement

**Tips:**
- State specific user problem, not general "help"
- Focus on user need, not AI capability
- Be clear and direct
- Use format: "Your purpose is to help users [solve specific problem]"

**Examples:**
- ✅ "help users extract reusable templates from example documents"
- ✅ "help users learn the PPP framework and apply it effectively"
- ❌ "help users with documents" (too vague)

### Core Objectives

**Tips:**
- List 3-6 specific objectives (focused but complete)
- Use action verbs (analyzing, extracting, generating, validating)
- Make each objective measurable and realistic
- Each should directly address the problem

**Examples:**
- ✅ "Analyzing uploaded documents to identify common patterns"
- ✅ "Generating formal template specifications in YAML format"
- ❌ "Help with analysis" (vague, no action verb)

### Specific Deliverables

**Tips:**
- Name specific artifacts users receive
- **Specify deliverable types by referencing specs** (e.g., "[[spec-for-charts]]")
- If no existing spec covers your deliverable type, create a new spec and guidance for it
- Be concrete about outputs and their structure
- Ensure deliverables align with objectives
- List at least 2 deliverables with explicit types

**Examples:**
- ✅ "Chart document conforming to [[spec-for-charts]]"
- ✅ "Assurance audit report conforming to [[spec-for-assurance-audits]]"
- ✅ "Template specification (create [[spec-for-template]] if none exists)"
- ✅ "Usage guidance document conforming to [[guidance-for-guidance]]"
- ❌ "Useful outputs" (not specific, no type)
- ❌ "A report" (what kind? create spec for report type)

### Constraints and Boundaries

**Tips:**
- Define what is OUT of scope
- Set clear boundaries to prevent scope creep
- Be explicit (list 3+ constraints)
- Manage expectations

**Examples:**
- ✅ "Only analyzes documents provided by user (no web searches)"
- ✅ "Requires minimum 2 example documents"
- ✅ "Does not modify or edit original files"
- ❌ No constraints listed (scope creep likely)

### Success Criteria

**Tips:**
- Make criteria measurable, not purely subjective
- Mix quality, completeness, usability, outcome measures
- Use format: "Your work is successful when:" + bullets
- Define how to verify success

**Examples:**
- ✅ "Template captures the true structure of provided examples"
- ✅ "Users understand how to apply the template to new instances"
- ✅ "Template passes automated verification checks"
- ❌ "Users are happy" (unmeasurable)

## Workflow Guidance

### Recommended Authoring Sequence

1. **Identify Core Problem** (10 minutes)
   - What struggle do users face?
   - What takes too much time without help?
   - What requires expertise users don't have?
   - **Checkpoint:** Can you state the specific user problem clearly?

2. **Define Objectives and Deliverables** (15 minutes)
   - How can AI address this problem?
   - Break solution into 3-6 concrete objectives with action verbs
   - Name specific artifacts users will receive
   - **Checkpoint:** Do objectives directly solve the problem?

3. **Set Constraints** (10 minutes)
   - What should AI NOT do?
   - What's out of scope?
   - List 3+ explicit boundaries
   - **Checkpoint:** Are boundaries clear to prevent scope creep?

4. **Define Success** (10 minutes)
   - How do we know it worked?
   - Mix quality, completeness, usability measures
   - Make criteria measurable
   - **Checkpoint:** Can success be verified?

### Total Estimated Time: 45 minutes

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Too Broad | Trying to solve too many problems | Narrow focus to specific problem area |
| Feature-Focused | Describing AI capabilities, not user problems | Reframe: what problem does this solve for users? |
| No Constraints | Unlimited scope | Explicitly state what's out of scope (3+ items) |
| Unmeasurable Success | "Users are happy" | Use verifiable criteria (tests pass, tasks completed) |
| Process vs Purpose | Confusing HOW with WHY | Purpose = WHY (problem + value), Protocol = HOW |
| Vague Objectives | "Help users" | Use action verbs + specific outcomes |

## Best Practices

1. **Design Purpose FIRST** - It's the anchor of PPP design
2. **Solve Specific Problems** - Not everything, just focused problem areas
3. **List 3-6 Measurable Objectives** - Use action verbs, be concrete
4. **Name Concrete Deliverables** - Specific artifacts users receive
5. **Type Your Deliverables** - Reference specs explicitly (e.g., [[spec-for-charts]]); create new spec + guidance if needed
6. **Set Clear Constraints** - Prevent scope creep, manage expectations
7. **Define Measurable Success** - Verifiable criteria, not subjective feelings
8. **Stay User-Focused** - Address real needs, not just AI features
9. **Ensure Alignment** - Objectives → Deliverables → Success must align

---

**Note:** This guidance supports the PPP framework. **Purpose is the anchor** - design it FIRST, then create Persona to match needed expertise, then Protocol to deliver results.
