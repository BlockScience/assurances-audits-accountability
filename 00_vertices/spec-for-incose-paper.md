---
type: vertex/spec
extends: doc
id: v:spec:incose-paper
name: Specification for INCOSE IS 2026 Research Paper
description: Comprehensive structural requirements for an INCOSE International Symposium 2026 research paper submission, derived from official Call for Submissions and INCOSE publication standards
tags:
  - vertex
  - doc
  - spec
version: 2.0.0
created: 2025-12-30T10:00:00Z
modified: 2025-12-30T18:00:00Z
dependencies: []
---

# Specification for INCOSE IS 2026 Research Paper

## Purpose

This specification defines the complete structural requirements for a research or practice paper submission to the 36th Annual INCOSE International Symposium (Yokohama, Japan, June 13-18, 2026). The spec captures all mandatory constraints from the official Call for Submissions, INCOSE Paper Preparation Guidelines, and Paper Evaluation Criteria documents, ensuring any conforming document meets minimum submission requirements for double-blind peer review.

This specification addresses **verification** concerns: deterministic, objective checks that can confirm structural compliance. Quality assessment (how well the paper achieves its goals) is covered in the corresponding guidance document.

---

## Document Classification

### Submission Categories

This specification covers two paper categories. Documents MUST declare their category:

| Category | Description | Publication Venue |
|----------|-------------|-------------------|
| **Research Paper** | Novel contribution advancing state-of-the-art through original research; articulates assumptions, methods, research procedures; presents rigorous approach to theory development, testing, and validation | Proceedings + INCOSE Website + Wiley Online Library |
| **Practice Paper** | Indicates problem space, assumptions, and approach through implementation; covers full scope of problem and solution; may present research proposals with initial results | Proceedings + INCOSE Website + Wiley Online Library |

**Note:** This specification does NOT cover paperless presentations (1,000-word extended abstracts), panels, or tutorials, which have distinct requirements.

---

## Structural Requirements

### Document Constraints

| Constraint | Requirement | Enforcement | Source |
|------------|-------------|-------------|--------|
| Word Limit | MUST NOT exceed **7,000 words** | REQUIRED | IS 2026 Call for Papers |
| Page Limit | SHOULD NOT exceed **15 pages** (including abstract, illustrations, appendices, biography) | RECOMMENDED | INCOSE Paper Preparation Guidelines |
| Template | MUST use official **INCOSE Paper Template** | REQUIRED | IS 2026 Call for Papers |
| File Format | MUST be submitted as **PDF** | REQUIRED | EasyChair Submission Requirements |
| Originality | MUST be **original work not previously published** | REQUIRED | IS 2026 Call for Papers |
| Language | MUST be written in **English** | REQUIRED | INCOSE Submission Requirements |
| Draft Quality | MUST be **close-to-final draft** (abstracts/outlines NOT acceptable) | REQUIRED | INCOSE Paper Preparation Guidelines |
| Plagiarism | MUST NOT contain plagiarized content; all sources MUST be properly cited | REQUIRED | INCOSE Publication Policy |

### Template Format Requirements

| Property | Requirement | Source |
|----------|-------------|--------|
| Column Format | **Single column** (except author section for multiple authors) | INCOSE Template |
| Hyphenation | **Enabled** for body text (DO NOT change settings) | INCOSE Template |
| Margins | **Pre-set** for identical pagination on US Letter and A4 (DO NOT change) | INCOSE Template |
| Title Formatting | **Centered** on first page with **title capitalization** | INCOSE Template |
| Author Section | **Centered** below title with name, organization, mailing address in **mixed case** | INCOSE Template |
| Email Formatting | **Arial Narrow** font, formatted as **hyperlinks** | INCOSE Template |
| Heading Styles | Use **Heading 1** style for main headings | INCOSE Template |

---

## Required Sections

All INCOSE papers MUST include the following sections. The order presented is the required sequence:

### Section Inventory

