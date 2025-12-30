# Validation Accountability Framework

**Document Type:** Technical Specification
**Version:** 1.0.0
**Date:** 2025-12-27

---

## Purpose

This document specifies the accountability framework for validation edges in the knowledge complex. It ensures that human responsibility is always clear, even when LLMs or automated systems assist in generating validation assessments.

## Core Principle

**All validations must have an identifiable, accountable human party.**

When LLMs or automated systems generate validation content, a human must explicitly approve and take responsibility for that content. The validation edge represents the human's judgment, with the machine serving as an assistive tool.

## Accountability Chain

### Three Validation Methods

#### 1. Manual Validation

**Use case:** Human performs the entire validation assessment.

**Frontmatter:**
```yaml
validator: "Alice Smith <alice@example.com>"
validation_method: manual
```

**Accountability:** The `validator` is the human who performed the assessment and is fully responsible for its contents.

**No additional approval required.**

#### 2. LLM-Assisted Validation

**Use case:** LLM generates initial assessment, human reviews and approves.

**Frontmatter:**
```yaml
validator: "claude-sonnet-4.5-20250929"
validation_method: llm-assisted
llm_model: "claude-sonnet-4.5-20250929"
human_approver: "Bob Jones <bob@example.com>"
```

**Accountability:** The `human_approver` is the person who:
- Reviewed the LLM-generated assessment
- Verified accuracy and appropriateness
- Made any necessary corrections
- Takes full responsibility for the final content

**The human approver is the accountable party**, not the LLM.

**Required fields:**
- `llm_model`: Exact model version for reproducibility and transparency
- `human_approver`: Identity of responsible human

#### 3. Automated Validation

**Use case:** Automated system performs validation, human approves system behavior.

**Frontmatter:**
```yaml
validator: "validation-bot v2.1.0"
validation_method: automated
human_approver: "Carol Davis <carol@example.com>"
```

**Accountability:** The `human_approver` is the person who:
- Is the authority accountable for the automated system's behavior
- Accepts responsibility for this validation output
- Would be responsible for correcting system errors

**The human approver is the accountable party**, not the automation.

## Why This Matters

### Trust and Auditability

Validation is subjective and requires judgment. For validation edges to be trustworthy:
1. **Humans must be accountable** - We need to know who to trust or hold responsible
2. **LLM assistance must be transparent** - Record which model, which version
3. **Approval must be explicit** - The human must actively sign off
4. **Audit trail must be clear** - Anyone reviewing can see the accountability chain

### Legal and Professional Responsibility

In regulated domains (healthcare, finance, safety-critical systems), validation may carry legal or professional obligations. The framework ensures:
- A licensed professional can sign as `human_approver`
- Their approval is recorded permanently
- LLM assistance is disclosed, not hidden
- Responsibility cannot be deflected to "the AI"

### Quality Assurance

Human oversight ensures:
- LLM hallucinations are caught
- Domain expertise is applied
- Context is properly considered
- Edge cases are handled appropriately

## Workflow Examples

### Example 1: Human Uses LLM to Draft Validation

```bash
# Step 1: User asks LLM to generate validation draft
$ claude-code "Validate 00_vertices/spec-for-guidance.md against \
               v:guidance:spec, create validation edge"

# LLM generates: 01_edges/validation-spec-guidance-guidance-spec.md
# With frontmatter:
#   validator: claude-sonnet-4.5-20250929
#   validation_method: llm-assisted
#   llm_model: claude-sonnet-4.5-20250929
#   human_approver: TBD

# Step 2: User reviews the generated validation assessment
$ cat 01_edges/validation-spec-guidance-guidance-spec.md
# (User reads through criteria evaluations, evidence, rationale)

# Step 3: User edits as needed
$ vim 01_edges/validation-spec-guidance-guidance-spec.md
# (User corrects any errors, adds missing points)

# Step 4: User adds their name as human_approver
#   human_approver: "Chief Engineer <chief@example.com>"

# Step 5: User commits, taking responsibility
$ git add 01_edges/validation-spec-guidance-guidance-spec.md
$ git commit -m "Add validation edge for spec-for-guidance

I have reviewed the LLM-generated validation assessment and
take responsibility for its accuracy and appropriateness.

Signed: Chief Engineer"
```

### Example 2: Fully Manual Validation

```bash
# Human writes validation edge from scratch
$ vim 01_edges/validation-guidance-guidance-guidance-guidance.md

# Frontmatter:
#   validator: "Chief Engineer <chief@example.com>"
#   validation_method: manual

# Human performs assessment, writes all criteria evaluations

# Human commits
$ git commit -m "Manual validation of guidance-for-guidance"
```

