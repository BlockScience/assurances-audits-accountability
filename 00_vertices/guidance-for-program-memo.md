---
type: vertex/guidance
extends: doc
id: v:guidance:program-memo
name: Guidance for Program Memo Documents
description: Quality criteria and best practices for creating effective program memos that synthesize documentation packages for executive audiences
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-01-04T14:00:00Z
modified: 2025-01-04T14:00:00Z
dependencies:
  - v:guidance:architecture
  - v:guidance:lifecycle
  - v:guidance:program-plan
criteria:
  - executive-accessibility
  - synthesis-quality
  - traceability
  - navigation-clarity
  - currency
  - appropriate-brevity
---

# Guidance for Program Memo Documents

**This guidance helps authors create high-quality program memos that effectively synthesize architecture, lifecycle, and program plan documents into accessible executive summaries.**

## Purpose

While spec-for-program-memo defines what structural elements must be present, this guidance helps authors assess **how well** a program memo serves its purpose. Great program memos enable executives and stakeholders to quickly understand a program without reading hundreds of pages of detailed documentation, while confidently navigating to specific details when needed.

## Document Overview

### What This Guidance Covers

Program memos serve as executive primers for documentation packages:
- **Architecture** defines what we're building (goal state)
- **Lifecycle** defines how we build it (process)
- **Program Plan** defines the execution details (who, when, with what)
- **Program Memo** synthesizes all three for stakeholder consumption

This guidance supports authors in creating memos that:
- Distill essential information without losing meaning
- Maintain accuracy to source documents
- Enable quick comprehension by busy stakeholders
- Provide clear navigation to detailed information
- Stay current as source documents evolve

### Best Use Cases

1. **Executive Briefings:** Preparing leadership for program decisions
2. **Board Presentations:** Summarizing programs for governance bodies
3. **Stakeholder Onboarding:** Orienting new team members or partners
4. **Funder Communication:** Providing sponsors with program visibility
5. **Cross-Team Alignment:** Ensuring shared understanding across organizations

### When NOT to Use

- When source documents don't exist yet (create them first)
- When detailed technical information is needed (use architecture)
- When process details are needed (use lifecycle)
- When execution specifics are needed (use program plan)
- When the audience needs to make detailed implementation decisions

## Quality Criteria

### 1. Executive Accessibility

**Excellent:**
- Any executive can understand the program in 10 minutes of reading
- No unexplained jargon or acronyms
- Key facts are immediately visible (not buried in prose)
- Visual elements aid quick comprehension
- Answers the questions executives actually ask

**Good:**
- Most executives can follow the content
- Limited jargon, mostly explained
- Key facts present but may require searching
- Some visual aids

**Needs Improvement:**
- Requires technical background to understand
- Heavy jargon without definitions
- Key facts buried or missing
- Wall of text without visual relief
- Assumes reader knows the domain

### 2. Synthesis Quality

**Excellent:**
- Distills essence without losing critical meaning
- Abstracts appropriately for audience level
- Captures the "so what" not just the "what"
- Identifies the most important elements from each source
- Creates coherent narrative from three separate documents

**Good:**
- Captures main points from each source
- Appropriate level of abstraction
- Reasonably coherent narrative

**Needs Improvement:**
- Copy-pastes from source documents (no synthesis)
- Loses critical information in abstraction
- Cherry-picks without representing full picture
- Incoherent—reads like three separate summaries
- Includes inappropriate detail for audience

### 3. Traceability

**Excellent:**
- Every major claim can be traced to a source document
- Section references explicitly link to source documents
- Reader can find detailed backup for any summary point
- Source document versions are clearly identified
- Updates to sources trigger memo review

**Good:**
- Major sections reference sources
- Most claims traceable
- Source versions noted

**Needs Improvement:**
- Claims without source attribution
- Missing or broken references to source documents
- No version tracking
- Cannot verify summary against sources
- Memo contradicts source documents

### 4. Navigation Clarity

**Excellent:**
- Reader knows exactly where to find any detail they need
- Document package section provides clear decision tree
- "When to consult" guidance is specific and actionable
- Links work and point to correct sections
- Progressive disclosure—summary → detail path is clear

**Good:**
- Source documents referenced
- General guidance on where to find details
- Links present

**Needs Improvement:**
- No guidance on where to find details
- Missing or broken links
- Reader must guess which document to consult
- No document package overview
- Dead ends—summary without path to detail

### 5. Currency

**Excellent:**
- Memo reflects current state of all source documents
- Version numbers and dates are accurate
- Update triggers are defined
- Staleness is immediately visible
- Currency statement included

**Good:**
- Generally reflects source documents
- Versions noted
- Recent updates reflected

