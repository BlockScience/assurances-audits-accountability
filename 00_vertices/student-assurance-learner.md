---
type: vertex/student
extends: vertex/actor
id: v:student:assurance-learner
name: Assurance Learner
description: Student who has completed assurance-audits module and can construct assurance triangles, audit assurance networks, and understand boundary complex foundations
tags:
  - vertex
  - actor
  - student
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
domain: knowledge-complexes
---

# Assurance Learner

## Purpose

This student represents a learner who has completed Module 05 ([[v:learning-module:assurance-audits]]) and now possesses [[v:skill:assurance-audits]] in addition to foundational and verification skills. This is the fourth learning state in the knowledge complex educational journey, adding complete assurance network capabilities.

## Actor Identity

The Assurance Learner is a student who has progressed from the verification-learner state ([[v:student:verification-learner]]) by completing the assurance and audits module. This learner now understands how to combine verification, validation, and coupling edges into complete assurance triangles, audit assurance network completeness using `audit_assurance_chart.py`, and trace assurance paths back to the boundary complex root. They understand the self-referential foundation provided by the boundary complex and its role in resolving circular dependencies.

This is a **learning state vertex** - a snapshot of student skill accumulation after completing specific modules, not a specific individual person.

## Capabilities

- **Learn systematically**: Can progress through structured learning modules building on prerequisites
- **Possess and acquire skills**: Has acquired four skills through module completion (cumulative)
- **Study learning modules**: Can engage with advanced composition and pattern library modules
- **Participate in learning paths**: Can follow syllabus sequences to document-architect state
- **Construct assurance faces**: Can combine verification, validation, coupling into assurance triangles
- **Audit assurance networks**: Can run `audit_assurance_chart.py` and interpret results
- **Trace to foundation**: Can follow assurance paths from documents back to boundary complex
- **Understand self-reference**: Can explain how boundary complex resolves circular dependencies

## Properties

- **Skills (`vertex/skill`)**: Possesses simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation, AND assurance-audits
- **Learning status**: Has completed simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation, and assurance-audits modules
- **Proficiency levels**: Intermediate-to-advanced level with complete assurance capability

## Learning Context

This student has completed four modules in the knowledge complex learning journey and is prepared for advanced composition and pattern library topics. The learner understands:

**From Module 1 (foundational topology):**
- Simplicial complex topology: Vertices, edges, faces as knowledge structures
- Euler characteristic: χ = V - E + F formula and topological interpretation
- Chart documents: Can read and understand knowledge complex charts

**From Module 2 (type systems):**
- Semantic vertex types: Comprehensive understanding of all vertex types
- Type-constrained edges: Valid and invalid edge configurations across types
- Type validation faces: prerequisite/completion/skill-gain/assurance validation
- Type system benefits: Preventing invalid relationships through type constraints

**From Module 4 (verification & validation):**
- Doc, Spec, Guidance types: Document, specification, and guidance vertices
- Verification: Deterministic structural compliance using automated tools
- Validation: Qualitative fitness-for-purpose using expert judgment
- Edge payloads: Tool outputs (verification) and quality assessments (validation)
- Coupling edges: Pairing specs with guidance for coherent quality assurance
- Accountability models: Manual, LLM-assisted, and automated validation patterns

**From Module 5 (assurance & audits):**
- Assurance triangles: Verification + validation + coupling as complete testimony
- Triangle coherence: How three edges integrate to encode quality
- Assurance faces: `face/assurance` structure and accountability
- Assurance auditing: Using `audit_assurance_chart.py` for network validation
- Trace paths: Following edges from documents to boundary complex root
- Boundary complex: 5-vertex self-referential foundation (b0:root, SS, SG, GS, GG)
- Boundary faces: Using root to create valid assurance for spec-for-spec, guidance-for-guidance
- Kernel pattern: SS-GS, SG-GG as mutually assured foundational pairs

The learner is ready to study:
- Document composition patterns (Module 06, requires Module 03 also)
- Doc-kit pattern libraries (Module 07)

## Prerequisite Skills

**Possessed Skills:**
- **[[v:skill:simplicial-complex-fundamentals]]**: Understanding of vertices, edges, faces, and Euler characteristic
- **[[v:skill:typed-simplicial-complexes]]**: Understanding of semantic types and type-driven constraints
- **[[v:skill:verification-validation]]**: Understanding of structural verification and qualitative validation
- **[[v:skill:assurance-audits]]**: Understanding of assurance triangles and network auditing

