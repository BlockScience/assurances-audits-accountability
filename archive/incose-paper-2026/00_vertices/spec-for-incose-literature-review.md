---
type: vertex/spec
extends: doc
id: v:spec:incose-literature-review
name: Specification for INCOSE Literature Review Documents
description: Defines structural requirements for literature review documents supporting INCOSE paper submissions
tags:
  - vertex
  - doc
  - spec
version: 1.0.0
created: 2025-12-30T19:00:00Z
modified: 2025-12-30T19:00:00Z
dependencies: []
---

# Specification for INCOSE Literature Review Documents

**This specification defines the structure and requirements for literature review documents that support INCOSE paper submissions by organizing citations, summarizing sources, and establishing scholarly context.**

## Purpose

Literature review documents serve as structured research artifacts that gather, organize, and synthesize scholarly sources relevant to an INCOSE paper. They capture citations, key findings, and relationships between sources, enabling authors to build on existing work and position their contributions within the field. This spec establishes what fields, sections, and properties must be present in any valid literature review document.

## Required Frontmatter Fields

All literature review documents MUST include the following YAML frontmatter:

### Core Identification

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `type` | string | REQUIRED | Must be `vertex/doc` |
| `extends` | string | REQUIRED | Must be `doc` |
| `id` | string | REQUIRED | Unique identifier (format: `v:doc:literature-review-<topic>`) |
| `name` | string | REQUIRED | Human-readable document name |
| `tags` | array[string] | REQUIRED | Must include `[vertex, doc, literature-review]` |
| `version` | string | REQUIRED | Semantic version (e.g., `1.0.0`) |

### Timestamps

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `created` | datetime | REQUIRED | ISO 8601 creation timestamp |
| `modified` | datetime | REQUIRED | ISO 8601 last modification timestamp |

### Literature Review Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `topic` | string | REQUIRED | Primary topic of the literature review |
| `target_paper` | string | REQUIRED | ID or name of the paper this review supports |
| `citation_count` | integer | REQUIRED | Total number of citations included |
| `theme_count` | integer | REQUIRED | Number of thematic categories (must be ≥2) |

### Optional Metadata

| Field | Type | Requirement | Description |
|-------|------|-------------|-------------|
| `description` | string | RECOMMENDED | Brief description of review scope |
| `search_strategy` | string | RECOMMENDED | How sources were identified |
| `date_range` | string | OPTIONAL | Publication date range covered |
| `databases_searched` | array[string] | OPTIONAL | Databases or sources consulted |

## Required Body Sections

The markdown body of a literature review document MUST contain:

### 1. Introduction / Scope

A clear statement of what this literature review covers and why.

**Format:**
```markdown
## Introduction

[1-2 paragraphs explaining:
- What topic(s) this review covers
- Why these sources are relevant to the target paper
- How the review is organized]
```

