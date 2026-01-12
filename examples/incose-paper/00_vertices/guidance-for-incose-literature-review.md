---
type: vertex/guidance
extends: doc
id: v:guidance:incose-literature-review
name: Guidance for INCOSE Literature Review Documents
description: Quality criteria and best practices for creating excellent literature reviews supporting INCOSE papers
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-30T19:00:00Z
modified: 2025-12-30T19:00:00Z
dependencies: []
---

# Guidance for INCOSE Literature Review Documents

**This guidance defines quality criteria and best practices for creating excellent literature review documents that support INCOSE paper submissions.**

## Purpose

While spec-for-incose-literature-review defines what structural elements must be present, this guidance helps authors assess **how well** a literature review serves its purpose. Great literature reviews are comprehensive, well-synthesized, appropriately scoped, and effectively position the target paper within the scholarly landscape.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating literature review documents by providing:
- Quality assessment criteria for scholarly source selection
- Best practices for synthesizing and organizing literature
- Guidelines for identifying meaningful gaps
- Section-by-section authoring recommendations
- Workflow for literature review development

### Best Use Cases

Use this guidance when:
- Creating a literature review to support an INCOSE paper submission
- Reviewing existing literature reviews for quality and completeness
- Teaching others how to conduct systematic literature reviews
- Evaluating whether a literature review adequately supports a paper's claims
- Establishing literature review standards for a research team

## Quality Criteria

### 1. Source Quality

**Excellent:**
- Majority of sources are peer-reviewed publications
- Includes foundational/seminal works in the field
- Standards and handbooks from authoritative bodies (IEEE, ISO, INCOSE)
- Recent sources (within 5 years) balanced with classics
- Sources from multiple research groups/perspectives
- No reliance on questionable or predatory publications

**Good:**
- Most sources peer-reviewed or authoritative
- Some foundational works included
- Reasonable recency
- Multiple perspectives represented

**Needs Improvement:**
- Heavy reliance on non-peer-reviewed sources
- Missing foundational works
- Outdated sources without justification
- Single perspective or research group dominates
- Includes questionable sources

### 2. Relevance and Scope

**Excellent:**
- Every source has clear, explicit connection to target paper
- Scope is appropriate—neither too broad nor too narrow
- Boundaries clearly defined and justified
- No tangential sources included just to pad count
- Missing obvious relevant sources would be hard to identify

**Good:**
- Most sources clearly relevant
- Scope generally appropriate
- Some boundary definition
- Few tangential inclusions

**Needs Improvement:**
- Sources included without clear relevance
- Scope too broad (unfocused) or too narrow (missing context)
- No boundary definition
- Obvious gaps in coverage
- Padding with marginally relevant sources

### 3. Synthesis Quality

**Excellent:**
- Themes emerge naturally from sources, not forced
- Summaries identify patterns, trends, and debates
- Sources are compared and contrasted, not just listed
- Connections between sources are explicit
- Reader gains understanding beyond what individual sources provide
- Critical assessment of source limitations

**Good:**
- Reasonable thematic organization
- Some synthesis in summaries
- Occasional comparison between sources
- Generally coherent narrative

**Needs Improvement:**
- Themes feel arbitrary or forced
- Summaries are just lists, not synthesis
- Sources presented in isolation
- No critical assessment
- Reader learns nothing beyond reading individual abstracts

### 4. Gap Identification

**Excellent:**
- Gaps are genuinely missing elements, not just "more research needed"
- Gaps directly connect to target paper's contribution
- Evidence from literature supports gap claims
- Gaps are specific and actionable
- Positioning statement is compelling and well-supported

**Good:**
- Reasonable gaps identified
- Connection to target paper clear
- Some supporting evidence
- Positioning understandable

**Needs Improvement:**
- Vague gaps ("more research needed")
- Gaps don't connect to target paper
- No evidence for gap claims
- Positioning feels forced or unsupported
- Gaps are strawmen easily knocked down

### 5. Citation Completeness

**Excellent:**
- All sources mentioned have full citations
- Citation format is consistent throughout
- Access information (DOI, URL) provided where available
- Categories are logical and help navigation
- No broken or incomplete citations
- Easy to locate any cited source

**Good:**
- Most citations complete
- Generally consistent format
- Some access information
- Reasonable categorization

**Needs Improvement:**
- Missing or incomplete citations
- Inconsistent formatting
- No access information
- Poor or no categorization
- Difficult to locate cited sources

### 6. Currency and Balance

**Excellent:**
- Includes recent work (within 2-3 years)
- Foundational works included regardless of age
- Emerging trends identified
- Multiple viewpoints on contested topics
- Historical context provided where relevant
- No obvious bias toward particular school of thought

**Good:**
- Reasonably current
- Some foundational works
- Major viewpoints represented
- Generally balanced

**Needs Improvement:**
- Outdated without justification
- Missing foundational works
- Single viewpoint dominates
- Obvious bias
- Ignores recent developments

