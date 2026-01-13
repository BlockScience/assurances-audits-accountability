---
type: vertex/guidance
extends: doc
id: v:guidance:persona
name: Guidance for Persona Documents
description: Quality criteria and best practices for creating excellent persona documents defining AI identity, expertise, approach, tone, and boundaries
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-27T22:00:00Z
modified: 2025-12-27T22:00:00Z
dependencies: []
---

# Guidance for Persona Documents

**This guidance defines quality criteria and best practices for creating excellent persona documents.**

## Purpose

While [[spec-for-persona]] defines what structural elements must be present, this guidance helps authors assess **how well** a persona establishes clear, credible AI identity. Great personas are specific, coherent, honest, and aligned with purpose.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating persona documents by providing:
- Quality assessment criteria for personas
- Best practices for defining AI identity, expertise, and boundaries
- Common pitfalls and solutions
- Section-by-section authoring advice
- Workflow recommendations for persona creation

### Best Use Cases

Use this guidance when:
- Creating a new persona for an AI model in the PPP framework
- Reviewing an existing persona for specificity and credibility
- Teaching others how to define effective AI identities
- Evaluating whether a persona establishes clear expectations
- Designing persona AFTER purpose (to match needed expertise)

## Quality Criteria

### 1. Role Specificity

**Excellent:**
- Role is highly specific and credible (e.g., "expert document analyst", "experienced teacher")
- Professional identity is clear and memorable
- Role matches purpose domain and requirements
- Avoids vague descriptions like "helpful assistant"

**Good:**
- Role is reasonably specific
- Professional identity is stated
- Generally appropriate for purpose

**Needs Improvement:**
- Role is vague or generic ("helpful AI", "assistant")
- No clear professional identity
- Doesn't match purpose domain

### 2. Expertise Appropriateness

**Excellent:**
- Lists 2-4 specific, focused expertise areas
- Uses domain-appropriate terminology
- Expertise directly enables purpose objectives
- Realistic breadth (not claiming impossible scope)

**Good:**
- Lists relevant expertise areas
- Generally appropriate depth
- Mostly enables purpose

**Needs Improvement:**
- Too few areas (too narrow) or too many (impossibly broad)
- Vague expertise claims
- Expertise doesn't support purpose
- Claims to "know everything"

### 3. Approach Clarity

**Excellent:**
- Describes HOW the AI thinks and works in behavioral terms
- Thinking style is clear (systematic, creative, analytical, collaborative)
- Working method is explicit
- Approach aligns with planned protocol

**Good:**
- Approach is stated
- Some behavioral description
- Reasonably clear methodology

**Needs Improvement:**
- No description of thinking style or methodology
- Vague statements ("I work hard")
- Approach doesn't fit purpose or protocol

### 4. Tone Appropriateness

**Excellent:**
- Tone is clearly defined (analytical, patient, professional, encouraging)
- Formality level is explicit
- Tone is appropriate for use case and audience
- Consistent with role, approach, and purpose

**Good:**
- Tone is stated
- Generally appropriate
- Mostly consistent

**Needs Improvement:**
- Tone is undefined or vague
- Inappropriate for use case (e.g., casual tone for technical analysis)
- Inconsistent with role or approach

### 5. Boundary Honesty

**Excellent:**
- Explicitly states 3+ clear limitations
- Defines scope boundaries to prevent overreach
- Acknowledges constraints honestly
- Sets realistic expectations

**Good:**
- Some boundaries stated
- Most limitations mentioned
- Generally realistic

**Needs Improvement:**
- No boundaries or limitations stated
- Claims unlimited capability
- Scope creep likely due to unclear boundaries

### 6. Internal Coherence

**Excellent:**
- All elements align: role, expertise, approach, tone work together
- No contradictions between sections
- Creates unified, believable persona
- Persona as a whole feels coherent and credible

**Good:**
- Most elements align
- Few minor contradictions
- Generally coherent

**Needs Improvement:**
- Elements contradict each other
- Expertise doesn't match role
- Tone conflicts with approach
- Feels incoherent or patchwork

### 7. Obsidian Compatibility

**Excellent:**
- Links to related purpose and protocol documents when applicable
- Uses consistent ID format (`v:persona:<name>`)
- Tags properly included in frontmatter
- Cross-references use `[[id]]` syntax where helpful

**Good:**
- Basic linking present
- ID format correct
- Tags included

**Needs Improvement:**
- No cross-references where appropriate
- ID format inconsistent
- Missing tags

## Section-by-Section Guidance

### Role and Identity

**Purpose:** Establish WHO the AI is - the core professional identity

**Tips:**
- Be specific - use credible professional titles
- Match the role to the purpose domain
- Make it memorable and distinctive
- Avoid vague generalities

**Examples:**
- ✅ "You are an expert document analyst specializing in pattern recognition"
- ✅ "You are an experienced teacher of the PPP framework"
- ❌ "You are a helpful assistant" (too vague)

### Domain Expertise

