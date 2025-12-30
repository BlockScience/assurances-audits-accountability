---
type: vertex/skill
extends: vertex/property
id: v:skill:verification-validation
name: Verification & Validation
description: Understanding structural verification and qualitative validation of documents using automated tools and human judgment
tags:
  - vertex
  - property
  - skill
version: 1.0.0
created: 2025-12-28T00:00:00Z
modified: 2025-12-28T00:00:00Z
domain: knowledge-complexes
level: intermediate
---

# Verification & Validation

## Purpose

This skill defines the capability to distinguish between and apply structural verification ("did we build it right?") and qualitative validation ("did we build the right thing?"). It represents mastery of quality assurance foundations through deterministic tool-based checking and expert human judgment.

## Property Definition

A **verification and validation** understanding is a learnable capability encompassing:
- **Structural verification:** Using automated tools to check document compliance against specs
- **Qualitative validation:** Performing expert assessment of fitness-for-purpose against guidance
- **Edge payloads:** Creating verification and validation edges with tool outputs and assessments
- **Accountability models:** Understanding manual, LLM-assisted, and automated validation with human approvers
- **Coupling relationships:** Recognizing how spec-guidance pairs enable complete quality assurance

This skill is abstract until possessed by an actor (student), at which point it represents concrete knowledge and capability.

## Acquisition

This skill is **learned** through study and practice:
- Completing the [[v:learning-module:verification-validation]] module
- Running verification scripts (`verify_spec.py`, `verify_template_based.py`)
- Creating verification edges with tool output payloads
- Performing LLM-assisted validation with human accountability
- Creating validation edges with quality assessments
- Understanding coupling edges that pair specs with guidance

## Applicable Actors

This skill can be possessed by:
- **`vertex/student`**: Students engaged in knowledge complex education
- **`vertex/actor`**: Any actor learning about quality assurance patterns

Rationale: This is a learnable capability appropriate for any actor who understands typed simplicial complexes and needs to ensure document quality.

## Learning Outcomes

After acquiring this skill, a learner can:

1. **Distinguish verification from validation** (explain "did we build it right?" vs "did we build the right thing?")
2. **Run verification scripts** (execute `verify_spec.py` and `verify_template_based.py` on documents)
3. **Interpret verification results** (analyze pass/fail checks, identify structural issues, fix errors)
4. **Create verification edges** (document tool outputs as payloads in `edge/verification` files)
5. **Perform LLM-assisted validation** (assess quality criteria from guidance, maintain human accountability)
6. **Create validation edges** (document assessments as payloads in `edge/validation` files with approver)
7. **Understand coupling edges** (recognize spec-guidance pairs form foundation of assurance)
8. **Apply accountability models** (distinguish manual, LLM-assisted, automated validation methods)

## Prerequisite Skills

**Required:**
- [[v:skill:typed-simplicial-complexes]] - Must understand typed vertices and edges before learning verification/validation patterns

**Background (helpful but not required):**
- Experience with automated testing and quality assurance
- Familiarity with schema validation and type checking
- Understanding of peer review and expert judgment processes

## Enables

Possessing this skill enables:

- **Document quality assurance**: Can verify and validate any document against its spec and guidance
- **Edge payload creation**: Can create verification and validation edges with proper payloads
- **Tool-driven workflows**: Can use verification scripts to catch structural issues early
- **LLM-assisted quality assessment**: Can leverage LLMs for validation while maintaining human accountability
- **Assurance foundation**: Prepared to learn assurance triangles and auditing (Module 05)

## Assessment Methods

Skill possession can be assessed through:

1. **Verification Execution:** Run verification on 5 documents, interpret all results correctly
2. **Verification Edge Creation:** Create verification edges with correct payloads for 3 documents
3. **Validation Performance:** Perform LLM-assisted validation on 3 documents with complete quality assessments
4. **Validation Edge Creation:** Create validation edges with proper accountability statements for 3 documents
5. **Coupling Analysis:** Identify coupling edges for 5 spec-guidance pairs
6. **Written Explanation:** Explain verification vs validation distinction and accountability models (2-3 paragraphs)

**Standard:** 80% accuracy on exercises and assessments demonstrates skill possession.

## Examples

**Students possessing this skill:**
- `v:student:verification-learner` - Has completed verification-validation module
- `v:student:assurance-learner` - Has this skill plus assurance-audits skill

**Usage in prerequisite faces:**
```yaml
type: face/prerequisite
vertices:
  - v:student:intermediate-learner  # has typed-simplicial-complexes
  - v:skill:typed-simplicial-complexes  # prerequisite for module
  - v:learning-module:verification-validation  # requires this skill
```

**Usage in skill-gain faces:**
```yaml
type: face/skill-gain
vertices:
  - v:student:verification-learner  # possesses this skill after completion
  - v:learning-module:verification-validation  # develops this skill
  - v:skill:verification-validation  # this skill
```

## Constraints

- Must be acquired through learning (not inherent)
- Requires typed-simplicial-complexes as prerequisite
- Cannot be possessed without completing learning process (module or equivalent study)
- Should be validated through assessment before considering possessed
- Human accountability is non-negotiable for validation (cannot be fully automated)

## Real-World Applications

This skill enables understanding of:

- **Quality assurance workflows**: Systematic verification before validation approach
- **Tool-driven documentation**: Using scripts to enforce structural quality
- **Expert review processes**: Balancing automation with human judgment
- **LLM-assisted workflows**: Leveraging AI while maintaining accountability
- **Edge-based evidence**: Documenting quality checks as graph edges with payloads

---

**Note:** This skill builds on [[v:skill:typed-simplicial-complexes]] to add quality assurance capability. It enables learners to systematically ensure document quality through deterministic verification tools and expert validation judgment, preparing them for complete assurance patterns in Module 05.