### 7. Practical Utility

**Excellent:**
- Directly usable for writing target paper's background section
- Citation IDs match recommended paper citation style
- Clear which sources support which claims
- Suggested citation format provided
- Easy to extract citations for paper

**Good:**
- Generally useful for paper writing
- Citations accessible
- Reasonable organization for extraction

**Needs Improvement:**
- Not organized for paper writing use
- Citation format doesn't match target venue
- Unclear how to use for paper
- Difficult to extract needed information

## Section-by-Section Guidance

### Introduction / Scope

**Purpose:** Orient reader and establish boundaries

**Tips:**
- State the target paper explicitly in first paragraph
- Define what's included AND what's excluded
- Explain organizational structure (themes)
- Keep to 2-3 paragraphs maximum
- Connect to target paper's contribution

**Anti-patterns:**
- Starting with generic statements about importance of literature reviews
- Not naming the target paper
- Unclear boundaries
- No preview of organization

**Example opening:**
> "This literature review supports the INCOSE IS 2026 paper 'Test-Driven Document Development' by gathering sources on verification and validation, simplicial complexes, and AI accountability. The review covers peer-reviewed publications, IEEE/ISO standards, and authoritative handbooks from 1979-2024, organized into four thematic categories that map to the paper's Background section."

### Thematic Categories

**Purpose:** Organize sources into meaningful groups

**Tips:**
- Let themes emerge from sources, don't force sources into pre-defined categories
- Each theme should map to a section or argument in target paper
- 3-5 themes is typical; 2 is minimum, >7 may indicate poor scoping
- Theme names should be descriptive and specific
- Brief introduction (2-3 sentences) explains why theme matters

**For Key Sources Tables:**
- Include 3-8 sources per theme (fewer for narrow topics, more for broad)
- "Key Contribution" should be specific, not generic ("studied verification")
- "Relevance" explains connection to YOUR paper, not general importance
- Order by importance or chronologically, not randomly

**For Summaries:**
- Synthesize, don't summarize—what patterns emerge across sources?
- Identify agreements, debates, trends
- Connect to target paper's argument
- 3-5 sentences typical

**Anti-patterns:**
- Themes that don't connect to target paper
- "Key Contribution" that's just the title restated
- "Relevance" that's generic ("important work")
- Summaries that list sources again instead of synthesizing

### Citation Catalog

**Purpose:** Provide complete, findable references

**Tips:**
- Use consistent citation format (AMA or IEEE recommended for INCOSE)
- Include DOI or URL for every source where available
- Categorize by type: Primary Research, Standards, Books, Web Resources
- Use citation IDs that match how you'll cite in paper
- Alphabetize within categories

**Format Recommendation (AMA-style):**
```
[Boehm-1984] Boehm BW. Verifying and validating software requirements
  and design specifications. IEEE Software. 1984;1(1):75-88.
  doi:10.1109/MS.1984.233702
```

**Anti-patterns:**
- Inconsistent formats (some APA, some MLA)
- Missing access information
- No categorization (one long list)
- Citation IDs that are hard to use
- Sources in body not appearing in catalog

### Gap Analysis

**Purpose:** Justify target paper's contribution

**Tips:**
- Gaps should be specific ("no framework couples V&V with human accountability")
- Support gap claims with evidence ("none of the 15 V&V frameworks reviewed...")
- Connect each gap to a specific contribution of target paper
- Positioning statement should be confident but not overclaiming
- 2-4 gaps is typical

**Strong Gap Examples:**
- "Existing V&V frameworks (IEEE 1012, ISO 15288) treat verification and validation as separate activities without formal coupling mechanisms."
- "No prior work provides explicit human accountability attribution for validation judgments in AI-assisted documentation."

**Weak Gap Examples:**
- "More research is needed in this area."
- "No one has studied this exact combination before."
- "The literature is incomplete."

**Anti-patterns:**
- Vague gaps that could apply to any paper
- Overclaiming ("no one has ever considered...")
- Gaps that don't connect to paper's contribution
- No evidence supporting gap claims

## Workflow Guidance

### Recommended Authoring Sequence

1. **Define Scope** (30-45 min)
   - Identify target paper and its key topics
   - List 5-10 search terms per topic
   - Define date range and source types
   - Document inclusion/exclusion criteria

2. **Gather Sources** (2-4 hours)
   - Search academic databases (IEEE Xplore, ACM DL, Google Scholar)
   - Search standards bodies (IEEE, ISO, INCOSE)
   - Follow citation chains (who cites foundational works?)
   - Aim for 15-25 sources total (varies by topic breadth)

3. **Read and Annotate** (3-5 hours)
   - For each source: key contribution, relevance to your paper
   - Note connections between sources
   - Identify emerging themes
   - Flag foundational vs. supporting sources