| # | Section | Requirement | Typical Length | Notes |
|---|---------|-------------|----------------|-------|
| 1 | Title | REQUIRED | 8-15 words | Descriptive, relevant to SE community |
| 2 | Author Information | REQUIRED (final only) | Per author | OMIT for anonymous submission |
| 3 | Abstract | REQUIRED | 150-300 words | Preceded by "Abstract" as SubHeading |
| 4 | Introduction | REQUIRED | 1-2 pages | SE challenge, context, paper structure |
| 5 | Background/Related Work | REQUIRED | 1-2 pages | Literature context, gap identification |
| 6 | Methodology/Approach | REQUIRED | 2-3 pages | Clear assumptions, methods, procedures |
| 7 | Results | REQUIRED | 2-3 pages | Findings, evidence, validation |
| 8 | Discussion | REQUIRED | 1-2 pages | Interpretation, limitations, implications |
| 9 | Conclusion | REQUIRED | 0.5-1 page | Summary, contribution, future work |
| 10 | Acknowledgments | REQUIRED | 0.25-0.5 page | Including AI disclosure statement |
| 11 | References | REQUIRED | 1-2 pages | Minimum 10 references RECOMMENDED |
| 12 | Author Biography | REQUIRED (final only) | 50-100 words/author | OMIT for anonymous submission |

### Section-Specific Requirements

#### 1. Title

| Property | Requirement |
|----------|-------------|
| Placement | First line of document, centered |
| Capitalization | Title case |
| Length | SHOULD be 8-15 words |
| Content | MUST be descriptive of SE contribution |
| Anonymization | Title MAY remain in anonymous submission |

#### 2. Author Information

| Property | Initial Submission | Final Submission |
|----------|-------------------|------------------|
| Author Names | OMIT | REQUIRED |
| Affiliations | OMIT | REQUIRED |
| Mailing Addresses | OMIT | REQUIRED |
| Email Addresses | OMIT | REQUIRED (Arial Narrow, hyperlinked) |
| Corresponding Author | OMIT | REQUIRED (indicate which author) |

#### 3. Abstract

| Property | Requirement |
|----------|-------------|
| Heading | "Abstract" formatted as SubHeading style |
| Length | 150-300 words |
| Structure | Problem → Approach → Results → Contribution |
| Self-Contained | No references, no undefined acronyms |
| Keywords | RECOMMENDED: 3-6 keywords following abstract |

#### 4. Introduction

The introduction MUST include:

| Element | Requirement |
|---------|-------------|
| SE Challenge | MUST clearly state the systems engineering challenge being addressed |
| Importance | MUST explain why this challenge matters to SE community |
| Context | MUST establish broader SE context and trends |
| Objectives | MUST state research questions or objectives |
| Contribution Preview | MUST preview the paper's contribution |
| Roadmap | SHOULD provide section-by-section overview |

#### 5. Background/Related Work

| Element | Requirement |
|---------|-------------|
| Literature Review | MUST review relevant prior work |
| Gap Identification | MUST identify gap(s) the paper addresses |
| Positioning | MUST position contribution against alternatives |
| SE Standards | SHOULD reference relevant INCOSE/ISO standards where applicable |

#### 6. Methodology/Approach

**For Research Papers, MUST include:**

| Element | Requirement |
|---------|-------------|
| Assumptions | MUST explicitly state all assumptions |
| Methods | MUST describe research methods in reproducible detail |
| Procedures | MUST explain research procedures |
| Rationale | MUST justify methodological choices |
| Data Description | If empirical: MUST describe data sources and collection |

**For Practice Papers, MUST include:**

| Element | Requirement |
|---------|-------------|
| Problem Space | MUST define the problem context |
| Assumptions | MUST state implementation assumptions |
| Approach | MUST describe implementation methodology |
| Context | MUST explain organizational/project context |

#### 7. Results

| Element | Requirement |
|---------|-------------|
| Findings | MUST present findings clearly |
| Evidence | MUST provide evidence supporting claims |
| Figures/Tables | SHOULD use visual aids to present data |
| Validation | For research papers: MUST include theory testing/validation |
| Outcomes | For practice papers: MUST report implementation outcomes |

#### 8. Discussion

