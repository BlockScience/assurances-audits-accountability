---
type: vertex/guidance
extends: doc
id: v:guidance:property
name: Guidance for Property Documents
description: Quality criteria and best practices for creating excellent property documents defining abstract attributes that can be possessed by vertices
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
dependencies: []
---

# Guidance for Property Documents

**This guidance defines quality criteria and best practices for creating excellent property documents.**

## Purpose

While [[spec-for-property]] defines what structural elements must be present, this guidance helps authors assess **how well** a property document establishes clear, abstract characteristics that become real when possessed by vertices. Great properties understand the reference/referent distinction and define appropriate acquisition and applicability.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating property documents by providing:
- Quality assessment criteria for properties
- Best practices for defining abstract attributes and characteristics
- Understanding the reference/referent relationship
- Guidance on property specialization through inheritance
- Common pitfalls and solutions
- Section-by-section authoring advice
- Workflow recommendations for property creation

### Best Use Cases

Use this guidance when:
- Creating a new property type that can be possessed by vertices
- Reviewing an existing property for clarity and applicability
- Teaching others about property abstraction and the reference/referent distinction
- Designing property types that will be specialized through inheritance
- Evaluating whether a property serves its domain purpose

## Philosophical Foundation: Reference vs Referent

### The Core Distinction

**Property as Referent (Abstract):**
- A property document defines what a characteristic IS in the abstract
- Properties exist as concepts/definitions, not as concrete possessions
- The property itself has no reality until possessed

**Possession as Reference (Concrete):**
- A vertex possesses a property → creates a concrete reference
- The possession relationship (edge) makes the abstract property real for that vertex
- Example: `skill:python-basics` is abstract; `student:alice has-skill skill:python-basics` is concrete

### Why This Matters

**Excellent property documents:**
- Clearly define the abstract characteristic
- Explain what it means when possessed (how abstract becomes concrete)
- Specify which vertex types can possess it (applicability)
- Describe how the property is acquired or assigned

**Poor property documents:**
- Confuse the property with its possession
- Fail to explain the abstract definition
- Don't clarify which vertices can possess it

## Quality Criteria

### 1. Abstraction Clarity

**Excellent:**
- Property definition is clearly abstract (defines WHAT the characteristic is)
- Distinction between property-as-concept and property-as-possessed is clear
- Definition works regardless of who possesses it
- Easy to understand the property independent of any specific possessor

**Good:**
- Property is defined abstractly
- Generally clear what the characteristic is
- Some explanation of possession

**Needs Improvement:**
- Conflates property with possession
- Definition only makes sense for specific vertices
- Unclear what the abstract characteristic is
- Assumes concrete context

### 2. Acquisition Clarity

**Excellent:**
- Clear explanation of HOW the property is acquired or assigned
- Acquisition process is well-defined (earned, learned, assigned, inherent)
- Different acquisition methods for different vertex types (if applicable)
- Realistic and verifiable

**Good:**
- Acquisition is mentioned
- Process is generally clear
- Some detail provided

**Needs Improvement:**
- No explanation of how property is acquired
- Acquisition is vague or unrealistic
- Unclear who can assign/grant the property

### 3. Applicability Specificity

**Excellent:**
- Clearly specifies which vertex types can possess this property
- Explains WHY those vertex types are appropriate
- References vertex type specs when available
- Handles edge cases (can any vertex possess it? specific types only?)

**Good:**
- Applicable vertex types are listed
- Some explanation provided
- Generally appropriate

**Needs Improvement:**
- No specification of applicable vertices
- "Any vertex can possess it" without justification
- Unclear why certain vertices are excluded
- Applicability doesn't match property definition

### 4. Specialization Potential

**Excellent:**
- If base property: Clear pattern for specialization shown
- If specialized property: Relationship to parent explained
- Extension adds meaningful constraints or context
- Easy to understand when to use base vs. specialized

**Good:**
- Specialization is possible/explained
- Some guidance on extension
- Relationship to parent present (if specialized)

