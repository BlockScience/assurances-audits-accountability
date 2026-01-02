---
type: edge/coupling
extends: edge
id: e:coupling:repository-policy
name: Coupling - Spec-for-Repository-Policy and Guidance-for-Repository-Policy
source: v:spec:repository-policy
target: v:guidance:repository-policy
source_type: vertex/spec
target_type: vertex/guidance
orientation: undirected
tags:
  - edge
  - coupling
version: 1.0.0
created: 2026-01-02T12:00:00Z
modified: 2026-01-02T12:00:00Z
---

# Coupling - Spec-for-Repository-Policy and Guidance-for-Repository-Policy

**This coupling connects the specification for repository policy documents with the guidance for repository policy documents.**

## Purpose

This coupling enables complete assurance for repository policy documents by connecting structural requirements with quality criteria:

- **Verification:** Checking that a repository policy document has required sections and structure (against [spec-for-repository-policy](../00_vertices/spec-for-repository-policy.md))
- **Validation:** Assessing whether a repository policy document is clear, complete, enforceable, inclusive, and maintainable (against [guidance-for-repository-policy](../00_vertices/guidance-for-repository-policy.md))

## Governed Document Type

Both documents govern **repository policy documents** - governance specifications that define contribution patterns, collaboration rules, and operational standards for git repositories.

Repository policy documents prescribe HOW contributors interact with a repository.

## Role in Repository Governance

Repository policies serve diverse contexts:
- **Open Source:** Community contribution, licensing, CLA/DCO
- **Internal/Corporate:** Access control, compliance, team boundaries
- **Private:** Personal projects, experiments, minimal governance
- **Hybrid:** Open-core models, consortium projects, mixed governance
- **Institutional:** External accountability, audit trails, regulatory compliance, traceability
- **Educational:** Expert-curated didactic content, academic rigor, edition-based lifecycle
- **Documentation:** Writing standards, review criteria, update processes
- **Research:** Reproducibility, citation, publication coordination
- **Operations:** Change control, rollback procedures, incident response

## Role in Assurance Faces

This coupling forms the base of assurance faces where:
- Child docs are repository-policy documents
- Verification edge: repository-policy → spec-for-repository-policy
- Validation edge: repository-policy → guidance-for-repository-policy
- Coupling edge: spec-for-repository-policy ↔ guidance-for-repository-policy (this edge)

## Semantic Alignment

The structural requirements in spec-for-repository-policy align with the quality criteria in guidance-for-repository-policy:

| Spec-for-Repository-Policy Requires | Guidance-for-Repository-Policy Assesses |
|-------------------------------------|----------------------------------------|
| Purpose Statement | Clarity - is the purpose understandable? |
| Repository Identity (Scope, Ownership) | Completeness - are boundaries well-defined? |
| Contribution Rules (Who, Types, Process, Review) | Enforceability - can rules be consistently applied? |
| RECOMMENDED: Quality Standards | Enforceability - are standards checkable? |
| RECOMMENDED: Governance | Enforceability - are decisions well-defined? |
| RECOMMENDED: Communication | Inclusivity - are channels accessible? |
| All sections present and coherent | Maintainability - can policy evolve? |

Together, they ensure repository policy documents are both **structurally valid** and **high quality**.

## Usage Context

Repository policy documents should be created:
- Early in repository setup (before active contribution begins)
- When formalizing informal practices that have emerged
- When onboarding new contributors at scale
- When governance disputes need authoritative resolution

**Design Considerations:**
- Match policy complexity to repository complexity
- Automate enforcement where possible
- Review and update regularly
- Test with actual new contributors

---

**Version:** 1.0.0
**Created:** 2026-01-02
