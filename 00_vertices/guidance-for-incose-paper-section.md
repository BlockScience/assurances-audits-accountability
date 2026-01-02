---
type: vertex/guidance
extends: doc
id: v:guidance:incose-paper-section
name: Guidance for INCOSE Paper Sections
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-31T17:50:00Z
modified: 2025-12-31T17:50:00Z
description: Quality criteria and best practices for writing excellent INCOSE symposium paper sections that resonate with reviewers
criteria:
  - clarity
  - coherence
  - contribution-visibility
  - practitioner-accessibility
  - rigor
  - engagement
rubric: validation-assessment
---

# Guidance for INCOSE Paper Sections

## Purpose Statement

While [spec-for-incose-paper-section](spec-for-incose-paper-section.md) defines **what** structural elements each section must contain, this guidance helps authors assess **how well** each section serves its purpose within an INCOSE research paper.

This document addresses **validation** concerns: qualitative assessment of section fitness-for-purpose that cannot be deterministically checked. Great INCOSE paper sections are clear, coherent, contribute visibly to the paper's argument, remain accessible to practitioners, demonstrate rigor, and engage readers.

## Document Overview

### What This Guidance Covers

This guidance supports authors writing INCOSE symposium paper sections by providing:

- Quality criteria for each section type (Introduction, Body, Conclusions, etc.)
- Section-specific best practices based on reviewer expectations
- Common pitfalls and anti-patterns to avoid
- Techniques for maintaining narrative flow across sections
- Balancing rigor with accessibility for diverse SE audiences
- Integration strategies for assembling sections into cohesive papers

### Best Use Cases

Use this guidance when:

- Drafting a new section and want to understand quality expectations
- Reviewing a completed section for fitness-for-purpose
- Receiving feedback that a section "doesn't work" but unsure why
- Ensuring section-level quality before integration
- Teaching others to write effective INCOSE paper sections
- Conducting peer review of section drafts

### Not Intended For

- Checking structural compliance (use [spec-for-incose-paper-section](spec-for-incose-paper-section.md))
- Overall paper-level quality (use [guidance-for-incose-paper](guidance-for-incose-paper.md))
- LaTeX formatting issues (use INCOSE template documentation)
- Presentation preparation (separate from paper writing)

## Quality Criteria

### 1. Clarity

**Definition:** Section content is understandable to INCOSE's diverse audience (practitioners, researchers, managers).

| Level | Indicators |
|-------|------------|
| **Excellent** | Technical concepts explained with examples; acronyms defined at first use; complex ideas built incrementally; jargon minimized and contextualized. A practitioner unfamiliar with the specific topic can follow the argument. |
| **Good** | Main ideas are clear with minor ambiguities; most technical terms explained; some concepts may require domain knowledge but not specialist expertise. |
| **Needs Improvement** | Assumes too much background; undefined acronyms; jargon-heavy without explanation; complex concepts introduced without scaffolding. Excludes non-specialist readers. |

**Anti-patterns:**
- Acronym soup: "The SoS leverages MBSE with SysML for V&V using STPA methodologies"
- Assumed expertise: References to niche methods without explanation
- Academic-only language: Writing only for researchers, excluding practitioners

### 2. Coherence

**Definition:** Section has internal logical structure and flows smoothly to/from adjacent sections.

| Level | Indicators |
|-------|------------|
| **Excellent** | Clear narrative arc within section; subsections build logically; smooth transitions between paragraphs; opening connects to prior section, closing transitions to next section. Reader never asks "why am I reading this?" |
| **Good** | Generally logical flow with minor gaps; most transitions present; connection to paper's overall argument is clear. |
| **Needs Improvement** | Disjointed paragraphs; subsections feel like separate essays; abrupt topic shifts; unclear how section supports paper's thesis. |

**Anti-patterns:**
- "Dumping ground" sections: Collection of related-but-disconnected points
- Missing bridges: No transition from Introduction to Background
- Circular logic: Section restates points without advancing argument