**Needs Improvement:**
- No guidance on specialization
- Unclear when to extend vs. use directly
- Specialized property adds no value over parent
- Extension breaks parent's abstraction

### 5. Domain Relevance

**Excellent:**
- Property serves clear purpose in its domain
- Definition aligns with domain concepts
- Acquisition and applicability are domain-appropriate
- Easy to see how this property is used in practice

**Good:**
- Property is relevant to domain
- Generally appropriate
- Domain purpose is stated

**Needs Improvement:**
- Unclear why this property exists
- Domain fit is questionable
- Seems like arbitrary characteristic

## The Specialization Pattern

### Why Specialize Properties

Properties are often specialized to restrict applicability to specific vertex types:

**Pattern:**
```
property (base - any vertex)
  ↓ extends
skill (specialized - actors only)
  ↓ extends
certification (specialized - professionals only)
```

**When to Specialize:**
- When you need type-specific acquisition rules
- When property only makes sense for certain vertices
- When you need to add type-specific constraints
- When domain demands it (e.g., skills for actors, statuses for systems)

### Example: Skill extends Property

**property (base):**
- Can be possessed by ANY vertex
- Generic acquisition: "obtained through process"
- Generic applicability: "applicable vertices"

**skill (specialized):**
- Can be possessed by ACTORS (specifically students)
- Specific acquisition: "learned through study and practice"
- Specific applicability: "actors engaged in learning"
- Adds: learning outcomes, prerequisite skills

This specialization is **valuable** because:
- It restricts to appropriate domain (education)
- It adds meaningful constraints (learning-specific)
- It provides clearer guidance for skill creation

## Section-by-Section Guidance

### Property Definition

**Purpose:** Define WHAT this characteristic is in the abstract

**Tips:**
- Focus on the essence of the characteristic
- Don't conflate with possession (the property exists as concept)
- Use clear, domain-appropriate terminology
- Explain what it MEANS when a vertex possesses this

**Examples:**
- ✅ "A skill is a learnable capability or knowledge area"
- ✅ "A status is a state or condition a system can be in"
- ❌ "A skill is something students have" (conflates property with possession)
- ❌ "A property" (circular definition)

**Reference vs Referent:**
- The definition describes the REFERENT (abstract concept)
- The possession creates a REFERENCE (concrete instance)

### Acquisition

**Purpose:** Explain HOW this property is obtained

**Tips:**
- Be specific about the process or mechanism
- Indicate who/what can grant or assign the property
- Distinguish earned vs. assigned vs. inherent
- Make acquisition verifiable when possible

**Categories:**
- **Learned:** Acquired through study, practice, experience
- **Assigned:** Granted by authority or system
- **Earned:** Achieved through meeting criteria
- **Inherent:** Intrinsic to the vertex type

**Examples:**
- ✅ "Learned through study and practice with assessment"
- ✅ "Assigned by organizational authority"
- ✅ "Earned by completing certification requirements"
- ❌ "Somehow obtained" (too vague)

### Applicable Actors (or Applicable Vertices)

**Purpose:** Specify WHICH vertices can possess this property

**Tips:**
- Be explicit about vertex types (not just "any vertex")
- Explain WHY those types are appropriate
- Reference vertex type specs when available
- If truly generic, justify why any vertex can possess it

**Levels of Restriction:**
- **Unrestricted:** Any vertex can possess (rare, needs justification)
- **Category-restricted:** Only certain categories (e.g., only actors)
- **Type-restricted:** Only specific types (e.g., only students)
- **Instance-restricted:** Only specific instances (very specific properties)

**Examples:**
- ✅ "`vertex/student`: Students can possess skills as part of learning"
- ✅ "`vertex/actor`: Any actor can have this status"
- ❌ "Anything can have this" (unclear why unrestricted)

### Verification (Optional but Recommended)

**Purpose:** Explain how to verify possession

**Tips:**
- Provide concrete verification methods
- Make verification observable or testable
- Distinguish self-attestation from external verification
- Consider who has authority to verify

