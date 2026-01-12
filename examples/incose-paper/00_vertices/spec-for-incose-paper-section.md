---
type: vertex/spec
extends: doc
id: v:spec:incose-paper-section
name: Specification for INCOSE Paper Sections
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-31T17:45:00Z
modified: 2025-12-31T17:45:00Z
description: Structural requirements for sections within an INCOSE symposium research paper, derived from INCOSE Conference LaTeX Template V1.2
sections:
  - purpose
  - structural_requirements
  - format_constraints
  - section_specific_requirements
schema_type: markdown-section
strictness: strict
---

# Specification for INCOSE Paper Sections

## Purpose Statement

This specification defines strict structural and formatting requirements for individual sections within INCOSE symposium research papers. While the overall paper template provides document-level requirements, this spec ensures each section (Introduction, Background, Conceptual Layer, etc.) meets INCOSE standards for content structure, heading levels, and integration.

Verification against this spec ensures sections can be assembled into a compliant INCOSE paper without formatting rework.

## Structural Requirements

### Required Frontmatter (for section markdown files)

Each section source file MUST include:

```yaml
---
section_name: <string>           # E.g., "Introduction", "Conceptual Layer"
section_type: <enum>             # abstract | introduction | body | conclusions | recommendations | acknowledgements
heading_level: <1|2|3>           # Maximum heading depth in this section
word_count_target: <integer>     # Target word count for this section
figures: [<list>]                # Figure references used in this section (may be empty)
tables: [<list>]                 # Table references used in this section (may be empty)
citations: [<list>]              # Citation keys referenced in this section (may be empty)
verified_against: v:spec:incose-paper-section
validated_by: <null or human>    # null until human validation
---
```

### Section Content Structure

Each section MUST:

1. **Begin with section heading**: First line after frontmatter MUST be section title as markdown heading
2. **Use proper heading hierarchy**:
   - Heading 1 (`#`) for major sections only
   - Heading 2 (`##`) for subsections
   - Heading 3 (`###`) for third-level (maximum depth)
   - MUST NOT skip heading levels
   - MUST NOT use more than 3 heading levels
3. **Maintain narrative flow**: Sections should flow logically from one to the next
4. **Include transitional elements**: Last paragraph should transition to next section (except Recommendations)

### Content Requirements by Section Type

#### Abstract (`section_type: abstract`)

- MUST be ≤300 words
- MUST NOT contain citations
- MUST NOT contain figures or tables
- MUST NOT contain mathematical formulas
- MUST include: purpose, scope, principal results, conclusions
- MUST match submitted abstract in EasyChair

#### Introduction (`section_type: introduction`)

- MUST state the problem or issue
- MUST provide background context
- MUST explain reason for the study
- SHOULD include subsections if >800 words
- MUST cite each figure before it appears
- SHOULD end with paper roadmap/organization

#### Body Sections (`section_type: body`)

- MUST have clear heading describing content
- MUST use heading hierarchy appropriately
- MUST cite figures/tables before they appear
- SHOULD be 500-1500 words per major section
- MUST maintain logical connection to research question

#### Conclusions (`section_type: conclusions`)

- MUST summarize results in accessible language ("layman's terms")
- MUST connect back to problem stated in Introduction
- MUST discuss limitations honestly
- SHOULD be 300-600 words
- MUST NOT introduce new concepts requiring explanation

#### Recommendations (`section_type: recommendations`)

- MUST provide specific, actionable steps
- MUST be relevant to INCOSE practitioner audience
- SHOULD be 200-500 words
- MUST follow from conclusions logically

#### Acknowledgements (`section_type: acknowledgements`)

- MUST note funding support (if any)
- MAY acknowledge non-author assistance
- SHOULD be <200 words
- MUST be placed before References

## Format Constraints

### Heading Formatting

Section headings MUST follow INCOSE template specifications:

- **Heading 1**: 18pt Helvetica bold, capitalize main words
  - Markdown: `# Major Section Heading`
  - LaTeX output: `\section{Major Section Heading}`

- **Heading 2**: 15pt Helvetica bold, capitalize main words
  - Markdown: `## Second Level Subheading`
  - LaTeX output: `\subsection{Second Level Subheading}`

- **Heading 3**: 12pt Helvetica bold, capitalize main words
  - Markdown: `### Third Level Subheading`
  - LaTeX output: `\subsubsection{Third Level Subheading}`

### Paragraph Formatting