### 3. Contribution Visibility

**Definition:** Reader can clearly see what new knowledge or capability this section contributes.

| Level | Indicators |
|-------|------------|
| **Excellent** | Section's contribution to paper's overall argument is explicit; what's novel vs. background is distinguished; reader can articulate "what I learned" after reading. |
| **Good** | Contribution is present but may require inference; novelty vs. prior art is mostly clear. |
| **Needs Improvement** | Unclear what is being contributed; mixes background and novelty without distinction; reads like a survey or textbook. |

**Anti-patterns:**
- Extended literature review without synthesis
- Background sections that overwhelm the contribution
- Framework descriptions without highlighting novel aspects

### 4. Practitioner Accessibility

**Definition:** Section provides actionable insights or understanding useful to SE practitioners.

| Level | Indicators |
|-------|------------|
| **Excellent** | Concrete examples from practice; clear "so what?" for practitioners; actionable recommendations; balance of theory and application. |
| **Good** | Relevance to practice is evident; some concrete examples; actionable insights present but may require adaptation. |
| **Needs Improvement** | Purely theoretical without practical grounding; no examples from real systems; unclear how practitioners would use this. |

**Anti-patterns:**
- "Toy examples" only: Trivial illustrations that don't reflect real complexity
- Missing application context: Framework without use cases
- Academic abstraction: Theory divorced from engineering practice

### 5. Rigor

**Definition:** Claims are appropriately supported; methods are sound; limitations are acknowledged.

| Level | Indicators |
|-------|------------|
| **Excellent** | Claims matched to evidence strength; methods described sufficiently for replication; assumptions stated explicitly; limitations discussed honestly; appropriate citations to prior art. |
| **Good** | Most claims supported; methods generally sound; major limitations acknowledged. Minor gaps in rigor that don't undermine core argument. |
| **Needs Improvement** | Unsupported claims; vague methods; limitations ignored; missing citations; overclaiming beyond evidence. |

**Anti-patterns:**
- Unqualified universals: "This framework solves all V&V problems"
- Missing validation: Framework presented without any application
- Cherry-picked evidence: Only showing successes, hiding failures
- Undefined metrics: "Significantly improved quality" without measurement

### 6. Engagement

**Definition:** Section maintains reader interest through effective writing and presentation.

| Level | Indicators |
|-------|------------|
| **Excellent** | Strong opening that hooks reader; varied sentence structure; effective use of figures/tables; compelling examples; crisp, active voice. |
| **Good** | Generally engaging with occasional dry passages; adequate use of visuals; mostly active voice. |
| **Needs Improvement** | Monotonous writing; passive voice dominates; walls of text without visual breaks; boring examples or no examples. |

**Anti-patterns:**
- Passive voice overload: "It was observed that improvements were achieved"
- Figure-free deserts: 1000+ words with no visual elements
- Formulaic writing: Every paragraph has identical structure
- Abstract-only examples: No concrete instantiation

## Section-by-Section Guidance

### Abstract (≤300 words)

**Purpose:** Convince reader the paper is worth reading; enable literature search/indexing.

**Quality Criteria:**
- Opens with the problem/gap (1-2 sentences)
- States the contribution clearly (1-2 sentences)
- Summarizes approach/method (2-3 sentences)
- Highlights key results (1-2 sentences)
- Concludes with significance/impact (1 sentence)

**Best Practices:**
- Write abstract LAST after paper is complete
- No citations, figures, or equations
- Use keywords naturally for searchability
- Match EasyChair submission exactly
- Test on colleagues: can they understand your contribution from abstract alone?

**Common Pitfalls:**
- Too vague: "We present a framework" (what framework? for what?)
- Too detailed: Trying to summarize every section
- Missing "so what?": Says what you did but not why it matters
- Jargon barrier: Excludes readers who would benefit

### Introduction