| Element | Requirement |
|---------|-------------|
| Interpretation | MUST interpret results in context of research questions |
| Implications | MUST discuss implications for SE practice |
| Limitations | MUST honestly address limitations |
| Comparison | SHOULD compare findings to related work |

#### 9. Conclusion

| Element | Requirement |
|---------|-------------|
| Summary | MUST summarize main contribution |
| Key Takeaways | MUST highlight key insights for practitioners |
| Future Work | SHOULD suggest future research directions |
| Closing | SHOULD end with forward-looking impact statement |

#### 10. Acknowledgments

| Element | Requirement |
|---------|-------------|
| Funding | MAY acknowledge funding sources (OMIT in anonymous submission) |
| Collaborators | MAY thank contributors (OMIT in anonymous submission) |
| AI Disclosure | MUST include AI Assistance Disclosure statement (see dedicated section) |

#### 11. References

| Property | Requirement |
|----------|-------------|
| Minimum Count | RECOMMENDED: At least 10 references |
| Citation Style | AMA (American Medical Association) style with superscript numerals |
| Recency | SHOULD include recent (last 5 years) references |
| SE Literature | SHOULD include relevant SE journal/symposium papers |
| Self-Citation | For anonymous submission: MUST anonymize self-references |

#### 12. Author Biography (Final Submission Only)

| Property | Requirement |
|----------|-------------|
| Length | 50-100 words per author |
| Content | Professional background and qualifications |
| Photo | MAY include headshot color photograph |
| Placement | End of paper, before or after references per template |

---

## AI Assistance Disclosure Requirements

### Mandatory Disclosure

Per INCOSE IS 2026 requirements, **all papers MUST include an AI Assistance Disclosure statement**.

> "Submissions that do not comply with this guidance may be rejected before review."

### Required Disclosure Elements

| Element | Requirement | Description |
|---------|-------------|-------------|
| Tools Used | REQUIRED | MUST list specific AI tools by name and version (e.g., "ChatGPT (GPT-4)", "Claude Opus 4.5", "Grammarly") |
| Usage Categories | REQUIRED | MUST specify one or more categories (see below) |
| Author Oversight | REQUIRED | MUST describe level of human involvement and oversight |
| Intellectual Contribution | CONDITIONALLY REQUIRED | If content_generation or conceptual use: MUST detail author's intellectual contributions |

### Usage Categories

Disclosure MUST categorize AI usage into one or more of the following:

| Category | Scope | Disclosure Detail Required |
|----------|-------|---------------------------|
| **Conceptual** | Idea generation, hypothesis development, research design | HIGH - must detail author's intellectual contribution |
| **Analysis** | Literature review, statistical support, data analysis, coding assistance | MEDIUM - describe what AI analyzed |
| **Content Generation** | Drafting sections, creating abstracts, methodology development | HIGH - must detail author's intellectual contribution and revision process |
| **Editorial** | Grammar correction, formatting, citation management, translation | LOW - simple statement sufficient |

### Disclosure Placement

- **Location:** Acknowledgments section OR footnote on first page
- **Timing:** MUST be present in BOTH anonymous and final submissions

### Disclosure Schema

```yaml
ai_disclosure:
  present: true  # REQUIRED
  tools_used:
    - name: <string>        # e.g., "Claude"
      version: <string>     # e.g., "Opus 4.5"
  usage_categories:         # At least one REQUIRED
    - conceptual: <boolean>
    - analysis: <boolean>
    - content_generation: <boolean>
    - editorial: <boolean>
  author_oversight: <string>           # REQUIRED
  intellectual_contribution: <string>  # REQUIRED if conceptual or content_generation
```

### Example AI Disclosure Statements

**Minimal (Editorial Only):**
```
AI Assistance Disclosure: Grammarly provided grammar and style corrections.
All content is original author work.
```

**Standard (Mixed Use):**
```
AI Assistance Disclosure: ChatGPT (GPT-4) assisted with grammar correction
and code generation for simulations. All analysis and conclusions are
original author work.
```

