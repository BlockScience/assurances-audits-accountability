---
type: vertex/spec
extends: doc
id: v:spec:incose-paper
name: Specification for INCOSE IS 2026 Research Paper
description: Defines structural requirements for an INCOSE International Symposium 2026 research paper submission
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-30T10:00:00Z
modified: 2025-12-30T10:00:00Z
dependencies: []
---

# Specification for INCOSE IS 2026 Research Paper

## Purpose Statement

This specification defines the structural requirements for a research paper submission to the INCOSE International Symposium 2026 (Yokohama, Japan, June 13-18, 2026). The spec captures mandatory constraints from the official Call for Submissions, ensuring any conforming document meets minimum submission requirements.

## Structural Requirements

### Document Constraints

| Constraint | Requirement | Source |
|------------|-------------|--------|
| Word Limit | MUST NOT exceed 7,000 words | INCOSE Call for Papers |
| Template | MUST use official INCOSE Paper Template | INCOSE Call for Papers |
| Originality | MUST be original work not previously published | INCOSE Call for Papers |
| Category | MUST be either Research Paper or Practice Paper | INCOSE Call for Papers |

### Required Sections

All INCOSE research papers MUST include the following sections in order:

| Section | Requirement | Notes |
|---------|-------------|-------|
| Title | REQUIRED | Descriptive, relevant to SE community |
| Author Information | REQUIRED | Name, affiliation, contact |
| Abstract | REQUIRED | Summary of problem, approach, results |
| Introduction | REQUIRED | SE challenge, context, paper structure |
| Body Sections | REQUIRED | Methodology, results, discussion |
| Conclusion | REQUIRED | Summary, contribution, future work |
| Acknowledgments | REQUIRED | Including AI disclosure statement |
| References | REQUIRED | Properly formatted citations |

### Body Section Requirements

For **Research Papers**, the body MUST include:

1. **Background/Related Work** - Literature context, prior art
2. **Methodology/Approach** - Clear assumptions, methods, research procedures
3. **Results** - Theory development, testing, validation
4. **Discussion** - Interpretation, limitations, implications

For **Practice Papers**, the body MUST include:

1. **Problem Space** - Context and assumptions
2. **Approach** - Implementation methodology
3. **Results** - Outcomes and findings
4. **Lessons Learned** - Practical insights

### AI Assistance Disclosure

Per INCOSE 2026 requirements, any paper using AI assistance MUST include an AI disclosure statement covering:

| Element | Requirement |
|---------|-------------|
| Tools Used | MUST list specific AI tools (e.g., ChatGPT, Claude, Grammarly) |
| Usage Category | MUST specify: conceptual, analysis, content generation, or editorial |
| Author Oversight | MUST describe level of human involvement and oversight |
| Intellectual Contribution | For content generation: MUST detail author's intellectual contributions |

**Placement:** Acknowledgments section or footnote.

**Non-compliance:** Submissions without proper AI disclosure may be rejected before review.

## Format Constraints

### Word Count Rules

| Element | Counted in 7,000 limit |
|---------|------------------------|
| Title | No |
| Abstract | Yes |
| Body text | Yes |
| Figure captions | Yes |
| Table content | Yes |
| Acknowledgments | Yes |
| References | No |

### Document Format

| Property | Requirement |
|----------|-------------|
| File Format | Per INCOSE template (typically Word/PDF) |
| Font | Per INCOSE template |
| Margins | Per INCOSE template |
| Heading Styles | Per INCOSE template |
| Citation Style | Per INCOSE template |

### Figures and Tables

| Property | Requirement |
|----------|-------------|
| Resolution | Sufficient for print publication |
| Captions | MUST be descriptive |
| Numbering | Sequential (Figure 1, Table 1, etc.) |
| Placement | Near first reference in text |

## Schema Definition

### Paper Metadata Schema

```yaml
# INCOSE Paper Metadata
title: <string, max 150 characters>
authors:
  - name: <string>
    affiliation: <string>
    email: <string>
    corresponding: <boolean>
category: research | practice
keywords:
  - <string>  # 3-6 keywords
abstract: <string, typically 150-300 words>
word_count: <integer, max 7000>
ai_disclosure:
  tools_used: [<string>]
  usage_categories: [conceptual | analysis | content_generation | editorial]
  author_oversight: <string>
  intellectual_contribution: <string>  # Required if content_generation used
```

### Section Schema

```yaml
sections:
  - title:
      required: true
  - abstract:
      required: true
      max_words: 300
  - introduction:
      required: true
      includes: [se_challenge, context, paper_structure]
  - background:
      required: true
      type: research | practice
  - methodology:
      required: true
  - results:
      required: true
  - discussion:
      required: true
  - conclusion:
      required: true
      includes: [summary, contribution, future_work]
  - acknowledgments:
      required: true
      includes: [ai_disclosure]
  - references:
      required: true
      min_count: 10
```

## Content Requirements

### SE Challenge Statement

The paper MUST clearly articulate:

1. The systems engineering challenge being addressed
2. Why this challenge is important to the SE community
3. How the contents contribute to attaining a solution

### Writing Style Requirements

| Criterion | Requirement |
|-----------|-------------|
| Accessibility | MUST be readable by novice to expert SE practitioners |
| Clarity | MUST avoid unnecessary jargon or define terms used |
| Focus | MUST clearly state contribution to SE practice |

### Theme Alignment (IS 2026)

Papers are ENCOURAGED (not required) to connect to the 2026 theme:

**"Beyond Digital Engineering: Seeking Wa in SE"**

Theme elements:
- Human-AI collaboration and harmony
- Human Systems Integration (HSI)
- Balance of technology and human creativity
- Nature-harmonized approaches

## Encouraged Topics

Papers on the following topics are actively encouraged:

- Systems Thinking
- Continuous Delivery
- Managing System Complexity
- Agile SE
- Energy Transformation
- Mission Engineering
- Emergency Management
- New Innovative Approaches
- Systems Science Foundations

## Validation Rules

A document claiming conformance to this specification is valid if:

1. Word count is at or below 7,000 words
2. All required sections are present
3. AI disclosure statement is included (if AI was used)
4. Document uses official INCOSE template format
5. Content is original and unpublished
6. SE challenge is clearly stated
7. Author information is complete

## Submission Requirements

| Property | Value |
|----------|-------|
| Submission Deadline | 2 January 2026 |
| Notification | 16 March 2026 |
| Final Paper Due | 16 May 2026 |
| Presentation | In-person only (Yokohama, Japan) |
| Registration | Required for accepted paper presenters |

## Example AI Disclosure Statement

```
AI Assistance Disclosure: Claude (Claude Opus 4.5) assisted with content
generation for drafting methodology sections and creating the assurance
framework documentation. All research design, framework architecture,
validation methodology, and conclusions are original author work. The
paper's central demonstration (using the framework to write itself) was
conceived and directed by the author. Claude also provided editorial
support for grammar and clarity. The author maintained oversight of all
AI-assisted work and made final editorial decisions.
```

## Compliance

A document claiming `type: vertex/doc` with target specification `v:spec:incose-paper` is compliant if and only if:

1. All REQUIRED sections are present
2. Word count constraint is satisfied
3. AI disclosure is present and complete (if AI was used)
4. Content requirements are met
5. INCOSE template format is used

---

**Note:** This specification is derived from the INCOSE IS 2026 Call for Submissions. It captures structural requirements that can be deterministically verified. Quality assessment (how well the paper achieves its goals) is covered in the corresponding guidance document.