**Purpose:** Motivate the problem, position your contribution, orient the reader.

**Quality Criteria:**
- Problem statement is concrete and relatable (not abstract)
- Background provides enough context for non-specialists
- Gap/need is explicit ("Current approaches cannot X, but Y is needed")
- Contribution summary is specific (not "we propose a framework" but "we formalize V&V using typed simplicial complexes")
- Paper roadmap helps reader navigate

**Best Practices:**
- Start with a concrete scenario or challenge practitioners face
- Build from familiar (current V&V practice) to novel (topological formalization)
- Use first figure here to introduce key concept visually
- Keep it to 10-15% of total paper length
- End with explicit roadmap: "Section 2 presents..., Section 3 describes..."

**Common Pitfalls:**
- Starting too abstract: "Quality is important in engineering" (obvious, boring)
- History lesson: Extended chronology without connecting to contribution
- Underselling: Burying the contribution in vague language
- Overselling: "First ever" claims that aren't true
- Missing roadmap: Reader doesn't know what's coming

**Example Structure:**
1. Opening scenario/challenge (1 paragraph)
2. Problem statement and context (2-3 paragraphs)
3. Why existing approaches fall short (1-2 paragraphs)
4. Contribution summary (1 paragraph)
5. Paper organization (1 paragraph)

### Background

**Purpose:** Establish foundational concepts; position work relative to prior art.

**Quality Criteria:**
- Covers only concepts needed to understand contribution (not comprehensive survey)
- Synthesizes rather than summarizes: identifies patterns, gaps, limitations
- Distinguishes related work from foundational concepts
- Sets up your contribution by showing what's missing
- Appropriate citations to primary sources

**Best Practices:**
- Organize by concept, not chronologically
- Use comparison tables to synthesize related work
- Explicitly state what gap your work addresses
- Define technical terms that appear later in paper
- Keep it proportional: don't let background overwhelm contribution (aim for 15-20% of paper)

**Common Pitfalls:**
- Comprehensive survey: Trying to cite everyone who's ever worked in the area
- Missing synthesis: Lists papers without identifying patterns or gaps
- Straw man comparisons: Misrepresenting prior work to make yours look better
- Orphaned background: Concepts introduced but never used later
- Burying the gap: Unclear why this work is needed

### Body Sections (Framework/Architecture/Methods)

**Purpose:** Present your contribution with sufficient detail for understanding and assessment.

**Quality Criteria:**
- Logical decomposition (e.g., layers, components, phases)
- Each subsection has clear purpose in overall architecture
- Design rationale: why these choices?
- Sufficient detail for assessment, not overwhelming minutiae
- Concrete examples grounding abstract concepts
- Visual representations (diagrams, tables) supporting text

**Best Practices:**
- Follow a consistent structure for parallel sections (e.g., all layers have: purpose, components, interactions)
- Use running example throughout to illustrate concepts
- Include "breadcrumb" references: "As discussed in Section 2.1..."
- Balance completeness with readability: relegate some details to tables/figures
- End each major subsection with transition to next

**Common Pitfalls:**
- Uneven detail: Some sections very deep, others superficial
- Missing rationale: Describes WHAT without explaining WHY
- Example-free abstraction: Theory without concrete instantiation
- Diagram mismatch: Figures that don't align with text description
- Kitchen sink: Including every detail regardless of relevance

**For Architecture Papers Specifically:**

Use established frameworks (like 4-layer SE model, V-model) to structure presentation:

- **Conceptual Layer**: Stakeholder needs, operational context, acceptance criteria
- **Functional Layer**: What the system does, functions and requirements
- **Logical Layer**: Design-independent component structure, interfaces
- **Physical Layer**: Implementation technologies, specific tools

This provides familiar structure for SE audience.

### Self-Demonstration / Case Study

**Purpose:** Provide evidence that your approach works in practice.