### Example 3: Automated System with Human Oversight

```bash
# Automated system runs and generates validation
$ validation-bot --source v:spec:data-format \
                  --target v:guidance:spec \
                  --output 01_edges/validation-data-format.md

# System creates edge with:
#   validator: "validation-bot v2.1.0"
#   validation_method: automated
#   human_approver: TBD

# Human reviews automation output
$ cat 01_edges/validation-data-format.md

# If acceptable, human adds approval
$ vim 01_edges/validation-data-format.md
#   human_approver: "Carol Davis <carol@example.com>"

# Commit represents human's acceptance of system behavior
$ git commit -m "Approve automated validation of data-format spec"
```

## Verification of Accountability

The `verify_typed.py` script enforces accountability requirements:

```python
# For llm-assisted validations:
if validation_method == 'llm-assisted':
    # Requires llm_model field
    # Requires human_approver field

# For automated validations:
if validation_method == 'automated':
    # Requires human_approver field

# For manual validations:
if validation_method == 'manual':
    # No additional fields required
    # validator is the accountable human
```

Failed validation examples:

```yaml
# ✗ FAIL: llm-assisted without human_approver
validator: claude-sonnet-4.5
validation_method: llm-assisted
llm_model: claude-sonnet-4.5
# Missing: human_approver

# ✗ FAIL: llm-assisted without llm_model
validator: claude-sonnet-4.5
validation_method: llm-assisted
human_approver: "Bob <bob@example.com>"
# Missing: llm_model

# ✗ FAIL: automated without human_approver
validator: validation-bot v2.1.0
validation_method: automated
# Missing: human_approver
```

## Accountability Statement in Body

Every validation edge body MUST include an accountability statement that makes the responsibility explicit to readers:

### For Manual Validation

```markdown
## Accountability Statement

This validation was performed manually by Alice Smith, who takes full
responsibility for the assessment.

**Signed:** Alice Smith
**Date:** 2025-12-27T14:00:00Z
```

### For LLM-Assisted Validation

```markdown
## Accountability Statement

This validation assessment was generated with assistance from
claude-sonnet-4.5-20250929. The assessment was reviewed and approved
by Bob Jones, who takes full responsibility for its accuracy and
appropriateness.

**Signed:** Bob Jones
**Date:** 2025-12-27T14:00:00Z
```

### For Automated Validation

```markdown
## Accountability Statement

This validation was performed by automated system validation-bot v2.1.0.
The system's behavior and output are the responsibility of Carol Davis,
who approves this validation.

**Signed:** Carol Davis
**Date:** 2025-12-27T14:00:00Z
```

## Implications for Boundary Complex

The four foundational validation edges demonstrate different accountability patterns:

1. **e:validation:spec-spec:guidance-spec**
   - Likely: `llm-assisted` (LLM drafts, Chief Engineer approves)
   - Demonstrates: Cross-domain validation

2. **e:validation:spec-guidance:guidance-spec**
   - Likely: `llm-assisted` (LLM drafts, Chief Engineer approves)
   - Demonstrates: Cross-domain validation

3. **e:validation:guidance-spec:guidance-guidance**
   - Likely: `manual` (Chief Engineer validates personally)
   - Demonstrates: Critical foundation warrants human attention

4. **e:validation:guidance-guidance:guidance-guidance**
   - Likely: `manual` (Chief Engineer validates personally)
   - Demonstrates: Self-validation requires human judgment

All carry clear human accountability, establishing trust in the boundary complex.

## Future Extensions

### Multi-Approver Validations

For high-stakes validations, future versions could support:

```yaml
validation_method: llm-assisted
llm_model: claude-sonnet-4.5-20250929
human_approvers:
  - name: "Alice Smith <alice@example.com>"
    role: "Domain Expert"
    approved: 2025-12-27T14:00:00Z
  - name: "Bob Jones <bob@example.com>"
    role: "Quality Lead"
    approved: 2025-12-27T15:30:00Z
```

### Validation Review Chains

For critical documents:

```yaml
validation_method: manual
validator: "Alice Smith <alice@example.com>"
reviewed_by: "Bob Jones <bob@example.com>"
review_date: 2025-12-28T10:00:00Z
```

## Conclusion

The validation accountability framework ensures:

1. **Human responsibility is always clear**
2. **LLM assistance is transparent and traceable**
3. **Automated systems have human oversight**
4. **Audit trails support trust and compliance**
5. **Accountability cannot be deflected to machines**

This enables responsible use of AI assistance while maintaining the trust and responsibility essential for validation in the knowledge complex.
