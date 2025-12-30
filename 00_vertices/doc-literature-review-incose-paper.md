---
type: vertex/doc
extends: doc
id: v:doc:literature-review-incose-paper
name: Literature Review - INCOSE IS 2026 Paper on Document Assurance Framework
description: Comprehensive literature review supporting the INCOSE paper on test-driven document development using typed simplicial complexes
tags:
  - vertex
  - doc
  - literature-review
version: 1.0.0
created: 2025-12-30T20:00:00Z
modified: 2025-12-30T20:00:00Z
topic: Document Verification, Validation, Assurance, and Accountability
target_paper: v:doc:incose-paper-2026
citation_count: 17
theme_count: 4
search_strategy: Targeted search of IEEE standards, INCOSE publications, topology textbooks, and AI ethics frameworks
date_range: 1979-2025
databases_searched:
  - IEEE Xplore
  - Google Scholar
  - SEBoK Wiki
  - INCOSE Publications
  - ISO Standards
---

# Literature Review - INCOSE IS 2026 Paper on Document Assurance Framework

## Introduction

This literature review supports the INCOSE IS 2026 paper "Test-Driven Document Development: Simplicial Complexes for Verification, Validation, and Assurance with Human Accountability" by gathering authoritative sources across four thematic areas: verification and validation foundations, simplicial complexes and computational topology, test-driven development methodology, and AI ethics and accountability frameworks.

The review covers peer-reviewed publications, IEEE/ISO standards, authoritative handbooks, and foundational textbooks from 1979-2025. Sources are organized into themes that map directly to the paper's Background section, enabling efficient extraction for citation. The review establishes the scholarly context for the paper's contribution: a framework that formally couples verification with validation through typed simplicial complexes while requiring explicit human accountability for all qualitative judgments.

**Scope boundaries:** This review focuses on sources directly relevant to document quality assurance with human accountability. It excludes general software verification methods, formal methods for code verification, and AI safety research not related to accountability attribution.

## Theme 1: Verification and Validation Foundations

This theme establishes the classic V&V distinction and its codification in systems engineering standards—the foundation upon which the paper's assurance triangle builds.

### Key Sources

| Citation | Year | Key Contribution | Relevance |
|----------|------|------------------|-----------|
| [Boehm-1979] | 1979 | Classic formulation: Verification = "building the product right"; Validation = "building the right product" | Foundational distinction that paper operationalizes through separate edge types |
| [IEEE-1012-2016] | 2016 | Standard for System and Software V&V processes | Authoritative definition of V&V processes; paper extends to documentation domain |
| [ISO-15288-2023] | 2023 | Systems and software engineering—System life cycle processes | Current standard defining V&V within lifecycle; paper aligns with process framework |
| [EIA-632-1999] | 1999 | Processes for Engineering a System—includes Requirements 31-33 on verification | Industry standard with explicit verification requirements; informs spec structure |
| [IEEE-1220-1998] | 1998 | Application and Management of Systems Engineering—Requirements Analysis through Physical Verification | Detailed V&V process model; paper's phases align with IEEE 1220 structure |

### Summary

The V&V literature establishes a clear distinction between structural compliance (verification) and fitness-for-purpose (validation), but treats them as separate activities without formal coupling mechanisms. Boehm's 1979 formulation remains definitive; IEEE 1012 and ISO 15288 codify the processes. The gap our paper addresses: no existing framework formally couples verification requirements (specifications) with validation criteria (guidance) to ensure coherent quality assessment. The assurance triangle provides this coupling.

## Theme 2: Simplicial Complexes and Computational Topology

This theme covers the mathematical foundations enabling the paper's formal model—typed simplicial complexes as a representation for document relationships and assurance patterns.

### Key Sources

| Citation | Year | Key Contribution | Relevance |
|----------|------|------------------|-----------|
| [Hatcher-2002] | 2002 | Algebraic Topology—comprehensive treatment of simplicial complexes, homology, Euler characteristic | Mathematical foundation for vertices, edges, faces model; provides rigor |
| [Edelsbrunner-Harer-2010] | 2010 | Computational Topology—algorithms for topological data analysis | Computational methods for analyzing simplicial complexes; enables tooling |
| [Carlsson-2009] | 2009 | Topology and Data—persistent homology for data analysis | Application of topology to structured data; precedent for non-geometric use |
| [Ghrist-2008] | 2008 | Barcodes: The persistent topology of data | Topological invariants as structural signatures; informs audit metrics |
| [Zomorodian-Carlsson-2005] | 2005 | Computing persistent homology | Algorithmic foundations for computing topological features |

