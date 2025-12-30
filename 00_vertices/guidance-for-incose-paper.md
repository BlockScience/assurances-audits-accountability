---
type: vertex/guidance
extends: doc
id: v:guidance:incose-paper
name: Guidance for INCOSE IS 2026 Research Paper
description: Comprehensive quality criteria, best practices, and evaluation guidance for creating an excellent INCOSE symposium paper that resonates with reviewers and practitioners
tags:
  - vertex
  - doc
  - guidance
version: 2.0.0
created: 2025-12-30T10:30:00Z
modified: 2025-12-30T19:00:00Z
dependencies: []
---

# Guidance for INCOSE IS 2026 Research Paper

## Purpose

While `spec-for-incose-paper` defines **what** structural elements must be present, this guidance helps authors assess **how well** a paper serves its purpose of contributing to the INCOSE community. This document addresses **validation** concerns: qualitative assessment of fitness-for-purpose that cannot be deterministically checked.

Great INCOSE papers are rigorous, accessible, engaging, and demonstrate clear value to systems engineering practice. This guidance provides the criteria and practices that distinguish excellent submissions from merely compliant ones.

---

## Document Overview

### What This Guidance Covers

This guidance supports authors creating INCOSE symposium papers by providing:

- Quality assessment criteria aligned with INCOSE Paper Evaluation Criteria
- Best practices for communicating with diverse SE audiences
- Section-by-section authoring recommendations with anti-patterns
- Reviewer perspective: what evaluators look for
- Theme alignment strategies for IS 2026 "Seeking Wa in SE"
- Common pitfalls and how to avoid them
- Workflow guidance from concept to submission

### Best Use Cases

Use this guidance when:

- Creating a new INCOSE symposium paper from scratch
- Reviewing a draft for quality before submission
- Assessing whether a paper will resonate with INCOSE reviewers
- Teaching others how to write effective SE papers
- Connecting research to the 2026 theme
- Self-evaluating against Best Paper Award criteria

### Not Intended For

- Checking structural compliance (use `spec-for-incose-paper`)
- Template formatting issues (use INCOSE template documentation)
- Non-SE academic papers (this guidance is SE-specific)
- Presentation slides preparation (separate from paper quality)

---

## INCOSE Reviewer Perspective

### What Reviewers Are Asked to Evaluate

Understanding the reviewer's task helps authors write better papers. INCOSE reviewers evaluate submissions against specific criteria:

#### Primary Evaluation Questions

| Question | What Reviewers Look For |
|----------|------------------------|
| Does the paper demonstrate the value of applying SE? | Clear connection between content and SE practice improvement |
| Does it provide usable information to practitioners? | Actionable insights, not just theoretical contributions |
| Does it offer insight to enable new concepts? | Advances thinking, opens new possibilities |
| Is there refinement OR articulation of SE principles? | Either improves existing knowledge or introduces new knowledge |
| Is the approach innovative? | Novel methods, frameworks, or applications |

#### Quality Signals Reviewers Notice

**Positive Signals:**
- Clear "so what?" answered in first two pages
- Specific, bounded claims with appropriate evidence
- Practitioner-focused language and examples
- Honest discussion of limitations
- Connection to broader SE trends and challenges

**Negative Signals:**
- Generic claims without specific evidence
- Jargon-heavy writing that excludes practitioners
- Missing or superficial limitations discussion
- Claims that exceed the evidence presented
- Paper still in outline or rough draft form

### Rating Implications

> "A paper that is still in outline form should not be rated highly. The rating should reflect the paper in its current form, even if the outline or rough draft has strong potential."

This means: **Submit polished work.** Potential doesn't count—execution does.

---

## Quality Criteria

### 1. Relevance to SE Community

This is the most fundamental criterion. Papers must matter to systems engineers.

#### Excellent (Target)

- Addresses a clearly identified SE challenge that practitioners actually face
- Contribution to SE practice is explicit, specific, and compelling
- Paper explains why this matters to the INCOSE community within the first page
- Connects to current SE trends, INCOSE Vision 2035, or emerging challenges
- Reader can immediately see how this applies to their work

#### Good

- SE challenge is stated but motivation could be stronger
- Contribution is present but could be more specific
- Relevance to practitioners is implied rather than explicit
- Some connection to SE community concerns

#### Needs Improvement

- SE challenge is vague, generic, or absent
- Reads as generic computer science/engineering without SE focus
- No clear value proposition for practitioners
- Doesn't answer "why should an INCOSE attendee care?"
- Could be published in any engineering venue without modification

#### Self-Assessment Questions

- [ ] Can I state the SE challenge in one sentence?
- [ ] Would a practicing systems engineer recognize this challenge?
- [ ] Have I explained why solving this matters?
- [ ] Is my contribution specific to SE (not generic engineering)?

