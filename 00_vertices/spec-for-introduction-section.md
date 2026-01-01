---
type: vertex/spec
extends: spec
id: v:spec:introduction-section
name: Specification for INCOSE Paper Introduction Section
tags:
  - vertex
  - spec
  - introduction
version: 1.0.0
created: 2025-12-31T19:00:00Z
modified: 2025-12-31T19:00:00Z
description: Detailed structural requirements for Introduction sections in INCOSE symposium papers
sections:
  - purpose
  - structural_requirements
  - content_requirements
  - format_constraints
strictness: strict
dependencies:
  - v:spec:incose-paper-section
---

# Specification for INCOSE Paper Introduction Section

## Purpose Statement

This specification defines strict structural and content requirements specifically for Introduction sections in INCOSE symposium research papers. It extends the general section spec with Introduction-specific requirements derived from INCOSE template guidelines and SE best practices.

Verification against this spec ensures the Introduction properly motivates the research, positions the contribution, and orients the reader.

## Structural Requirements

### Required Subsections

The Introduction MUST contain the following logical components (may use subsections or integrated narrative):

1. **Problem Statement / Motivation** (1-3 paragraphs)
   - Opening hook that establishes relevance
   - Clear statement of the problem or challenge
   - Why this problem matters to SE community

2. **Gap Analysis** (1-2 paragraphs)
   - What current approaches/frameworks lack
   - Why existing solutions are insufficient
   - Specific deficiency being addressed

3. **Contribution Summary** (1-2 paragraphs)
   - Clear statement of what this paper contributes
   - Specific innovations or advances
   - How contribution addresses the gap

4. **Paper Organization** (1 paragraph)
   - Roadmap of remaining sections
   - Format: "Section 2 presents..., Section 3 describes..."

### Heading Structure

- Section heading: `\section{Introduction}` (required, Heading 1)
- Subsections: `\subsection{...}` (optional, Heading 2) - use ONLY if Introduction exceeds 800 words
- Third-level headings: NOT RECOMMENDED for Introduction

### Length Constraints

- **Target**: 800-1200 words
- **Minimum**: 600 words (below this, insufficient motivation)
- **Maximum**: 1500 words (above this, excessive preamble)
- **Proportion**: Should be 10-15% of total paper length

## Content Requirements

### Opening Paragraph

The first paragraph MUST:
- Open with a concrete, relatable statement (not abstract platitude)
- Establish relevance to systems engineering practice
- Hook reader interest immediately
- Avoid starting with "In recent years..." or similar clichés

**Anti-pattern Examples:**
- ❌ "Quality is important in systems engineering." (too obvious)
- ❌ "Since the beginning of time, humans have sought..." (too grandiose)
- ❌ "Systems engineering faces many challenges today." (too vague)

**Good Pattern:**
- ✅ Opens with specific challenge, current trend, or concrete scenario

### Problem Statement

The problem statement MUST:
- Be specific and bounded (not "all documentation is hard")
- Connect to identifiable stakeholder need
- Be solvable within scope of a single paper
- Avoid overgeneralization

### Gap Identification

The gap MUST:
- Reference what exists (current V&V frameworks, standards, tools)
- Specify what is missing or insufficient
- Explain why gap matters (consequences of not filling it)
- Set up the contribution naturally

### Contribution Statement

The contribution statement MUST:
- Be explicit (not buried or vague)
- List specific innovations (numbered list acceptable)
- Match what paper actually delivers
- Avoid overclaiming ("first ever", "only", "solves all")

**Required Format Example:**
```
This paper presents/contributes/demonstrates:
1. [Specific contribution 1]
2. [Specific contribution 2]
3. [Specific contribution 3]
```

### Paper Organization Roadmap

The roadmap paragraph MUST:
- Appear as last paragraph of Introduction
- Reference ALL major sections by number and name
- Use consistent format: "Section X [verb] [topic]"
- Match actual section structure

**Required Pattern:**
```
Section 2 presents..., Section 3 describes...,
Section 4 demonstrates..., Section 5 discusses...,
Section 6 concludes...
```