**Quality Criteria:**
- Real application (not toy example)
- Sufficient context: what was demonstrated, under what conditions
- Honest results: both successes and limitations
- Clear connection to claims: how does this validate your approach?
- Metrics or evidence of outcomes

**Best Practices:**
- Self-demonstration (using framework to build itself) is powerful proof-of-concept
- Include "lessons learned" from application
- Use tables/figures to summarize results
- Discuss what worked and what didn't
- Connect back to quality criteria or requirements from earlier sections

**Common Pitfalls:**
- Cherry-picking: Only showing best-case results
- Insufficient context: Reader can't assess whether demo is meaningful
- Trivial example: Demonstration doesn't test the interesting aspects
- Disconnected from claims: Demo doesn't actually validate what you claimed
- Missing reflection: No discussion of what you learned from application

### Conclusions

**Purpose:** Synthesize contributions, acknowledge limitations, leave reader with clear takeaways.

**Quality Criteria:**
- Summarizes key contributions in accessible language
- Connects back to problem from Introduction (closing the loop)
- Honestly discusses limitations and scope boundaries
- Positions work in broader context
- Forward-looking: future work or implications

**Best Practices:**
- No new concepts requiring explanation
- "Layman's terms" accessible to SE managers
- Limitations discussed without undermining contribution
- 3-5 key takeaways reader should remember
- Optimistic but honest tone

**Common Pitfalls:**
- Just repeating abstract: No synthesis or reflection
- Underselling: Apologizing for limitations excessively
- Overselling: Claiming more than was demonstrated
- Orphaned conclusions: Not connected to earlier sections
- Missing limitations: Pretending work is perfect

**Example Structure:**
1. Restate problem and approach (1 paragraph)
2. Key contributions and results (2-3 paragraphs)
3. Limitations and scope (1-2 paragraphs)
4. Broader significance (1 paragraph)

### Recommendations

**Purpose:** Provide actionable guidance for practitioners adopting or building on your work.

**Quality Criteria:**
- Specific and actionable (not vague advice)
- Targeted to INCOSE practitioner audience
- Grounded in lessons from your work
- Realistic about prerequisites and effort
- Organized by stakeholder or use case if multiple audiences

**Best Practices:**
- Use imperative voice: "Start by...", "Establish...", "Avoid..."
- Sequence recommendations: what to do first, next, later
- Include anti-recommendations: what NOT to do
- Connect to specific sections of paper for details
- Keep it concise: 3-7 key recommendations

**Common Pitfalls:**
- Vague platitudes: "Organizations should adopt best practices"
- Theory repetition: Recommendations are just paper summary
- Unrealistic demands: Advice that ignores practical constraints
- Missing prioritization: All recommendations weighted equally
- Disconnected from work: Generic advice that could apply to any paper

**Example Structure:**
1. For practitioners adopting this framework...
2. For researchers building on this work...
3. For organizations implementing these practices...

## Workflow Guidance

### Writing Process

1. **Outline first**: Create section skeleton with key points before drafting
2. **Draft quickly**: Get ideas down without perfectionism
3. **Verify structure**: Check against spec before investing in polish
4. **Refine iteratively**: Multiple passes for clarity, coherence, engagement
5. **Validate fitness**: Assess against quality criteria in this guidance
6. **Peer review**: Get feedback from colleagues before final

### Integration Strategy

When assembling sections into complete paper:

1. **Check transitions**: Last paragraph of section N → first paragraph of section N+1
2. **Verify forward/backward references**: "As discussed in..." and "We will show in..."
3. **Balance lengths**: Ensure sections are proportional to their importance
4. **Consistent terminology**: Same concepts called same thing throughout
5. **Figure/table sequencing**: Numbering is consecutive across sections

### Quality Assurance

Before marking section as complete:

- [ ] Passes verification against spec
- [ ] Meets quality criteria at "Good" or better in all 6 dimensions
- [ ] Peer reviewer can understand section without author present
- [ ] Contribution is visible and explicit
- [ ] Limitations acknowledged where appropriate
- [ ] Figures/tables effectively support text