---

### 2. Accessibility and Clarity

INCOSE symposium audiences range from novice practitioners to industry leaders. Papers must be readable across this spectrum.

#### Excellent (Target)

- Readable by practitioners from novice to expert level
- Technical terms defined or contextualized on first use
- Clear logical flow from problem to solution to results
- Figures and tables enhance understanding (not just decorate)
- Writing is concise without sacrificing clarity
- One reading is sufficient to understand the main contribution
- Structure helps readers navigate (clear signposting)

#### Good

- Generally accessible to SE practitioners
- Most jargon explained
- Logical structure present
- Figures support the text adequately
- May require re-reading for full comprehension

#### Needs Improvement

- Assumes too much specialized knowledge
- Heavy unexplained jargon or acronyms
- Disorganized or hard to follow
- Figures confuse rather than clarify
- Unnecessarily verbose or dense
- Requires expert knowledge in narrow subdomain

#### Writing Style Guidelines

**Prefer:**
- Active voice ("We developed..." not "A framework was developed...")
- Concrete examples over abstract descriptions
- Short sentences for complex ideas
- Parallel structure in lists and comparisons
- Specific numbers over vague qualifiers

**Avoid:**
- Passive voice chains ("It was determined that it had been shown...")
- Undefined acronyms (define on first use, even common ones)
- Long paragraphs without breaks (aim for 4-6 sentences)
- Hedge stacking ("It might possibly be somewhat likely...")
- Nominalizations ("utilization" → "use"; "implementation" → "implement")

#### The "Breakfast Test"

> Can someone reading this over breakfast at the symposium understand your main contribution before they finish their coffee?

If not, the paper needs more clarity work.

---

### 3. Rigor and Validity

Claims must be supported. Methods must be sound. Limitations must be acknowledged.

#### Excellent (Target)

- Methods clearly articulated and justified
- Assumptions explicitly stated (not hidden)
- Evidence supports claims appropriately (not over- or under-claimed)
- Limitations honestly and specifically discussed
- Validation approach matches claim strength
- Results reproducible or verifiable by others
- Alternative approaches considered and addressed

#### Good

- Methods described adequately
- Most assumptions stated
- Evidence generally supports claims
- Some limitations noted
- Validation present but could be stronger

#### Needs Improvement

- Methods unclear or unjustified
- Hidden assumptions that affect conclusions
- Claims exceed evidence (overclaiming)
- No discussion of limitations
- Results not verifiable
- "Trust us" without supporting evidence

#### Claim-Evidence Alignment

| Claim Type | Required Evidence |
|------------|-------------------|
| "We propose a framework..." | Framework description + rationale |
| "Our framework improves..." | Comparison data or case study |
| "Our framework is better than..." | Direct comparison with alternatives |
| "Our framework solves..." | Validation demonstrating solution |
| "Our framework is optimal..." | Proof or comprehensive comparison |

**Rule:** Match claim strength to evidence strength. When in doubt, make weaker claims.

#### Limitations That Build Credibility

Good limitations sections:
- Acknowledge scope boundaries ("This applies to X but not Y")
- Note threats to validity ("Our sample was limited to...")
- Identify assumptions that could be challenged
- Suggest conditions where results might not hold
- Are specific (not generic "more research needed")

---

### 4. Novelty and Contribution

Papers must advance knowledge, not just report known things.

#### Excellent (Target)

- Clear advancement over prior work (explicitly stated)
- Novel approach, framework, method, or insight
- Fills an identified gap in SE knowledge
- Contribution is specific and defensible
- Reader learns something new and useful
- "Aha moment" is present

#### Good

- Some novelty present
- Adds to existing body of work
- Contribution is identifiable
- Incremental but meaningful advance

#### Needs Improvement

- Incremental or obvious extension
- Duplicates existing work without acknowledgment
- Contribution unclear or buried
- "So what?" question unanswered
- Review paper disguised as research paper

#### Contribution Types (All Valid)

| Type | Example | What to Emphasize |
|------|---------|-------------------|
| New Framework | Novel structure for organizing SE activities | Why existing frameworks are insufficient |
| New Method | Technique for requirements elicitation | How it differs from existing methods |
| New Application | SE applied to new domain | What adaptations were needed, lessons learned |
| Empirical Finding | Study revealing practitioner practices | Sample, methodology, generalizability |
| Synthesis | Integration of disparate SE concepts | What the integration enables |
| Case Study | Deep analysis of real project | Generalizable lessons, not just description |
| Tool/Technique | Practical aid for SE work | Validation of utility, availability |

---

### 5. Theme Alignment (IS 2026)

The 2026 theme offers opportunity for papers to resonate more deeply with the symposium.

