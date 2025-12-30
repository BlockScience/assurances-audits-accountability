---
type: vertex/guidance
extends: doc
id: v:guidance:novel-contributions
name: Guidance for Novel Contributions Documents
description: Quality criteria and best practices for creating effective novel contributions documents
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-30T18:00:00Z
modified: 2025-12-30T18:00:00Z
criteria:
  - contribution-clarity
  - novelty-calibration
  - evidence-quality
  - ranking-coherence
  - actionability
  - intellectual-honesty
dependencies: []
---

# Guidance for Novel Contributions Documents

**This guidance defines quality criteria and best practices for novel contributions documents that effectively communicate research novelty.**

## Purpose

This guidance helps authors create novel contributions documents that accurately characterize, rank, and communicate intellectual contributions. While the spec-for-novel-contributions defines structural requirements, this guidance evaluates whether contributions are well-characterized, appropriately ranked, and useful for their intended purpose.

## Document Overview

### What This Guidance Covers

Novel contributions documents enumerate research contributions with novelty assessments. This guidance evaluates:

- Clarity of contribution descriptions
- Calibration of novelty claims
- Quality of supporting evidence
- Coherence of rankings
- Actionability of recommendations
- Intellectual honesty about limitations

### Best Use Cases

- **Pre-writing:** Inventory contributions before drafting a paper
- **Self-assessment:** Evaluate which contributions deserve emphasis
- **Collaboration:** Align co-authors on contribution significance
- **Review preparation:** Anticipate reviewer questions about novelty
- **Archive:** Document contributions for future reference

## Quality Criteria

### 1. Contribution Clarity

**Definition:** Each contribution is described clearly enough that readers understand what it is and why it matters.

| Level | Indicators |
|-------|------------|
| **Excellent** | Contributions are self-contained explanations; a reader unfamiliar with the work can understand each contribution from its entry alone. Technical terms are explained or contextualized. |
| **Good** | Contributions are clear to domain experts; some familiarity with the work helps but isn't required. Minor ambiguities exist but don't impede understanding. |
| **Needs Improvement** | Contributions assume too much context; unclear what is actually being contributed vs. what existed before. Jargon without explanation. |

### 2. Novelty Calibration

**Definition:** Novelty claims are appropriately calibrated—neither overclaimed nor underclaimed.

| Level | Indicators |
|-------|------------|
| **Excellent** | Novelty levels accurately reflect comparison to prior art. "Highly novel" contributions are genuinely first-known formalizations. Incremental work is honestly labeled. Calibration shows awareness of related work. |
| **Good** | Novelty levels are reasonable with minor calibration issues. May slightly over- or under-claim in 1-2 entries, but overall assessment is sound. |
| **Needs Improvement** | Systematic over-claiming (everything is "highly novel") or under-claiming (genuine contributions labeled incremental). Lack of awareness of prior art. |

### 3. Evidence Quality

**Definition:** Each contribution is supported by concrete, verifiable evidence from the work itself.

| Level | Indicators |
|-------|------------|
| **Excellent** | Evidence is specific and verifiable: file names, code references, experimental results, or documented artifacts. A reader could verify claims by examining the referenced evidence. |
| **Good** | Evidence is present and reasonable but less specific. Claims are plausible given the evidence, though independent verification would require more work. |
| **Needs Improvement** | Evidence is vague, missing, or does not support the claimed contribution. Assertions without substantiation. |

### 4. Ranking Coherence

**Definition:** The ranking of contributions is internally consistent and defensible.

| Level | Indicators |
|-------|------------|
| **Excellent** | Rankings reflect a clear, consistent logic (e.g., novelty + impact + relevance). Higher-ranked contributions are demonstrably more significant. The ranking would survive challenge from a skeptical reviewer. |
| **Good** | Rankings are reasonable with defensible logic. Minor reorderings might be argued, but the overall hierarchy makes sense. |
| **Needs Improvement** | Rankings appear arbitrary or inconsistent. Lower-ranked contributions seem more significant than higher-ranked ones. Logic behind ranking is unclear. |

### 5. Actionability

**Definition:** The document provides clear guidance on how to use the contributions for the intended purpose.

| Level | Indicators |
|-------|------------|
| **Excellent** | Each contribution includes specific guidance for the target output (e.g., "central thesis," "supporting material," "future work"). Key insights are directly actionable. A paper writer could use this as a blueprint. |
| **Good** | Guidance is present but somewhat generic. Actionable recommendations exist but may require interpretation for specific use. |
| **Needs Improvement** | No clear guidance on how to use contributions. Document inventories contributions but doesn't help author decide emphasis or treatment. |

### 6. Intellectual Honesty

**Definition:** The document honestly acknowledges limitations, gaps, and areas where claims are uncertain.

| Level | Indicators |
|-------|------------|
| **Excellent** | Explicitly identifies limitations, discovered issues, and areas of uncertainty. Distinguishes between confident and tentative novelty claims. Acknowledges what the work does NOT contribute. |
| **Good** | Generally honest with some acknowledgment of limitations. May not fully explore all uncertainties but doesn't overclaim. |
| **Needs Improvement** | Presents only positive framing; ignores or minimizes limitations. No acknowledgment of discovered issues or areas of uncertainty. |

## Section-by-Section Guidance

### Introduction

**Purpose:** Orient readers to the research context and document purpose.