4. **Organize Themes** (1-2 hours)
   - Group sources into 3-5 themes
   - Write theme introductions
   - Create Key Sources tables
   - Draft synthesis summaries

5. **Build Citation Catalog** (1 hour)
   - Format all citations consistently
   - Categorize by type
   - Add DOIs/URLs
   - Verify completeness

6. **Analyze Gaps** (1 hour)
   - Identify what's missing from literature
   - Connect gaps to your paper's contribution
   - Write positioning statement
   - Ensure evidence supports claims

7. **Review and Refine** (1 hour)
   - Check all sources appear in catalog
   - Verify relevance claims
   - Ensure synthesis quality
   - Polish writing

**Total estimated time:** 10-15 hours for comprehensive literature review

### Quality Checkpoints

- **After step 2:** Do you have sources for each major topic in target paper?
- **After step 4:** Do themes map clearly to paper sections?
- **After step 5:** Can you find full citation for every source mentioned?
- **After step 6:** Are gaps specific and well-supported?
- **After step 7:** Would this help someone write the Background section?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Padding** | Including marginally relevant sources to increase count | Every source needs explicit relevance; remove if can't articulate connection |
| **List-itis** | Summaries that just list sources | Synthesize: what patterns, debates, trends emerge? |
| **Vague Gaps** | "More research needed" | Specify: "No framework does X" with evidence |
| **Inconsistent Citations** | Mix of APA, MLA, informal | Choose one format (AMA/IEEE) and apply consistently |
| **Missing Foundations** | Recent sources but no classics | Include seminal works (Boehm, INCOSE Handbook) |
| **Single Perspective** | All sources from one group | Actively seek alternative viewpoints |
| **Broken Chain** | Sources in body not in catalog | Cross-check all mentions against catalog |
| **Forced Themes** | Categories don't fit sources | Let themes emerge from reading, not pre-defined |

## Best Practices

1. **Start with Seminal Works** - Identify the 3-5 foundational sources in your area first
2. **Follow Citation Chains** - Who cites the foundational works? Who do recent papers cite?
3. **Include Standards** - IEEE, ISO, INCOSE standards are authoritative and often overlooked
4. **Be Specific in Relevance** - "Relevant" is not enough; explain HOW it connects to YOUR paper
5. **Synthesize, Don't Summarize** - Your value-add is finding patterns across sources
6. **Support Gap Claims** - "No one does X" requires evidence you've looked
7. **Match Target Venue Format** - Use citation style your paper will use
8. **Keep It Current** - Include sources from last 2-3 years
9. **Acknowledge Limitations** - Note what your review doesn't cover
10. **Make It Usable** - Organize for easy extraction when writing paper

## Validation vs. Verification

**Verification** (deterministic, against spec-for-incose-literature-review):
- Are all required sections present?
- Are there at least 2 thematic categories?
- Does citation count match actual sources?
- Is gap analysis present?

**Validation** (qualitative, against this guidance):
- Are sources high-quality and appropriate?
- Is scope well-defined and relevant?
- Is synthesis insightful, not just listing?
- Are gaps specific and well-supported?
- Are citations complete and consistent?
- Is the review balanced and current?
- Is it practically useful for writing the paper?

This guidance document supports **validation** - assessing fitness-for-purpose.

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

- **Source Quality:** References authoritative sources (spec-for-incose-literature-review)
- **Relevance:** All content directly supports literature review creation
- **Synthesis Quality:** Best practices are synthesized from multiple perspectives
- **Gap Identification:** Clearly states what this guidance addresses
- **Citation Completeness:** References spec and provides examples
- **Currency and Balance:** Incorporates modern practices (DOIs, databases)
- **Practical Utility:** Organized for use during literature review creation

## Examples

| Literature Review | Target Paper | Themes | Citation Count |
|-------------------|--------------|--------|----------------|
| Architecture Layers & V-Model | INCOSE IS 2026 Paper | V&V Foundations, Simplicial Complexes, TDD, AI Accountability | ~17 |

## Tooling Support

### Verification Commands

```bash
# Verify literature review structure against spec
python scripts/verify_template_based.py 00_vertices/literature-review-*.md --templates templates
```

### Useful Resources

- **IEEE Xplore:** ieeexplore.ieee.org
- **ACM Digital Library:** dl.acm.org
- **Google Scholar:** scholar.google.com
- **SEBoK:** sebokwiki.org
- **INCOSE:** incose.org/publications

## Document Metadata

| Property | Value |
|----------|-------|
| Specification | [[spec-for-incose-literature-review]] |
| Guidance Version | 1.0.0 |
| Specification Version | 1.0.0 |
| Terminology | VERIFICATION = structural compliance; VALIDATION = quality assessment |
| Target Users | Researchers preparing INCOSE paper submissions |

---

**Note:** This guidance is coupled with [[spec-for-incose-literature-review]] via a coupling edge, supporting the assurance of literature review artifacts within the typed simplicial complex framework.
