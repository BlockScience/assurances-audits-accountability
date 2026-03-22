#!/usr/bin/env python3
"""
Figure 2: INCOSE Paper Audit Chart - Iterative refinement

This is the hero figure showing the complete assurance network.
Given the complexity (8 vertices, 20 edges, 7 faces), 2D hierarchical
layout is likely clearer than 3D.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, RegularPolygon, FancyArrowPatch
from matplotlib.lines import Line2D
from pathlib import Path

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica'],
    'font.size': 10,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

COLORS = {
    'spec': '#27AE60',
    'guidance': '#E67E22',
    'doc': '#3498DB',
    'root': '#F1C40F',
    'verification': '#27AE60',
    'validation': '#E74C3C',
    'coupling': '#8E44AD',
    'boundary': '#95A5A6',
    'face_paper': '#FEF9E7',
    'face_standard': '#E8F8F5',
    'face_boundary': '#EBF5FB',
    'text': '#2C3E50',
    'check': '#27AE60',
}


def generate_figure2_v1(output_path: Path):
    """Version 1 - kept for reference"""
    pass


def generate_figure2_v2(output_path: Path):
    """
    Version 2: Cleaner layout, fixed edge routing, proper checkmarks

    Layout:
        Layer 2:              [PAPER]
                             /       \
        Layer 1:         [I-S]  ---  [I-G]
                         /   \       /   \
        Layer 0:      [SS]  [SG]--[GS]  [GG]
                         \    |    |    /
                          \   +----+   /
                           \    |    /
        Root:               [ROOT]
    """
    fig, ax = plt.subplots(figsize=(10, 9))

    # Positions (x, y) for hierarchical layout
    y2 = 0.88  # Layer 2
    y1 = 0.65  # Layer 1
    y0 = 0.40  # Layer 0
    yr = 0.15  # Root

    positions = {
        'paper': (0.5, y2),
        'i_spec': (0.30, y1),
        'i_guidance': (0.70, y1),
        'ss': (0.15, y0),
        'sg': (0.38, y0),
        'gs': (0.62, y0),
        'gg': (0.85, y0),
        'root': (0.5, yr),
    }

    labels = {
        'paper': 'PAPER',
        'i_spec': 'I-S',
        'i_guidance': 'I-G',
        'ss': 'SS',
        'sg': 'SG',
        'gs': 'GS',
        'gg': 'GG',
        'root': 'ROOT',
    }

    # Draw layer backgrounds
    layer_boxes = [
        (0.03, y2-0.07, 0.94, 0.14, 'Layer 2: This Paper', COLORS['face_paper']),
        (0.03, y1-0.10, 0.94, 0.20, 'Layer 1: Paper Type', COLORS['face_standard']),
        (0.03, y0-0.10, 0.94, 0.20, 'Layer 0: Foundation', COLORS['face_boundary']),
        (0.03, yr-0.08, 0.94, 0.16, 'Anchor', '#F5F5F5'),
    ]

    for x, y, w, h, label, color in layer_boxes:
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.01,rounding_size=0.02",
                               facecolor=color, edgecolor='#CCCCCC', linewidth=1, alpha=0.6)
        ax.add_patch(rect)
        ax.text(0.04, y + h - 0.02, label, fontsize=9, fontweight='bold',
                color='#666666', va='top')

    # Helper functions
    def draw_arrow(start, end, color, style='-', width=2):
        x1, y1 = positions[start]
        x2, y2 = positions[end]
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                   arrowprops=dict(arrowstyle='-|>', color=color,
                                  linewidth=width, linestyle=style,
                                  shrinkA=15, shrinkB=15))

    def draw_line(start, end, color, style='-', width=2):
        x1, y1 = positions[start]
        x2, y2 = positions[end]
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=width,
                linestyle=style, zorder=1)

    # EDGES - draw from bottom to top for proper layering

    # Boundary edges to root (dotted gray)
    draw_arrow('ss', 'root', COLORS['boundary'], ':', 1.5)
    draw_arrow('gg', 'root', COLORS['boundary'], ':', 1.5)
    draw_line('root', 'sg', COLORS['boundary'], ':', 1.5)
    draw_line('root', 'gs', COLORS['boundary'], ':', 1.5)

    # Layer 0 coupling edges (purple solid)
    draw_line('ss', 'gs', COLORS['coupling'], '-', 2)
    draw_line('sg', 'gg', COLORS['coupling'], '-', 2)
    draw_line('sg', 'gs', COLORS['coupling'], '-', 2)

    # Layer 1 → Layer 0 edges (CORRECTED routing)
    # I-S verifies against SS, validates against GS
    draw_arrow('i_spec', 'ss', COLORS['verification'], '-', 1.8)
    draw_arrow('i_spec', 'gs', COLORS['validation'], '--', 1.8)
    # I-G verifies against SG, validates against GG
    draw_arrow('i_guidance', 'sg', COLORS['verification'], '-', 1.8)
    draw_arrow('i_guidance', 'gg', COLORS['validation'], '--', 1.8)

    # Layer 1 coupling (purple)
    draw_line('i_spec', 'i_guidance', COLORS['coupling'], '-', 2)

    # Layer 2 → Layer 1 edges
    draw_arrow('paper', 'i_spec', COLORS['verification'], '-', 2.5)
    draw_arrow('paper', 'i_guidance', COLORS['validation'], '--', 2.5)

    # VERTICES - draw on top
    vertex_size = 0.05

    # Paper (blue circle, larger, highlighted)
    paper_x, paper_y = positions['paper']
    paper_circle = Circle((paper_x, paper_y), 0.06, facecolor=COLORS['doc'],
                          edgecolor='white', linewidth=3, zorder=10)
    ax.add_patch(paper_circle)
    ax.text(paper_x, paper_y, labels['paper'], ha='center', va='center',
            fontsize=12, fontweight='bold', color='white', zorder=11)

    # Spec vertices (green)
    for v in ['i_spec', 'ss', 'sg']:
        x, y = positions[v]
        rect = FancyBboxPatch((x - vertex_size/2, y - vertex_size/2),
                               vertex_size, vertex_size,
                               boxstyle="round,pad=0.005,rounding_size=0.005",
                               facecolor=COLORS['spec'], edgecolor='white',
                               linewidth=2, zorder=10)
        ax.add_patch(rect)
        ax.text(x, y, labels[v], ha='center', va='center',
                fontsize=10, fontweight='bold', color='white', zorder=11)

    # Guidance vertices (orange)
    for v in ['i_guidance', 'gs', 'gg']:
        x, y = positions[v]
        rect = FancyBboxPatch((x - vertex_size/2, y - vertex_size/2),
                               vertex_size, vertex_size,
                               boxstyle="round,pad=0.005,rounding_size=0.015",
                               facecolor=COLORS['guidance'], edgecolor='white',
                               linewidth=2, zorder=10)
        ax.add_patch(rect)
        ax.text(x, y, labels[v], ha='center', va='center',
                fontsize=10, fontweight='bold', color='white', zorder=11)

    # Root (gold hexagon)
    root_x, root_y = positions['root']
    star = RegularPolygon((root_x, root_y), numVertices=6, radius=0.045,
                          facecolor=COLORS['root'], edgecolor='#B7950B',
                          linewidth=2, zorder=10)
    ax.add_patch(star)
    ax.text(root_x, root_y, 'R', ha='center', va='center',
            fontsize=12, fontweight='bold', color='#7D6608', zorder=11)

    # Checkmarks - draw as simple green circles with white check
    for v, pos in positions.items():
        x, y = pos
        # Green circle background
        check_circle = Circle((x + 0.055, y + 0.03), 0.018, facecolor=COLORS['check'],
                              edgecolor='white', linewidth=1, zorder=12)
        ax.add_patch(check_circle)
        # White "v" as checkmark
        ax.plot([x + 0.048, x + 0.055, x + 0.065], [y + 0.03, y + 0.022, y + 0.042],
                color='white', linewidth=2, solid_capstyle='round', zorder=13)

    # Full labels below vertices (for Layer 0 only)
    full_labels_text = [
        (positions['ss'][0], positions['ss'][1] - 0.055, 'spec-for-spec', 7),
        (positions['sg'][0], positions['sg'][1] - 0.055, 'spec-for-guidance', 7),
        (positions['gs'][0], positions['gs'][1] - 0.055, 'guidance-for-spec', 7),
        (positions['gg'][0], positions['gg'][1] - 0.055, 'guidance-for-guidance', 7),
    ]
    for x, y, text, size in full_labels_text:
        ax.text(x, y, text, ha='center', va='top', fontsize=size,
                color='#666666', fontstyle='italic')

    # Legend
    legend_elements = [
        Line2D([0], [0], color=COLORS['verification'], linewidth=2.5, marker='>',
               markersize=7, label='Verification (structural)'),
        Line2D([0], [0], color=COLORS['validation'], linewidth=2.5, linestyle='--',
               marker='>', markersize=7, label='Validation (qualitative)'),
        Line2D([0], [0], color=COLORS['coupling'], linewidth=2.5,
               label='Coupling (type coherence)'),
        Line2D([0], [0], color=COLORS['boundary'], linewidth=2, linestyle=':',
               label='Boundary (to root)'),
    ]
    leg = ax.legend(handles=legend_elements, loc='upper right', framealpha=0.95,
                    fontsize=9, frameon=True, fancybox=True)
    leg.get_frame().set_edgecolor('#CCCCCC')

    # Statistics box (use chi symbol that renders)
    stats_text = "V = 8   E = 20   F = 7\nEuler char. = -5\nCoverage: 100%"
    ax.text(0.97, 0.02, stats_text, transform=ax.transAxes, fontsize=9,
            ha='right', va='bottom', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.95,
                      edgecolor='#CCCCCC', pad=0.5))

    # Title
    ax.set_title('INCOSE Paper Audit Chart', fontsize=15, fontweight='bold',
                 pad=12, color=COLORS['text'])

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {output_path}")


if __name__ == '__main__':
    output_dir = Path('figures')
    output_dir.mkdir(exist_ok=True)
    generate_figure2_v2(output_dir / 'figure2-v2.png')