#### IS 2026 Theme: "Beyond Digital Engineering: Seeking Wa in SE"

**Core Concept:** Wa (和) represents harmony—not passive equilibrium, but active, dynamic balance between elements.

#### Theme Dimensions

| Dimension | Description | Paper Alignment Opportunity |
|-----------|-------------|----------------------------|
| **Human-AI Harmony** | Integration of AI capabilities with human judgment and creativity | AI-assisted SE, human-in-the-loop systems, trust in automation |
| **Kansei (感性)** | Human sensibility, emotional/affective aspects | User experience in SE, stakeholder engagement, intuition in decision-making |
| **Human Systems Integration** | Sociotechnical approach ensuring human elements addressed throughout | HSI methods, human factors, organizational SE |
| **Nature-Harmonized** | Systems in balance with natural and social environments | Sustainability, environmental SE, social impact |
| **Digital Engineering Evolution** | Moving beyond pure DE to human-centric approaches | Limitations of pure automation, human-DE collaboration |
| **Cross-Cultural Integration** | Blending diverse perspectives and approaches | Global SE teams, cultural factors, inclusive design |

#### Excellent Theme Alignment

- Deep, natural connection to one or more theme dimensions
- Theme concepts woven throughout, not just mentioned in introduction
- Paper contributes to understanding how SE can achieve "harmony"
- Connection illuminates the work (not forced or superficial)

#### Good Theme Alignment

- Mentions theme connection explicitly
- Some alignment with Wa/harmony concepts
- Human factors or integration considered
- Theme adds context but isn't central

#### Missed Opportunity

- Theme connection absent despite relevant content
- Superficial theme mention in introduction only
- Forced connection that doesn't fit naturally
- Paper would benefit from theme framing but doesn't use it

#### Theme Connection Strategies

**Natural Fits:**
- Any paper on AI in SE → Human-AI harmony
- Any paper on stakeholders → Kansei/sensibility
- Any paper on complexity → Balance/harmony
- Any paper on sustainability → Nature-harmonized
- Any paper on organizational SE → Human Systems Integration
- Any paper on MBSE evolution → Beyond Digital Engineering

**Connection Techniques:**
- Frame challenge as a harmony problem (elements out of balance)
- Discuss how solution achieves integration/harmony
- Reflect on human role in your approach
- Consider what "Wa" would mean in your domain

---

### 6. Engagement and Impact

Great papers generate discussion, get cited, and change practice.

#### Excellent (Target)

- Will spark discussion among attendees
- Challenges conventional thinking or offers new perspective
- Actionable insights for practitioners (they can do something Monday)
- Memorable contributions (quotable findings or frameworks)
- Likely to be cited in future work
- Makes readers think differently about a problem

#### Good

- Interesting to target audience
- Some discussion potential
- Useful insights present
- Solid contribution to literature

#### Needs Improvement

- Dry or unengaging presentation
- No clear "aha" moments
- Unlikely to generate discussion
- Forgettable after reading
- No actionable implications

#### Creating Engagement

**Hooks:**
- Open with a provocative question or surprising fact
- Use a compelling case or example early
- Challenge a common assumption
- Promise a useful takeaway

**Memorability:**
- Name your framework/method (makes it citable)
- Create a visual that captures the key idea
- Offer a memorable formulation or principle
- Provide concrete "try this" recommendations

**Discussion Potential:**
- Acknowledge open questions
- Invite extension or critique
- Position against alternatives
- Connect to current debates in SE

---

## Section-by-Section Guidance

### Title

**Purpose:** Attract readers and convey paper's essence in 8-15 words.

#### Effective Title Patterns

| Pattern | Example | When to Use |
|---------|---------|-------------|
| [Method] for [Problem] in [Context] | "Model-Based Verification for Safety-Critical Systems in Automotive SE" | Method papers |
| [Finding]: [Implication] | "Requirements Volatility Predicts Project Risk: Evidence from 50 Defense Programs" | Empirical papers |
| [Concept]: [Elaboration] | "Harmony Engineering: Integrating HSI and MBSE for Human-AI Systems" | Framework/concept papers |
| [Question Form] | "When Does Agile SE Fail? Lessons from Complex System Programs" | Provocative/challenging papers |
| [Action] [Object] through [Means] | "Reducing Integration Defects through Early Verification Modeling" | Practice papers |

#### Title Anti-Patterns

| Anti-Pattern | Problem | Better Alternative |
|--------------|---------|-------------------|
| "A Novel Framework for..." | Generic, oversells novelty | Name the framework specifically |
| "Towards..." | Signals incomplete work | State what you actually did |
| "A Study of..." | Vague, uninformative | State what you found |
| "An Approach to..." | Could be anything | Name the approach |
| All acronyms | Excludes readers | Expand key terms |
| 25+ words | Too long to remember | Edit ruthlessly |

