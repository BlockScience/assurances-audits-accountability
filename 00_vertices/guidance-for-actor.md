---
type: vertex/guidance
extends: doc
id: v:guidance:actor
name: Guidance for Actor Documents
description: Quality criteria and best practices for creating excellent actor documents defining entities that can act, possess properties, and participate in relationships
tags:
  - vertex
  - doc
  - guidance
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
dependencies: []
---

# Guidance for Actor Documents

**This guidance defines quality criteria and best practices for creating excellent actor documents.**

## Purpose

While [[spec-for-actor]] defines what structural elements must be present, this guidance helps authors assess **how well** an actor document establishes clear identity, actionable capabilities, and appropriate property types. Great actors are specific, purposeful, and domain-appropriate.

## Document Overview

### What This Guidance Covers

This guidance supports authors creating actor documents by providing:
- Quality assessment criteria for actors
- Best practices for defining actor identity, capabilities, and properties
- Common pitfalls and solutions
- Section-by-section authoring advice
- Workflow recommendations for actor creation

### Best Use Cases

Use this guidance when:
- Creating a new actor type for a domain (student, staff, team, etc.)
- Reviewing an existing actor for clarity and completeness
- Teaching others how to define entity types
- Evaluating whether an actor type serves its purpose
- Extending the base actor type for domain-specific needs

## Quality Criteria

### 1. Identity Clarity

**Excellent:**
- Actor identity is highly specific and unambiguous
- Clear explanation of what this actor IS (type of entity)
- Role in the system is explicit
- Easy to distinguish from other actor types

**Good:**
- Actor identity is stated
- Generally clear entity type
- Role is mentioned

**Needs Improvement:**
- Vague identity ("an entity that does things")
- Unclear what differentiates this from other actors
- No clear purpose or role

### 2. Capability Actionability

**Excellent:**
- Capabilities describe concrete ACTIONS the actor can perform
- Uses action verbs (possess, perform, participate, create, analyze)
- Each capability is distinct and meaningful
- Capabilities distinguish this actor from others

**Good:**
- Most capabilities are actionable
- Generally uses action verbs
- Capabilities are relevant

**Needs Improvement:**
- Capabilities are vague or abstract
- Uses passive voice or non-action descriptions
- Capabilities don't distinguish this actor type
- Too few capabilities (< 2) or too many (> 6)

### 3. Property Appropriateness

**Excellent:**
- Property types are well-defined and domain-relevant
- Clear explanation of WHAT properties the actor can possess
- References specific property specs when available
- Property types make sense for this actor

**Good:**
- Property types are listed
- Generally relevant to domain
- Some explanation provided

**Needs Improvement:**
- Properties are vague or generic
- No explanation of property types
- Property types don't match actor capabilities
- Claims actor can possess any/all properties

### 4. Domain Fit

**Excellent:**
- Actor serves clear purpose in its domain
- Identity aligns with domain concepts
- Capabilities and properties are domain-appropriate
- Easy to see how this actor is used in practice

**Good:**
- Actor is relevant to domain
- Generally appropriate capabilities/properties
- Domain purpose is stated

**Needs Improvement:**
- Unclear why this actor exists
- Domain fit is questionable
- Capabilities/properties seem arbitrary

### 5. Extension Clarity

**Excellent:**
- If base type: Clear extension pattern shown with examples
- If extended type: Clear relationship to parent explained
- Inheritance is logical and adds value
- Easy to understand when to use vs. extend

**Good:**
- Extension pattern is present
- Inheritance makes sense
- Some examples provided

**Needs Improvement:**
- No explanation of extension
- Unclear relationship to parent (if extended)
- Extension adds no value over parent
- When to extend vs. when to use directly is unclear

### 6. Obsidian Compatibility

**Excellent:**
- Links to related property specs when referenced
- Uses consistent ID format (`v:actor:<name>`)
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

### Actor Identity

**Purpose:** Establish WHAT this actor is - the core entity type

**Tips:**
- Be specific about the type of entity
- Explain the actor's primary function or role
- Distinguish from similar actor types
- Use domain-appropriate terminology

**Examples:**
- ✅ "This actor represents a learner engaged in educational activities"
- ✅ "This actor represents a staff member in an organization"
- ❌ "This actor is something that does stuff" (too vague)

### Capabilities

**Purpose:** Define WHAT the actor can DO

**Tips:**
- Use action verbs (possess, perform, participate, create, learn)
- List 2-4 distinct capabilities (not too few, not too many)
- Make each capability meaningful and specific
- Ensure capabilities match the actor's identity

