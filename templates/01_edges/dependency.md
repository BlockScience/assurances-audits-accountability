---
type: template/edge/dependency
extends: edge
id: template:edge:dependency
name: Dependency Edge Template
description: Tracks compositional dependencies where source document uses target document type in typed subsections
instantiable: true
tags:
  - template
  - edge
  - dependency
version: 1.0.0
created: 2025-12-27T23:00:00Z
modified: 2025-12-27T23:00:00Z
---

# Dependency Edge Template

**Tracks that one document type uses/depends on another document type in its structure (compositional dependency).**

## Type Hierarchy

```
edge (abstract)
└── dependency (concrete) ← YOU ARE HERE
```

## Inheritance

- **Extends:** `edge`
- **Extended by:** None (terminal type)
- **Instantiable:** Yes

## Required Frontmatter Fields

Inherits all edge fields, plus dependency-specific constraints:

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | Must be `edge/dependency` |
| `extends` | string | Must be `edge` |
| `id` | string | Unique identifier (format: `e:dependency:<dependent>:<dependency>`) |
| `name` | string | Human-readable edge name |
| `description` | string | Clear explanation of the dependency relationship |
| `source` | string | Dependent vertex ID (the document that uses/requires) |
| `target` | string | Dependency vertex ID (the document type being used) |
| `source_type` | string | Type of source vertex (must match source's type field) |
| `target_type` | string | Type of target vertex (must match target's type field) |
| `orientation` | string | Must be `directed` |
| `dependency_type` | string | Type of dependency (see below) |
| `subsection_field` | string | Optional: Which field/subsection uses the dependency |
| `required` | boolean | Whether this dependency is mandatory |
| `tags` | array | Must include `[edge, dependency]` |
| `version` | string | Semantic version |
| `created` | datetime | ISO 8601 creation timestamp |
| `modified` | datetime | ISO 8601 last modification timestamp |

## Tag Requirements

The `tags` array MUST include the full inheritance chain:

```yaml
tags:
  - edge        # base type
  - dependency  # concrete type
```

## Endpoint Constraints

### Source Vertex (Dependent - the one that uses)
- **Role:** The document that contains/uses the dependency
- **Type Constraint:** Must be same document class as target (spec→spec, guidance→guidance)
- **Direction:** Uses/depends on target

### Target Vertex (Dependency - the one being used)
- **Role:** The document type being used/required
- **Type Constraint:** Must be same document class as source
- **Direction:** Used by source

### Type Consistency Rule
Both vertices MUST be the same document class:
- Spec → Spec: `vertex/spec` → `vertex/spec`
- Guidance → Guidance: `vertex/guidance` → `vertex/guidance`

**Invalid:** Spec depending on Guidance, or any cross-class dependencies

## Orientation

Dependency edges are **directed** - dependency flows from dependent to dependency:
- Arrow points from dependent TO dependency: `dependent --depends-on--> dependency`
- Source uses/requires target
- Target is used by source

## Dependency Type

The `dependency_type` field MUST be one of:

- **`typed_subsection`** (most common): Source has a subsection that must conform to target type
  - Example: `system_prompt` has `persona` subsection that must conform to `spec:persona`
  - Like JSON-LD `@context` - defines type constraints for nested content
- **`compositional`**: Source is built from target as a component
- **`reference`**: Source references target but doesn't contain it
- **`structural`**: Source's structure requires target's structure

## Relationship to Inheritance

**CRITICAL:** Dependency edges are **different from inherits edges**.

```
Inheritance (inherits edges):
  v:spec:assurance_audit --inherits--> v:spec:chart
  (assurance_audit IS A chart - specialization)

Dependency (dependency edges):
  v:spec:system_prompt --depends-on--> v:spec:persona
  (system_prompt HAS A persona - composition)
```

**Inherits edges** model "is-a" relationships (domain specialization)
**Dependency edges** model "uses" or "has-a" relationships (composition)

## Relationship to Assurance DAG

Like inherits edges, dependency edges are **separate from the assurance DAG**.

```
Dependency Graph (dependency edges):
  v:spec:system_prompt --depends-on--> v:spec:persona
  v:spec:system_prompt --depends-on--> v:spec:purpose
  v:spec:system_prompt --depends-on--> v:spec:protocol

Assurance DAG (verification edges):
  v:spec:system_prompt --verifies--> v:spec:spec
  v:spec:persona --verifies--> v:spec:spec
  v:spec:purpose --verifies--> v:spec:spec
  v:spec:protocol --verifies--> v:spec:spec
```

**Dependency edges** explain composition: "what uses what"
**Verification edges** prove assurance: "what verifies against what"

## Validation Rules

1. **Direction Consistency:** Source MUST use/require target (not vice versa)
2. **Type Consistency:** Both source and target MUST be same document class
3. **Acyclic:** Dependency graph SHOULD be a DAG (no cycles - prevents circular dependencies)
4. **Subsection Clarity:** If `dependency_type: typed_subsection`, should specify `subsection_field`
5. **Separate from Assurance:** Dependency edges MUST NOT be confused with verification edges

## Required Sections

All dependency edges MUST include these markdown sections:

### 1. Dependency Relationship

**Required heading:** `# Dependency Relationship` or `## Dependency Relationship`

**Must document:**
- Dependent (source) vertex identification
- Dependency (target) vertex identification
- Dependency direction explanation
- How the dependency is used (which subsection, field, or structural element)
- Relationship to assurance DAG (clarify separation)

**Example:**
```markdown
## Dependency Relationship

**Dependent:** `v:spec:system_prompt` (Specification for System Prompt Documents)
**Dependency:** `v:spec:persona` (Specification for Persona Documents)
**Relationship:** system_prompt uses persona (typed subsection)

**Usage:** System prompts have a `persona` subsection that must conform to the persona spec. This is a compositional dependency - system prompts are built FROM persona, purpose, and protocol components.

**Assurance Note:** This dependency edge tracks composition and is separate from the assurance DAG. For assurance, system_prompt verifies against v:spec:spec (because system_prompt is a spec), not against v:spec:persona.
```

### 2. Dependency Usage

**Required heading:** `# Dependency Usage` or `## Dependency Usage`

**Must document:**
- How the dependency is used structurally
- Which fields/subsections require the dependency
- Whether the dependency is required or optional
- Cardinality (one or many instances)

### 3. Compositional Justification

**Required heading:** `# Compositional Justification` or `## Compositional Justification`

**Must explain:**
- Why this composition makes sense
- Use case explanation
- How this differs from inheritance (why not "is-a")
- How this differs from assurance relationships

## Role in Type System

Dependency edges provide:
- **Compositional Clarity:** What document types are built from other types
- **Type Safety:** Subsections have defined type constraints (like JSON-LD context)
- **Dependency Tracking:** What depends on what (for impact analysis)
- **Documentation:** Clear compositional relationships

They do NOT provide:
- **Inheritance:** That's the role of inherits edges (is-a vs has-a)
- **Assurance:** That's the role of verification/validation edges
- **Quality Guarantees:** Using a type doesn't guarantee quality

## Common Patterns

### Pattern 1: Typed Subsections (PPP Framework)
```yaml
# System prompt depends on persona
source: v:spec:system_prompt    # composite document
target: v:spec:persona          # component document
source_type: vertex/spec
target_type: vertex/spec
dependency_type: typed_subsection
subsection_field: persona
required: true
```

### Pattern 2: Parallel Dependencies (Spec and Guidance)
Often specs and guidances have parallel dependencies:
- `e:dependency:system_prompt:persona` (spec → spec)
- `e:dependency:system_prompt-guidance:persona-guidance` (guidance → guidance)

### Pattern 3: Multiple Dependencies
A document can depend on multiple types:
- `system_prompt` depends on `persona`, `purpose`, `protocol`
- Each is a separate dependency edge

## Examples

### Example 1: System Prompt → Persona
```yaml
---
type: edge/dependency
extends: edge
id: e:dependency:system_prompt:persona
name: Dependency - System Prompt uses Persona
description: System prompts have a persona subsection conforming to persona spec
source: v:spec:system_prompt
target: v:spec:persona
source_type: vertex/spec
target_type: vertex/spec
orientation: directed
dependency_type: typed_subsection
subsection_field: persona
required: true
version: 1.0.0
created: 2025-12-27T23:00:00Z
modified: 2025-12-27T23:00:00Z
tags:
  - edge
  - dependency
  - typed-subsection
---
```

### Example 2: Guidance Dependencies
```yaml
---
type: edge/dependency
extends: edge
id: e:dependency:system_prompt-guidance:persona-guidance
name: Dependency - Guidance for System Prompts uses Guidance for Personas
description: System prompt guidances reference persona quality criteria
source: v:guidance:system_prompt
target: v:guidance:persona
source_type: vertex/guidance
target_type: vertex/guidance
orientation: directed
dependency_type: typed_subsection
subsection_field: persona
required: true
---
```

## Notes

- Dependency edges model **composition** ("has-a", "uses")
- Inherits edges model **specialization** ("is-a", "extends")
- Both are separate from assurance edges
- Typed subsections are like JSON-LD `@context` - they constrain nested content types
- Dependencies enable modular, composable document types
- Keep dependency graphs acyclic to avoid circular dependencies
- Visualization tools should render these separately from inherits and assurance edges

## Comparison Table

| Edge Type | Relationship | Example | Purpose |
|-----------|-------------|---------|---------|
| **Inherits** | is-a (specialization) | assurance_audit extends chart | Domain hierarchy |
| **Dependency** | uses/has-a (composition) | system_prompt uses persona | Compositional structure |
| **Verification** | verifies-against (assurance) | system_prompt verifies against spec | Structural compliance |
| **Validation** | validates-against (assurance) | system_prompt validates against guidance | Quality assessment |

---

**Template Version:** 1.0.0
**Template Status:** Active
**Last Modified:** 2025-12-27
