---
type: chart/standard
extends: chart
id: c:doc-kit-registry
name: Doc-Kit Registry
description: Registry of all doc-kit faces providing complete documentation packages for document types in the knowledge complex

# Chart construction metadata
constructed_by: "claude-assistant"
construction_method: assisted
construction_date: 2025-12-29T00:00:00Z

# Chart purpose
purpose: Catalog all doc-kit faces that provide complete documentation packages (spec, guidance, example) for creating typed documents
scope: 6 doc-kit faces with complete assurance network connecting all specs to SS/GS and all guidances to SG/GG

# Elements comprising this chart
elements:
  vertices:
    # Doc-kit target specs (6)
    - v:spec:persona
    - v:spec:purpose
    - v:spec:protocol
    - v:spec:spec
    - v:spec:guidance
    - v:spec:system_prompt
    # Corresponding guidances (6)
    - v:guidance:persona
    - v:guidance:purpose
    - v:guidance:protocol
    - v:guidance:spec
    - v:guidance:guidance
    - v:guidance:system_prompt
    # Example documents (6 unique, some overlap with above)
    - v:persona:claude-assistant
    - v:purpose:claude-assistant
    - v:protocol:claude-assistant
    - v:system_prompt:claude-assistant-compiled
    # Note: v:spec:purpose and v:guidance:purpose already listed above as examples for spec/guidance doc-kits
  edges:
    # === COUPLING EDGES (7) ===
    # spec ↔ guidance for each type
    - e:coupling:persona
    - e:coupling:purpose
    - e:coupling:protocol
    - e:coupling:spec
    - e:coupling:guidance
    - e:coupling:system_prompt
    # Cross-domain coupling for foundational assurance (SG ↔ GS)
    - e:coupling:spec-guidance:guidance-spec

    # === DOC-KIT INTERNAL EDGES ===
    # Verification edges (example → spec) for doc-kits
    - e:verification:persona-claude:spec
    - e:verification:purpose-claude:spec
    - e:verification:protocol-claude:spec
    - e:verification:purpose:spec           # spec doc-kit uses purpose spec as example
    - e:verification:purpose-guidance:guidance  # guidance doc-kit uses purpose guidance as example
    - e:verification:system_prompt-compiled:spec
    # Validation edges (example → guidance) for doc-kits
    - e:validation:persona-claude:guidance
    - e:validation:purpose-claude:guidance
    - e:validation:protocol-claude:guidance
    - e:validation:purpose:guidance-spec        # purpose spec validated against guidance-for-spec
    - e:validation:purpose-guidance:guidance-guidance  # purpose guidance validated against guidance-for-guidance
    - e:validation:system_prompt-compiled:guidance

    # === SPEC ASSURANCE EDGES ===
    # All specs verify against spec-spec (SS)
    - e:verification:spec-spec:spec-spec    # SS self-verifies
    - e:verification:spec-guidance:spec-spec  # SG verifies against SS
    - e:verification:persona:spec            # persona spec → SS
    - e:verification:purpose:spec            # purpose spec → SS (already above, but listed for clarity)
    - e:verification:protocol:spec           # protocol spec → SS
    - e:verification:system_prompt:spec      # system_prompt spec → SS
    # All specs validate against guidance-spec (GS)
    - e:validation:spec-spec:guidance-spec    # SS validates against GS
    - e:validation:spec-guidance:guidance-spec  # SG validates against GS
    - e:validation:persona:guidance-spec      # persona spec → GS
    - e:validation:protocol:guidance-spec     # protocol spec → GS
    - e:validation:system_prompt:guidance-spec  # system_prompt spec → GS

    # === GUIDANCE ASSURANCE EDGES ===
    # All guidances verify against spec-guidance (SG)
    - e:verification:guidance-guidance:spec-guidance  # GG verifies against SG
    - e:verification:guidance-spec:spec-guidance      # GS verifies against SG
    - e:verification:persona-guidance:guidance        # persona guidance → SG
    - e:verification:protocol-guidance:guidance       # protocol guidance → SG
    - e:verification:system_prompt-guidance:guidance  # system_prompt guidance → SG
    # All guidances validate against guidance-guidance (GG)
    - e:validation:guidance-guidance:guidance-guidance  # GG self-validates
    - e:validation:guidance-spec:guidance-guidance    # GS validates against GG
    - e:validation:persona-guidance:guidance-guidance  # persona guidance → GG
    - e:validation:protocol-guidance:guidance-guidance  # protocol guidance → GG
    - e:validation:system_prompt-guidance:guidance-guidance  # system_prompt guidance → GG

  faces:
    # === DOC-KIT FACES (6) ===
    - f:doc_kit:persona
    - f:doc_kit:purpose
    - f:doc_kit:protocol
    - f:doc_kit:spec
    - f:doc_kit:guidance
    - f:doc_kit:system_prompt

    # === FOUNDATIONAL ASSURANCE FACES (4) ===
    # The 4 self-referential assurance triangles for the boundary complex core
    - f:assurance:spec-spec         # SS self-assured
    - f:assurance:spec-guidance     # SG assured
    - f:assurance:guidance-spec     # GS assured
    - f:assurance:guidance-guidance # GG self-assured