**Needs Improvement:**
- Memo contradicts current source documents
- Version numbers missing or wrong
- No way to tell if memo is current
- Stale information presented as current
- No update process defined

### 6. Appropriate Brevity

**Excellent:**
- 3-5 pages total—no longer than necessary
- Every sentence earns its place
- No redundancy between sections
- Tables and visuals used efficiently
- Executive can read in one sitting

**Good:**
- Reasonable length (5-7 pages)
- Most content necessary
- Some efficiency in presentation

**Needs Improvement:**
- Too long (>7 pages) for executive consumption
- Redundant information across sections
- Verbose where concise would serve
- Includes details that belong in source documents
- Reader loses focus before finishing

## Section-by-Section Guidance

### Program Overview

**Purpose:** Orient the reader immediately to what this program is about

**Tips:**

- Lead with the problem being solved, not the solution
- State sponsor and recipient in first paragraph
- Use the summary table for key facts—don't bury them in prose
- Write for someone who knows nothing about this program
- Answer: "Why should I care about this program?"

**Anti-patterns:**

- ❌ Starting with technical details or project history
- ❌ Assuming reader knows the context
- ❌ Burying sponsor/recipient/timeline in prose

**Preferred:**

- ✅ "This program delivers [capability] to [recipient], solving [problem]"
- ✅ Key facts in scannable table format

### What We're Building

**Purpose:** Synthesize architecture into accessible goal state description

**Tips:**

- Focus on conceptual and logical layers—skip physical implementation
- Success criteria should be measurable and meaningful to stakeholders
- Key components should be described by function, not technology
- Reference architecture document for anyone wanting details

**Anti-patterns:**

- ❌ Including technology choices (Python, AWS, etc.)
- ❌ Copying architecture document sections verbatim
- ❌ Listing all components instead of key 3-5
- ❌ Technical success criteria ("99.9% uptime")

**Preferred:**

- ✅ Capability-focused descriptions ("Document verification service")
- ✅ Stakeholder-meaningful criteria ("Engineers can verify in <10 seconds")

### How We're Building It

**Purpose:** Synthesize lifecycle into accessible process overview

**Tips:**

- Phase table should fit on half a page maximum
- Durations should be approximate (weeks/months, not days)
- Quality assurance summary should build confidence without detail
- Reference lifecycle document for process details

**Anti-patterns:**

- ❌ Including detailed process steps
- ❌ Listing all gates and checkpoints
- ❌ Technical V&V terminology without explanation
- ❌ Phase table with 10+ phases

**Preferred:**

- ✅ 4-6 phases maximum in summary table
- ✅ "We verify quality through [brief approach]"

### Execution Summary

**Purpose:** Synthesize program plan into actionable execution overview

**Tips:**

- Timeline visualization should show ≤7 milestones
- Top risks should be genuinely top (not comprehensive)
- Resource summary should be high-level (teams, not individuals)
- Reference program plan for schedules, RACI, risk register

**Anti-patterns:**

- ❌ Including full Gantt chart
- ❌ Listing all risks from risk register
- ❌ Individual resource assignments
- ❌ Detailed budget breakdown

**Preferred:**

- ✅ Visual timeline with major milestones only
- ✅ "Top 3 risks" not "Risk register summary"
- ✅ "X teams, Y total FTEs" not role-by-role breakdown

### Document Package

**Purpose:** Enable navigation to detailed information

**Tips:**

- "When to consult" column is the key value—make it specific
- Currency table helps readers assess staleness
- Links should work and be tested
- Include this memo in the package list

**Anti-patterns:**

- ❌ Just listing documents without navigation guidance
- ❌ Missing version/date information
- ❌ Generic "when to consult" guidance

**Preferred:**

- ✅ Specific triggers: "Consult architecture for component interface details"
- ✅ All versions and dates current and accurate

### Approval and Accountability

**Purpose:** Establish authority and responsibility for memo accuracy

**Tips:**

- Preparer, reviewer, approver should be different people
- Accountability statement should address currency responsibility
- Dates should reflect actual review/approval

**Anti-patterns:**

- ❌ Same person in all roles
- ❌ Missing accountability for keeping memo current
- ❌ Placeholder names or dates

**Preferred:**

- ✅ Clear separation of duties
- ✅ "[Role] is responsible for updating this memo when source documents change"

## Workflow Guidance

### Recommended Authoring Sequence

1. **Verify Source Documents Exist** (10 min)
   - Confirm architecture, lifecycle, program plan are complete
   - Note versions and dates
   - Identify any gaps or pending updates

2. **Extract Key Facts** (45 min)
   - From Architecture: problem statement, goal state, key components, success criteria
   - From Lifecycle: phases, durations, V&V approach
   - From Program Plan: milestones, resources, top risks, sponsor, recipient, timeline, budget

