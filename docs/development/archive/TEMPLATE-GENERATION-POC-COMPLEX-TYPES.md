# Template Generation POC - Complex Document Types

**Status**: POC Complete - Findings Documented
**Date**: 2025-12-28
**Purpose**: Test template generation feasibility for edges, faces, and charts

## Executive Summary

Tested template generation on three complex document types:
1. **Chart (from spec-for-charts)** - ⚠️ Partial Success
2. **Verification Edge (no spec exists)** - ❌ Cannot Generate (no spec)
3. **Assurance Face (no spec exists)** - ❌ Cannot Generate (no spec)

**Key Finding**: Template generation works for simple vertices but faces **significant limitations** for complex structured types (charts, edges, faces) due to:
- Nested object structures not parsed correctly
- Missing specs for edges and faces
- Complex field relationships not captured in simple requirement tables

---

## POC Test 1: Chart Template Generation

### Input
- **Spec**: [00_vertices/spec-for-charts.md](../00_vertices/spec-for-charts.md)
- **Command**: `python scripts/generate_template_from_spec.py 00_vertices/spec-for-charts.md --output /tmp/chart-generated.md`
- **Expected**: Generate template matching [templates/charts/chart.md](../templates/charts/chart.md)

### Results

#### What Worked ✓

1. **Basic Frontmatter Fields**: Simple string/datetime fields generated correctly
   ```yaml
   type: chart/chart
   extends: doc
   id: c:<name>
   name: <Name>
   tags:
     - chart
   version: <Version>
   created: YYYY-MM-DDTHH:MM:SSZ
   modified: YYYY-MM-DDTHH:MM:SSZ
   ```

2. **Body Sections**: All 7 required sections detected and generated
   - Chart Overview
   - Why This Chart Exists
   - What This Chart Contains
   - How This Chart Was Constructed
   - Element Tables
   - Chart Properties
   - Verification

3. **Section Detection**: Parser correctly found numbered sections in spec

#### What Failed ✗

1. **Nested Object Fields - CRITICAL ISSUE**

   **Expected** (from spec):
   ```yaml
   elements:
     vertices:
       - <vertex-id-1>
       - <vertex-id-2>
     edges:
       - <edge-id-1>
       - <edge-id-2>
     faces:  # OPTIONAL
       - <face-id-1>
   ```

   **Generated** (BROKEN):
   ```yaml
   elements: <elements>
   elements.vertices:
     - <elements.vertices_item>
   elements.edges:
     - <elements.edges_item>
   elements.faces:
   ```

   **Problem**: Parser treats `elements.vertices` as a field name rather than recognizing it as a nested structure. YAML output is malformed.

2. **Array of Objects - CRITICAL ISSUE**

   **Expected** (from spec):
   ```yaml
   visualizations:  # OPTIONAL
     - file: <path>
       format: <format>
       description: <description>
       generated: YYYY-MM-DDTHH:MM:SSZ
       generator: <tool>
   ```

   **Generated** (BROKEN):
   ```yaml
   visualizations: <visualizations>
   file: <File>
   format: <Format>
   generated: YYYY-MM-DDTHH:MM:SSZ
   generator: <Generator>
   ```

   **Problem**: Parser doesn't understand object arrays. Fields appear at root level instead of being objects within an array.

3. **Optional Nested Fields**

   **Expected**: `elements.faces` should show as empty array or omitted with comment
   **Generated**: `elements.faces:` with no value (malformed YAML)

#### Verification Result

```bash
$ python scripts/verify_template_based.py /tmp/chart-generated.md --templates templates
```

**Result**: ❌ Would FAIL - Malformed YAML frontmatter due to nested objects

### Analysis

**Root Cause**: The current `SpecParser.extract_frontmatter_requirements()` method parses the requirements table row-by-row and doesn't understand:
- Object hierarchies (`elements:` contains `vertices:`, `edges:`, `faces:`)
- Arrays of objects (`visualizations` is an array where each item has multiple fields)
- Conditional structure (`faces` is OPTIONAL within `elements`)

**Impact**: **HIGH** - Charts, and potentially other complex types, cannot have templates auto-generated without significant parser enhancements.

---

## POC Test 2: Verification Edge Template

