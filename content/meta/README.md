# Meta Domain Pack - Meta-level Specifications

## Overview

The Meta pack provides infrastructure for documenting and organizing other documents. It includes types for specifications, guidances, charts, and audit trails.

## Dependencies

- **foundation**: Base ontology and genesis elements

## Vertex Types

| Type | Description |
|------|-------------|
| chart | Organizes elements into a verifiable simplicial complex |
| assurance-audit | Audit trail documenting assurance status |
| runbook | Step-by-step operational procedures |
| organization | Organizational entity documentation |
| repository-policy | Repository governance policies |
| literature-review | Survey of related work |
| property | Named property assertions |

## Domain Rules

### chart_completeness
All elements referenced in a chart must exist and be properly defined.

## Demo Chart

See `charts/demo-assurance-audit.md` for an example audit chart.