tags:
  - chart
  - standard
  - doc-kit
  - registry
  - ppp
version: 1.0.0
created: 2025-12-29T00:00:00Z
modified: 2025-12-29T00:00:00Z
---

# Doc-Kit Registry

This chart catalogs all **doc-kit faces** in the knowledge complex. Doc-kits are complete documentation packages that provide everything needed to create instances of a document type.

## What Are Doc-Kits?

Doc-kits extend assurance faces by adding usage context and creation guidance. Each doc-kit contains:

1. **Specification** - Structural requirements (what MUST be present)
2. **Guidance** - Quality criteria and best practices (what makes it good)
3. **Example** - Canonical instance demonstrating both

Doc-kits answer: "How do I create a good [document type]?"

## Registered Doc-Kits

### Foundational PPP Types

| Doc-Kit | Type | Spec | Guidance | Example |
|---------|------|------|----------|---------|
| [[doc-kit-persona]] | persona | [[spec-for-persona]] | [[guidance-for-persona]] | [[persona-claude-assistant]] |
| [[doc-kit-purpose]] | purpose | [[spec-for-purpose]] | [[guidance-for-purpose]] | [[purpose-claude-assistant]] |
| [[doc-kit-protocol]] | protocol | [[spec-for-protocol]] | [[guidance-for-protocol]] | [[protocol-claude-assistant]] |
| [[doc-kit-system_prompt]] | system_prompt | [[spec-for-system-prompt]] | [[guidance-for-system-prompt]] | [[system_prompt-claude-assistant]] |

### Meta Types (Self-Referential)

| Doc-Kit | Type | Spec | Guidance | Example |
|---------|------|------|----------|---------|
| [[doc-kit-spec]] | spec | [[spec-for-spec]] | [[guidance-for-spec]] | [[spec-for-purpose]] |
| [[doc-kit-guidance]] | guidance | [[spec-for-guidance]] | [[guidance-for-guidance]] | [[guidance-for-purpose]] |

## Doc-Kit Structure

Each doc-kit face contains:

```
Doc-Kit Face
├── Vertices (3)
│   ├── Specification (v:spec:*)
│   ├── Guidance (v:guidance:*)
│   └── Example (v:[type]:*)
├── Edges (3)
│   ├── Coupling (spec ↔ guidance)
│   ├── Verification (example → spec)
│   └── Validation (example → guidance)
└── Content
    ├── Document Type Overview
    ├── When to Use / When NOT to Use
    ├── Creation Workflow (with checkpoints)
    ├── Verification & Validation instructions
    ├── Related Document Types
    ├── Common Pitfalls & Solutions
    └── Assurance Triangle Review
```

## Chart Topology

| Metric | Count |
|--------|-------|
| Vertices | 16 (6 specs + 6 guidances + 4 examples) |
| Edges | 40 (7 coupling + 12 doc-kit V/V + 11 spec assurance + 10 guidance assurance) |
| Faces | 10 (6 doc-kits + 4 foundational assurance) |
| Euler (χ) | -14 |

**Structure**: This chart is a **connected component** through the assurance network:

- All specs connect back to SS (spec-for-spec) and GS (guidance-for-spec) via verification/validation edges
- All guidances connect back to SG (spec-for-guidance) and GG (guidance-for-guidance) via verification/validation edges
- The foundational boundary complex (SS, SG, GS, GG) forms the core hub
- Doc-kit faces provide the "canonical reference triple" interpretation for each document type

## Usage

### Finding a Doc-Kit

To create a document of a specific type:

1. Find the doc-kit for that type in the registry above
2. Read the doc-kit face for usage context and workflow
3. Reference the spec for structural requirements
4. Reference the guidance for quality criteria
5. Study the example for practical demonstration

### Creating New Doc-Kits

When adding new document types to the knowledge complex:

1. Create spec for the document type
2. Create guidance for the document type
3. Create coupling edge linking spec and guidance
4. Create example document of the type
5. Create doc-kit face cataloging all components
6. Add doc-kit to this registry

## PPP Framework Integration

The foundational doc-kits support the **PPP (Persona-Purpose-Protocol) framework**:

- **Purpose** (design FIRST): Defines what value is delivered
- **Persona** (design second): Matches expertise to purpose
- **Protocol** (design LAST): Integrates persona and purpose into workflow
- **System Prompt**: Composes all three into complete AI configuration

The meta doc-kits (spec, guidance) enable the creation of new document types.

## Related Charts

- [[compound-document]] - Demonstrates PPP composition pattern
- [[boundary-complex]] - Foundational spec/guidance relationships

---

**Note**: This registry should be updated whenever new doc-kits are added to the knowledge complex.
