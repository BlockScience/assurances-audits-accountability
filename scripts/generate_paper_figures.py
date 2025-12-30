#!/usr/bin/env python3
"""
Generate High-Quality SVG Figures for INCOSE IS 2026 Paper

Creates three publication-quality figures:
1. Figure 1: The Assurance Triangle Pattern (conceptual)
2. Figure 2: INCOSE Paper Audit Chart (empirical result)
3. Figure 3: Boundary Complex Structure (foundation)

Usage:
    python scripts/generate_paper_figures.py [--output-dir figures/]
"""

import argparse
import math
from pathlib import Path
from typing import Tuple, List, Optional
from dataclasses import dataclass


# =============================================================================
# Color Palette
# =============================================================================

COLORS = {
    # Vertex colors
    'spec_fill': '#2ECC71',
    'spec_stroke': '#1D8348',
    'guidance_fill': '#E67E22',
    'guidance_stroke': '#A04000',
    'doc_fill': '#3498DB',
    'doc_stroke': '#2471A3',
    'root_fill': '#FFD700',
    'root_stroke': '#B8860B',

    # Edge colors
    'verification': '#2ECC71',
    'validation': '#E67E22',
    'coupling': '#9B59B6',
    'boundary': '#95A5A6',

    # Face colors
    'face_standard': '#E8F8E8',
    'face_boundary': '#E0F0FF',
    'face_paper': '#FFF8E8',
    'face_conceptual': '#F8F9FA',

    # Text colors
    'text_dark': '#2C3E50',
    'text_light': '#FFFFFF',
    'text_muted': '#7F8C8D',
    'text_annotation': '#666666',

    # Checkmark
    'checkmark': '#27AE60',
}


# =============================================================================
# SVG Primitives
# =============================================================================

def svg_header(width: int, height: int, title: str) -> str:
    """Generate SVG header with proper namespaces."""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{width}" height="{height}"
     viewBox="0 0 {width} {height}">
  <title>{title}</title>
  <defs>
    <style>
      .label {{ font-family: Arial, Helvetica, sans-serif; }}
      .label-bold {{ font-family: Arial, Helvetica, sans-serif; font-weight: bold; }}
      .mono {{ font-family: 'Consolas', 'Monaco', monospace; }}
    </style>
    <!-- Arrow marker for directed edges -->
    <marker id="arrow-verification" markerWidth="10" markerHeight="7"
            refX="9" refY="3.5" orient="auto" markerUnits="strokeWidth">
      <polygon points="0 0, 10 3.5, 0 7" fill="{COLORS['verification']}" />
    </marker>
    <marker id="arrow-validation" markerWidth="10" markerHeight="7"
            refX="9" refY="3.5" orient="auto" markerUnits="strokeWidth">
      <polygon points="0 0, 10 3.5, 0 7" fill="{COLORS['validation']}" />
    </marker>
    <marker id="arrow-boundary" markerWidth="10" markerHeight="7"
            refX="9" refY="3.5" orient="auto" markerUnits="strokeWidth">
      <polygon points="0 0, 10 3.5, 0 7" fill="{COLORS['boundary']}" />
    </marker>
  </defs>
