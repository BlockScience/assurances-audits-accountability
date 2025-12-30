---
type: vertex/skill
extends: vertex/property
id: v:skill:document-composition
name: Document Composition
description: Understanding compositional document architecture using Obsidian embeds, typed subsections, and systematic assurance of compound documents
tags:
  - vertex
  - property
  - skill
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
domain: knowledge-complexes
level: advanced
---

# Document Composition

## Purpose

This skill defines the capability to design and maintain compositional document architectures where complex documents are assembled from independently assured components. It represents mastery of the single-source-of-truth principle through Obsidian embed syntax, typed subsection specifications, and systematic compilation and assurance workflows.

## Property Definition

A **document composition** understanding is a learnable capability encompassing:
- **Compositional architecture:** Designing documents as assemblies of independently maintained components
- **Obsidian embeds:** Using `![[reference]]` syntax to include documents inline
- **Typed subsections:** Defining spec sections as references to other specs with type constraints
- **PPP framework:** Understanding Persona + Purpose + Protocol → System Prompt composition pattern
- **Compilation workflow:** Using `compile_document.py` to expand embeds into standalone deployable documents
- **Dependency tracking:** Creating `edge/dependency` with `dependency_type: compositional` and `compilation`
- **Component assurance:** Independently verifying and validating constituent documents
- **Compound assurance:** Assuring compiled documents as complete deployable artifacts
- **Reference integrity:** Verifying all embedded components exist and satisfy type constraints

This skill is abstract until possessed by an actor (student), at which point it represents concrete knowledge and capability.

## Acquisition

This skill is **learned** through study and practice:
- Completing the [[v:learning-module:document-composition]] module
- Building compositional documents with Obsidian embeds
- Creating typed subsection specifications
- Running `compile_document.py` to generate standalone documents
- Independently assuring constituent components
- Assuring compiled compound documents
- Creating dependency edges for compositional relationships
- Verifying reference integrity and type consistency

## Applicable Actors

This skill can be possessed by:
- **`vertex/student`**: Students engaged in knowledge complex education
- **`vertex/actor`**: Any actor learning about compositional documentation architectures

Rationale: This is a learnable capability appropriate for any actor who understands both assurance networks and chart composition, enabling systematic design of modular documentation systems.

## Learning Outcomes

After acquiring this skill, a learner can:

1. **Design compositional architectures** (identify reusable components and define composition relationships)
2. **Use Obsidian embed syntax** (write `![[reference]]` inclusions correctly in source documents)
3. **Define typed subsections** (specify sections in specs as references to other specs with type constraints)
4. **Understand PPP framework** (explain Persona-Purpose-Protocol composition pattern and its benefits)
5. **Compile documents** (use `compile_document.py` to expand embeds into standalone markdown)
6. **Assure components independently** (verify and validate constituent documents before composition)
7. **Assure compiled documents** (verify and validate expanded compound documents after compilation)
8. **Track dependencies** (create `edge/dependency` with compositional and compilation types)
9. **Verify reference integrity** (check all embedded components exist and satisfy type constraints)
10. **Apply single-source-of-truth** (maintain components independently, avoiding duplication)

## Prerequisite Skills

**Required:**
- [[v:skill:assurance-audits]] - Must understand assurance networks before independently assuring components
- [[v:skill:composing-typed-simplicial-complexes]] - Must understand identification and composition operations

**Background (helpful but not required):**
- Experience with modular software architecture
- Familiarity with document templating systems
- Understanding of dependency management

## Enables

Possessing this skill enables:

- **Modular documentation systems**: Can design reusable component libraries
- **Systematic maintenance**: Can update components once and propagate changes
- **Independent assurance**: Can verify/validate components before assembly
- **Type-safe composition**: Can enforce constraints on component relationships
- **Deterministic compilation**: Can generate deployable artifacts from source references
- **Documentation architecture**: Prepared to design large-scale doc systems (advanced work)

## Assessment Methods

Skill possession can be assessed through:

1. **Compositional Design:** Design a 3-component compositional document with typed subsections
2. **Embed Usage:** Write source document with 3+ Obsidian embeds correctly
3. **Compilation:** Use `compile_document.py` to expand embeds, verify output correctness
4. **Component Assurance:** Independently assure 3 constituent documents (verification + validation)
5. **Compound Assurance:** Assure compiled document against its spec and guidance
6. **Dependency Tracking:** Create dependency edges for compositional and compilation relationships
7. **Reference Integrity:** Verify all embedded components exist and match type constraints
8. **PPP Application:** Create a Persona-Purpose-Protocol → System Prompt composition

**Standard:** 80% accuracy on exercises and assessments demonstrates skill possession.

## Examples

**Students possessing this skill:**
- `v:student:document-architect` - Has completed document-composition module (or doc-kit module)

**Usage in prerequisite faces:**
```yaml
type: face/prerequisite
vertices:
  - v:student:assurance-learner  # has assurance-audits skill
  - v:skill:assurance-audits  # prerequisite 1
  - v:learning-module:document-composition  # requires this skill
```

```yaml
type: face/prerequisite
vertices:
  - v:student:compositional-learner  # has composing-typed-simplicial-complexes
  - v:skill:composing-typed-simplicial-complexes  # prerequisite 2
  - v:learning-module:document-composition  # requires this skill
```

**Usage in skill-gain faces:**
```yaml
type: face/skill-gain
vertices:
  - v:student:document-architect  # possesses this skill after completion
  - v:learning-module:document-composition  # develops this skill
  - v:skill:document-composition  # this skill
```

## Constraints

- Must be acquired through learning (not inherent)
- Requires both assurance-audits AND composing-typed-simplicial-complexes as prerequisites (dual dependency)
- Cannot be possessed without completing learning process (module or equivalent study)
- Should be validated through assessment before considering possessed
- Component assurance before compilation is non-negotiable (ensures quality foundation)

## Real-World Applications

This skill enables understanding of:

- **Modular system architectures**: Compositional design patterns across software and documentation
- **Single-source-of-truth principles**: Avoiding duplication through systematic reference
- **Type-safe composition**: Enforcing constraints on component relationships
- **Systematic compilation**: Deterministic transformation from source to deployment
- **Quality assurance workflows**: Independent verification of components before assembly
- **Documentation as code**: Treating documentation with same rigor as software systems

---

**Note:** This skill requires dual prerequisites (assurance-audits + composing-typed-simplicial-complexes) and represents advanced capability. It builds on Module 05's assurance foundation and Module 03's composition understanding to enable systematic design of modular documentation architectures. Students completing this module achieve `document-architect` status alongside those completing Module 07 (reference-reuse).
