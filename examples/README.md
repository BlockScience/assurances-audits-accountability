# Examples

This directory contains complete usage demonstrations of the AAA framework.

## Directory Structure

```
examples/
├── incose-paper/    # INCOSE paper self-demonstration
└── programs/        # Program development examples
```

## INCOSE Paper Self-Demonstration

The `incose-paper/` directory contains a complete knowledge complex demonstrating the framework applied to the INCOSE symposium paper "Test-Driven Document Development: Simplicial Complexes for Verification, Validation, and Assurance with Human Accountability".

This example demonstrates:
- Self-referential assurance (the paper assures itself)
- Complete V&V coverage with human accountability
- Type inheritance from framework base types

```bash
# Build the example cache
uv run aaa build examples/incose-paper

# Audit assurance coverage
uv run aaa audit examples/incose-paper/charts/incose-paper-assurance
```

## Program Development Examples

The `programs/` directory contains example program documentation:
- Bus Electrification Program
- Water Quality Monitoring Program
- Digital Transformation Program

These examples demonstrate how to apply the framework to real-world systems engineering programs, including program memos, plans, architecture documents, lifecycle models, and field surveys.

## Using Examples as Templates

Each example is self-contained with its own:
- `00_vertices/` - Document vertices
- `01_edges/` - Relationship edges
- `02_faces/` - Assurance faces
- `charts/` - Audit charts
- `complex.json` - Built cache (generated)

To create a new project based on an example:
1. Copy the example directory
2. Modify documents to match your domain
3. Update edges and faces to reflect new relationships
4. Run `uv run aaa build <your-project>` to validate