**Comprehensive (Content Generation):**
```
AI Assistance Disclosure: Claude Opus 4.5 assisted with content generation
for drafting methodology sections and creating the assurance framework
documentation. All research design, framework architecture, validation
methodology, and conclusions are original author work. The paper's central
contribution was conceived and directed by the author. Claude also provided
editorial support for grammar and clarity. The author maintained oversight
of all AI-assisted work and made final editorial decisions.
```

---

## Anonymization Requirements

### Double-Blind Review Process

INCOSE uses double-blind peer review:
- Author identity is concealed from reviewer
- Reviewer identity is concealed from author
- Goal: Remove potential bias; select papers based on merit

### Anonymization Checklist for Initial Submission

| Element | Action Required |
|---------|-----------------|
| Author names | MUST REMOVE from title page |
| Affiliations | MUST REMOVE from title page |
| Funding sources | MUST REMOVE all references |
| Participating organizations | MUST REMOVE all mentions |
| Acknowledgments | MUST REMOVE (except AI disclosure) |
| Author biographies | MUST REMOVE entirely |
| Self-citations | MUST ANONYMIZE (see below) |
| Headers/Footers | MUST NOT contain identifying information |
| Document properties | SHOULD remove author metadata from PDF |

### Self-Citation Anonymization

**Anonymous Submission Format:**
- DO NOT write: "In our previous work (Smith 2023), we showed..."
- DO write: "Prior work [Anonymous 2023] demonstrated..."
- Or: "Previous research has shown..." (omit citation)

**Final Submission Format:**
- Restore full citation information
- Include proper self-references

---

## Word Count Rules

### Elements Counted Toward 7,000 Limit

| Element | Counted | Notes |
|---------|---------|-------|
| Title | NO | |
| Author Information | NO | |
| Abstract | YES | 150-300 words typical |
| Keywords | NO | |
| All Body Sections | YES | Introduction through Conclusion |
| Figure Captions | YES | Keep concise |
| Table Content | YES | Including headers and data |
| Acknowledgments | YES | Including AI disclosure |
| References | NO | Not counted |
| Author Biography | NO | |

### Word Count Allocation Guide

| Section | Suggested Allocation | Words (of 7,000) |
|---------|---------------------|------------------|
| Abstract | 3-4% | 200-300 |
| Introduction | 12-15% | 850-1,050 |
| Background | 12-15% | 850-1,050 |
| Methodology | 20-25% | 1,400-1,750 |
| Results | 20-25% | 1,400-1,750 |
| Discussion | 12-15% | 850-1,050 |
| Conclusion | 5-8% | 350-550 |
| Acknowledgments | 2-3% | 100-200 |
| **Total** | **100%** | **≤7,000** |

---

## Figures and Tables

### Requirements

| Property | Requirement |
|----------|-------------|
| Resolution | MUST be sufficient for print publication (300 DPI minimum) |
| Numbering | MUST be sequential (Figure 1, Figure 2...; Table 1, Table 2...) |
| Captions | MUST be descriptive and self-contained |
| Placement | MUST be near first reference in text |
| References | MUST be referenced in text before appearance |
| Quantity | SHOULD be 3-5 figures for a 7,000-word paper (each must earn space) |
| Color | MAY use color; SHOULD be comprehensible in grayscale |
| Size | MUST fit within template margins |

### Caption Format

```
Figure 1. [Descriptive title]. [Additional explanation if needed].

Table 1. [Descriptive title]. [Column/row explanations if needed].
```

---

## Content Requirements

### SE Challenge Statement

The paper MUST clearly articulate:

| Element | Requirement | Location |
|---------|-------------|----------|
| Challenge Definition | MUST define the specific SE challenge | Introduction |
| Importance | MUST explain why challenge matters to SE community | Introduction |
| Contribution | MUST state how paper contributes to solving challenge | Introduction + Conclusion |
| Industry Relevance | SHOULD identify relevant industries/domains | Introduction |

### Supported Claims

