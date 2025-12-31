---
type: template/edge/validation
extends: edge
id: template:edge:validation
name: Validation Edge Template
description: Connects a document to the guidance it should satisfy (quality assessment)
instantiable: true
tags:
  - template
  - edge
  - validation
version: 1.0.0
created: 2025-12-27T21:00:00Z
modified: 2025-12-27T21:00:00Z
---

# Validation Edge Template

**Connects a document to the guidance document that defines quality criteria for assessment.**

Validation edges represent the relationship "this document has been validated against this guidance" - meaning the document's quality has been assessed against the guidance's criteria by a responsible party.

## Type Hierarchy

```
edge (abstract)
└── validation (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `edge`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all edge fields, plus validation-specific constraints:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `edge/validation` |
| `extends` | string | Must be `edge` |
| `id` | string | Unique identifier (format: `e:validation:<child>:<parent-guidance>`) |
| `name` | string | Human-readable edge name |
| `source` | string | Child document ID (any doc type) |
| `target` | string | Parent guidance ID (format: `v:guidance:<name>`) |
| `source_type` | string | Must be `vertex/doc` or subtype |
| `target_type` | string | Must be `vertex/guidance` |
| `orientation` | string | Must be `directed` (child → guidance) |
| `validator` | string | Identity of responsible party (person or system) |
| `validation_method` | string | How validation was performed: `manual`, `llm-assisted`, `automated` |
| `llm_model` | string | REQUIRED if `validation_method` is `llm-assisted` (e.g., `claude-sonnet-4.5-20250929`) |
| `human_approver` | string | REQUIRED if `validation_method` is `llm-assisted` or `automated` |
| `tags` | array | Must include `[edge, validation]` |
| `version` | string | Semantic version |
| `created` | datetime | ISO 8601 creation timestamp |
| `modified` | datetime | ISO 8601 last modification timestamp |

## Accountability Chain

Validation edges MUST establish clear accountability:

### Manual Validation

```yaml
validator: "Alice Smith <alice@example.com>"
validation_method: manual
```

- **validator** is the human who performed and is accountable for the assessment
- No additional approval required

### LLM-Assisted Validation

```yaml
validator: "claude-sonnet-4.5-20250929"
validation_method: llm-assisted
llm_model: "claude-sonnet-4.5-20250929"
human_approver: "Bob Jones <bob@example.com>"
```

- **validator** is the LLM system that generated the assessment
- **llm_model** specifies the exact model version for reproducibility
- **human_approver** is REQUIRED - the person who reviewed and takes responsibility
- Human approver is accountable for the validation, even if LLM generated content

### Automated Validation

```yaml
validator: "validation-bot v2.1.0"
validation_method: automated
human_approver: "Carol Davis <carol@example.com>"
```

- **validator** is the automated system
- **human_approver** is REQUIRED - the person accountable for system behavior
- Human approver accepts responsibility for the automated system's output

## Accountability Principle

**The human approver, when present, is the accountable party.** They are responsible either because:
1. They reviewed and approved the machine-generated content, OR
2. They are the authority accountable for the automated system's behavior

The validation edge represents their judgment, with the LLM/automation serving as an assistive tool.

## Tag Requirements

The `tags` array MUST include the full inheritance chain:

```yaml
tags:
  - edge         # base type
  - validation   # concrete type
```

## Endpoint Constraints

### Source Vertex (Child Document)
- **Type:** MUST be `vertex/doc` or subtype (`vertex/spec`, `vertex/guidance`)
- **Role:** The document being validated
- **Constraint:** Must be assessed for quality against the target guidance's criteria

### Target Vertex (Parent Guidance)
- **Type:** MUST be `vertex/guidance`
- **ID Format:** `v:guidance:<name>`
- **Role:** Defines the quality criteria the child should meet

## Orientation

Validation edges are **directed** from child to guidance:
- **Direction:** child_doc → parent_guidance
- **Meaning:** "This child document has been assessed against this guidance's quality criteria"
- **Validation:** Requires expert judgment (not deterministic)

## Body Content Requirements

The markdown body MUST contain the validation assessment structured by the guidance's quality criteria.

### Required Section: Validation Assessment

```markdown
## Validation Assessment

**Guidance:** [Link to guidance document]
**Validator:** [Person/system who performed validation]
**Method:** Manual | LLM-Assisted | Automated
**Date:** [ISO 8601 timestamp]

### Quality Criteria Evaluation

[For each quality criterion in the guidance:]

#### [Criterion Name]

**Level:** Excellent | Good | Needs Improvement
**Rationale:** [2-3 sentences explaining the assessment]
**Evidence:** [Specific examples or citations from the document]

[Repeat for each criterion...]

## Overall Assessment

**Recommendation:** Pass | Conditional Pass | Fail
**Summary:** [2-4 sentences summarizing overall quality]

### Strengths
- [Key strength 1]
- [Key strength 2]

### Areas for Improvement
- [Suggestion 1]
- [Suggestion 2]
```

### Required Section: Accountability

```markdown
## Accountability Statement

[IF validation_method = manual:]
This validation was performed manually by [validator name], who takes full responsibility for the assessment.

[IF validation_method = llm-assisted:]
This validation assessment was generated with assistance from [llm_model]. The assessment was reviewed and approved by [human_approver name], who takes full responsibility for its accuracy and appropriateness.

[IF validation_method = automated:]
This validation was performed by automated system [validator]. The system's behavior and output are the responsibility of [human_approver name], who approves this validation.

**Signed:** [human_approver or validator]
**Date:** [ISO 8601 timestamp]
```

### Optional Sections

- **Validation Notes:** Additional context, caveats, or observations
- **Follow-up Actions:** Recommended improvements or next steps
- **Version History:** If validation is updated/repeated

## Role in Assurance Pattern

Validation edges form one side of the assurance triangle:

```
          child_doc
           /      \
          /        \
  verification   validation
        /            \
       /              \
   parent_spec ---- parent_guidance
              coupling