'''


def svg_footer() -> str:
    return '</svg>\n'


def svg_rect(x: float, y: float, w: float, h: float,
             fill: str, stroke: str, stroke_width: float = 2,
             rx: float = 0, ry: float = 0) -> str:
    """Draw a rectangle (optionally rounded)."""
    return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />\n'


def svg_circle(cx: float, cy: float, r: float,
               fill: str, stroke: str, stroke_width: float = 2) -> str:
    """Draw a circle."""
    return f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />\n'


def svg_star(cx: float, cy: float, r_outer: float, r_inner: float,
             points: int, fill: str, stroke: str, stroke_width: float = 2) -> str:
    """Draw a star polygon."""
    path_data = []
    for i in range(points * 2):
        angle = (i * math.pi / points) - math.pi / 2
        r = r_outer if i % 2 == 0 else r_inner
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        cmd = 'M' if i == 0 else 'L'
        path_data.append(f'{cmd} {x:.1f} {y:.1f}')
    path_data.append('Z')
    return f'  <path d="{" ".join(path_data)}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />\n'


def svg_line(x1: float, y1: float, x2: float, y2: float,
             stroke: str, stroke_width: float = 2,
             dash: Optional[str] = None, marker_end: Optional[str] = None) -> str:
    """Draw a line."""
    attrs = f'x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{stroke_width}"'
    if dash:
        attrs += f' stroke-dasharray="{dash}"'
    if marker_end:
        attrs += f' marker-end="url(#{marker_end})"'
    return f'  <line {attrs} />\n'


def svg_double_line(x1: float, y1: float, x2: float, y2: float,
                    stroke: str, gap: float = 3) -> str:
    """Draw a double line (for coupling edges)."""
    # Calculate perpendicular offset
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx*dx + dy*dy)
    if length == 0:
        return ''
    nx = -dy / length * gap / 2
    ny = dx / length * gap / 2

    line1 = svg_line(x1 + nx, y1 + ny, x2 + nx, y2 + ny, stroke, 1.5)
    line2 = svg_line(x1 - nx, y1 - ny, x2 - nx, y2 - ny, stroke, 1.5)
    return line1 + line2


def svg_polygon(points: List[Tuple[float, float]], fill: str,
                opacity: float = 1.0, stroke: Optional[str] = None,
                stroke_width: float = 0) -> str:
    """Draw a filled polygon."""
    points_str = ' '.join(f'{x},{y}' for x, y in points)
    attrs = f'points="{points_str}" fill="{fill}" fill-opacity="{opacity}"'
    if stroke:
        attrs += f' stroke="{stroke}" stroke-width="{stroke_width}"'
    return f'  <polygon {attrs} />\n'


def svg_text(x: float, y: float, text: str, font_size: int = 11,
             fill: str = '#2C3E50', anchor: str = 'middle',
             weight: str = 'normal', css_class: str = 'label') -> str:
    """Draw text."""
    style = f'font-size: {font_size}px; font-weight: {weight};'
    return f'  <text x="{x}" y="{y}" text-anchor="{anchor}" class="{css_class}" style="{style}" fill="{fill}">{text}</text>\n'


def svg_checkmark(x: float, y: float, size: float = 12) -> str:
    """Draw a checkmark."""
    return f'''  <g transform="translate({x}, {y})">
    <circle cx="0" cy="0" r="{size/2 + 2}" fill="{COLORS['checkmark']}" />
    <path d="M {-size/3} 0 L {-size/8} {size/4} L {size/3} {-size/4}"
          stroke="white" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" />
  </g>\n'''


# =============================================================================
# Figure 1: Assurance Triangle Pattern
# =============================================================================

def generate_figure1_assurance_triangle() -> str:
    """
    Generate conceptual diagram showing the assurance triangle pattern.

    Layout:
        Document ─────── Guidance
            ╲             ╱
             ╲    △     ╱
              ╲       ╱
               Specification
    """
    width, height = 350, 280
    svg = svg_header(width, height, "Figure 1: The Assurance Triangle Pattern")

    # Vertex positions (point-down triangle)
    doc_pos = (100, 70)
    guidance_pos = (250, 70)
    spec_pos = (175, 200)

    # Draw face (triangle fill) FIRST (background)
    svg += '  <!-- Face fill -->\n'
    svg += svg_polygon(
        [doc_pos, guidance_pos, spec_pos],
        COLORS['face_conceptual'], opacity=0.7
    )

    # Draw edges
    svg += '  <!-- Edges -->\n'

    # Verification: Document → Specification (solid green arrow)
    # Shorten line to not overlap with shapes
    svg += svg_line(doc_pos[0] + 15, doc_pos[1] + 20,
                    spec_pos[0] - 20, spec_pos[1] - 15,
                    COLORS['verification'], 2.5, marker_end='arrow-verification')

    # Validation: Document → Guidance (dashed orange arrow)
    svg += svg_line(doc_pos[0] + 25, doc_pos[1],
                    guidance_pos[0] - 25, guidance_pos[1],
                    COLORS['validation'], 2.5, dash='5,3', marker_end='arrow-validation')

    # Coupling: Specification ↔ Guidance (purple double line, no arrow)
    svg += svg_double_line(spec_pos[0] + 20, spec_pos[1] - 15,
                           guidance_pos[0] - 15, guidance_pos[1] + 20,
                           COLORS['coupling'], gap=4)

    # Draw vertices
    svg += '  <!-- Vertices -->\n'

    # Document vertex (blue circle)
    svg += svg_circle(doc_pos[0], doc_pos[1], 28,
                      COLORS['doc_fill'], COLORS['doc_stroke'], 2.5)
    svg += svg_text(doc_pos[0], doc_pos[1] + 4, "Doc", 11,
                    COLORS['text_light'], weight='bold')

    # Guidance vertex (orange rounded rectangle)
    svg += svg_rect(guidance_pos[0] - 32, guidance_pos[1] - 18, 64, 36,
                    COLORS['guidance_fill'], COLORS['guidance_stroke'], 2.5, rx=8, ry=8)
    svg += svg_text(guidance_pos[0], guidance_pos[1] + 5, "Guidance", 11,
                    COLORS['text_light'], weight='bold')

    # Specification vertex (green rectangle)
    svg += svg_rect(spec_pos[0] - 32, spec_pos[1] - 18, 64, 36,
                    COLORS['spec_fill'], COLORS['spec_stroke'], 2.5)
    svg += svg_text(spec_pos[0], spec_pos[1] + 5, "Spec", 11,
                    COLORS['text_light'], weight='bold')

    # Edge labels/annotations
    svg += '  <!-- Edge annotations -->\n'

    # Verification annotation (along Doc→Spec edge)
    svg += svg_text(115, 145, "Verification", 9, COLORS['text_annotation'])
    svg += svg_text(115, 157, "(structural)", 8, COLORS['text_muted'])

    # Validation annotation (along Doc→Guidance edge)
    svg += svg_text(175, 50, "Validation", 9, COLORS['text_annotation'])
    svg += svg_text(175, 62, "(qualitative)", 8, COLORS['text_muted'])

    # Coupling annotation (along Spec↔Guidance edge)
    svg += svg_text(235, 150, "Coupling", 9, COLORS['text_annotation'])
    svg += svg_text(235, 162, "(type coherence)", 8, COLORS['text_muted'])

    # Legend box
    svg += '  <!-- Legend -->\n'
    svg += svg_rect(250, 220, 90, 55, '#FFFFFF', '#CCCCCC', 1, rx=4, ry=4)
    svg += svg_text(295, 234, "Legend", 9, COLORS['text_dark'], weight='bold')

    # Legend items
    svg += svg_line(258, 248, 278, 248, COLORS['verification'], 2)
    svg += svg_text(282, 252, "Verification", 8, COLORS['text_dark'], anchor='start')

    svg += svg_line(258, 262, 278, 262, COLORS['validation'], 2, dash='4,2')
    svg += svg_text(282, 266, "Validation", 8, COLORS['text_dark'], anchor='start')

    svg += svg_double_line(258, 275, 278, 275, COLORS['coupling'], gap=3)
    svg += svg_text(282, 279, "Coupling", 8, COLORS['text_dark'], anchor='start')

    svg += svg_footer()
    return svg


# =============================================================================
# Figure 2: INCOSE Paper Audit Chart
# =============================================================================

def generate_figure2_audit_chart() -> str:
    """
    Generate the INCOSE paper audit chart - the hero figure.

    Hierarchical layout with 3 layers showing complete assurance network.
    """
    width, height = 550, 420
    svg = svg_header(width, height, "Figure 2: INCOSE Paper Audit Chart")

    # Vertex positions by layer
    positions = {
        # Layer 2 - The Paper (top)
        'v:doc:incose-paper-2026': (275, 55),

        # Layer 1 - INCOSE Type Documents
        'v:spec:incose-paper': (175, 135),
        'v:guidance:incose-paper': (375, 135),

        # Layer 0 - Boundary Complex Foundation
        'v:spec:spec': (95, 245),
        'v:spec:guidance': (195, 245),
        'v:guidance:spec': (295, 245),
        'v:guidance:guidance': (395, 245),

        # Root
        'b0:root': (245, 335),
    }

    # Abbreviated labels
    labels = {
        'v:doc:incose-paper-2026': 'PAPER',
        'v:spec:incose-paper': 'I-S',
        'v:guidance:incose-paper': 'I-G',
        'v:spec:spec': 'SS',
        'v:spec:guidance': 'SG',
        'v:guidance:spec': 'GS',
        'v:guidance:guidance': 'GG',
        'b0:root': '★',
    }

    # Draw faces first (background)
    svg += '  <!-- Faces -->\n'

    # Paper's assurance face (highlighted)
    paper_face = [positions['v:doc:incose-paper-2026'],
                  positions['v:spec:incose-paper'],
                  positions['v:guidance:incose-paper']]
    svg += svg_polygon(paper_face, COLORS['face_paper'], 0.7,
                       stroke='#DAA520', stroke_width=2)

    # INCOSE spec assurance face
    incose_spec_face = [positions['v:spec:incose-paper'],
                        positions['v:spec:spec'],
                        positions['v:guidance:spec']]
    svg += svg_polygon(incose_spec_face, COLORS['face_standard'], 0.5)

    # INCOSE guidance assurance face
    incose_guidance_face = [positions['v:guidance:incose-paper'],
                            positions['v:spec:guidance'],
                            positions['v:guidance:guidance']]
    svg += svg_polygon(incose_guidance_face, COLORS['face_standard'], 0.5)

    # Spec-guidance assurance face
    sg_face = [positions['v:spec:guidance'],
               positions['v:spec:spec'],
               positions['v:guidance:spec']]
    svg += svg_polygon(sg_face, COLORS['face_standard'], 0.4)

    # Guidance-spec assurance face
    gs_face = [positions['v:guidance:spec'],
               positions['v:spec:guidance'],
               positions['v:guidance:guidance']]
    svg += svg_polygon(gs_face, COLORS['face_standard'], 0.4)

    # Boundary faces (b2)
    b2_ss_face = [positions['b0:root'],
                  positions['v:guidance:spec'],
                  positions['v:spec:spec']]
    svg += svg_polygon(b2_ss_face, COLORS['face_boundary'], 0.5)

    b2_gg_face = [positions['b0:root'],
                  positions['v:spec:guidance'],
                  positions['v:guidance:guidance']]
    svg += svg_polygon(b2_gg_face, COLORS['face_boundary'], 0.5)

    # Draw edges
    svg += '  <!-- Edges -->\n'

    # Helper function to draw edge between vertices with offset
    def edge(v1, v2, etype, offset_start=0, offset_end=0):
        p1 = positions[v1]
        p2 = positions[v2]
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        length = math.sqrt(dx*dx + dy*dy)
        if length == 0:
            return ''
        ux, uy = dx/length, dy/length
        x1 = p1[0] + ux * offset_start
        y1 = p1[1] + uy * offset_start
        x2 = p2[0] - ux * offset_end
        y2 = p2[1] - uy * offset_end

        if etype == 'verification':
            return svg_line(x1, y1, x2, y2, COLORS['verification'], 1.5,
                           marker_end='arrow-verification')
        elif etype == 'validation':
            return svg_line(x1, y1, x2, y2, COLORS['validation'], 1.5,
                           dash='4,2', marker_end='arrow-validation')
        elif etype == 'coupling':
            return svg_double_line(x1, y1, x2, y2, COLORS['coupling'], gap=3)
        elif etype == 'boundary':
            return svg_line(x1, y1, x2, y2, COLORS['boundary'], 1.5,
                           dash='2,2', marker_end='arrow-boundary')
        return ''

    # Layer 2 → Layer 1 edges
    svg += edge('v:doc:incose-paper-2026', 'v:spec:incose-paper', 'verification', 30, 25)
    svg += edge('v:doc:incose-paper-2026', 'v:guidance:incose-paper', 'validation', 30, 25)
    svg += edge('v:spec:incose-paper', 'v:guidance:incose-paper', 'coupling', 28, 28)

    # Layer 1 → Layer 0 edges
    svg += edge('v:spec:incose-paper', 'v:spec:spec', 'verification', 25, 22)
    svg += edge('v:spec:incose-paper', 'v:guidance:spec', 'validation', 25, 22)
    svg += edge('v:guidance:incose-paper', 'v:spec:guidance', 'verification', 25, 22)
    svg += edge('v:guidance:incose-paper', 'v:guidance:guidance', 'validation', 25, 22)

    # Layer 0 internal edges
    svg += edge('v:spec:spec', 'v:guidance:spec', 'coupling', 25, 25)
    svg += edge('v:spec:guidance', 'v:guidance:guidance', 'coupling', 25, 25)
    svg += edge('v:spec:guidance', 'v:guidance:spec', 'coupling', 25, 25)
    svg += edge('v:spec:guidance', 'v:spec:spec', 'verification', 25, 25)
    svg += edge('v:guidance:spec', 'v:spec:guidance', 'verification', 25, 25)
    svg += edge('v:guidance:guidance', 'v:spec:guidance', 'verification', 25, 25)
    svg += edge('v:spec:spec', 'v:guidance:spec', 'validation', 25, 25)
    svg += edge('v:spec:guidance', 'v:guidance:spec', 'validation', 25, 25)
    svg += edge('v:guidance:spec', 'v:guidance:guidance', 'validation', 25, 25)

    # Boundary edges to root
    svg += edge('v:spec:spec', 'b0:root', 'boundary', 22, 22)
    svg += edge('v:guidance:guidance', 'b0:root', 'boundary', 22, 22)
    svg += edge('b0:root', 'v:guidance:spec', 'boundary', 22, 22)
    svg += edge('b0:root', 'v:spec:guidance', 'boundary', 22, 22)

    # Draw vertices
    svg += '  <!-- Vertices -->\n'

    for vid, pos in positions.items():
        label = labels[vid]

        if vid == 'b0:root':
            # Star shape for root
            svg += svg_star(pos[0], pos[1], 20, 10, 6,
                           COLORS['root_fill'], COLORS['root_stroke'], 2.5)
            svg += svg_text(pos[0], pos[1] + 5, label, 14, COLORS['text_dark'], weight='bold')
        elif vid.startswith('v:doc:'):
            # Blue circle for document (larger, highlighted)
            svg += svg_circle(pos[0], pos[1], 32,
                             COLORS['doc_fill'], COLORS['doc_stroke'], 3)
            svg += svg_text(pos[0], pos[1] + 5, label, 12,
                           COLORS['text_light'], weight='bold')
        elif vid.startswith('v:spec:'):
            # Green rectangle for specs
            svg += svg_rect(pos[0] - 22, pos[1] - 15, 44, 30,
                           COLORS['spec_fill'], COLORS['spec_stroke'], 2)
            svg += svg_text(pos[0], pos[1] + 5, label, 11,
                           COLORS['text_light'], weight='bold')
        elif vid.startswith('v:guidance:'):
            # Orange rounded rectangle for guidance
            svg += svg_rect(pos[0] - 22, pos[1] - 15, 44, 30,
                           COLORS['guidance_fill'], COLORS['guidance_stroke'], 2, rx=6, ry=6)
            svg += svg_text(pos[0], pos[1] + 5, label, 11,
                           COLORS['text_light'], weight='bold')

    # Add checkmarks next to each vertex
    svg += '  <!-- Assurance checkmarks -->\n'
    for vid, pos in positions.items():
        offset_x = 35 if vid.startswith('v:doc:') else 28
        svg += svg_checkmark(pos[0] + offset_x, pos[1] - 15, 10)

    # Layer labels (left margin)
    svg += '  <!-- Layer labels -->\n'
    svg += svg_text(25, 55, "Layer 2", 10, COLORS['text_dark'],
                    anchor='start', weight='bold')
    svg += svg_text(25, 68, "This Paper", 9, COLORS['text_muted'], anchor='start')

    svg += svg_text(25, 135, "Layer 1", 10, COLORS['text_dark'],
                    anchor='start', weight='bold')
    svg += svg_text(25, 148, "Paper Type", 9, COLORS['text_muted'], anchor='start')

    svg += svg_text(25, 245, "Layer 0", 10, COLORS['text_dark'],
                    anchor='start', weight='bold')
    svg += svg_text(25, 258, "Foundation", 9, COLORS['text_muted'], anchor='start')

    # Statistics box (bottom right)
    svg += '  <!-- Statistics box -->\n'
    svg += svg_rect(435, 345, 105, 65, '#FFFFFF', '#CCCCCC', 1, rx=4, ry=4)
    svg += svg_text(487, 360, "Topology", 9, COLORS['text_dark'], weight='bold')
    svg += svg_text(445, 378, "V = 8, E = 20, F = 7", 9, COLORS['text_dark'],
                    anchor='start', css_class='mono')
    svg += svg_text(445, 393, "χ = -5", 9, COLORS['text_dark'],
                    anchor='start', css_class='mono')

    # Coverage badge (top right)
    svg += '  <!-- Coverage badge -->\n'
    svg += svg_rect(450, 15, 90, 28, COLORS['checkmark'], COLORS['checkmark'], 0, rx=14, ry=14)
    svg += svg_text(495, 34, "100% Coverage", 10, COLORS['text_light'], weight='bold')

    # Legend box
    svg += '  <!-- Legend -->\n'
    svg += svg_rect(10, 345, 120, 65, '#FFFFFF', '#CCCCCC', 1, rx=4, ry=4)
    svg += svg_text(70, 360, "Legend", 9, COLORS['text_dark'], weight='bold')

    svg += svg_line(18, 375, 38, 375, COLORS['verification'], 2)
    svg += svg_text(42, 379, "Verification", 8, COLORS['text_dark'], anchor='start')

    svg += svg_line(18, 390, 38, 390, COLORS['validation'], 2, dash='4,2')
    svg += svg_text(42, 394, "Validation", 8, COLORS['text_dark'], anchor='start')

    svg += svg_double_line(80, 375, 100, 375, COLORS['coupling'], gap=2)
    svg += svg_text(104, 379, "Coupling", 8, COLORS['text_dark'], anchor='start')

    svg += svg_line(80, 390, 100, 390, COLORS['boundary'], 2, dash='2,2')
    svg += svg_text(104, 394, "Boundary", 8, COLORS['text_dark'], anchor='start')

    svg += svg_footer()
    return svg


# =============================================================================
# Figure 3: Boundary Complex Structure
# =============================================================================

def generate_figure3_boundary_complex() -> str:
    """
    Generate the boundary complex showing the self-referential foundation.

    Layout: Root at center with 4 foundational vertices around it.
    """
    width, height = 350, 300
    svg = svg_header(width, height, "Figure 3: Boundary Complex Structure")

    # Vertex positions (root at center, 4 corners)
    positions = {
        'b0:root': (175, 155),
        'v:spec:spec': (75, 70),
        'v:spec:guidance': (275, 70),
        'v:guidance:spec': (75, 220),
        'v:guidance:guidance': (275, 220),
    }

    # Full labels for this figure
    full_labels = {
        'v:spec:spec': 'Spec-for-Spec',
        'v:spec:guidance': 'Spec-for-Guidance',
        'v:guidance:spec': 'Guidance-for-Spec',
        'v:guidance:guidance': 'Guidance-for-Guidance',
    }

    short_labels = {
        'v:spec:spec': 'SS',
        'v:spec:guidance': 'SG',
        'v:guidance:spec': 'GS',
        'v:guidance:guidance': 'GG',
    }

    # Draw faces first
    svg += '  <!-- Faces -->\n'

    # Boundary face b2:spec-spec (left triangle)
    b2_ss = [positions['b0:root'], positions['v:guidance:spec'], positions['v:spec:spec']]
    svg += svg_polygon(b2_ss, COLORS['face_boundary'], 0.5)

    # Boundary face b2:guidance-guidance (right triangle)
    b2_gg = [positions['b0:root'], positions['v:spec:guidance'], positions['v:guidance:guidance']]
    svg += svg_polygon(b2_gg, COLORS['face_boundary'], 0.5)

    # Standard face f:assurance:spec-guidance (top triangle)
    f_sg = [positions['v:spec:guidance'], positions['v:spec:spec'], positions['v:guidance:spec']]
    svg += svg_polygon(f_sg, COLORS['face_standard'], 0.4)

    # Standard face f:assurance:guidance-spec (bottom-ish, overlapping)
    f_gs = [positions['v:guidance:spec'], positions['v:spec:guidance'], positions['v:guidance:guidance']]
    svg += svg_polygon(f_gs, COLORS['face_standard'], 0.4)

    # Draw edges
    svg += '  <!-- Edges -->\n'

    def edge(v1, v2, etype, offset=25):
        p1 = positions[v1]
        p2 = positions[v2]
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        length = math.sqrt(dx*dx + dy*dy)
        if length == 0:
            return ''
        ux, uy = dx/length, dy/length
        x1 = p1[0] + ux * offset
        y1 = p1[1] + uy * offset
        x2 = p2[0] - ux * offset
        y2 = p2[1] - uy * offset

        if etype == 'verification':
            return svg_line(x1, y1, x2, y2, COLORS['verification'], 2,
                           marker_end='arrow-verification')
        elif etype == 'validation':
            return svg_line(x1, y1, x2, y2, COLORS['validation'], 2,
                           dash='4,2', marker_end='arrow-validation')
        elif etype == 'coupling':
            return svg_double_line(x1, y1, x2, y2, COLORS['coupling'], gap=4)
        elif etype == 'boundary':
            return svg_line(x1, y1, x2, y2, COLORS['boundary'], 1.5,
                           dash='2,2', marker_end='arrow-boundary')
        return ''

    # Coupling edges (between 4 corners)
    svg += edge('v:spec:spec', 'v:guidance:spec', 'coupling', 28)
    svg += edge('v:spec:guidance', 'v:guidance:guidance', 'coupling', 28)
    svg += edge('v:spec:guidance', 'v:guidance:spec', 'coupling', 28)

    # Verification edges
    svg += edge('v:spec:guidance', 'v:spec:spec', 'verification', 28)
    svg += edge('v:guidance:spec', 'v:spec:guidance', 'verification', 28)
    svg += edge('v:guidance:guidance', 'v:spec:guidance', 'verification', 28)

    # Validation edges
    svg += edge('v:spec:spec', 'v:guidance:spec', 'validation', 28)
    svg += edge('v:spec:guidance', 'v:guidance:spec', 'validation', 28)
    svg += edge('v:guidance:spec', 'v:guidance:guidance', 'validation', 28)

    # Boundary edges to root
    svg += edge('v:spec:spec', 'b0:root', 'boundary', 28)
    svg += edge('v:guidance:guidance', 'b0:root', 'boundary', 28)
    svg += edge('b0:root', 'v:guidance:spec', 'boundary', 22)
    svg += edge('b0:root', 'v:spec:guidance', 'boundary', 22)

    # Draw vertices
    svg += '  <!-- Vertices -->\n'

    # Root (star at center)
    root_pos = positions['b0:root']
    svg += svg_star(root_pos[0], root_pos[1], 24, 12, 8,
                   COLORS['root_fill'], COLORS['root_stroke'], 2.5)
    svg += svg_text(root_pos[0], root_pos[1] + 5, "ROOT", 9,
                   COLORS['text_dark'], weight='bold')

    # Spec vertices (green rectangles)
    for vid in ['v:spec:spec', 'v:spec:guidance']:
        pos = positions[vid]
        svg += svg_rect(pos[0] - 25, pos[1] - 17, 50, 34,
                       COLORS['spec_fill'], COLORS['spec_stroke'], 2)
        svg += svg_text(pos[0], pos[1] + 5, short_labels[vid], 12,
                       COLORS['text_light'], weight='bold')

    # Guidance vertices (orange rounded rectangles)
    for vid in ['v:guidance:spec', 'v:guidance:guidance']:
        pos = positions[vid]
        svg += svg_rect(pos[0] - 25, pos[1] - 17, 50, 34,
                       COLORS['guidance_fill'], COLORS['guidance_stroke'], 2, rx=8, ry=8)
        svg += svg_text(pos[0], pos[1] + 5, short_labels[vid], 12,
                       COLORS['text_light'], weight='bold')

    # Full labels under/above vertices
    svg += '  <!-- Full labels -->\n'
    svg += svg_text(positions['v:spec:spec'][0], positions['v:spec:spec'][1] - 25,
                   full_labels['v:spec:spec'], 8, COLORS['text_muted'])
    svg += svg_text(positions['v:spec:guidance'][0], positions['v:spec:guidance'][1] - 25,
                   full_labels['v:spec:guidance'], 8, COLORS['text_muted'])
    svg += svg_text(positions['v:guidance:spec'][0], positions['v:guidance:spec'][1] + 28,
                   full_labels['v:guidance:spec'], 8, COLORS['text_muted'])
    svg += svg_text(positions['v:guidance:guidance'][0], positions['v:guidance:guidance'][1] + 28,
                   full_labels['v:guidance:guidance'], 8, COLORS['text_muted'])

    # Face type labels
    svg += '  <!-- Face labels -->\n'
    svg += svg_text(110, 140, "b2", 10, '#3498DB', weight='bold')
    svg += svg_text(240, 140, "b2", 10, '#3498DB', weight='bold')
    svg += svg_text(155, 100, "f", 10, '#27AE60', weight='bold')
    svg += svg_text(195, 180, "f", 10, '#27AE60', weight='bold')

    # Legend box
    svg += '  <!-- Legend -->\n'
    svg += svg_rect(250, 255, 95, 40, '#FFFFFF', '#CCCCCC', 1, rx=4, ry=4)
    svg += svg_text(297, 270, "Face Types", 8, COLORS['text_dark'], weight='bold')
    svg += svg_rect(258, 277, 10, 10, COLORS['face_boundary'], '#3498DB', 1)
    svg += svg_text(272, 286, "b2: Boundary", 7, COLORS['text_dark'], anchor='start')
    svg += svg_rect(258, 290, 10, 10, COLORS['face_standard'], '#27AE60', 1)
    svg += svg_text(272, 299, "f: Standard", 7, COLORS['text_dark'], anchor='start')

    # Statistics
    svg += '  <!-- Statistics -->\n'
    svg += svg_text(55, 280, "V=5, E=12, F=4", 8, COLORS['text_muted'], css_class='mono')
    svg += svg_text(55, 292, "χ = -3", 8, COLORS['text_muted'], css_class='mono')

    svg += svg_footer()
    return svg


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Generate high-quality SVG figures for INCOSE paper'
    )
    parser.add_argument(
        '--output-dir', '-o',
        type=str,
        default='figures',
        help='Output directory for figures (default: figures/)'
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Generating INCOSE paper figures...")
    print()

    # Figure 1: Assurance Triangle
    fig1_path = output_dir / 'figure1-assurance-triangle.svg'
    fig1_svg = generate_figure1_assurance_triangle()
    with open(fig1_path, 'w') as f:
        f.write(fig1_svg)
    print(f"✓ Figure 1: {fig1_path}")

    # Figure 2: Audit Chart
    fig2_path = output_dir / 'figure2-audit-chart.svg'
    fig2_svg = generate_figure2_audit_chart()
    with open(fig2_path, 'w') as f:
        f.write(fig2_svg)
    print(f"✓ Figure 2: {fig2_path}")

    # Figure 3: Boundary Complex
    fig3_path = output_dir / 'figure3-boundary-complex.svg'
    fig3_svg = generate_figure3_boundary_complex()
    with open(fig3_path, 'w') as f:
        f.write(fig3_svg)
    print(f"✓ Figure 3: {fig3_path}")

    print()
    print("All figures generated successfully!")
    print(f"Output directory: {output_dir.absolute()}")


if __name__ == '__main__':
    main()