- MUST use 0pt indentation (no paragraph indents)
- MUST use 6pt spacing between paragraphs
- MUST be fully justified (not in source markdown, but in LaTeX compilation)
- MUST NOT use manual line breaks within paragraphs

### Figure References

When referencing figures:

```markdown
As shown in Figure 1, the V-model architecture...

[Figure must appear AFTER this reference in text]
```

Figure captions MUST:
- Be numbered consecutively
- Include period after figure number
- Be followed by caption text
- Be centered
- Use 11pt PT Serif font

### Table References

Tables MUST:
- Be numbered consecutively
- Have captions ABOVE the table
- Be referenced in text before appearance
- Use proper column alignment
- Include headers with gray background (`tableheader` color)

### Mathematical Notation

Equations MUST:
- Be preceded and followed by blank line
- Be numbered if referenced in text
- Have equation numbers in parentheses, right-aligned
- Use proper LaTeX math environment

Example:
```latex
\begin{equation}
  \chi = V - E + F
  \label{eq:euler}
\end{equation}
```

### Citation Format

Citations MUST:
- Follow APA 7th edition style
- Use format: `(Author, Year)` for in-text
- Use `(Author1 & Author2, Year)` for two authors
- Use `(Author et al., Year)` for three or more authors
- Match entries in references.bib exactly

## Section-Specific Requirements

### Introduction Section

MUST contain:
- Problem statement (1-2 paragraphs)
- Background and context (2-4 paragraphs)
- Research motivation (1-2 paragraphs)
- Paper organization roadmap (1 paragraph)

SHOULD contain:
- Subsections for >800 words
- At least one figure introducing key concepts
- Forward references to later sections

MUST NOT:
- Dive into technical details (save for Body)
- Include extensive literature review (use Background section)
- Exceed 1200 words

### Background Section (if present)

MUST contain:
- Related work discussion
- Foundational concepts explanation
- Gap analysis (what's missing in prior work)

SHOULD contain:
- Comparison table of related approaches
- Key citations to prior art

### Architecture/Framework Body Sections

For papers presenting frameworks (like this one):

MUST contain:
- Clear layer/component descriptions
- Component interaction explanations
- Design rationale for key choices

SHOULD contain:
- Diagrams showing structure
- Tables summarizing components
- Examples demonstrating concepts

### Self-Demonstration Section (if applicable)

MUST contain:
- Evidence that framework was applied to itself
- Specific artifacts produced using framework
- Reflection on meta-application experience

SHOULD contain:
- Metrics showing coverage/completeness
- Discussion of bootstrapping challenges

## Verification Checklist

A section PASSES verification if:

- [ ] Frontmatter present with all required fields
- [ ] Section heading at appropriate level
- [ ] No heading levels skipped
- [ ] Maximum 3 heading levels used
- [ ] Word count within ±20% of target (if specified)
- [ ] All figures cited before appearance
- [ ] All tables cited before appearance
- [ ] All citations match entries in references.bib
- [ ] No footnotes used (INCOSE prohibits footnotes)
- [ ] Proper capitalization in headings
- [ ] Transitions between subsections present
- [ ] Content matches section_type requirements above

## Schema Definition

```yaml
incose_paper_section:
  type: object
  required:
    - section_name
    - section_type
    - heading_level
    - word_count_target
    - verified_against
  properties:
    section_name:
      type: string
      description: Human-readable section name
    section_type:
      type: string
      enum: [abstract, introduction, body, conclusions, recommendations, acknowledgements]
    heading_level:
      type: integer
      minimum: 1
      maximum: 3
      description: Maximum heading depth used in this section
    word_count_target:
      type: integer
      minimum: 0
      description: Target word count for this section
    figures:
      type: array
      items:
        type: string
        pattern: "^fig:[a-z0-9-]+$"
      description: Figure labels referenced in this section
    tables:
      type: array
      items:
        type: string
        pattern: "^tab:[a-z0-9-]+$"
      description: Table labels referenced in this section
    citations:
      type: array
      items:
        type: string
      description: Citation keys from references.bib
    verified_against:
      type: string
      const: "v:spec:incose-paper-section"
    validated_by:
      type: [string, "null"]
      description: Human approver name or null if not yet validated
```

---

**Note:** This specification enables verification of individual paper sections before assembly into the final INCOSE paper, ensuring each component meets structural requirements independently. Sections verified against this spec can be confidently integrated without rework.