### Input
- **Spec**: ❌ NONE - No `spec-for-verification.md` exists
- **Template**: [templates/01_edges/verification.md](../templates/01_edges/verification.md) (hand-crafted)
- **Example**: [01_edges/verification-persona:spec.md](../01_edges/verification-persona:spec.md)

### Findings

#### Why No Spec Exists

Verification edges are **meta-constructs** - they represent the relationship "document X satisfies spec Y structurally". Creating a spec for verification edges would be:
- Self-referential (spec-for-verification would need verification edges)
- Redundant with template (template already defines structure)
- Circular dependency issue

#### Template Structure Analysis

The verification edge template has:

**Frontmatter** (11 required fields):
```yaml
type: edge/verification
extends: edge
id: e:verification:<child>:<parent-spec>
name: <string>
source: <child-doc-id>
target: <parent-spec-id>
source_type: vertex/doc or subtype
target_type: vertex/spec
orientation: directed
tags: [edge, verification]
version: <semver>
created: <datetime>
modified: <datetime>
```

**Body Sections**:
1. Verification Output (REQUIRED)
2. Verification Status (REQUIRED)
3. What This Verifies (OPTIONAL)
4. Role in Assurance (OPTIONAL)

#### Could We Generate This?

**Hypothetically**: Yes, IF we had a spec-for-verification that:
- Defines source/target constraints (both type and semantic)
- Specifies orientation requirements
- Lists required body sections

**Practically**: No good reason to create spec-for-verification because:
- Verification edges are generated by tools (not humans)
- Template serves as the spec (reflexive equality)
- Adding another layer adds complexity without value

---

## POC Test 3: Assurance Face Template

### Input
- **Spec**: ❌ NONE - No `spec-for-assurance.md` or `spec-for-assurance-face.md` exists
- **Template**: [templates/02_faces/assurance.md](../templates/02_faces/assurance.md) (hand-crafted)
- **Example**: [02_faces/assurance-persona:spec.md](../02_faces/assurance-persona:spec.md)

### Findings

#### Why No Spec Exists

Assurance faces are **composite meta-constructs** - they bundle:
- 3 vertices (target, spec, guidance)
- 3 edges (coupling, verification, validation)
- Assurance assessment (triangle coherence, overall status)
- Accountability statement (human sign-off)

Creating a spec for assurance faces would require:
- Defining vertex/edge relationship constraints
- Specifying triangle coherence rules
- Formalizing accountability requirements
- Self-referential assurance of spec-for-assurance

#### Template Structure Analysis

The assurance face template has:

**Frontmatter** (20+ fields including nested structures):
```yaml
type: face/assurance
extends: face
id: f:assurance:<name>
name: <string>
description: <string>
boundary:  # array of 3 edge IDs
  - <coupling-edge-id>
  - <verification-edge-id>
  - <validation-edge-id>
vertices:  # array of 3 vertex IDs
  - <target-vertex-id>
  - <spec-vertex-id>
  - <guidance-vertex-id>
target: <target-vertex-id>
spec: <spec-vertex-id>
guidance: <guidance-vertex-id>
coupling_edge: <coupling-edge-id>
verification_edge: <verification-edge-id>
validation_edge: <validation-edge-id>
assurer: <string>
assurance_method: manual | llm-assisted | automated
llm_model: <string>  # REQUIRED if llm-assisted
human_approver: <string>  # REQUIRED if llm-assisted or automated
tags: [face, assurance]
version: <semver>
created: <datetime>
modified: <datetime>
```

**Body Sections**:
1. Face Structure (vertices + edges)
2. Assurance Triangle (diagram)
3. Assurance Assessment (triangle coherence review)
   - Coupling Coherence
   - Verification Completeness
   - Validation Quality
   - Triangle Integration
4. Overall Assurance (status + criteria)
5. Accountability Statement
6. Assurance Metadata

#### Could We Generate This?

**Hypothetically**: Yes, IF we had a spec that:
- Defines the assurance triangle pattern formally
- Specifies conditional field requirements (llm_model only if llm-assisted)
- Lists coherence review requirements
- Defines accountability statement templates

**Practically**: ❌ **Very difficult** because:
- Assurance faces have complex semantic constraints (3 edges must form triangle, vertices must match, etc.)
- Body content is assessment-based, not template-fillable
- Accountability section varies by method (manual vs llm-assisted vs automated)
- Creating spec-for-assurance would itself need assurance (circular dependency)