**Acquisition Path:**
1. Module 1 ([[v:learning-module:simplicial-complex-fundamentals]]) → gained simplicial-complex-fundamentals
2. Module 2 ([[v:learning-module:typed-simplicial-complexes]]) → gained typed-simplicial-complexes
3. Module 4 ([[v:learning-module:verification-validation]]) → gained verification-validation
4. Module 5 ([[v:learning-module:assurance-audits]]) → gained assurance-audits

## Learning Goals

The Assurance Learner aims to acquire additional skills through further study:

- **Document composition skills**: Compositional architectures and PPP framework (Module 06, requires Module 03)
- **Pattern library skills**: Doc-kit creation and registry maintenance (Module 07)
- **Both paths lead to**: document-architect state with 6 total skills

## Examples

This learning state can be instantiated as:

- **Any student after completing Module 5**: Generic progression from verification-learner
- **Fourth milestone in syllabus**: Students reach this state before final advanced modules
- **Prerequisite state for Modules 06 and 07**: Required starting point for both advanced paths

## Relationships

This student participates in the following relationship patterns:

### has-skill Edges

```yaml
# Student possesses foundational topology skill
type: edge/has-skill
source: v:student:assurance-learner
target: v:skill:simplicial-complex-fundamentals

# Student possesses type system skill
type: edge/has-skill
source: v:student:assurance-learner
target: v:skill:typed-simplicial-complexes

# Student possesses verification-validation skill
type: edge/has-skill
source: v:student:assurance-learner
target: v:skill:verification-validation

# Student possesses assurance-audits skill
type: edge/has-skill
source: v:student:assurance-learner
target: v:skill:assurance-audits
```

### studies Edges

```yaml
# Student can study document composition module
type: edge/studies
source: v:student:assurance-learner
target: v:learning-module:document-composition

# Student can study doc-kit module
type: edge/studies
source: v:student:assurance-learner
target: v:learning-module:reference-reuse
```

### transitions-to Edge (from previous state)

```yaml
# Transition from verification-learner to assurance-learner
type: edge/transitions-to
source: v:student:verification-learner
target: v:student:assurance-learner
```

### completion Face (how this state was reached)

```yaml
# Completion of Module 5 created this state
type: face/completion
vertices:
  - v:student:verification-learner  # initial state (3 skills)
  - v:learning-module:assurance-audits  # completed module
  - v:student:assurance-learner  # resulting state (4 skills)
```

### skill-gain Face

```yaml
# Student gained assurance-audits skill from Module 5
type: face/skill-gain
vertices:
  - v:student:assurance-learner  # possesses assurance-audits skill
  - v:learning-module:assurance-audits  # developed skill
  - v:skill:assurance-audits  # the skill gained
```

## Constraints

- Must have completed assurance-audits module (or equivalent)
- Must possess all four skills: simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation, AND assurance-audits
- Represents discrete learning state (skill set snapshot), not individual person
- Skills are supermodular (this state has all skills from previous state PLUS new skills)

## Skill Accumulation

**Skill set computation:**
```
verification-learner.skills = {simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation}
assurance-audits.develops = {assurance-audits}

assurance-learner.skills = {simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation} ∪ {assurance-audits}
                          = {simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation, assurance-audits}

Cardinality: |assurance-learner.skills| = 4 >= |verification-learner.skills| = 3 ✓

Supermodular: assurance-learner.skills ⊇ verification-learner.skills ✓
```

**Skill accumulation verification:**
- verification-learner had: {simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation}
- Module 5 requires: {verification-validation} ✓
- Module 5 develops: {assurance-audits}
- assurance-learner has: {simplicial-complex-fundamentals, typed-simplicial-complexes, verification-validation, assurance-audits} ✓

## Fork Point

**Important:** This student state is a **fork point** in the learning journey:

- **Path 1 (Module 06):** Requires assurance-audits + composing-typed-simplicial-complexes → gains document-composition
- **Path 2 (Module 07):** Requires only assurance-audits → gains reference-reuse
- **Both paths:** Lead to document-architect state (students completing both have 6 total skills)

Students may take either module next, or both in either order. Module 06 requires an additional prerequisite from Module 03.

---

**Note:** This student represents the fourth learning state and first fork point in the knowledge complex educational journey. It demonstrates continued skill accumulation through module completion following the completion face pattern with supermodular skill growth. Students at this state can proceed to either Module 06 (if they also possess composing-typed-simplicial-complexes) or Module 07, or both in either order.