| Requirement | Description |
|-------------|-------------|
| Evidence | All assertions MUST be backed by supporting data or citations |
| Appropriate Claims | Claim strength MUST match evidence strength |
| Limitations | Paper MUST acknowledge scope and limitations |

### Writing Style

| Criterion | Requirement |
|-----------|-------------|
| Accessibility | MUST be readable by novice to expert SE practitioners |
| Jargon | MUST define technical terms on first use or avoid |
| Voice | SHOULD use active voice |
| Clarity | MUST clearly state contribution to SE practice |
| Concision | SHOULD be concise without sacrificing clarity |

---

## Theme Alignment

### IS 2026 Theme: "Beyond Digital Engineering: Seeking Wa in SE"

**[Wa] (和) - Harmony**

Papers are ENCOURAGED (not REQUIRED) to connect to the 2026 theme.

### Theme Elements

| Element | Description |
|---------|-------------|
| **Wa (Harmony)** | Japanese concept of dynamic balance and mutual respect |
| **Human-AI Collaboration** | Integration of AI with human creativity and judgment |
| **Kansei (感性)** | Human sensibility, emotional/affective engineering |
| **Human Systems Integration** | Sociotechnical approach ensuring human elements addressed |
| **Digital Engineering Evolution** | Moving beyond DE to human-centric approaches |
| **Nature-Harmonized Design** | Systems in harmony with natural and social systems |

### Encouraged Topics

Papers on the following topics are actively encouraged:

| Core Topics | Alignment Topics |
|-------------|------------------|
| Systems Thinking | Human Systems Integration (HSI) |
| Continuous Delivery | AI integration with human creativity |
| Managing System Complexity | Human-machine teaming |
| Agile SE | Kansei engineering |
| Energy Transformation | Sociotechnical systems |
| Mission Engineering | Digital twin evolution |
| Emergency Management | Model-based SE (MBSE) |
| New Innovative Approaches | Resilient systems |
| Systems Science Foundations | Systems of systems |

---

## Topic and Domain Classification

### Submission Metadata

Submitters MUST select classifications for paper routing:

| Classification | Limit | Purpose |
|----------------|-------|---------|
| Topics | Select up to 3 | Match paper to reviewers by subject |
| Domains | Select up to 3 | Match paper to reviewers by industry |
| Sector | Select exactly 1 | Government, Industry, or Academia |

### Topic Categories

Select from (representative list, not exhaustive):

- System Architecture/Design Definition
- Model-Based Systems Engineering (MBSE)
- Systems Thinking
- Needs and Requirements Definition
- Modeling/Simulation/Analysis
- Processes
- Systems of Systems
- Resilience
- Decision Analysis/Management
- Complexity
- Product Line Engineering
- Integration, Verification & Validation
- Risk Management
- Human Systems Integration
- Systems Security Engineering

### Domain Categories

Select from (representative list, not exhaustive):

- Defense
- Enterprise SE
- Aerospace
- Academia
- Automotive
- Social/Sociotechnical Systems
- Industry 4.0 & Society 5.0
- Healthcare/Biomed
- Infrastructure
- Energy/Power Systems
- Transportation
- Information Communications Technology
- Space Systems

---

## Submission Timeline

| Milestone | Date | Requirement |
|-----------|------|-------------|
| **Submissions Due** | **2 January 2026** | Paper MUST be submitted by this date |
| Notification of Acceptance | 16 March 2026 | Authors informed of decision |
| Authors Acceptance Due | 31 March 2026 | Authors MUST confirm intent to present |
| **Final Papers Due** | **16 May 2026** | De-anonymized final version MUST be submitted |
| Symposium | 13-18 June 2026 | Authors MUST present in person |

---

## Presentation Requirements

### Presenter Obligations

| Requirement | Description |
|-------------|-------------|
| Attendance | Presenter MUST register and attend IS 2026 in person |
| Presentation Day | MUST attend at least the day of presentation |
| Speaker Breakfast | MUST attend Speaker & Session Chair Breakfast (07:00 on presentation day) |
| Registration Deadline | Failure to register by deadline may result in exclusion from proceedings |
| Presentation File | MUST bring presentation on USB stick |
| Backup | Room computer MUST be used; personal USB only with approval |

