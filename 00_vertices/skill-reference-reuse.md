---
type: vertex/skill
extends: vertex/property
id: v:skill:reference-reuse
name: Reference & Reuse via Doc-Kits
description: Understanding doc-kit pattern for extending assurance with usage documentation and maintaining reusable documentation pattern registries
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

# Reference & Reuse via Doc-Kits

## Purpose

This skill defines the capability to create and maintain reusable documentation patterns through the doc-kit pattern. It represents mastery of extending assurance faces with usage context, creating systematic "how-to" guidance for document types, and organizing pattern libraries for efficient knowledge reuse.

## Property Definition

A **reference and reuse** understanding is a learnable capability encompassing:
- **Doc-kit pattern:** Extending `face/assurance` with usage documentation sections
- **Pattern components:** Spec + Guidance + Canonical Example + Usage Context
- **Usage documentation:** "When to Use", "How to Create", "Related Types", "Common Pitfalls", "Examples in the Wild"
- **Reusable references:** Canonical examples serving as templates for new instances
- **Doc-kit registry:** Maintaining central catalog of foundational documentation patterns
- **Pattern relationships:** Understanding inheritance, composition, and alternative pattern connections
- **Living documentation:** Updating patterns as usage evolves and new instances emerge
- **Boundary connection:** Tracing doc-kits to boundary complex through assurance relationships

This skill is abstract until possessed by an actor (student), at which point it represents concrete knowledge and capability.

## Acquisition

This skill is **learned** through study and practice:
- Completing the [[v:learning-module:reference-reuse]] module
- Creating doc-kit faces from existing assurance faces
- Writing "When to Use" decision criteria for document types
- Documenting "How to Create" workflows with verification checkpoints
- Identifying related types and pattern relationships
- Creating doc-kit registry chart for foundational patterns
- Using doc-kits to create new document instances
- Maintaining "Examples in the Wild" registries

## Applicable Actors

This skill can be possessed by:
- **`vertex/student`**: Students engaged in knowledge complex education
- **`vertex/actor`**: Any actor learning about reusable documentation patterns and knowledge management

Rationale: This is a learnable capability appropriate for any actor who understands assurance and needs to create systematic, reusable documentation pattern libraries.

## Learning Outcomes

After acquiring this skill, a learner can:

1. **Distinguish assurance from doc-kit** (explain how doc-kit extends assurance with usage context)
2. **Create doc-kit faces** (write `face/doc_kit` documents with all required sections)
3. **Write usage criteria** ("When to Use" sections with decision criteria and anti-patterns)
4. **Document creation workflows** ("How to Create" step-by-step with verification checkpoints)
5. **Identify pattern relationships** (inheritance, composition, alternatives across document types)
6. **Create doc-kit registry charts** (organize foundational patterns in catalog structure)
7. **Use doc-kits systematically** (follow documented workflows to create new instances)
8. **Maintain pattern libraries** (update doc-kits as usage evolves, add new examples)
9. **Trace to boundary complex** (understand how doc-kits connect to SS, SG, GS, GG foundation)

## Prerequisite Skills

**Required:**
- [[v:skill:assurance-audits]] - Must understand assurance faces before extending them with usage documentation

**Background (helpful but not required):**
- Experience with design patterns and pattern languages
- Familiarity with template libraries and documentation standards
- Understanding of knowledge management systems

## Enables

Possessing this skill enables:

- **Pattern library creation**: Can design and maintain reusable documentation pattern catalogs
- **Systematic documentation**: Can use doc-kits to create consistent, high-quality documents
- **Knowledge transfer**: Can encode expert knowledge as reusable patterns
- **Efficient onboarding**: Can provide clear guidance for creating new document types
- **Living pattern maintenance**: Can evolve patterns as usage and understanding grow
- **Documentation architecture**: Prepared to design organization-wide doc systems (advanced work)

## Assessment Methods

Skill possession can be assessed through:

1. **Doc-Kit Creation:** Create 2 doc-kit faces from existing assurance faces (add all usage sections)
2. **Usage Criteria:** Write "When to Use" sections for 3 document types with clear decision criteria
3. **Workflow Documentation:** Create "How to Create" workflows for 3 document types with checkpoints
4. **Pattern Relationships:** Map inheritance, composition, and alternative relationships for 5 document types
5. **Registry Chart:** Create doc-kit registry chart with 5 foundational patterns (SS-GS, SG-GG, SC-GC, SA-GA, SP-GP)
6. **Doc-Kit Usage:** Use a doc-kit to create new document instance, verify it passes assurance
7. **Boundary Trace:** Trace 3 doc-kits back to boundary complex through assurance relationships

**Standard:** 80% accuracy on exercises and assessments demonstrates skill possession.

## Examples

**Students possessing this skill:**
- `v:student:document-architect` - Has completed reference-reuse module (or document-composition module)

**Usage in prerequisite faces:**
```yaml
type: face/prerequisite
vertices:
  - v:student:assurance-learner  # has assurance-audits skill
  - v:skill:assurance-audits  # prerequisite
  - v:learning-module:reference-reuse  # requires this skill
```

**Usage in skill-gain faces:**
```yaml
type: face/skill-gain
vertices:
  - v:student:document-architect  # possesses this skill after completion
  - v:learning-module:reference-reuse  # develops this skill
  - v:skill:reference-reuse  # this skill
```

## Constraints

- Must be acquired through learning (not inherent)
- Requires assurance-audits as prerequisite (cannot create doc-kits without understanding assurance)
- Cannot be possessed without completing learning process (module or equivalent study)
- Should be validated through assessment before considering possessed
- Pattern maintenance is ongoing (doc-kits are living documents, not static)

## Real-World Applications

This skill enables understanding of:

- **Design pattern libraries**: Systematic catalogs of reusable solutions
- **Documentation standards**: Organization-wide consistency through shared patterns
- **Knowledge codification**: Transforming expert knowledge into reusable guidance
- **Onboarding efficiency**: Reducing learning curves through clear usage documentation
- **Pattern evolution**: Maintaining living libraries that adapt to changing needs
- **Community knowledge**: Building shared understanding through documented patterns

---

**Note:** This skill builds on [[v:skill:assurance-audits]] to add pattern library capability. It prepares learners for advanced documentation architecture work by providing systematic methods for codifying, organizing, and reusing quality-assured documentation patterns. Students completing this module achieve `document-architect` status alongside those completing Module 06 (document-composition).