**Examples:**
- ✅ "Assessment results demonstrate skill possession"
- ✅ "Certificate issued by recognized authority"
- ✅ "Observable behavior matching property definition"
- ❌ "Trust the vertex" (unverifiable)

## Workflow Guidance

### Recommended Authoring Sequence

1. **Identify the Abstract Characteristic** (15 minutes)
   - What characteristic do you need to model?
   - Is it truly abstract (exists as concept)?
   - What does it mean independent of possession?
   - **Checkpoint:** Can you define it without reference to specific possessors?

2. **Define the Property** (15 minutes)
   - Write clear abstract definition
   - Explain what possession means
   - Use domain-appropriate terminology
   - **Checkpoint:** Is the definition clear and abstract?

3. **Specify Acquisition** (15 minutes)
   - How is this property obtained?
   - Who/what grants or assigns it?
   - Is it learned, assigned, earned, or inherent?
   - **Checkpoint:** Is acquisition process clear and realistic?

4. **Determine Applicability** (15 minutes)
   - Which vertex types can possess this?
   - Why those types and not others?
   - Reference vertex type specs
   - **Checkpoint:** Is applicability justified?

5. **Consider Specialization** (10 minutes)
   - Is this a base property for extension?
   - Or a specialized property extending a parent?
   - Document the pattern
   - **Checkpoint:** Is the inheritance relationship clear?

### Total Estimated Time: 70 minutes

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Conflation | Property defined in terms of possession | Define abstractly: what IS this characteristic? |
| No Acquisition | Unclear how property is obtained | Specify: learned, assigned, earned, or inherent |
| Vague Applicability | "Any vertex can have this" | Be specific about vertex types and justify |
| No Specialization Guidance | When to extend unclear | Document base pattern or parent relationship |
| Circular Definition | "A property is a property" | Define essence: what characteristic does it represent? |
| Possession Confusion | "Who has this property" in definition | Keep definition abstract, possession is separate |

## Best Practices

1. **Define Abstractly** - Properties are concepts/referents until possessed
2. **Explain Acquisition Clearly** - Be specific about how properties are obtained
3. **Specify Applicability** - Which vertex types can possess this and why
4. **Show Specialization Pattern** - If base, show extension; if specialized, show parent relationship
5. **Keep Reference/Referent Distinct** - Don't conflate property definition with possession
6. **Consider Verification** - How can possession be verified or demonstrated
7. **Use Domain Terms** - Properties should align with domain concepts

## Specialization Guidance

### When to Create Base Property

Create a base (generic) property when:
- The characteristic could apply to multiple vertex types
- You want to enable domain-specific specializations
- The property is fundamentally abstract
- Acquisition varies by vertex type

**Example:** `property` as base for `skill`, `status`, `role`, etc.

### When to Specialize Property

Specialize an existing property when:
- You need to restrict to specific vertex types
- Acquisition rules are type-specific
- Domain requires specialized handling
- Parent property is too generic for your needs

**Example:** `skill extends property` to restrict to actors and add learning-specific sections

### Extension Anti-Patterns

**Don't:**
- ❌ Specialize without adding value
- ❌ Break parent's abstraction
- ❌ Create deep inheritance chains (property → A → B → C → D)
- ❌ Specialize just to rename

**Do:**
- ✅ Add meaningful constraints
- ✅ Restrict applicability appropriately
- ✅ Keep inheritance shallow (1-2 levels)
- ✅ Specialize for domain clarity

## Validation vs. Verification

**Verification** (deterministic):
- All required sections present
- Applicable Actors/Vertices lists 1+ item
- ID format correct
- Tags include [vertex, property]

**Validation** (qualitative):
- Abstraction clarity (property as referent)
- Acquisition process clarity and realism
- Applicability appropriateness and justification
- Specialization pattern clarity (if applicable)
- Domain relevance and fit
- Reference/referent distinction maintained

---

**Note:** Property is a foundational type for abstract characteristics. Understanding the reference/referent distinction is critical - properties are concepts that become real through possession by vertices.