### Presentation Format

| Property | Specification |
|----------|---------------|
| Duration | 30 or 45 minutes (assigned upon acceptance) |
| Structure | Presentation + Q&A + Transfer time |
| 30-minute slot | ~20-25 min presentation, ~5-10 min Q&A |
| 45-minute slot | ~35-40 min presentation, ~5-10 min Q&A |

---

## Schema Definition

### Paper Metadata Schema

```yaml
# INCOSE IS 2026 Paper Metadata Schema
# Version: 2.0.0

paper:
  # Required Identification
  title:
    type: string
    max_length: 150
    required: true

  category:
    type: enum
    values: [research, practice]
    required: true

  # Author Information (final submission only)
  authors:
    type: array
    min_items: 1
    items:
      name:
        type: string
        required: true
      affiliation:
        type: string
        required: true
      email:
        type: string
        format: email
        required: true
      address:
        type: string
        required: true
      corresponding:
        type: boolean
        default: false
    note: "OMIT for anonymous submission"

  # Abstract and Keywords
  abstract:
    type: string
    min_words: 150
    max_words: 300
    required: true

  keywords:
    type: array
    min_items: 3
    max_items: 6
    items:
      type: string
    required: true

  # Document Constraints
  word_count:
    type: integer
    max_value: 7000
    required: true

  page_count:
    type: integer
    max_value: 15
    recommended: true

  # Classification
  topics:
    type: array
    max_items: 3
    required: true

  domains:
    type: array
    max_items: 3
    required: true

  sector:
    type: enum
    values: [government, industry, academia]
    required: true

  # AI Disclosure (Required)
  ai_disclosure:
    type: object
    required: true
    properties:
      tools_used:
        type: array
        items:
          type: object
          properties:
            name:
              type: string
              required: true
            version:
              type: string
        required: true
      usage_categories:
        type: array
        items:
          type: enum
          values: [conceptual, analysis, content_generation, editorial]
        min_items: 1
        required: true
      author_oversight:
        type: string
        required: true
      intellectual_contribution:
        type: string
        required_if: "usage_categories contains conceptual OR content_generation"
```

### Section Schema

```yaml
# Required Sections Schema
sections:
  title:
    required: true
    position: 1

  author_information:
    required: true
    position: 2
    note: "OMIT for anonymous submission"

  abstract:
    required: true
    position: 3
    max_words: 300
    includes:
      - problem_statement
      - approach_summary
      - results_summary
      - contribution_statement

  introduction:
    required: true
    position: 4
    includes:
      - se_challenge
      - importance
      - context
      - objectives
      - contribution_preview
      - paper_roadmap

  background:
    required: true
    position: 5
    includes:
      - literature_review
      - gap_identification
      - positioning

  methodology:
    required: true
    position: 6
    research_paper_includes:
      - assumptions
      - methods
      - procedures
      - rationale
    practice_paper_includes:
      - problem_space
      - assumptions
      - approach
      - context

  results:
    required: true
    position: 7
    includes:
      - findings
      - evidence
      - validation

  discussion:
    required: true
    position: 8
    includes:
      - interpretation
      - implications
      - limitations

  conclusion:
    required: true
    position: 9
    includes:
      - summary
      - key_takeaways
      - future_work

  acknowledgments:
    required: true
    position: 10
    includes:
      - ai_disclosure  # REQUIRED
      - funding        # Optional, OMIT for anonymous
      - collaborators  # Optional, OMIT for anonymous

  references:
    required: true
    position: 11
    min_count: 10
    style: "AMA (American Medical Association)"

  author_biography:
    required: true
    position: 12
    note: "OMIT for anonymous submission"
    per_author:
      min_words: 50
      max_words: 100
      photo: optional
```

---

## Validation Rules

### Automated Verification Checks

A document claiming conformance to this specification MUST pass these checks:

