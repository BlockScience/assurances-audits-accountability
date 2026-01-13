# Learning Domain Pack

This pack provides document types for educational content and skill tracking, including syllabi, learning modules, skills, and student progress.

## Pack Info

- **Dependencies:** boundary, foundation, meta
- **Manifest:** [pack.yaml](pack.yaml)

## Vertex Types

| Type | Description |
|------|-------------|
| student | Student profile and progress tracking |
| skill | Named skill that can be learned |
| syllabus | Course structure and learning objectives |
| learning-module | Individual learning unit within a syllabus |

## Learning Workflow

```text
syllabus → learning-module → skill
    ↓           ↓              ↑
student ──── studies ──── has-skill
```

Students study syllabi and learning modules. Completing modules grants skills. Prerequisites are enforced through the requires-skill edge type.

## Edge Types

| Type | Source → Target | Description |
|------|-----------------|-------------|
| studies | student → syllabus/module | Student is studying content |
| has-skill | student → skill | Student has acquired skill |
| requires-skill | learning-module → skill | Module requires prerequisite skill |
| inherits | vertex → vertex | Type inheritance relationship |

## Face Types

| Type | Boundary | Description |
|------|----------|-------------|
| prerequisite | requires-skill, has-skill, studies | Student meets prerequisites for module |
| skill-gain | studies, completion, has-skill | Student gains skill through completion |
| completion | studies, validation, signature | Student completes learning unit |

## Domain Rules

### prerequisites_met
**Severity:** error

Student must have all required skills before starting a module. This enforces prerequisite chains.

### skill_gain_requires_completion
**Severity:** error

Skills gained must trace to completed modules. No skill is granted without demonstrable completion.

## Directory Structure

```text
content/learning/
├── 00_vertices/     # Student, skill, syllabus, module specs and instances
├── 01_edges/        # Studies, has-skill, requires-skill edges
├── 02_faces/        # Prerequisite, skill-gain, completion faces
└── charts/          # Demo charts for learning workflows
```

## Related Packs

- **meta**: Learning content organized into charts
- **rbac**: Can be combined with rbac for completion attestations with authorized signatures
- **ppp**: Can be combined with ppp for student persona definitions