### Summary

Algebraic topology provides rigorous mathematical structures for representing compositional relationships. Simplicial complexes (vertices, edges, faces) naturally model the paper's document-specification-guidance triad. The closure property—a face exists only if all bounding edges exist—maps precisely to assurance requirements: a document is assured only when verification, validation, and coupling are all present. Euler characteristic provides a topological invariant for validating audit charts. This mathematical foundation distinguishes our approach from ad-hoc quality checklists.

## Theme 3: Test-Driven Development and Engineering V

This theme covers the methodological inspiration for "test-driven document development" and the V-model lifecycle that structures the paper's architecture layers.

### Key Sources

| Citation | Year | Key Contribution | Relevance |
|----------|------|------------------|-----------|
| [Beck-2003] | 2003 | Test-Driven Development: By Example—red-green-refactor cycle | Methodological inspiration: write spec (test) first, then document (code) to pass |
| [Forsberg-Mooz-1991] | 1991 | The Relationship of System Engineering to the Project Cycle—introduced the Vee diagram | Foundational V-model paper; architecture layers map to V-model phases |
| [INCOSE-SEH-2023] | 2023 | INCOSE Systems Engineering Handbook v5.0 | Current authoritative SE reference; defines lifecycle, V&V, architecture layers |
| [Friedenthal-2015] | 2015 | A Practical Guide to SysML, 3rd ed.—SysML 1.4 with V&V relationships | SysML satisfy/verify stereotypes; precedent for formal V&V relationships |

### Summary

Test-driven development's core insight—write the test before the code—transfers directly to documentation: write the specification (verification criteria) and guidance (validation criteria) before the document. The V-model from Forsberg & Mooz provides the lifecycle structure: conceptual → functional → logical → physical on the left side corresponds to acceptance → system → integration → unit testing on the right. Our paper's 4-layer architecture (Conceptual, Functional, Logical, Physical) aligns with this established SE pattern, while the assurance triangle formalizes the V&V relationships at each layer.

## Theme 4: AI Ethics and Human Accountability

This theme addresses the paper's central concern: maintaining human accountability when AI assists with documentation, and the governance frameworks informing our approach.

### Key Sources

| Citation | Year | Key Contribution | Relevance |
|----------|------|------------------|-----------|
| [Floridi-Cowls-2019] | 2019 | AI4People—five principles including explicability = intelligibility + accountability | Theoretical foundation for accountability requirements; paper operationalizes |
| [UNESCO-2021] | 2021 | Recommendation on the Ethics of AI—global framework | International governance context; paper aligns with accountability requirements |
| [UN-HLAB-2024] | 2024 | Governing AI for Humanity—governance recommendations | Recent UN guidance on AI governance; supports timeliness of paper's contribution |
| [DORA-2024] | 2024 | State of DevOps Report—76% AI adoption, 7.2% stability decline | Empirical evidence of AI-quality gap; motivates paper's practical contribution |

### Summary

AI ethics frameworks consistently emphasize accountability as a core principle, but lack practical mechanisms for achieving it in documentation workflows. Floridi's formulation (explicability = intelligibility + accountability) provides theoretical grounding; UNESCO and UN HLAB provide governance context. The DORA 2024 finding—that widespread AI adoption correlates with decreased delivery stability—provides empirical motivation. Our paper addresses this gap by making human accountability structurally required: validation edges cannot close without a named `human_approver`, ensuring AI assistance is transparent and humans retain responsibility for quality judgments.

## Citation Catalog

### Primary Research