---

## Summary of Findings

### Generation Feasibility Matrix

| Document Type | Has Spec? | Complexity | Generation Feasible? | Notes |
|---------------|-----------|------------|---------------------|-------|
| **Persona** (vertex) | ✅ Yes | Low | ✅ YES (95%+) | POC Phase 1 success |
| **Chart** (chart) | ✅ Yes | High | ⚠️ PARTIAL (40%) | Nested objects broken |
| **Verification** (edge) | ❌ No | Medium | ❌ NO | No spec exists, template IS spec |
| **Assurance** (face) | ❌ No | Very High | ❌ NO | No spec, complex constraints |

### Critical Gaps Identified

#### 1. Nested Object Parsing (BLOCKER for Charts)

**Problem**: Parser cannot handle:
```yaml
elements:
  vertices: [...]
  edges: [...]
```

**Required Enhancement**:
```python
class SpecParser:
    def extract_nested_objects(self, field_name: str) -> Dict:
        """Parse nested object structures from specs."""
        # Identify parent field (elements)
        # Parse child fields (vertices, edges, faces)
        # Return hierarchical structure
```

**Impact**: Blocks chart generation, may block other complex types

#### 2. Array of Objects (BLOCKER for Charts)

**Problem**: Parser cannot handle:
```yaml
visualizations:
  - file: path
    format: svg
  - file: path2
    format: png
```

**Required Enhancement**:
```python
class TemplateGenerator:
    def generate_array_of_objects(self, field_spec: Dict) -> str:
        """Generate template for array of objects."""
        # Detect object array pattern
        # Generate example object with placeholders
        # Format as YAML array
```

**Impact**: Blocks visualization metadata, potentially other optional structured fields

#### 3. Missing Specs for Edges/Faces

**Problem**: No spec-for-verification, spec-for-validation, spec-for-assurance exist

**Options**:
- **A**: Create specs for all edge/face types (adds complexity, circular dependencies)
- **B**: Treat templates as authoritative for meta-constructs (pragmatic, avoids circularity)
- **C**: Create lightweight "structural specs" that don't require assurance

**Recommendation**: **Option B** - Templates are specs for meta-constructs. Focus Phase 2 on vertex types and charts.

---

## Implications for Phase 2 Plan

### Original Phase 2 Scope
- Generate all 16 document type templates from specs
- **Document Types**: 7 vertices, 5 edges, 2 faces, 2 charts

### Revised Feasibility Assessment

**CAN Generate** (with enhancements):
- ✅ 7 vertex types: persona, purpose, protocol, spec, guidance, system_prompt, b0
- ⚠️ 2 chart types: chart, assurance_audit (REQUIRES nested object parser)

**CANNOT Generate** (no specs):
- ❌ 5 edge types: verification, validation, coupling, dependency, inherits
- ❌ 2 face types: assurance, doc-kit

**Total Feasible**: 7-9 types (depending on nested object parser)

### Recommended Phase 2 Scope Revision

**Option A - Vertices Only** (Conservative):
- Generate 7 vertex type templates
- Defer edges/faces/charts to Phase 3
- Faster delivery (6-8 hours)

**Option B - Vertices + Charts** (Moderate):
- Implement nested object parser (4-6 hours)
- Generate 7 vertex + 2 chart templates
- Higher value (charts are complex, high-leverage)
- Longer timeline (10-14 hours)

**Option C - Full Attempt** (Aggressive):
- Implement nested object parser
- Create specs for edges/faces
- Generate all 16 types
- Risk: circular dependencies, complexity explosion
- Timeline: 20-30 hours

**My Recommendation**: **Option B** - Vertices + Charts with enhanced parser

---

## Technical Requirements for Phase 2

### Must-Have Enhancements

1. **Nested Object Parser**
   ```python
   def parse_nested_field_structure(spec: Dict, field_name: str) -> Dict:
       """
       Parse hierarchical field structures like:
       elements:
         vertices: array
         edges: array
         faces: array
       """
   ```

2. **Object Array Generator**
   ```python
   def generate_object_array_template(field_spec: Dict) -> str:
       """
       Generate YAML for arrays of objects:
       visualizations:
         - file: <path>
           format: <format>
       """
   ```

