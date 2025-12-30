---
type: vertex/guidance
extends: doc
id: v:guidance:protocol
name: Guidance for Protocol Documents
description: Quality criteria and best practices for creating excellent protocol documents defining systematic workflows, phases, collaboration, quality checks, and principles
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-27T22:00:00Z
modified: 2025-12-27T22:00:00Z
dependencies: []
---

# Guidance for Protocol Documents

**This guidance defines quality criteria and best practices for creating excellent protocol documents.**

## Purpose

While [[spec-for-protocol]] defines what structural elements must be present, this guidance helps authors assess **how well** a protocol operationalizes purpose through systematic workflow. Great protocols are structured, actionable, collaborative, quality-focused, and consistent.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating protocol documents for the PPP framework.

### Best Use Cases

Use this guidance when creating protocols that systematically achieve purpose objectives through persona's expertise and approach.

## Quality Criteria

### 1. Phase Structure

**Excellent:** 3-5 clear phases with logical progression
**Good:** Phases are present and mostly ordered
**Needs Improvement:** No clear phases or too many (> 6)

### 2. Step Actionability

**Excellent:** Each phase has 3-6 specific, executable steps
**Good:** Steps are present and generally clear
**Needs Improvement:** Vague steps or too few/many

### 3. User Collaboration

**Excellent:** Clear validation points, input gathering, approval steps specified
**Good:** Some collaboration points defined
**Needs Improvement:** No user engagement specified

### 4. Quality Assurance

**Excellent:** Input validation, process verification, output quality checks defined
**Good:** Some quality checks present
**Needs Improvement:** No quality checks

### 5. Consistent Principles

**Excellent:** 3-5 cross-phase principles clearly stated
**Good:** Some principles mentioned
**Needs Improvement:** No consistent principles

### 6. Tools and Scripts Documentation

**Excellent:** All tools explicitly listed with path, when to use, what they do, and command syntax; tools integrated into phase steps
**Good:** Tools mentioned but missing some details (path, usage, or timing)
**Needs Improvement:** Tools referenced in workflow but not documented, or no tools listed when workflow implies automation

**Key Indicators of Excellence:**
- Each tool listed with full invocation path (e.g., `python scripts/verify_template_based.py`)
- Clear trigger for each tool (which phase, what condition)
- Purpose and expected output documented
- Command syntax with parameters shown
- Tools referenced by name in phase steps match Tools section
- Grouped by category (verification, analysis, generation, etc.)

### 7. Purpose Alignment

**Excellent:** Protocol phases directly achieve purpose objectives
**Good:** General alignment with purpose
**Needs Improvement:** Protocol doesn't achieve purpose

### 8. Obsidian Compatibility

**Excellent:** Links to [[spec-for-persona]], [[spec-for-purpose]] when applicable
**Good:** Basic linking present
**Needs Improvement:** No cross-references

## Section-by-Section Guidance

### Workflow Overview
- State number of phases
- Explain overall approach (2-3 sentences)

### Phase Definitions
- Define 3-5 phases
- Each phase needs: trigger, 3-6 steps, outputs, transition
- Steps must be concrete and executable (not vague)

### User Collaboration Points
- When to validate findings
- When to gather input
- When to get approval
- When to defer to user expertise

### Quality Assurance
- Input validation (check before starting)
- Process verification (check during work)
- Output quality checks (check deliverables)

### Tools and Scripts
- List ALL tools/scripts referenced in phase steps
- For each tool, specify:
  - Full invocation path (e.g., `python scripts/verify_template_based.py <file> --templates templates`)
  - When to use (which phase, what triggers it)
  - What it does (purpose and expected output)
  - Command syntax with parameters
- Group by category (verification, compilation, analysis, assurance, etc.)
- Ensure tools mentioned in phases match Tools section

### Consistent Principles
- List 3-5 behaviors that apply throughout
- Examples: "Evidence-based", "Transparent reasoning", "User collaboration"

## Best Practices

1. Design Protocol to achieve Purpose through Persona
2. Define 3-5 clear phases (not too rigid, not chaotic)
3. Specify 3-6 actionable steps per phase
4. Include user collaboration points
5. Build in quality checks
6. **Document all tools and scripts explicitly** - include path, when to use, what it does, command syntax
7. Integrate tool references into phase steps (mention tools by name in workflow)
8. State consistent cross-phase principles

---

**Note:** Protocol is designed LAST in PPP framework - after Purpose and Persona - to operationalize Purpose using Persona's expertise.