**Tips:**
- State the research project/context clearly in the first paragraph
- Explain why this contributions inventory exists (paper writing, self-assessment, etc.)
- Preview the ranking methodology used
- Keep it concise—1-3 paragraphs maximum

**Anti-patterns:**
- ❌ Jumping into contributions without context
- ❌ Over-long introductions that delay the substance
- ❌ Failing to explain the ranking/organization scheme

### Contribution Entries

**Purpose:** Document each contribution with sufficient detail to understand and use it.

**Tips:**
- Lead with the most novel/important contributions
- Make "What" descriptions self-contained
- In "Why" sections, explicitly compare to prior art when possible
- Evidence should be specific enough to verify
- Projections should be concrete recommendations, not vague suggestions

**Anti-patterns:**
- ❌ "What" descriptions that require reading the whole project to understand
- ❌ "Why" sections that assert novelty without reasoning
- ❌ Evidence that is generic or unverifiable ("we did experiments")
- ❌ Projections that just restate novelty level ("include because it's novel")

### Summary Table

**Purpose:** Provide at-a-glance overview of all contributions and their treatment.

**Tips:**
- Maintain strict alignment with individual entries
- Use consistent novelty level terminology
- Treatment column should be specific (not just "include" or "mention")
- Table should be scannable—brief entries, not sentences

**Anti-patterns:**
- ❌ Summary that contradicts individual entries
- ❌ Vague treatment recommendations
- ❌ Missing contributions from table
- ❌ Overly verbose table cells

### Key Insights

**Purpose:** Synthesize patterns and provide actionable recommendations.

**Tips:**
- Focus on insights that emerge from the collection, not just individual contributions
- Prioritize actionable recommendations over observations
- Connect insights to the target output (paper, presentation, etc.)
- Order by importance or natural sequence

**Anti-patterns:**
- ❌ Insights that just summarize contributions without synthesis
- ❌ Generic advice that could apply to any research
- ❌ Missing connection to intended use

## Workflow Guidance

### Recommended Authoring Sequence

1. **Brainstorm (30 min):** List all potential contributions without filtering
2. **Characterize (45 min):** For each, write What/Why/Evidence
3. **Rank (30 min):** Order by novelty and significance
4. **Calibrate (20 min):** Review novelty claims against prior art awareness
5. **Synthesize (20 min):** Write summary table and key insights
6. **Review (15 min):** Check for intellectual honesty and gaps

**Total:** ~2.5 hours for initial draft

### Quality Checkpoints

After each phase, verify:

- **After Brainstorm:** Did you include everything, even small contributions?
- **After Characterize:** Can each contribution stand alone?
- **After Rank:** Would a reviewer agree with the ordering?
- **After Calibrate:** Are you being honest about novelty?
- **After Synthesize:** Are insights actionable?

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Everything is "highly novel" | Overclaiming reduces credibility | Recalibrate against prior art; most work has only 1-2 highly novel contributions |
| Evidence is vague | Claims are unverifiable | Point to specific artifacts: files, commits, test results |
| Rankings feel arbitrary | No clear logic | Establish explicit criteria (novelty × impact × relevance) and apply consistently |
| Contributions overlap | Redundancy in list | Merge related contributions or make distinctions explicit |
| Missing limitations | Intellectual dishonesty | Add "Discovered" category for issues found during work |
| Projections are generic | Not actionable | Specify exactly how each contribution should appear in target |

## Best Practices

1. **Be honest about novelty**—overclaiming damages credibility more than underclaiming
2. **Specific evidence beats general claims**—point to artifacts
3. **Distinguish contribution from implementation**—what's new vs. how you built it
4. **Include discovered limitations**—shows intellectual honesty
5. **Rank ruthlessly**—not everything can be "central thesis"
6. **Compare to prior art**—novelty is relative to what exists
7. **Make it actionable**—the document should guide paper writing
8. **Review with skeptical eyes**—would a reviewer accept these claims?
9. **Update as understanding evolves**—novelty assessment can change
10. **Use consistent terminology**—define novelty levels and stick to them

## Validation Guidance

When validating a novel contributions document, assess:

1. **Could a reader understand each contribution without external context?** (Clarity)
2. **Would domain experts agree with the novelty assessments?** (Calibration)
3. **Can claims be verified from the cited evidence?** (Evidence)
4. **Does the ranking make sense given the novelty assessments?** (Coherence)
5. **Could a paper writer use this as a blueprint?** (Actionability)
6. **Are limitations and uncertainties acknowledged?** (Honesty)

A document that scores "Good" or "Excellent" on all six criteria is ready for use. Documents with "Needs Improvement" on any criterion should be revised before relying on them for paper writing.

## Self-Consistency

This guidance document itself demonstrates quality criteria:

- ✓ **Contribution Clarity:** Each criterion is explained with levels
- ✓ **Novelty Calibration:** We don't overclaim what this guidance achieves
- ✓ **Evidence Quality:** Examples and anti-patterns are specific
- ✓ **Ranking Coherence:** Criteria are ordered by importance (clarity first)
- ✓ **Actionability:** Workflow, checkpoints, and common issues are concrete
- ✓ **Intellectual Honesty:** Common issues section acknowledges failure modes

---

**Note:** This guidance pairs with `spec-for-novel-contributions.md` via a coupling edge. The spec defines what must be present; this guidance defines what makes it good.