3. **Conditional Field Logic**
   ```python
   def apply_conditional_requirements(field: str, context: Dict) -> bool:
       """
       Handle "REQUIRED when X" or "OPTIONAL - omit if Y"
       """
   ```

### Nice-to-Have Enhancements

1. **Enum Value Extraction**: Parse `manual | assisted | automated` into placeholder
2. **Format Example Preservation**: Use spec's format examples verbatim when available
3. **Comment Generation**: Add `# OPTIONAL` comments for optional fields

---

## Verification Strategy

### How to Verify Generated Templates

1. **Structural Verification** (automated):
   ```bash
   python scripts/verify_template_based.py <generated-template>
   ```
   **Pass Criteria**: Template itself passes template verification

2. **Example Instantiation** (semi-automated):
   ```bash
   # Create example instance from generated template
   cp <generated-template> <example-instance>
   # Fill placeholders with real values
   # Verify instance
   python scripts/verify_template_based.py <example-instance> --templates templates
   ```
   **Pass Criteria**: Instances created from template pass verification

3. **Human Review** (manual):
   - Compare generated template to hand-crafted original
   - Check for missing fields, malformed YAML, unclear placeholders
   - Verify body sections match spec requirements

**Success Criteria**: All three verification methods pass

---

## Recommendations

### For Phase 2 Implementation

1. **Prioritize Nested Object Parser**: This is the critical blocker for charts

2. **Test Incrementally**:
   - Generate persona template (already works)
   - Enhance parser for nested objects
   - Generate chart template
   - Verify chart template works
   - Proceed to other vertex types

3. **Accept Template-as-Spec for Meta-Constructs**:
   - Don't create specs for verification, validation, assurance edges/faces
   - Document that templates are authoritative for these types
   - Focus generation effort on high-value, spec-backed types

4. **Update Phase 2 Plan**:
   - Revise scope to 7 vertices + 2 charts (9 types)
   - Add nested object parser as Task 1a
   - Adjust timeline to 10-14 hours
   - Document why edges/faces are excluded

### For Future Phases

1. **Phase 3 - Edge/Face Specs** (if needed):
   - Create lightweight structural specs for edges/faces
   - Accept that they won't have full assurance (circular dependency)
   - Generate templates if value justifies effort

2. **Phase 4 - Advanced Parsers**:
   - Parse complex conditional logic
   - Handle cross-field dependencies
   - Support format examples with variables

---

## Appendix: Generated Chart Template

**File**: /tmp/chart-generated.md
**Size**: 65 lines, 1117 bytes
**Status**: ❌ FAILS verification (malformed YAML)

### Frontmatter (BROKEN)

```yaml
---
type: chart/chart
extends: doc
id: c:<name>
name: <Name>
tags:
  - chart
version: <Version>
created: YYYY-MM-DDTHH:MM:SSZ
modified: YYYY-MM-DDTHH:MM:SSZ
constructed_by: <Constructed By>
construction_method: <construction_method>
construction_date: YYYY-MM-DDTHH:MM:SSZ
purpose: <Purpose>
scope: <Scope>
elements: <elements>          # BROKEN: should be object, not placeholder
elements.vertices:             # BROKEN: should be nested under elements:
  - <elements.vertices_item>
elements.edges:                # BROKEN: should be nested under elements:
  - <elements.edges_item>
elements.faces:                # BROKEN: no value, malformed
description: <Description>
visualizations: <visualizations>  # BROKEN: should be array of objects
file: <File>                   # BROKEN: should be inside visualization object
format: <Format>               # BROKEN: should be inside visualization object
generated: YYYY-MM-DDTHH:MM:SSZ  # BROKEN: should be inside visualization object
generator: <Generator>         # BROKEN: should be inside visualization object
---
```

### Body (OK)

```markdown
# Chart - <Name>

## Chart Overview

# Chart: <Chart Name>

<Brief description of the chart and its purpose>

## Why This Chart Exists

[Why This Chart Exists content]

## What This Chart Contains

[What This Chart Contains content]

## How This Chart Was Constructed

[How This Chart Was Constructed content]

## Element Tables

[Element Tables content]

## Chart Properties

[Chart Properties content]

## Verification

[Verification content]

---

**Note:** This document is part of the PPP (Persona-Purpose-Protocol) framework.
```

---

**End of POC Report**
**Next Step**: Review findings with user, decide on Phase 2 scope revision