```

The validation edge connects:
- Child document (any doc)
- Parent guidance (quality criteria)

Together with a verification edge and coupling edge, this forms an **assurance face**.

## Verification vs. Validation

| Aspect | Verification | Validation |
|--------|--------------|------------|
| **Checks** | Structure, required fields, data types | Quality, clarity, fitness-for-purpose |
| **Method** | Deterministic, automated | Qualitative, expert judgment |
| **Result** | Pass/Fail | Quality level (Excellent/Good/Poor) |
| **Edge Type** | `verification` | `validation` |
| **Target** | Spec | Guidance |
| **Accountability** | Tool version | Human validator/approver |

## LLM Integration

Validation edges SHOULD leverage LLM assistance for initial assessment, with human oversight:

Example workflow:
```bash
# Generate initial validation assessment
# (Human runs this, LLM generates draft)
claude-code "Validate 00_vertices/my-doc.md against v:guidance:spec,
            output validation edge following template"

# Human reviews LLM output
# Human edits as needed
# Human adds their name as human_approver
# Human commits, taking responsibility
```

The human approver's role:
1. Review LLM-generated assessment for accuracy
2. Verify criteria coverage is complete
3. Check that evidence citations are valid
4. Adjust levels/rationale if needed
5. Add their approval signature
6. Commit the validation edge

## Example Instance

```yaml
---
type: edge/validation
extends: edge
id: e:validation:spec-guidance:guidance-spec
name: Validation - Spec-for-Guidance validates against Guidance-for-Spec
source: v:spec:guidance
target: v:guidance:spec
source_type: vertex/spec
target_type: vertex/guidance
orientation: directed
validator: claude-sonnet-4.5-20250929
validation_method: llm-assisted
llm_model: claude-sonnet-4.5-20250929
human_approver: "Chief Engineer <chief@example.com>"
tags:
  - edge
  - validation
version: 1.0.0
created: 2025-01-15T14:00:00Z
modified: 2025-01-15T14:00:00Z
---

# Validation - Spec-for-Guidance validates against Guidance-for-Spec

This validation edge confirms that spec-for-guidance meets the quality criteria defined in guidance-for-spec.

## Validation Assessment

**Guidance:** [guidance-for-spec](../00_vertices/guidance-for-spec.md)
**Validator:** claude-sonnet-4.5-20250929
**Method:** LLM-Assisted
**Human Approver:** Chief Engineer <chief@example.com>
**Date:** 2025-01-15T14:00:00Z

### Quality Criteria Evaluation

#### Clarity and Precision

**Level:** Excellent
**Rationale:** The spec uses precise technical language with well-defined terms. Each requirement is stated unambiguously with clear success criteria.
**Evidence:** Section "Required Frontmatter Fields" provides exact types and constraints. Schema section uses formal notation.

#### Completeness

**Level:** Excellent
**Rationale:** All aspects of guidance document structure are specified. No gaps in coverage. Both required and optional elements are addressed.
**Evidence:** Covers frontmatter fields, body sections, quality criteria structure, and guidance workflow.

[... additional criteria ...]

## Overall Assessment

**Recommendation:** Pass
**Summary:** This specification demonstrates excellent quality across all criteria. It provides clear, complete structural requirements that enable deterministic verification while supporting qualitative validation.

### Strengths
- Exceptionally clear and precise language
- Comprehensive coverage of guidance structure
- Well-integrated with broader assurance framework

### Areas for Improvement
- Could provide more examples of edge cases
- Workflow guidance section could be expanded

## Accountability Statement

This validation assessment was generated with assistance from claude-sonnet-4.5-20250929. The assessment was reviewed and approved by Chief Engineer <chief@example.com>, who takes full responsibility for its accuracy and appropriateness.

**Signed:** Chief Engineer
**Date:** 2025-01-15T14:00:00Z
```

## Validation Rules

1. **Type Format:** `type` must be `edge/validation`
2. **Source Type:** Source must be a doc (`vertex/doc` or subtype)
3. **Target Type:** Target must be guidance (`vertex/guidance`)
4. **Orientation:** Must be `directed`
5. **Tag Chain:** Tags must include `[edge, validation]`
6. **Accountability:** Must specify `validator` and `validation_method`
7. **Human Approval:** `human_approver` REQUIRED for `llm-assisted` or `automated` methods
8. **LLM Model:** `llm_model` REQUIRED when `validation_method` is `llm-assisted`
9. **Body Content:** Must include validation assessment and accountability statement
10. **Assurance:** Should participate in an assurance face with verification edge and coupling edge

## Boundary Complex

The four foundational validation edges in the boundary complex:

1. **e:validation:spec-spec:guidance-spec** - spec-for-spec validates against guidance-for-spec
2. **e:validation:spec-guidance:guidance-spec** - spec-for-guidance validates against guidance-for-spec
3. **e:validation:guidance-spec:guidance-guidance** - guidance-for-spec validates against guidance-for-guidance
4. **e:validation:guidance-guidance:guidance-guidance** - guidance-for-guidance validates against itself (self-validation)

These demonstrate both cross-validation and self-validation properties of the knowledge complex.

## Audit Trail

Validation edges are part of the permanent record. The accountability chain ensures:
- Human responsibility is always clear
- LLM assistance is transparent (model version recorded)
- Validation can be reproduced or re-evaluated
- Trust is based on identified humans, not opaque systems

When validation is updated:
- Create new validation edge with incremented version
- Reference previous validation in notes
- Update validation face to point to new edge
- Preserve old edge for audit history