## Format Constraints

### Citations

- MUST cite at least 2-3 key references in Introduction
- Citations establish context and position work
- Use APA in-text format: `\parencite{Author2024}`
- Avoid citation-heavy paragraphs (balance with own voice)

### Figures

- MAY include 1 figure in Introduction (not required)
- If included, MUST be introductory/conceptual (not detailed)
- MUST cite figure before it appears: "As shown in Figure 1..."
- Figure should illustrate key concept or framework overview

### Mathematical Notation

- SHOULD NOT include equations in Introduction
- If unavoidable, keep to simple definitions only
- No numbered equations in Introduction

### Tone and Voice

- Active voice preferred over passive
- "We present..." better than "This paper presents..."
- Direct engagement: "Our contribution is..."
- Avoid hedging: "might", "could potentially", "may possibly"

## Verification Checklist

An Introduction section PASSES verification if:

- [ ] Section begins with `\section{Introduction}`
- [ ] Length is 600-1500 words
- [ ] Contains all 4 required components (Problem, Gap, Contribution, Roadmap)
- [ ] Opening paragraph avoids clichés and platitudes
- [ ] Problem statement is specific and bounded
- [ ] Gap is explicitly identified with reference to existing work
- [ ] Contribution statement is explicit and specific (not vague)
- [ ] Contributions are numbered or clearly listed
- [ ] Paper organization roadmap is present as last paragraph
- [ ] Roadmap references all major sections by number
- [ ] At least 2-3 citations present
- [ ] If figure included, it is cited before appearance
- [ ] No numbered equations
- [ ] Active voice used predominantly
- [ ] No subsections if Introduction < 800 words
- [ ] If subsections used, they follow heading hierarchy

## Anti-Patterns to Detect

The following indicate FAILED verification:

- ❌ Introduction starts with dictionary definition
- ❌ First paragraph is abstract/philosophical without concrete grounding
- ❌ Problem statement is overly broad ("all of SE")
- ❌ No explicit gap identified
- ❌ Contribution buried in middle paragraph without emphasis
- ❌ Contribution claims don't match paper content
- ❌ No paper organization roadmap
- ❌ Roadmap doesn't match actual sections
- ❌ Introduction exceeds 20% of total paper length
- ❌ Excessive passive voice ("It is shown that...")

## Schema Definition

```yaml
introduction_section:
  type: object
  required:
    - section_heading
    - problem_statement
    - gap_analysis
    - contribution_statement
    - paper_roadmap
    - word_count
    - citations
  properties:
    section_heading:
      type: string
      const: "\\section{Introduction}"
    problem_statement:
      type: object
      required: [present, specific, bounded]
      properties:
        present: {type: boolean}
        specific: {type: boolean}
        bounded: {type: boolean}
    gap_analysis:
      type: object
      required: [present, explicit, references_existing_work]
      properties:
        present: {type: boolean}
        explicit: {type: boolean}
        references_existing_work: {type: boolean}
    contribution_statement:
      type: object
      required: [present, explicit, numbered_or_listed]
      properties:
        present: {type: boolean}
        explicit: {type: boolean}
        numbered_or_listed: {type: boolean}
        matches_paper_content: {type: boolean}
    paper_roadmap:
      type: object
      required: [present, as_last_paragraph, references_all_sections]
      properties:
        present: {type: boolean}
        as_last_paragraph: {type: boolean}
        references_all_sections: {type: boolean}
    word_count:
      type: integer
      minimum: 600
      maximum: 1500
    citations:
      type: integer
      minimum: 2
      description: Number of citations in Introduction
    figures:
      type: integer
      maximum: 1
      description: Number of figures (0 or 1 acceptable)
    subsections:
      type: integer
      maximum: 3
      description: Number of subsections (discouraged unless >800 words)
```

---

**Note:** This specification enables precise verification of Introduction sections before integration into the complete INCOSE paper. It is designed to work with [guidance-for-introduction-section](guidance-for-introduction-section.md) for complete V&V.