**Purpose:** Define WHAT the AI knows and can do

**Tips:**
- List 2-4 specific areas (not too narrow, not impossibly broad)
- Use domain-appropriate terminology
- Ensure expertise enables the purpose objectives
- Be realistic about depth vs. breadth

**Anti-patterns:**
- ❌ Claiming to know "everything about all documents"
- ❌ Listing 10+ expertise areas (impossibly broad)
- ❌ Single narrow area when purpose requires more
- ✅ 2-4 focused, relevant areas

### Approach and Methodology

**Purpose:** Describe HOW the AI thinks and works

**Tips:**
- Describe thinking style behaviorally
- Explain working method
- Ensure approach supports purpose and aligns with protocol
- Use concrete terms (systematic, collaborative, evidence-based)

**Examples:**
- ✅ "Your analytical approach is systematic and evidence-based"
- ✅ "You take a collaborative, iterative approach"
- ❌ "You work well" (too vague)

### Communication Tone

**Purpose:** Specify HOW the AI communicates

**Tips:**
- Define tone clearly (analytical, patient, professional, encouraging)
- Specify formality level
- Ensure tone is appropriate for use case
- Must be consistent with approach and role

**Anti-patterns:**
- ❌ Analytical persona with casual, chatty tone
- ❌ Teaching persona with curt, dismissive tone
- ✅ Analytical work → analytical tone
- ✅ Teaching → patient, encouraging tone

### Boundaries and Limitations

**Purpose:** Define what the AI does NOT do or claim

**Tips:**
- List at least 3 explicit limitations
- Be honest about constraints
- Define scope to prevent overreach
- Manage user expectations

**Examples:**
- ✅ "You only analyze documents provided by users"
- ✅ "You require minimum 2 examples to identify patterns"
- ✅ "You acknowledge uncertainty when appropriate"
- ❌ No boundaries stated (suggests unlimited capability)

## Workflow Guidance

### Recommended Authoring Sequence

1. **Review Purpose First** (10 minutes)
   - Read the purpose document thoroughly
   - Identify what expertise is needed
   - Consider what role would achieve this purpose
   - **Checkpoint:** Can you identify what kind of expert is needed?

2. **Define Core Identity** (10 minutes)
   - Write the role/identity statement
   - Be specific about professional identity
   - Ensure it matches purpose domain
   - **Checkpoint:** Is the role specific, credible, and appropriate?

3. **Specify Expertise** (15 minutes)
   - List 2-4 areas of expertise
   - Use domain-appropriate terminology
   - Ensure expertise enables purpose objectives
   - Check breadth is realistic
   - **Checkpoint:** Does expertise enable purpose objectives?

4. **Describe Approach and Tone** (15 minutes)
   - Describe how AI thinks and works
   - Define communication tone
   - Ensure both match purpose and planned protocol
   - **Checkpoint:** Do approach and tone support the work?

5. **Set Boundaries** (10 minutes)
   - List explicit limitations (3+)
   - Be honest about constraints
   - Define scope limits
   - **Checkpoint:** Are boundaries clear and realistic?

### Total Estimated Time: 60 minutes

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Vague Role | Generic "helpful assistant" identity | Be specific: "expert document analyst", "experienced teacher" |
| Too Much Expertise | Claiming to know everything | Focus on 2-4 specific, relevant areas |
| Missing Approach | No description of HOW AI works | Add behavioral description of methodology |
| No Boundaries | Unlimited capability implied | Explicitly list what AI doesn't do (3+ items) |
| Tone Mismatch | Tone conflicts with role/purpose | Align tone with professional role and use case |
| Incoherence | Elements contradict each other | Ensure all sections align and support each other |

## Best Practices

1. **Design Persona AFTER Purpose** - Know what expertise is needed to achieve the purpose
2. **Be Specific About Role** - Avoid vague descriptions, use credible professional identities
3. **List 2-4 Focused Expertise Areas** - Not too narrow, not impossibly broad
4. **Describe Approach Behaviorally** - Use concrete terms for thinking style and method
5. **Choose Appropriate Tone** - Match tone to use case (analytical for analysis, patient for teaching)
6. **Be Honest About Boundaries** - Users trust AIs that acknowledge limitations
7. **Ensure Internal Coherence** - All elements (role, expertise, approach, tone) must align
8. **Make Persona Memorable** - Distinctive identity helps users understand and trust the AI

## Validation vs. Verification

**Verification** (deterministic):
- All required sections present
- Expertise lists 2-4 items
- Boundaries lists 3+ items
- ID format correct

**Validation** (qualitative):
- Role specificity and credibility
- Expertise appropriateness for purpose
- Approach clarity and behavioral description
- Tone appropriateness and consistency
- Boundary honesty and realism
- Internal coherence across all elements

---

**Note:** This guidance supports the PPP (Persona-Purpose-Protocol) framework. Persona should be designed AFTER Purpose to ensure expertise matches what's needed to achieve objectives.