#### Title Checklist

- [ ] 8-15 words
- [ ] Key SE terms for discoverability
- [ ] Specific enough to differentiate from similar papers
- [ ] Comprehensible to general SE audience
- [ ] Theme keywords if naturally fitting
- [ ] Active, not passive construction

---

### Abstract

**Purpose:** Summarize the complete paper in 150-300 words. This is often the only part reviewers read carefully before deciding relevance.

#### Abstract Structure (PARC)

| Element | Content | Typical Length |
|---------|---------|----------------|
| **P**roblem | SE challenge being addressed | 1-2 sentences |
| **A**pproach | What you did to address it | 2-3 sentences |
| **R**esults | What you found/built/demonstrated | 2-3 sentences |
| **C**ontribution | Why it matters, what readers gain | 1-2 sentences |

#### Abstract Quality Indicators

**Excellent Abstract:**
- First sentence hooks with the SE challenge
- Specific about what was done (not vague "we propose...")
- Results include concrete findings or demonstrations
- Contribution is explicit and compelling
- Self-contained (no references, no undefined acronyms)
- Reader can decide relevance from abstract alone

**Abstract Red Flags:**
- Opens with background instead of problem
- Vague about methods ("various techniques were used")
- No results mentioned ("results are discussed")
- Contribution buried or missing
- Requires reading paper to understand abstract

#### Example Abstract Structure

```
[PROBLEM - 2 sentences]
Systems engineering organizations struggle to integrate AI-generated
artifacts with human-authored documentation, leading to consistency
failures and trust issues. Current approaches lack systematic methods
for maintaining traceability across human-AI collaborative work products.

[APPROACH - 2 sentences]
We present the Harmonized Documentation Framework (HDF), a structured
approach for managing human-AI collaborative SE documentation. The
framework defines artifact types, traceability relationships, and
verification procedures validated through application to three defense
programs.

[RESULTS - 2 sentences]
Application of HDF reduced documentation inconsistencies by 47% and
improved stakeholder confidence in AI-assisted artifacts from 2.3 to
4.1 on a 5-point scale. The framework successfully maintained
traceability across 2,400+ requirements through multiple AI-assisted
revision cycles.

[CONTRIBUTION - 1 sentence]
This paper contributes a practical, validated framework for achieving
harmony between human and AI contributions in SE documentation,
directly addressing the IS 2026 theme of human-AI integration.
```

---

### Introduction

**Purpose:** Motivate the work, orient the reader, and preview the contribution.

#### Introduction Structure

| Element | Purpose | Typical Length |
|---------|---------|----------------|
| Opening Hook | Capture attention with the challenge | 1-2 paragraphs |
| Context | Situate in broader SE landscape | 1-2 paragraphs |
| Problem Statement | Specific gap or need addressed | 1 paragraph |
| Contribution | What this paper offers | 1 paragraph |
| Roadmap | How paper is organized | 1 paragraph (optional) |

#### Opening Strategies

**Effective Openings:**
- Start with the SE challenge (not history or definitions)
- Use a concrete example or scenario
- Cite a compelling statistic about the problem
- Reference a known pain point for practitioners
- Connect to recent SE community discussions

**Ineffective Openings:**
- "In recent years..." (generic, overused)
- "Systems engineering is defined as..." (reader knows)
- Long historical background before stating problem
- Definition-heavy without motivation
- "This paper presents..." (skip to contribution, not meta-statement)

#### Introduction Checklist

