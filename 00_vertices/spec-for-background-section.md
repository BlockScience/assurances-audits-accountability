---
type: vertex/spec
extends: spec
id: v:spec:background-section
name: Specification for INCOSE Paper Background/Related Work Section
tags:
  - vertex
  - spec
  - background
version: 1.0.0
created: 2025-12-31T19:30:00Z
modified: 2025-12-31T19:30:00Z
description: Detailed structural requirements for Background and Related Work sections in INCOSE symposium papers
sections:
  - purpose
  - structural_requirements
  - content_requirements
  - format_constraints
strictness: strict
dependencies:
  - v:spec:incose-paper-section
---

# Specification for INCOSE Paper Background/Related Work Section

## Purpose Statement

This specification defines strict structural and content requirements for Background and Related Work sections in INCOSE symposium research papers. These sections establish the foundation, position the work relative to prior art, and identify gaps.

Verification against this spec ensures the Background properly contextualizes the contribution without overwhelming it.

## Structural Requirements

### Section Heading

- MUST use `\section{Background and Related Work}` OR `\section{Background}` OR `\section{Related Work}`
- Heading 1 level (18pt Helvetica bold)
- Single section (do not split into separate Background AND Related Work sections)

### Required Subsections

Background sections MUST organize content by theme/topic, NOT chronologically. Recommended subsection structure:

**Minimum 3 subsections, Maximum 6 subsections**

Typical organization:
1. Foundational concepts (e.g., "Verification and Validation Foundations")
2. Related methodologies (e.g., "Test-Driven Development")
3. Enabling technologies (e.g., "Algebraic Topology and Simplicial Complexes")
4. Application domain context (e.g., "AI Ethics and Accountability")
5. Prior art / closest related work (e.g., "Prior Art: Ghrist's The Forge")

Each subsection MUST:
- Use `\subsection{Descriptive Title}` (Heading 2, 15pt)
- Have descriptive title indicating content
- Contain 100-400 words
- Include at least 2 citations

### Heading Hierarchy

- Section: `\section{Background and Related Work}`
- Subsections: `\subsection{Topic Name}`
- Third-level: `\subsubsection{Specific Aspect}` (USE SPARINGLY, only if needed)

### Length Constraints

- **Target**: 1200-2000 words
- **Minimum**: 800 words (below this, insufficient context)
- **Maximum**: 2500 words (above this, overwhelms contribution)
- **Proportion**: Should be 15-25% of total paper length
- **Balance**: No single subsection should exceed 30% of Background length

## Content Requirements

### Foundational Concepts

When introducing foundational concepts, MUST:
- Define technical terms used later in paper
- Cite primary sources (original papers, standards, textbooks)
- Explain WHY concept matters to your work
- Avoid tutorial-style exposition (assume educated reader)

**Example Pattern:**
```latex
Boehm's 1984 formulation distinguishes verification
("Are we building the product right?") from validation
("Are we building the right product?") \parencite{Boehm1984}.
This distinction has guided systems engineering for four
decades, codified in IEEE 1012 \parencite{IEEE1012}.
```

### Related Work Coverage

For each related approach/framework, MUST provide:
- What it does (brief description)
- Key citation to primary source
- Relationship to your work (enables, contrasts, extends)
- Gap or limitation (sets up your contribution)

**Anti-patterns:**
- ❌ Exhaustive literature survey trying to cite everyone
- ❌ Straw man arguments misrepresenting prior work
- ❌ Orphaned background (concepts never used later)

### Citation Density

- **Minimum**: 10 unique citations across Background section
- **Target**: 15-20 citations
- **Distribution**: Every subsection MUST have at least 2 citations
- **Balance**: No subsection should have >40% of total citations

### Prior Art Positioning

