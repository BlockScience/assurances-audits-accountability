# Educational Images

This directory contains static visualizations used in teaching guides and documentation.

## Contents

### assurance.png

**Purpose:** Illustrates the assurance triangle pattern

**Shows:**
- The three-edge structure of an assurance face
- Verification edge (doc → spec)
- Validation edge (doc → guidance)
- Coupling edge (spec ↔ guidance)
- How these form a complete quality framework

**Used in:**
- [charts/boundary-complex/TEACHING-GUIDE.md](../../charts/boundary-complex/TEACHING-GUIDE.md) - Stage 3

**Size:** ~138 KB

### boundary.png

**Purpose:** Visualizes the complete boundary complex structure

**Shows:**
- b0:root vertex (center anchor)
- Four foundational documents (SS, GG, SG, GS)
- Boundary edges (b1) connecting to root
- Standard edges connecting foundational docs
- Green faces (standard assurance: SG, GS)
- Blue faces (boundary assurance: SS, GG)
- Complete topological structure resolving self-reference

**Used in:**
- [charts/boundary-complex/TEACHING-GUIDE.md](../../charts/boundary-complex/TEACHING-GUIDE.md) - Stage 3

**Size:** ~212 KB

## Generating Interactive Visualizations

While these static PNG images are useful for documentation, learners are encouraged to generate **interactive 3D HTML visualizations** using the provided scripts:

```bash
# Export chart to JSON
python scripts/export_chart_direct.py charts/boundary-complex/boundary-complex.md

# Generate interactive 3D visualization
python scripts/visualize_chart.py charts/boundary-complex/boundary-complex.json

# Opens in browser - explore in 3D!
```

The interactive visualizations allow:
- Rotation and zoom
- Vertex/edge/face inspection
- Dynamic highlighting
- Better understanding of 3D structure

## Adding New Images

When adding educational images:

1. **Name clearly:** Use descriptive names (e.g., `assurance-triangle.png`, `boundary-complex.png`)
2. **Optimize size:** Compress images to reasonable file sizes
3. **Document:** Update this README with description and usage
4. **Reference:** Link from teaching guides with alt text and captions
5. **Static + Interactive:** Provide both static images (docs) and scripts to generate interactive versions

## Image Guidelines

- **Format:** PNG for diagrams and visualizations
- **Resolution:** High enough to be readable, but compressed for web use
- **Alt text:** Always include descriptive alt text in markdown
- **Captions:** Add italic caption below images explaining what's shown
- **Context:** Embed images near related concepts in teaching guides

---

**Note:** These images complement the interactive visualizations - they don't replace them. Static images work in all contexts (PDFs, printed docs, quick reference), while interactive visualizations enable hands-on exploration.