| ID | Full Citation | Type | Access |
|----|---------------|------|--------|
| [Boehm-1979] | Boehm BW. Guidelines for verifying and validating software requirements and design specifications. In: Euro IFIP 79. 1979. | Conference | doi:10.1007/978-3-642-67587-5_48 |
| [Forsberg-Mooz-1991] | Forsberg K, Mooz H. The relationship of system engineering to the project cycle. In: Proceedings of the NCOSE Conference. Chattanooga, TN; 1991:57-65. | Conference | NCOSE Proceedings |
| [Carlsson-2009] | Carlsson G. Topology and data. Bull Am Math Soc. 2009;46(2):255-308. | Journal | doi:10.1090/S0273-0979-09-01249-X |
| [Ghrist-2008] | Ghrist R. Barcodes: The persistent topology of data. Bull Am Math Soc. 2008;45(1):61-75. | Journal | doi:10.1090/S0273-0979-07-01191-3 |
| [Zomorodian-Carlsson-2005] | Zomorodian A, Carlsson G. Computing persistent homology. Discrete Comput Geom. 2005;33(2):249-274. | Journal | doi:10.1007/s00454-004-1146-y |
| [Floridi-Cowls-2019] | Floridi L, Cowls J. A unified framework of five principles for AI in society. Harvard Data Sci Rev. 2019;1(1). | Journal | doi:10.1162/99608f92.8cd550d1 |

### Standards and Handbooks

| ID | Full Citation | Type | Access |
|----|---------------|------|--------|
| [IEEE-1012-2016] | IEEE. IEEE Standard for System, Software, and Hardware Verification and Validation. IEEE Std 1012-2016. 2016. | Standard | doi:10.1109/IEEESTD.2017.7942406 |
| [IEEE-1220-1998] | IEEE. IEEE Standard for Application and Management of the Systems Engineering Process. IEEE Std 1220-1998. 1998. | Standard | IEEE Standards |
| [ISO-15288-2023] | ISO/IEC/IEEE. Systems and software engineering—System life cycle processes. ISO/IEC/IEEE 15288:2023. 2023. | Standard | iso.org |
| [EIA-632-1999] | EIA. Processes for Engineering a System. EIA-632. 1999. | Standard | SAE International |
| [INCOSE-SEH-2023] | INCOSE. Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities. 5th ed. Hoboken, NJ: Wiley; 2023. | Handbook | ISBN: 978-1-119-81429-0 |
| [UNESCO-2021] | UNESCO. Recommendation on the Ethics of Artificial Intelligence. 2021. | Policy | unesco.org |
| [UN-HLAB-2024] | UN High-Level Advisory Body on AI. Governing AI for Humanity. 2024. | Report | un.org |
| [DORA-2024] | DORA. State of DevOps Report 2024. Google Cloud; 2024. | Report | cloud.google.com/devops |

### Books

| ID | Full Citation | Type | Access |
|----|---------------|------|--------|
| [Hatcher-2002] | Hatcher A. Algebraic Topology. Cambridge: Cambridge University Press; 2002. | Textbook | pi.math.cornell.edu/~hatcher |
| [Edelsbrunner-Harer-2010] | Edelsbrunner H, Harer JL. Computational Topology: An Introduction. Providence, RI: American Mathematical Society; 2010. | Textbook | ISBN: 978-0-8218-4925-5 |
| [Beck-2003] | Beck K. Test-Driven Development: By Example. Boston: Addison-Wesley; 2003. | Book | ISBN: 978-0321146533 |
| [Friedenthal-2015] | Friedenthal S, Moore A, Steiner R. A Practical Guide to SysML: The Systems Modeling Language. 3rd ed. Burlington, MA: Morgan Kaufmann; 2015. | Book | ISBN: 978-0128002025 |

## Gap Analysis

### Identified Gaps

| Gap | Current State | How Target Paper Addresses |
|-----|---------------|---------------------------|
| **No formal V&V coupling** | IEEE 1012 and ISO 15288 define verification and validation as separate processes; no standard requires formal linkage between structural requirements (specs) and quality criteria (guidance) | Paper introduces **coupling edges** that formally link specifications to corresponding guidance, ensuring V&V use semantically related criteria |
| **Missing accountability mechanisms** | AI ethics frameworks (Floridi, UNESCO) call for accountability but lack practical implementation patterns for documentation workflows | Paper requires **named human_approver** on all validation edges and assurance faces—accountability is structurally enforced, not just recommended |
| **No assurance formalization** | V&V literature lacks mathematical formalization enabling automated audit and topological integrity checking | Paper uses **typed simplicial complexes** with assurance triangles (2-simplices) that close only when all conditions met; Euler characteristic provides audit invariant |
| **TDD not applied to documents** | Test-driven development (Beck) well-established for code; no equivalent framework for documentation | Paper introduces **test-driven document development**: specs are "tests" that documents must pass; verification before/during authoring |