**Requirements:**
- MUST state the target paper being supported
- MUST explain the scope boundaries (what's included/excluded)
- MUST preview the organizational structure

### 2. Thematic Categories

Organization of sources into thematic groups (minimum 2 themes).

**Format:**
```markdown
## Theme N: [Theme Name]

[Brief introduction to why this theme is relevant]

### Key Sources

| Citation | Year | Key Contribution | Relevance |
|----------|------|------------------|-----------|
| [Author] | [Year] | [What they contributed] | [Why it matters for target paper] |

### Summary

[2-4 sentences synthesizing this theme's contribution to the paper]
```

**Requirements:**
- MUST include at least 2 thematic categories
- Each theme MUST have a Key Sources table
- Each theme MUST have a Summary synthesizing the sources
- Table MUST include: Citation, Year, Key Contribution, Relevance columns

### 3. Citation Catalog

Complete list of all citations in standard format.

**Format:**
```markdown
## Citation Catalog

### Primary Sources

| ID | Full Citation | Type | Access |
|----|---------------|------|--------|
| [ID] | [Full citation in consistent format] | [Type] | [URL or DOI if available] |

### Standards and Handbooks

| ID | Full Citation | Type | Access |
|----|---------------|------|--------|
| [ID] | [Full citation] | [standard/handbook] | [URL] |
```

**Requirements:**
- MUST list all sources cited in the document
- MUST use consistent citation format (recommend AMA or IEEE style)
- MUST categorize sources (Primary, Standards, Books, etc.)
- SHOULD include access information (URL, DOI) where available

### 4. Gap Analysis

Identification of gaps in existing literature that the target paper addresses.

**Format:**
```markdown
## Gap Analysis

### Identified Gaps

| Gap | Current State | How Target Paper Addresses |
|-----|---------------|---------------------------|
| [Gap description] | [What literature says/doesn't say] | [Paper's contribution] |

### Positioning Statement

[2-3 sentences stating how the target paper positions itself relative to existing work]
```

**Requirements:**
- MUST identify at least 1 gap in existing literature
- MUST explain how target paper addresses each gap
- MUST include positioning statement

## Optional Body Sections

### Search Methodology

Documents how sources were found.

**Format:**
```markdown
## Search Methodology

**Databases:** [List of databases searched]
**Search Terms:** [Key terms used]
**Date Range:** [Publication years covered]
**Inclusion Criteria:** [What qualified a source]
**Exclusion Criteria:** [What disqualified a source]
```

### Source Relationships

Maps how sources relate to each other.

**Format:**
```markdown
## Source Relationships

[Description or diagram showing how sources build on each other]

| Source | Builds On | Extended By |
|--------|-----------|-------------|
| [Source] | [Prior work] | [Later work] |
```

### Recommended Citation Format

Suggests how to cite sources in the target paper.

**Format:**
```markdown
## Recommended Citation Format

For the target paper, use [format name] style:

**Example:**
[Author]. [Title]. [Publication]. [Year];[Volume]:[Pages]. [DOI]
```

## Type Constraints

1. **Type Field:** MUST be exactly `vertex/doc`
2. **Extends Field:** MUST be exactly `doc`
3. **ID Format:** MUST match pattern `v:doc:literature-review-[kebab-case-topic]`
4. **Tag Requirement:** Tags MUST include `literature-review`

## Content Requirements

1. **Scholarly Focus:** Sources should be peer-reviewed, standards, or authoritative references
2. **Relevance:** Every source must have explicit connection to target paper
3. **Currency:** Include recent sources (within 5-10 years) unless foundational
4. **Balance:** Cover multiple perspectives where relevant debates exist
5. **Synthesis:** Not just lists—must synthesize and analyze sources

## Coupling Requirement

Every literature review document SHOULD be verified against this spec and validated against the corresponding `guidance-for-incose-literature-review` document via appropriate edges. The guidance defines how to evaluate quality and fitness-for-purpose for literature review documents.

## Verification vs. Validation

- **Verification** (against this spec): Deterministic checking that all required sections, themes, and citation catalog are present
- **Validation** (against guidance): Qualitative assessment that sources are appropriate, synthesis is insightful, and gaps are meaningful

## Schema Summary

```yaml
# Required frontmatter
type: vertex/doc
extends: doc
id: v:doc:literature-review-<topic>
name: <string>
tags: [vertex, doc, literature-review]
version: <semver>
created: <ISO8601>
modified: <ISO8601>
topic: <string>
target_paper: <string>
citation_count: <integer>
theme_count: <integer ≥2>

# Optional frontmatter
description: <string>
search_strategy: <string>
date_range: <string>
databases_searched: [<strings>]

# Required body sections (markdown)
## Introduction
## Theme 1: [Name]
  - Key Sources table
  - Summary
## Theme 2: [Name]
  - Key Sources table
  - Summary
## [Additional Themes...]
## Citation Catalog
  - Categorized tables with full citations
## Gap Analysis
  - Identified Gaps table
  - Positioning Statement

# Optional body sections
## Search Methodology
## Source Relationships
## Recommended Citation Format
```

## Compliance

A document claiming to be a literature review document is compliant with this specification if and only if:

1. All REQUIRED frontmatter fields are present and correctly typed
2. All REQUIRED body sections are present with required subsections
3. At least 2 thematic categories with Key Sources tables and Summaries
4. Citation Catalog includes all referenced sources
5. Gap Analysis identifies at least 1 gap with positioning statement
6. Type constraints are satisfied
7. Citation count matches actual number of sources

---

**Note:** This specification supports the creation of literature review artifacts that can be assured within the typed simplicial complex framework, enabling traceable scholarly foundations for INCOSE papers.