| Rule | Check | Severity |
|------|-------|----------|
| V1 | Word count ≤ 7,000 | REQUIRED |
| V2 | All required sections present | REQUIRED |
| V3 | Abstract present with 150-300 words | REQUIRED |
| V4 | AI disclosure statement present | REQUIRED |
| V5 | Category declared (research OR practice) | REQUIRED |
| V6 | References section present with ≥ 1 reference | REQUIRED |
| V7 | For anonymous: No author information present | REQUIRED |
| V8 | For final: Author information complete | REQUIRED |
| V9 | Title present and ≤ 150 characters | REQUIRED |
| V10 | INCOSE template format used | REQUIRED |
| V11 | PDF format for submission | REQUIRED |
| V12 | Page count ≤ 15 | RECOMMENDED |
| V13 | References count ≥ 10 | RECOMMENDED |
| V14 | Keywords present (3-6) | RECOMMENDED |
| V15 | Figures numbered sequentially | RECOMMENDED |

### Pre-Submission Checklist

#### Anonymous Submission (Due: 2 January 2026)

- [ ] Word count at or below 7,000
- [ ] All required sections present
- [ ] Abstract: 150-300 words, self-contained
- [ ] AI disclosure statement included
- [ ] Author information REMOVED
- [ ] Funding sources REMOVED
- [ ] Acknowledgments REMOVED (except AI disclosure)
- [ ] Author biographies REMOVED
- [ ] Self-citations anonymized
- [ ] INCOSE template used
- [ ] PDF format
- [ ] SE challenge clearly stated
- [ ] Document properties cleared of author metadata

#### Final Submission (Due: 16 May 2026)

- [ ] All anonymous submission requirements
- [ ] Author information ADDED (names, affiliations, addresses, emails)
- [ ] Corresponding author indicated
- [ ] Funding acknowledgments restored (if applicable)
- [ ] Full acknowledgments section
- [ ] Author biographies ADDED (50-100 words each)
- [ ] Self-citations restored
- [ ] Final formatting verified
- [ ] All reviewer feedback addressed

---

## Copyright and Publication

### Copyright Policy

> "Those who contribute their material to INCOSE retain the copyright to their submissions and grant an unlimited license to INCOSE to use their contributions."

### Author Rights

Authors retain:
- Copyright to their work
- Right to include in future thesis, dissertation, or scholarly publication
- Right to make oral presentation in any forum
- Right to archive and preserve (personal or institutional)

### Publication Venues

| Venue | Research/Practice Papers | Presentations |
|-------|-------------------------|---------------|
| IS Proceedings | YES | NO |
| INCOSE Website | YES | YES |
| Wiley Online Library | YES | NO |

---

## Compliance Statement

A document claiming `type: vertex/doc` with target specification `v:spec:incose-paper` is **compliant** if and only if:

### Required Compliance

1. Word count is at or below 7,000 words
2. All REQUIRED sections are present in correct order
3. AI disclosure statement is present and complete
4. Paper category (research or practice) is declared
5. Content is original and unpublished
6. SE challenge is clearly stated in introduction
7. INCOSE template format is used
8. PDF format for submission
9. English language

### For Anonymous Submission (add)

10. All author-identifying information removed
11. Self-citations anonymized

### For Final Submission (add)

10. Author information complete
11. Author biographies present (50-100 words each)
12. Self-citations restored

---

## Related Documents

| Document | Relationship | Purpose |
|----------|--------------|---------|
| `v:guidance:incose-paper` | Coupled guidance | Quality assessment criteria |
| `INCOSE-IS2026-REQUIREMENTS-CACHE.md` | Reference source | Complete research cache |
| INCOSE Paper Template | External template | Required formatting |
| INCOSE Paper Preparation Guidelines | External standard | Detailed formatting rules |
| INCOSE Paper Evaluation Criteria | External standard | Reviewer criteria |

---

**Note:** This specification (v2.0.0) is derived from comprehensive research of official INCOSE IS 2026 Call for Submissions, Paper Preparation Guidelines, Paper Evaluation Criteria, and INCOSE publication standards. It captures all structural requirements that can be deterministically verified. Quality assessment is covered in the corresponding guidance document (`v:guidance:incose-paper`).