If closely related prior work exists, MUST:
- Acknowledge it explicitly (don't ignore competition)
- Cite accurately and fairly
- Distinguish your contribution clearly
- Show respect for prior work while identifying gaps

### Gap Synthesis

Background section SHOULD (not MUST) end with synthesis:
- Brief paragraph connecting themes
- Explicit statement of what's missing
- Transition to Framework section

**Optional Pattern:**
```latex
While these frameworks provide [X], [Y], and [Z],
they lack [gap]. Our framework addresses this by...
```

## Format Constraints

### Citations

- Use APA in-text format: `\parencite{Author2024}`
- For direct quotes (rare in Background): `\textcite{Author2024} states "..."`
- For multiple citations: `\parencite{Author2024,Other2023}`
- First mention of standard: spell out + cite (e.g., "IEEE 1012 \parencite{IEEE1012}")

### Tables

- MAY include comparison tables (e.g., comparing related frameworks)
- If used, table MUST be cited before appearance
- Use format:
```latex
\begin{table}[H]
\centering
\begin{tabular}{...}
...
\end{tabular}
\caption{Comparison of V\&V Frameworks}
\label{tab:comparison}
\end{table}
```

### Figures

- MAY include figures illustrating concepts
- Keep figures conceptual (not detailed)
- MUST cite before appearance
- Limit to 1-2 figures in Background

### Mathematical Notation

- Simple definitions acceptable (e.g., Euler characteristic χ = V - E + F)
- Avoid dense mathematical exposition
- If equations needed, keep inline when possible
- Numbered equations only if referenced later

### Quotations

- Use sparingly (paraphrase preferred)
- Only quote if specific wording matters
- Use standard LaTeX quotes: ``quoted text''
- Must include citation

## Verification Checklist

A Background section PASSES verification if:

- [ ] Section begins with `\section{Background...}` or `\section{Related Work}`
- [ ] Length is 800-2500 words
- [ ] Contains 3-6 subsections organized by theme
- [ ] Each subsection uses `\subsection{...}` heading
- [ ] Subsections are thematic, not chronological
- [ ] At least 10 unique citations total
- [ ] Every subsection has at least 2 citations
- [ ] No subsection exceeds 30% of Background length
- [ ] Foundational concepts are defined with citations
- [ ] Related work is acknowledged fairly
- [ ] No straw man misrepresentations
- [ ] Technical terms used later are defined here
- [ ] If tables included, they are cited before appearance
- [ ] If figures included, they are cited before appearance
- [ ] Citations use proper APA format
- [ ] No orphaned content (everything connects to paper)

## Anti-Patterns to Detect

The following indicate FAILED verification:

- ❌ Chronological organization ("In 1980... In 1990... In 2000...")
- ❌ Literature dump without synthesis
- ❌ Missing citations in subsections
- ❌ Single subsection > 800 words (should be split)
- ❌ Extensive quotations instead of paraphrase
- ❌ Tutorial-style textbook exposition
- ❌ Ignoring closely related prior work
- ❌ Background longer than contribution sections
- ❌ Undefined technical jargon
- ❌ Citations without context (drive-by citing)

## Schema Definition

```yaml
background_section:
  type: object
  required:
    - section_heading
    - subsection_count
    - word_count
    - citations
    - thematic_organization
  properties:
    section_heading:
      type: string
      pattern: "^\\\\section\\{(Background|Related Work|Background and Related Work)\\}$"
    subsection_count:
      type: integer
      minimum: 3
      maximum: 6
    word_count:
      type: integer
      minimum: 800
      maximum: 2500
    citations:
      type: object
      required: [total, per_subsection]
      properties:
        total:
          type: integer
          minimum: 10
        per_subsection:
          type: array
          items:
            type: integer
            minimum: 2
    thematic_organization:
      type: boolean
      description: Subsections organized by theme, not chronology
    tables:
      type: integer
      maximum: 2
      description: Number of comparison tables
    figures:
      type: integer
      maximum: 2
      description: Number of figures
    orphaned_content:
      type: boolean
      description: All content connects to paper (false = pass)
    straw_man_arguments:
      type: boolean
      description: Prior work misrepresented (true = fail)
```

---

**Note:** This specification enables precise verification of Background sections, ensuring proper contextualization without overwhelming the contribution. Designed to work with [guidance-for-background-section](guidance-for-background-section.md) for complete V&V.