## Common Issues and Solutions

### Issue: Section feels disconnected from paper

**Symptoms:** Reviewers say "not sure why this is here" or "tangential to main argument"

**Solutions:**
- Add explicit connection to problem statement from Introduction
- Include forward reference to how this section's content is used later
- Consider whether section is actually necessary or should be condensed
- Strengthen transitions from previous and to next section

### Issue: Too technical for practitioner audience

**Symptoms:** Jargon-heavy, assumes specialist knowledge, inaccessible to managers

**Solutions:**
- Add concrete example grounding abstract concepts
- Define technical terms at first use
- Include "plain English" summary of key points
- Use analogies to familiar SE concepts
- Test on non-specialist colleague

### Issue: Not rigorous enough for researchers

**Symptoms:** Vague claims, insufficient detail, missing validation

**Solutions:**
- Add citations to support claims
- Include methodology details
- Provide metrics or evidence for assertions
- Discuss assumptions and limitations explicitly
- Use tables to present detailed data

### Issue: Section too long, overwhelming

**Symptoms:** Dense walls of text, reader fatigue, difficulty maintaining attention

**Solutions:**
- Move detailed data to tables
- Use figures to replace textual descriptions
- Break into smaller subsections with clearer topics
- Summarize key points in bulleted lists where appropriate
- Relegate some content to appendices (if appropriate)

### Issue: Contribution not visible

**Symptoms:** Readers finish section unsure what was novel vs. background

**Solutions:**
- Explicitly label novelty: "We contribute X by..."
- Use contrast: "Unlike prior work which Y, our approach Z"
- Highlight in figures with annotations
- Include design rationale explaining unique choices

## Best Practices

### Effective Use of Figures

- **Introduce visually first**: Lead with diagram, then explain in text
- **Annotate diagrams**: Don't make reader guess what elements mean
- **Reference explicitly**: "As shown in Figure 3..." not "the figure shows..."
- **High information density**: Figures should convey what text cannot
- **Consistent notation**: Same symbols/colors mean same things across figures

### Effective Use of Tables

- **Comparison tables**: Show multiple approaches side-by-side
- **Summary tables**: Condense detailed information from text
- **Enumeration tables**: List components, functions, requirements systematically
- **Headers matter**: Clear column/row headers make table self-explanatory
- **Gray header rows**: Use INCOSE template `tableheader` color for visual clarity

### Writing for Diverse Audiences

INCOSE reviewers include practitioners, researchers, managers, and students. Balance:

- **Concrete ↔ Abstract**: Ground abstract concepts in concrete examples
- **Specific ↔ General**: Specific enough to be actionable, general enough to transfer
- **Rigorous ↔ Accessible**: Maintain rigor without excluding non-specialists
- **Depth ↔ Breadth**: Sufficient detail for assessment without overwhelming

### Maintaining Narrative Flow

Great papers tell a story. Techniques:

- **Problem → Solution arc**: Every section advances the problem-solving narrative
- **Signposting**: Tell reader where you are and where you're going
- **Callbacks**: Reference earlier sections to show integration
- **Forward references**: Preview what's coming to maintain interest
- **Transitions**: Bridge paragraphs and sections smoothly

### Honesty and Intellectual Integrity

- **Acknowledge limitations**: Shows maturity and builds trust
- **Qualify claims**: Match claim strength to evidence strength
- **Credit prior work**: Appropriately cite influences and related work
- **Discuss failures**: What didn't work and why teaches as much as successes
- **Avoid overclaiming**: "First", "only", "always" are rarely true

---

**Note:** This guidance enables validation of INCOSE paper sections for fitness-for-purpose. Used in combination with [spec-for-incose-paper-section](spec-for-incose-paper-section.md), it supports the complete assurance cycle: verification (structural compliance) + validation (quality assessment) = assurance (confidence in fitness).