- [ ] SE challenge clear by end of first page
- [ ] "Why should I care?" answered explicitly
- [ ] Connection to broader SE trends or Vision 2035
- [ ] Research questions or objectives stated
- [ ] Contribution previewed (reader knows what they'll get)
- [ ] Paper structure outlined (helps navigation)
- [ ] ~1-2 pages (10-15% of paper)

---

### Background/Related Work

**Purpose:** Establish context, demonstrate knowledge of the field, and position your contribution.

#### Organization Strategies

**Thematic Organization (Preferred):**
- Group related work by theme, not chronologically
- Each paragraph addresses one aspect of the problem space
- Shows gaps that your work fills
- Ends with clear positioning statement

**Comparative Organization:**
- Compare approaches along dimensions relevant to your contribution
- Table summarizing related work can be effective
- Highlight what each approach lacks that yours provides

#### Positioning Your Contribution

| Positioning Type | When to Use | Language |
|------------------|-------------|----------|
| Gap-filling | Your work addresses unaddressed problem | "No prior work has addressed..." |
| Extension | Building on specific prior work | "We extend [X] by..." |
| Integration | Combining previously separate ideas | "We integrate [X] and [Y] to..." |
| Alternative | Different approach to solved problem | "Unlike [X], our approach..." |
| Application | Existing method in new domain | "We apply [X] to [new domain]..." |

#### Related Work Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Literature dump | List without synthesis | Organize thematically, show relationships |
| Missing key citations | Appears uninformed | Review SE journals and recent symposia |
| Only citing own work | Self-promotional | Engage broadly with community |
| Straw man positioning | Unfair to prior work | Acknowledge strengths of alternatives |
| "To our knowledge, no one has..." | Often wrong, easily challenged | Be specific about the gap |

#### Background Checklist

- [ ] Key prior work in the area covered
- [ ] Organized thematically (not chronologically)
- [ ] Gap(s) this paper addresses clearly identified
- [ ] Positioning against alternatives explicit
- [ ] INCOSE/ISO standards referenced where relevant
- [ ] Fair treatment of prior work
- [ ] ~1-2 pages (10-15% of paper)

---

### Methodology/Approach

**Purpose:** Explain what you did and why, with sufficient detail for evaluation.

#### Research Paper Methodology

| Element | Content | Why It Matters |
|---------|---------|----------------|
| Assumptions | Explicit statement of premises | Allows reader to assess applicability |
| Research Questions | Specific questions addressed | Focuses evaluation |
| Method Selection | Why this method for these questions | Demonstrates rigor |
| Procedures | Step-by-step what was done | Enables reproducibility |
| Data | Sources, collection, characteristics | Assesses validity |
| Analysis | How data was processed/interpreted | Enables verification |

#### Practice Paper Methodology

| Element | Content | Why It Matters |
|---------|---------|----------------|
| Problem Context | Organizational/project setting | Allows reader to assess relevance |
| Constraints | What limited solution options | Explains choices |
| Approach | What was implemented | Core content |
| Implementation | How it was deployed | Practical details |
| Adaptation | Changes from standard practice | Shows customization |

#### Methodology Quality Indicators

**Strong Methodology:**
- Reader could replicate the work
- Choices justified, not just stated
- Alternatives considered
- Threats to validity acknowledged
- Appropriate for research questions

**Weak Methodology:**
- "We did X" without explaining why X
- Missing steps in the process
- No justification for choices
- Validation approach doesn't match claims
- Hidden assumptions

#### Methodology Checklist

- [ ] Assumptions explicitly stated
- [ ] Method/approach clearly described
- [ ] Rationale for methodological choices
- [ ] Sufficient detail for evaluation
- [ ] If empirical: data sources and collection described
- [ ] If framework: structure and components clear
- [ ] Limitations of method acknowledged
- [ ] ~2-3 pages (20-25% of paper)

---

### Results

**Purpose:** Present what you found, built, or demonstrated.

#### Results Presentation Principles

| Principle | Application |
|-----------|-------------|
| Evidence first | Present findings before interpretation |
| Visual support | Use figures/tables for complex data |
| Honest reporting | Include negative/unexpected results |
| Appropriate precision | Don't over-report decimal places |
| Clear organization | One major finding per subsection |

#### Effective Results Visualization

| Data Type | Best Visualization | Tips |
|-----------|-------------------|------|
| Comparisons | Bar charts, tables | Include baseline |
| Trends | Line charts | Label axes clearly |
| Relationships | Scatter plots | Note correlation strength |
| Processes | Flow diagrams | Keep steps minimal |
| Structures | Block diagrams | Use consistent notation |
| Categories | Tables | Sort meaningfully |

#### Framework/Method Results

For non-empirical papers, "results" means demonstrating the framework:

- **Walk through an example** - Show framework applied to realistic case
- **Demonstrate completeness** - Show it handles important scenarios
- **Validate with experts** - Report feedback from practitioners
- **Compare to alternatives** - Show advantages in specific dimensions

#### Results Checklist

- [ ] All research questions addressed
- [ ] Evidence clearly presented
- [ ] Figures/tables used effectively
- [ ] Results specific and concrete
- [ ] Negative or unexpected findings reported honestly
- [ ] Appropriate precision (not false precision)
- [ ] For frameworks: demonstration or validation included
- [ ] ~2-3 pages (20-25% of paper)

---

### Discussion

**Purpose:** Interpret results, place in context, and discuss implications.

#### Discussion Structure

| Element | Content | Purpose |
|---------|---------|---------|
| Summary | Brief recap of key findings | Orient reader |
| Interpretation | What results mean | Add insight |
| Implications | Consequences for practice | Make actionable |
| Comparison | Relation to prior work | Position contribution |
| Limitations | Scope and validity concerns | Build credibility |
| Future Work | Open questions, next steps | Invite continuation |

#### Interpretation Guidelines

**Do:**
- Connect findings to research questions
- Explain unexpected results
- Draw practical implications
- Compare to prior work findings
- Speculate carefully (label as speculation)

**Don't:**
- Simply repeat results
- Overclaim significance
- Ignore contradictory evidence
- Hide limitations
- Make unsupported generalizations

#### Limitations That Strengthen Papers

| Limitation Type | Example | How to Present |
|-----------------|---------|----------------|
| Scope | "Validated in defense domain only" | Note generalization needs |
| Sample | "12 practitioners interviewed" | Discuss representativeness |
| Method | "Self-reported data subject to bias" | Acknowledge and bound impact |
| Threats | "Hawthorne effect possible" | Explain mitigation attempts |
| Assumptions | "Assumes MBSE maturity level 3+" | State applicability bounds |

#### Discussion Checklist

- [ ] Key findings summarized and interpreted
- [ ] Implications for SE practice stated
- [ ] Results compared to related work
- [ ] Limitations honestly discussed (specific, not generic)
- [ ] Future directions suggested
- [ ] No new results introduced
- [ ] ~1-2 pages (12-15% of paper)

---

### Conclusion

**Purpose:** Summarize contribution and send reader away with key message.

#### Conclusion Elements

| Element | Purpose | Tips |
|---------|---------|------|
| Contribution Summary | Remind reader what paper offered | Be specific, not generic |
| Key Takeaways | What practitioner should remember | Limit to 3-5 points |
| Practical Impact | What changes because of this work | Make concrete |
| Closing Statement | Memorable ending | Connect to theme or big picture |

#### Conclusion Patterns

**Problem-Solution Echo:**
Restate the problem, summarize how you addressed it, emphasize the advance.

**Takeaway List:**
Enumerate 3-5 key insights readers should retain.

**Future Vision:**
End with forward-looking statement about how the contribution enables future work.

**Call to Action:**
Invite readers to apply, extend, or build on the work.

#### Conclusion Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Copy of abstract | Lazy, adds nothing | Write fresh summary |
| New content | Wrong place for it | Move to results/discussion |
| "Future work includes..." as ending | Weak finish | End with impact statement |
| Overclaiming | Undermines credibility | Match claims to evidence |
| Generic SE platitudes | Forgettable | Be specific to your contribution |

#### Conclusion Checklist

- [ ] Main contribution clearly restated
- [ ] Key takeaways explicit (3-5 points)
- [ ] Practical implications highlighted
- [ ] Forward-looking closing statement
- [ ] No new material introduced
- [ ] Memorable and quotable
- [ ] ~0.5-1 page (5-8% of paper)

---

### Acknowledgments and AI Disclosure

**Purpose:** Credit contributions and comply with AI disclosure requirements.

#### AI Disclosure Best Practices

The AI disclosure is **required**, but how you frame it matters for credibility.

**Effective Disclosure Framing:**
- Position AI as tool, human as director
- Be specific about what AI did and didn't do
- Emphasize human intellectual contribution
- Note oversight and revision process
- Match detail to usage extent

**Disclosure by Usage Level:**

| Usage Level | Disclosure Approach |
|-------------|---------------------|
| Editorial only | Brief statement sufficient |
| Analysis support | Describe what was analyzed, human interpretation |
| Content generation | Detail revision process, human intellectual contribution |
| Conceptual | Explain how ideas originated, AI's role in development |

**Example Disclosures by Level:**

*Minimal (Editorial):*
> "Grammarly assisted with grammar and style. All content is original author work."

*Moderate (Analysis + Editorial):*
> "ChatGPT (GPT-4) assisted with literature search organization and grammar review. All analysis, synthesis, and conclusions are original author work."

*Substantial (Content Generation):*
> "Claude (Opus 4.5) assisted with drafting methodology sections and documentation structure development under author direction. All research design, framework architecture, validation methodology, and conclusions are original author work. Drafts were extensively revised by the author, who maintained oversight of all AI-assisted work and made all editorial decisions."

#### Acknowledgments Checklist

- [ ] AI disclosure present and complete
- [ ] All AI tools listed with versions
- [ ] Usage categories specified
- [ ] Author oversight described
- [ ] For content generation: intellectual contribution detailed
- [ ] Funding sources acknowledged (final version only)
- [ ] Contributors thanked appropriately (final version only)

---

### References

**Purpose:** Credit sources and enable reader follow-up.

#### Reference Quality Indicators

**Strong Reference List:**
- Recent sources (within 5 years) included
- Seminal/foundational works cited
- SE-specific venues represented (SE Journal, INCOSE Symposium)
- Relevant standards cited (ISO 15288, INCOSE Handbook)
- Balanced (not all self-citations or single research group)
- Sufficient quantity (10+ for full paper)

**Reference Red Flags:**
- All sources old (nothing recent)
- Missing obvious relevant work
- Only citing own prior work
- Generic references (Wikipedia, textbooks only)
- Too few sources for claims made

#### Key SE Sources to Consider

| Source Type | Examples |
|-------------|----------|
| INCOSE Publications | Systems Engineering Journal, IS Proceedings, SE Handbook |
| Standards | ISO/IEC/IEEE 15288, ISO 42010, ISO 15926 |
| Foundational Texts | Kossiakoff, Blanchard & Fabrycky, INCOSE SE Vision 2035 |
| Recent Symposia | IS 2023-2025 proceedings |
| Working Group Products | INCOSE Technical Products |

---

## Workflow Guidance

### Recommended Authoring Sequence

#### Phase 1: Foundation (Before Writing)

**Step 1.1: Define Core Contribution**
- What is the SE challenge? (one sentence)
- What is your novel contribution? (one sentence)
- Why should INCOSE audience care? (one sentence)
- What type of paper? (research or practice)

**Step 1.2: Identify Target Audience**
- Which practitioners will benefit?
- What background can you assume?
- What will they do differently after reading?

**Step 1.3: Map to Theme**
- How does your work connect to "Seeking Wa"?
- Which theme dimension(s) align?
- Is connection natural or forced?

#### Phase 2: Structure (Outlining)

**Step 2.1: Create Detailed Outline**
- Map all sections with key points (bullet level)
- Identify figures/tables needed
- Estimate word allocation per section
- Identify evidence needed for each claim

**Step 2.2: Validate Structure**
- Does outline tell complete story?
- Is contribution clear from outline alone?
- Are sections balanced appropriately?
- Is there a logical flow?

#### Phase 3: Drafting (Core Content First)

**Step 3.1: Draft Methodology** (~2,000 words)
- What you did and why
- This is the foundation—get it right

**Step 3.2: Draft Results** (~2,000 words)
- What you found/built/demonstrated
- Include figures and tables

**Step 3.3: Draft Discussion** (~1,000 words)
- Interpretation, implications, limitations
- Connect back to research questions

#### Phase 4: Framing (Context and Summary)

**Step 4.1: Draft Introduction** (~1,000 words)
- Now you know what you're introducing
- Hook, context, problem, contribution, roadmap

**Step 4.2: Draft Background** (~1,000 words)
- Position against the work you're now citing
- Identify gaps you've addressed

**Step 4.3: Draft Conclusion** (~500 words)
- Summarize what you've presented
- End memorably

#### Phase 5: Polish (Refinement)

**Step 5.1: Write Abstract** (~250 words)
- Last, after content is stable
- PARC structure

**Step 5.2: Review and Refine**
- Check word count (target ≤6,500 to leave margin)
- Verify all claims have evidence
- Ensure accessibility
- Strengthen theme connections
- Get external review

**Step 5.3: Final Preparation**
- AI disclosure statement
- Reference formatting and completeness
- Template formatting verification
- Anonymization check
- PDF creation and metadata clearing

### Quality Checkpoints

| After Phase | Checkpoint Question |
|-------------|---------------------|
| 1 (Foundation) | Is the contribution specific and defensible? |
| 2 (Structure) | Does the outline tell a complete story? |
| 3 (Drafting) | Do results support the claimed contribution? |
| 4 (Framing) | Is "why should I care?" clear in introduction? |
| 5 (Polish) | Would a practitioner find this useful? |

---

## Common Issues and Solutions

### Content Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Weak Motivation** | "We did X" without why X matters | Open with practitioner pain point, then solution |
| **Overclaiming** | "Revolutionary breakthrough" | Match claim strength to evidence; be specific about scope |
| **Underclaiming** | Buried contribution | State contribution explicitly in intro and conclusion |
| **Missing Validation** | Framework without demonstration | Add case study, example, or evaluation |
| **Scope Creep** | Trying to cover too much | Focus on one contribution done well |

### Writing Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Jargon Overload** | Reader needs glossary | Define terms; prefer plain language |
| **Passive Voice** | "It was found that..." | Use active voice: "We found..." |
| **Long Sentences** | 40+ word sentences | Break up; one idea per sentence |
| **Vague Language** | "Various," "several," "significant" | Use specific numbers and descriptions |
| **Redundancy** | Same point repeated | Cut ruthlessly; trust the reader |

### Structure Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Front-Loading Background** | Two pages before problem stated | Move problem to first paragraph |
| **Results in Discussion** | New findings in interpretation | Separate presentation from interpretation |
| **Conclusion Repetition** | Exact copy of abstract | Write fresh summary with different emphasis |
| **Unbalanced Sections** | 4 pages of background, 1 page results | Reallocate to match guidance proportions |
| **Missing Roadmap** | Reader lost in structure | Add section overview at end of introduction |

### Submission Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| **Word Count Exceeded** | >7,000 words | Cut background, combine figures, tighten prose |
| **Missing AI Disclosure** | No disclosure statement | Add per spec requirements |
| **Identifying Information** | Author name in anonymous submission | Review all text, metadata, file properties |
| **Template Violations** | Wrong fonts, margins, styles | Use unmodified INCOSE template |
| **Incomplete References** | Missing page numbers, venues | Complete all citation fields |

---

## Best Practice Summary

### The 15 Practices of Excellent INCOSE Papers

1. **Lead with the Challenge** - Open with the SE problem, not background
2. **Answer "So What?" Early** - First page should establish why readers should care
3. **Write for Practitioners** - Primary audience is working systems engineers
4. **Show, Don't Just Tell** - Concrete examples beat abstract claims
5. **Quantify When Possible** - Numbers are more compelling than qualifiers
6. **Be Honest About Limitations** - Acknowledging scope increases credibility
7. **Connect to Practice** - Always answer "what does this mean for my project?"
8. **Embrace the Theme** - "Seeking Wa" aligns naturally with integration topics
9. **Use Figures Strategically** - One great diagram beats 500 words
10. **Front-Load Key Points** - Don't bury the contribution in section 5
11. **Respect Word Limits** - Concision is a feature, not a constraint
12. **Get External Review** - Fresh eyes catch what you've become blind to
13. **Match Claims to Evidence** - Neither overclaim nor underclaim
14. **Name Your Contribution** - Named frameworks/methods get cited
15. **End Memorably** - Conclusion should resonate, not just summarize

---

## Verification vs. Validation

Understanding the distinction helps use spec and guidance appropriately.

### Verification (Against spec-for-incose-paper)

Deterministic checks with yes/no answers:

- Is word count ≤7,000?
- Are all required sections present?
- Is AI disclosure included?
- Does it use INCOSE template?
- Is it properly anonymized?

**Tool:** Checklist, automated verification

### Validation (Against This Guidance)

Qualitative assessment requiring judgment:

- Is the SE challenge compelling?
- Is the paper accessible to practitioners?
- Are claims supported by appropriate evidence?
- Will it spark discussion at the symposium?
- Does it connect meaningfully to the theme?
- Is it likely to be cited?

**Tool:** Expert review, self-assessment against criteria

---

## Self-Assessment Rubric

Use this rubric to evaluate your paper before submission.

### Overall Quality Assessment

| Criterion | Poor (1) | Fair (2) | Good (3) | Excellent (4) |
|-----------|----------|----------|----------|---------------|
| SE Relevance | No clear SE connection | SE mentioned but not central | Clear SE challenge addressed | Compelling SE challenge, practice impact obvious |
| Accessibility | Expert-only readable | Some jargon unexplained | Generally accessible | Clear to novice and expert alike |
| Rigor | Claims unsupported | Some evidence gaps | Most claims supported | All claims appropriately evidenced |
| Novelty | Obvious or duplicate | Minor advance | Clear contribution | Significant new insight |
| Theme Alignment | No connection | Superficial mention | Natural connection | Deep integration with theme |
| Engagement | Dry, forgettable | Competent but routine | Interesting, useful | Discussion-provoking, memorable |

**Scoring:**
- 20-24: Excellent - strong acceptance candidate
- 15-19: Good - competitive, may need minor revision
- 10-14: Fair - needs significant improvement
- 6-9: Poor - major revision needed

---

## Related Documents

| Document | Relationship | Purpose |
|----------|--------------|---------|
| `v:spec:incose-paper` | Coupled specification | Structural requirements (verification) |
| `INCOSE-IS2026-REQUIREMENTS-CACHE.md` | Reference source | Complete research cache |
| INCOSE Paper Evaluation Criteria | External standard | Official reviewer criteria |
| INCOSE SE Vision 2035 | Context | Strategic SE direction |
| IS 2026 Call for Submissions | External standard | Official requirements |

---

## Self-Consistency Note

This guidance document demonstrates the quality criteria it defines:

- **Relevance:** Specifically addresses INCOSE paper authoring challenges
- **Accessibility:** Clear language, structured for scanning, tables for quick reference
- **Rigor:** Criteria are specific and assessable with examples
- **Contribution:** Provides actionable guidance beyond generic paper-writing advice
- **Theme Alignment:** Naturally connects to human-AI collaboration (AI disclosure guidance)
- **Engagement:** Practical tips, anti-patterns, examples, and checklists

---

**Note:** This guidance (v2.0.0) is derived from comprehensive research of INCOSE Paper Evaluation Criteria, Best Paper Award criteria, SE Vision 2035, and IS 2026 theme materials. It is coupled with `spec-for-incose-paper` (v2.0.0) via a coupling edge, forming the assurance foundation for INCOSE paper quality.