3. **Draft Program Overview** (20 min)
   - Synthesize problem and capability
   - Create summary table
   - Test: Would an outsider understand this?

4. **Draft What We're Building** (20 min)
   - Synthesize architecture at appropriate level
   - Select key components (3-5 max)
   - Include success criteria
   - Add architecture reference

5. **Draft How We're Building It** (20 min)
   - Create phase summary table
   - Write approach paragraph
   - Summarize quality assurance
   - Add lifecycle reference

6. **Draft Execution Summary** (30 min)
   - Create milestone timeline visual
   - Summarize resources
   - Select and summarize top 3-5 risks
   - Add program plan reference

7. **Complete Document Package Section** (15 min)
   - Create navigation table with specific guidance
   - Create currency table with versions/dates
   - Verify all links work

8. **Complete Approval Section** (10 min)
   - Identify preparer, reviewer, approver
   - Write accountability statement
   - Schedule review/approval

9. **Quality Review** (30 min)
   - Check against quality criteria
   - Verify traceability to sources
   - Test executive accessibility
   - Confirm brevity (3-5 pages)

**Total estimated time:** 3-4 hours for initial memo from complete source documents

### Quality Checkpoints

- **After step 3:** Would someone unfamiliar with the program understand the overview?
- **After step 6:** Can every claim be traced to a source document?
- **After step 7:** Can a reader find any detail they need?
- **After step 9:** Would an executive read this in one sitting?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| **Too Long** | Memo exceeds 5 pages | Cut detail; push to source documents; use tables not prose |
| **Too Technical** | Executives can't follow | Replace jargon with plain language; focus on "so what" not "what" |
| **Copy-Paste Syndrome** | Sections lifted from sources | Rewrite to synthesize; abstract to appropriate level |
| **Missing Traceability** | Can't verify claims | Add section references; include document links |
| **Stale Content** | Memo doesn't match sources | Update from current sources; add currency tracking |
| **Navigation Gaps** | Reader can't find details | Improve "when to consult" guidance; verify links |
| **Buried Key Facts** | Important info in prose | Use summary tables; lead with conclusions |
| **Risk Overload** | All risks included | Select top 3-5; reference program plan for full register |
| **Milestone Overload** | Too many milestones | Show ≤7 major milestones; reference program plan for full schedule |

## Best Practices

1. **Write for the Busiest Reader** - Assume they have 10 minutes; front-load the important stuff
2. **Synthesize, Don't Summarize** - Create new coherent narrative, don't just shorten
3. **Use Tables for Facts** - Prose for context, tables for data
4. **Test with an Outsider** - Have someone unfamiliar read it; note where they get confused
5. **Maintain Traceability** - Every claim should have a source; every section should link to detail
6. **Keep it Current** - Stale memos are worse than no memo; build in update triggers
7. **Respect the Page Budget** - 3-5 pages is a feature, not a constraint
8. **Answer Executive Questions** - What, why, when, how much, what could go wrong?
9. **Progressive Disclosure** - Summary here, detail there; make the path clear
10. **Version Everything** - Source versions, memo version, dates everywhere

## Validation vs. Verification

**Verification** (deterministic, against spec-for-program-memo):
- Are all required sections present?
- Are all three source documents referenced?
- Is the document package section complete?
- Are approval roles identified?

**Validation** (qualitative, against this guidance):
- Is the memo accessible to executives?
- Does it effectively synthesize source documents?
- Are claims traceable to sources?
- Is navigation to detail clear?
- Is it appropriately brief?
- Is it current with source documents?

This guidance document supports **validation** - assessing fitness-for-purpose.

## Self-Consistency

This guidance document demonstrates the quality criteria it defines:

- **Executive Accessibility:** Written for program memo authors with clear value proposition
- **Synthesis Quality:** Integrates advice from architecture, lifecycle, and program plan guidance
- **Traceability:** References spec-for-program-memo and related guidance documents
- **Navigation Clarity:** Clear section-by-section guidance with specific tips
- **Currency:** Version controlled with clear update expectations
- **Appropriate Brevity:** Focused on essentials; avoids unnecessary detail

## Document Metadata

| Property | Value |
|----------|-------|
| Specification | [[spec-for-program-memo]] |
| Guidance Version | 1.0.0 |
| Specification Version | 1.0.0 |
| Prerequisites | [[guidance-for-architecture]], [[guidance-for-lifecycle]], [[guidance-for-program-plan]] |
| Target Users | Authors creating executive summaries of documentation packages |

---

**Note:** This guidance is coupled with [[spec-for-program-memo]] via a coupling edge. Together with architecture, lifecycle, and program plan guidance, it supports the complete documentation package for program delivery.