**Anti-patterns:**
- ❌ "Can exist" (too vague, everything can exist)
- ❌ Listing 10+ capabilities (too many, loses focus)
- ❌ Passive descriptions ("can be acted upon")
- ✅ "Can possess skills and knowledge"
- ✅ "Can participate in learning activities"

### Properties

**Purpose:** Define WHAT the actor can POSSESS

**Tips:**
- Reference specific property types (skill, role, attribute)
- Explain why these property types are appropriate
- Link to property specs when available
- Keep the list focused (2-4 property types typically)

**Examples:**
- ✅ "Skills (`vertex/skill`): Can possess learnable capabilities"
- ✅ "Roles (`vertex/role`): Can hold organizational positions"
- ❌ "Can have properties" (which properties?)

### Examples (Optional but Recommended)

**Purpose:** Show concrete instances of this actor type

**Tips:**
- Provide 2-3 concrete examples
- Show diversity within the type
- Link to actual instance documents if they exist
- Help readers understand when to use this type

**Examples:**
- ✅ "**Alice**: A student learning knowledge complexes"
- ✅ "**Knowledge-Complex-Learner**: Generic student for syllabi"

## Workflow Guidance

### Recommended Authoring Sequence

1. **Identify the Need** (10 minutes)
   - What entity type do you need to model?
   - Why doesn't an existing actor type work?
   - What makes this entity distinct?
   - **Checkpoint:** Is a new actor type necessary?

2. **Define Actor Identity** (15 minutes)
   - Write a clear statement of what this actor IS
   - Explain the actor's role in the system
   - Distinguish from other actor types
   - **Checkpoint:** Is the identity clear and specific?

3. **Specify Capabilities** (15 minutes)
   - List 2-4 actionable capabilities
   - Use action verbs
   - Ensure capabilities distinguish this actor
   - **Checkpoint:** Do capabilities match the identity?

4. **Define Properties** (15 minutes)
   - List property types this actor can possess
   - Reference property specs when available
   - Explain why these properties fit
   - **Checkpoint:** Are properties domain-appropriate?

5. **Add Examples** (10 minutes)
   - Provide 2-3 concrete instances
   - Show when to use this actor type
   - **Checkpoint:** Do examples clarify usage?

### Total Estimated Time: 65 minutes

## Common Issues and Solutions

| Issue | Problem | Solution |
|-------|---------|----------|
| Vague Identity | "An entity that exists" | Be specific: "A learner engaged in education" |
| Passive Capabilities | "Can be taught" | Active voice: "Can learn from modules" |
| Generic Properties | "Can have properties" | Specific: "Can possess skills (vertex/skill)" |
| Unclear Extension | When to use vs. when to extend? | Document extension pattern with examples |
| Too Many Capabilities | Lists 10+ capabilities | Focus on 2-4 core, distinguishing capabilities |
| No Domain Fit | Unclear why actor exists | Explain purpose in domain context |

## Best Practices

1. **Start with Domain Need** - Don't create actors speculatively, create for specific domain requirements
2. **Be Specific About Identity** - Avoid vague descriptions, use clear entity types
3. **List 2-4 Capabilities** - Focus on core, distinguishing actions
4. **Reference Property Specs** - Link to specific property types when possible
5. **Show Extension Pattern** - If base type, show how to extend; if extended, show relationship to parent
6. **Provide Concrete Examples** - Help readers understand when to use this actor type
7. **Keep Domain Focus** - All sections should align with domain purpose

## Extension Guidance

### When to Create a New Actor Type

Create a new actor type when:
- You need an entity with distinct capabilities
- Existing actor types don't fit your domain
- The entity can possess properties and participate in relationships
- The type will be reused (not just a single instance)

### When to Extend Existing Actor

Extend an existing actor type when:
- Your actor shares most capabilities with the parent
- You need to ADD specific capabilities or constraints
- The parent actor is well-established (like `vertex/actor`)
- Your domain is a specialization of the parent's domain

**Example:**
```yaml
# Student extends Actor
type: vertex/student
extends: vertex/actor
# Inherits: capabilities, properties
# Adds: learning-specific sections
```

## Validation vs. Verification

**Verification** (deterministic):
- All required sections present
- Capabilities lists 2+ items
- Properties lists 1+ item
- ID format correct
- Tags include [vertex, actor]

**Validation** (qualitative):
- Identity clarity and specificity
- Capability actionability
- Property appropriateness for actor
- Domain fit and purpose
- Extension pattern clarity (if applicable)
- Example quality and helpfulness

---

**Note:** Actor is a foundational type intended for extension. Good actor documents make the extension pattern clear and provide concrete examples to guide usage.