### Positioning Statement

The target paper occupies a unique position at the intersection of four established fields: it applies the mathematical rigor of algebraic topology (Theme 2) to formalize the classic V&V distinction (Theme 1), using the test-first methodology of TDD (Theme 3) while addressing the urgent need for AI accountability (Theme 4). No existing work combines these elements into a practical, self-demonstrating framework for assured document development.

## Search Methodology

**Databases searched:**
- IEEE Xplore (standards, conference papers)
- Google Scholar (academic papers, citations)
- SEBoK Wiki (systems engineering body of knowledge)
- INCOSE Publications (handbooks, symposium proceedings)
- ISO/IEC Standards (international standards)

**Search terms:**
- "verification and validation" + "systems engineering"
- "simplicial complex" + "data" OR "topology"
- "test-driven development"
- "AI accountability" + "documentation" OR "governance"
- "V-model" + "systems engineering" + "lifecycle"
- "architecture layers" + "conceptual functional logical physical"

**Inclusion criteria:**
- Peer-reviewed or authoritative (standards, handbooks)
- Directly relevant to at least one theme
- Foundational works regardless of age; recent works (2019+) for AI ethics

**Exclusion criteria:**
- Blog posts, white papers without peer review
- General AI safety not focused on accountability
- Software verification methods not applicable to documents

## Source Relationships

The sources form a coherent intellectual lineage:

```
Boehm (1979) ─────────────────────┐
     │                            │
     └──▶ IEEE 1012 (2016) ◀──────┤
               │                  │
               └──▶ ISO 15288 (2023)
                         │
Forsberg-Mooz (1991) ────┼───────▶ INCOSE SEH (2023)
                         │
Beck (2003) ─────────────┼───────▶ Test-Driven Docs (our paper)
                         │
Hatcher (2002) ──────────┼───────▶ Typed Simplicial Complexes (our paper)
     │                   │
     └──▶ Carlsson (2009)│
           │             │
           └──▶ Computational Topology (tooling)
                         │
Floridi (2019) ──────────┼───────▶ Accountability Model (our paper)
     │                   │
     └──▶ UNESCO (2021) ─┘
           │
           └──▶ UN HLAB (2024)
```

## Recommended Citation Format

For the INCOSE IS 2026 paper, use AMA (American Medical Association) citation style as recommended by INCOSE:

**Format:**
```
[Author(s)]. [Title]. [Journal/Conference/Publisher]. [Year];[Volume]([Issue]):[Pages]. [DOI/URL]
```

**Examples:**

Journal article:
> Boehm BW. Guidelines for verifying and validating software requirements and design specifications. Euro IFIP 79. 1979. doi:10.1007/978-3-642-67587-5_48

Standard:
> IEEE. IEEE Standard for System, Software, and Hardware Verification and Validation. IEEE Std 1012-2016. 2016. doi:10.1109/IEEESTD.2017.7942406

Book:
> Hatcher A. Algebraic Topology. Cambridge: Cambridge University Press; 2002.

Handbook:
> INCOSE. Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities. 5th ed. Hoboken, NJ: Wiley; 2023.

---

## Accountability Statement

This literature review was compiled with Claude (Opus 4.5) assistance for source gathering, organization, and synthesis. The author directed the search strategy, evaluated source relevance, and made all inclusion/exclusion decisions. The gap analysis and positioning statement represent the author's original scholarly judgment.

**Human Approver:** mzargham
**LLM Assistance:** claude-opus-4-5-20251101
**Date:** 2025-12-30

---

**Note:** This literature review is verified against [[spec-for-incose-literature-review]] and validated against [[guidance-for-incose-literature-review]]. It supports [[v:doc:incose-paper-2026]] by providing the scholarly foundation for the Background section.
