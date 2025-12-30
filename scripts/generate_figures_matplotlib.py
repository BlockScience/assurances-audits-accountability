#!/usr/bin/env python3
"""
Generate Publication-Quality 3D Figures for INCOSE IS 2026 Paper

Uses Matplotlib 3D with manually specified positions for:
1. Figure 1: The Assurance Triangle Pattern (conceptual)
2. Figure 2: INCOSE Paper Audit Chart (empirical result)
3. Figure 3: Boundary Complex Structure (foundation)

Usage:
    python scripts/generate_figures_matplotlib.py [--output-dir figures/] [--format pdf]
"""

import argparse
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

# Set up matplotlib for publication quality
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
})

# =============================================================================
# Color Palette (same as before, matplotlib compatible)
# =============================================================================

COLORS = {
    # Vertex colors
    'spec': '#2ECC71',
    'spec_dark': '#1D8348',
    'guidance': '#E67E22',
    'guidance_dark': '#A04000',
    'doc': '#3498DB',
    'doc_dark': '#2471A3',
    'root': '#FFD700',
    'root_dark': '#B8860B',

    # Edge colors
    'verification': '#27AE60',
    'validation': '#E74C3C',
    'coupling': '#9B59B6',
    'boundary': '#7F8C8D',

    # Face colors (with alpha)
    'face_standard': '#2ECC71',
    'face_boundary': '#3498DB',
    'face_paper': '#F39C12',

    # Text
    'text_dark': '#2C3E50',
    'text_light': '#FFFFFF',
}


def draw_sphere(ax, center, radius, color, alpha=1.0):
    """Draw a 3D sphere at the given center."""
    u = np.linspace(0, 2 * np.pi, 20)
    v = np.linspace(0, np.pi, 15)
    x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = center[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color=color, alpha=alpha, shade=True,
                    linewidth=0, antialiased=True)


def draw_box(ax, center, size, color, alpha=1.0):
    """Draw a 3D box (rectangular prism) at the given center."""
    dx, dy, dz = size[0]/2, size[1]/2, size[2]/2
    cx, cy, cz = center

    # Define the 8 vertices
    vertices = np.array([
        [cx-dx, cy-dy, cz-dz],
        [cx+dx, cy-dy, cz-dz],
        [cx+dx, cy+dy, cz-dz],
        [cx-dx, cy+dy, cz-dz],
        [cx-dx, cy-dy, cz+dz],
        [cx+dx, cy-dy, cz+dz],
        [cx+dx, cy+dy, cz+dz],
        [cx-dx, cy+dy, cz+dz],
    ])

    # Define the 6 faces
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # bottom
        [vertices[4], vertices[5], vertices[6], vertices[7]],  # top
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # front
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # back
        [vertices[0], vertices[3], vertices[7], vertices[4]],  # left
        [vertices[1], vertices[2], vertices[6], vertices[5]],  # right
    ]

    ax.add_collection3d(Poly3DCollection(faces, facecolors=color,
                                          edgecolors=color, alpha=alpha,
                                          linewidths=0.5, shade=True))


def draw_rounded_box(ax, center, size, color, alpha=1.0):
    """Draw a 3D box with slightly rounded appearance (using spheres at corners)."""
    # For simplicity, just draw a regular box with softer edges
    draw_box(ax, center, size, color, alpha)


def draw_star(ax, center, radius, color):
    """Draw a star marker in 3D."""
    ax.scatter(*center, s=radius*50, c=color, marker='*',
               edgecolors=COLORS['root_dark'], linewidths=1, zorder=10)


def draw_edge(ax, start, end, color, style='-', width=2, arrow=False):
    """Draw a 3D edge between two points."""
    ax.plot([start[0], end[0]],
            [start[1], end[1]],
            [start[2], end[2]],
            color=color, linestyle=style, linewidth=width, zorder=5)

    if arrow:
        # Add arrowhead
        direction = np.array(end) - np.array(start)
        direction = direction / np.linalg.norm(direction)
        arrow_pos = np.array(end) - direction * 0.15
        ax.quiver(arrow_pos[0], arrow_pos[1], arrow_pos[2],
                  direction[0]*0.1, direction[1]*0.1, direction[2]*0.1,
                  color=color, arrow_length_ratio=0.5, linewidth=width)


def draw_face(ax, vertices, color, alpha=0.3):
    """Draw a triangular face in 3D."""
    verts = [list(zip(*vertices))]
    triangle = [[vertices[0], vertices[1], vertices[2]]]
    ax.add_collection3d(Poly3DCollection(triangle, facecolors=color,
                                          edgecolors='none', alpha=alpha))


# =============================================================================
# Figure 1: Assurance Triangle Pattern
# =============================================================================

def generate_figure1(output_path: Path, fmt: str = 'pdf'):
    """
    Generate the conceptual assurance triangle diagram.

    3D layout with triangle tilted for depth perception.
    """
    fig = plt.figure(figsize=(7, 5.5))
    ax = fig.add_subplot(111, projection='3d')

    # 3D positions for the triangle vertices (tilted for visual depth)
    # Document at top-front, Guidance at top-back, Spec at bottom-center
    positions = {
        'doc': np.array([0, 0.5, 1.2]),
        'guidance': np.array([1.2, -0.3, 1.0]),
        'spec': np.array([0.6, 0.1, 0]),
    }

    # Draw the face (triangle) first
    face_verts = [positions['doc'], positions['guidance'], positions['spec']]
    draw_face(ax, face_verts, '#E8E8E8', alpha=0.4)

    # Draw edges with different styles
    # Verification: Doc → Spec (solid green, arrow)
    draw_edge(ax, positions['doc'], positions['spec'],
              COLORS['verification'], '-', 2.5, arrow=True)

    # Validation: Doc → Guidance (dashed orange, arrow)
    draw_edge(ax, positions['doc'], positions['guidance'],
              COLORS['validation'], '--', 2.5, arrow=True)

    # Coupling: Spec ↔ Guidance (solid purple, no arrow)
    draw_edge(ax, positions['spec'], positions['guidance'],
              COLORS['coupling'], '-', 2.5, arrow=False)

    # Draw vertices as spheres
    draw_sphere(ax, positions['doc'], 0.15, COLORS['doc'], alpha=0.95)
    draw_sphere(ax, positions['guidance'], 0.12, COLORS['guidance'], alpha=0.95)
    draw_sphere(ax, positions['spec'], 0.12, COLORS['spec'], alpha=0.95)

    # Add labels
    ax.text(positions['doc'][0], positions['doc'][1]-0.25, positions['doc'][2]+0.15,
            'Document', fontsize=11, fontweight='bold', ha='center', color=COLORS['text_dark'])
    ax.text(positions['guidance'][0]+0.15, positions['guidance'][1], positions['guidance'][2]+0.2,
            'Guidance', fontsize=11, fontweight='bold', ha='center', color=COLORS['text_dark'])
    ax.text(positions['spec'][0], positions['spec'][1]-0.2, positions['spec'][2]-0.15,
            'Specification', fontsize=11, fontweight='bold', ha='center', color=COLORS['text_dark'])

    # Edge labels
    mid_ver = (positions['doc'] + positions['spec']) / 2
    ax.text(mid_ver[0]-0.25, mid_ver[1]+0.15, mid_ver[2],
            'Verification\n(structural)', fontsize=8, ha='center', color=COLORS['verification'])

    mid_val = (positions['doc'] + positions['guidance']) / 2
    ax.text(mid_val[0]+0.1, mid_val[1]-0.15, mid_val[2]+0.2,
            'Validation\n(qualitative)', fontsize=8, ha='center', color=COLORS['validation'])

    mid_coup = (positions['spec'] + positions['guidance']) / 2
    ax.text(mid_coup[0]+0.2, mid_coup[1], mid_coup[2]-0.1,
            'Coupling\n(type coherence)', fontsize=8, ha='center', color=COLORS['coupling'])

    # Set axis properties
    ax.set_xlim(-0.5, 1.8)
    ax.set_ylim(-0.8, 1.0)
    ax.set_zlim(-0.5, 1.8)

    # Hide axes for cleaner look
    ax.set_axis_off()

    # Set viewing angle
    ax.view_init(elev=25, azim=-60)

    # Add legend
    legend_elements = [
        Line2D([0], [0], color=COLORS['verification'], linewidth=2, label='Verification'),
        Line2D([0], [0], color=COLORS['validation'], linewidth=2, linestyle='--', label='Validation'),
        Line2D([0], [0], color=COLORS['coupling'], linewidth=2, label='Coupling'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', framealpha=0.9, fontsize=9)

    # Title
    ax.set_title('Figure 1: The Assurance Triangle Pattern', fontsize=12, fontweight='bold', pad=10)

    # Save
    fig.savefig(output_path, format=fmt, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    return output_path


# =============================================================================
# Figure 2: INCOSE Paper Audit Chart
# =============================================================================

def generate_figure2(output_path: Path, fmt: str = 'pdf'):
    """
    Generate the INCOSE paper audit chart - the hero figure.

    3D hierarchical layout with 3 layers showing the complete assurance network.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # 3D positions organized by layer (z-axis = layer height)
    # Layer 0 (bottom): Boundary complex foundation
    # Layer 1 (middle): INCOSE type documents
    # Layer 2 (top): The paper itself

    z_layer0, z_layer1, z_layer2 = 0, 1.5, 3.0

    positions = {
        # Layer 2 - The Paper (top, center-front)
        'paper': np.array([0, 0, z_layer2]),

        # Layer 1 - INCOSE Type Documents
        'i_spec': np.array([-0.8, 0.3, z_layer1]),
        'i_guidance': np.array([0.8, 0.3, z_layer1]),

        # Layer 0 - Boundary Complex Foundation (spread out)
        'ss': np.array([-1.2, 0.8, z_layer0]),
        'sg': np.array([-0.4, -0.6, z_layer0]),
        'gs': np.array([0.4, 0.8, z_layer0]),
        'gg': np.array([1.2, -0.6, z_layer0]),

        # Root (below center)
        'root': np.array([0, 0.2, -0.8]),
    }

    labels = {
        'paper': 'PAPER',
        'i_spec': 'I-S',
        'i_guidance': 'I-G',
        'ss': 'SS',
        'sg': 'SG',
        'gs': 'GS',
        'gg': 'GG',
        'root': '★',
    }

    # Draw faces (triangular assurance regions)
    # Paper's assurance face (highlighted)
    draw_face(ax, [positions['paper'], positions['i_spec'], positions['i_guidance']],
              COLORS['face_paper'], alpha=0.35)

    # INCOSE spec assurance
    draw_face(ax, [positions['i_spec'], positions['ss'], positions['gs']],
              COLORS['face_standard'], alpha=0.25)

    # INCOSE guidance assurance
    draw_face(ax, [positions['i_guidance'], positions['sg'], positions['gg']],
              COLORS['face_standard'], alpha=0.25)

    # Boundary faces
    draw_face(ax, [positions['root'], positions['gs'], positions['ss']],
              COLORS['face_boundary'], alpha=0.2)
    draw_face(ax, [positions['root'], positions['sg'], positions['gg']],
              COLORS['face_boundary'], alpha=0.2)

    # Draw edges
    # Layer 2 → Layer 1
    draw_edge(ax, positions['paper'], positions['i_spec'], COLORS['verification'], '-', 1.8, arrow=True)
    draw_edge(ax, positions['paper'], positions['i_guidance'], COLORS['validation'], '--', 1.8, arrow=True)
    draw_edge(ax, positions['i_spec'], positions['i_guidance'], COLORS['coupling'], '-', 1.5)

    # Layer 1 → Layer 0
    draw_edge(ax, positions['i_spec'], positions['ss'], COLORS['verification'], '-', 1.5, arrow=True)
    draw_edge(ax, positions['i_spec'], positions['gs'], COLORS['validation'], '--', 1.5, arrow=True)
    draw_edge(ax, positions['i_guidance'], positions['sg'], COLORS['verification'], '-', 1.5, arrow=True)
    draw_edge(ax, positions['i_guidance'], positions['gg'], COLORS['validation'], '--', 1.5, arrow=True)

    # Layer 0 internal (some key edges)
    draw_edge(ax, positions['ss'], positions['gs'], COLORS['coupling'], '-', 1.2)
    draw_edge(ax, positions['sg'], positions['gg'], COLORS['coupling'], '-', 1.2)
    draw_edge(ax, positions['sg'], positions['gs'], COLORS['coupling'], '-', 1.2)

    # Boundary edges to root
    draw_edge(ax, positions['ss'], positions['root'], COLORS['boundary'], ':', 1.2, arrow=True)
    draw_edge(ax, positions['gg'], positions['root'], COLORS['boundary'], ':', 1.2, arrow=True)
    draw_edge(ax, positions['root'], positions['gs'], COLORS['boundary'], ':', 1.2)
    draw_edge(ax, positions['root'], positions['sg'], COLORS['boundary'], ':', 1.2)

    # Draw vertices
    # Paper (blue sphere, larger)
    draw_sphere(ax, positions['paper'], 0.18, COLORS['doc'], alpha=0.95)

    # Spec vertices (green)
    for v in ['i_spec', 'ss', 'sg']:
        draw_sphere(ax, positions[v], 0.12, COLORS['spec'], alpha=0.9)

    # Guidance vertices (orange)
    for v in ['i_guidance', 'gs', 'gg']:
        draw_sphere(ax, positions[v], 0.12, COLORS['guidance'], alpha=0.9)

    # Root (gold star)
    ax.scatter(*positions['root'], s=400, c=COLORS['root'], marker='*',
               edgecolors=COLORS['root_dark'], linewidths=1, zorder=10)

    # Add vertex labels
    for vid, pos in positions.items():
        label = labels[vid]
        offset = np.array([0, -0.25, 0.1])
        if vid == 'paper':
            offset = np.array([0, -0.3, 0.15])
        elif vid == 'root':
            offset = np.array([0.2, 0, -0.15])
        ax.text(pos[0]+offset[0], pos[1]+offset[1], pos[2]+offset[2],
                label, fontsize=10 if vid in ['paper', 'root'] else 9,
                fontweight='bold', ha='center', color=COLORS['text_dark'])

    # Add checkmarks next to vertices (as green dots)
    for vid, pos in positions.items():
        check_offset = np.array([0.2, 0.15, 0.1])
        ax.scatter(pos[0]+check_offset[0], pos[1]+check_offset[1], pos[2]+check_offset[2],
                   s=50, c='#27AE60', marker='o', zorder=11)

    # Layer labels on the side
    ax.text(-2.0, 0, z_layer2, 'Layer 2\nThis Paper', fontsize=9,
            fontweight='bold', ha='left', color=COLORS['text_dark'])
    ax.text(-2.0, 0, z_layer1, 'Layer 1\nPaper Type', fontsize=9,
            fontweight='bold', ha='left', color=COLORS['text_dark'])
    ax.text(-2.0, 0, z_layer0, 'Layer 0\nFoundation', fontsize=9,
            fontweight='bold', ha='left', color=COLORS['text_dark'])

    # Set axis properties
    ax.set_xlim(-2.5, 2.0)
    ax.set_ylim(-1.5, 1.5)
    ax.set_zlim(-1.5, 4.0)

    ax.set_axis_off()
    ax.view_init(elev=20, azim=-50)

    # Legend
    legend_elements = [
        Line2D([0], [0], color=COLORS['verification'], linewidth=2, label='Verification'),
        Line2D([0], [0], color=COLORS['validation'], linewidth=2, linestyle='--', label='Validation'),
        Line2D([0], [0], color=COLORS['coupling'], linewidth=2, label='Coupling'),
        Line2D([0], [0], color=COLORS['boundary'], linewidth=2, linestyle=':', label='Boundary'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['spec'],
               markersize=10, label='Spec vertex'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['guidance'],
               markersize=10, label='Guidance vertex'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['doc'],
               markersize=10, label='Document vertex'),
    ]
    ax.legend(handles=legend_elements, loc='upper right', framealpha=0.9, fontsize=8)

    # Statistics text box
    stats_text = "V = 8, E = 20, F = 7\nχ = −5\nCoverage: 100%"
    ax.text2D(0.02, 0.02, stats_text, transform=ax.transAxes, fontsize=9,
              verticalalignment='bottom', fontfamily='monospace',
              bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))

    # Title
    ax.set_title('Figure 2: INCOSE Paper Audit Chart', fontsize=12, fontweight='bold', pad=10)

    # Save
    fig.savefig(output_path, format=fmt, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    return output_path


# =============================================================================
# Figure 3: Boundary Complex Structure
# =============================================================================

def generate_figure3(output_path: Path, fmt: str = 'pdf'):
    """
    Generate the boundary complex structure diagram.

    Shows the 5-vertex foundation with root at center/bottom.
    Tetrahedral-like structure.
    """
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection='3d')

    # 3D positions: Root at center-bottom, 4 foundational vertices above in tetrahedral arrangement
    positions = {
        'root': np.array([0, 0, -0.5]),
        'ss': np.array([-1.0, 0.6, 0.8]),      # Spec-for-Spec (top-left-back)
        'sg': np.array([1.0, 0.6, 0.8]),       # Spec-for-Guidance (top-right-back)
        'gs': np.array([-0.8, -0.8, 0.5]),     # Guidance-for-Spec (bottom-left-front)
        'gg': np.array([0.8, -0.8, 0.5]),      # Guidance-for-Guidance (bottom-right-front)
    }

    full_labels = {
        'root': 'ROOT',
        'ss': 'Spec-for-Spec',
        'sg': 'Spec-for-Guidance',
        'gs': 'Guidance-for-Spec',
        'gg': 'Guidance-for-Guidance',
    }

    short_labels = {
        'root': '★',
        'ss': 'SS',
        'sg': 'SG',
        'gs': 'GS',
        'gg': 'GG',
    }

    # Draw faces
    # Boundary face b2:spec-spec (root-GS-SS)
    draw_face(ax, [positions['root'], positions['gs'], positions['ss']],
              COLORS['face_boundary'], alpha=0.3)

    # Boundary face b2:guidance-guidance (root-SG-GG)
    draw_face(ax, [positions['root'], positions['sg'], positions['gg']],
              COLORS['face_boundary'], alpha=0.3)

    # Standard face f:assurance:spec-guidance (SG-SS-GS)
    draw_face(ax, [positions['sg'], positions['ss'], positions['gs']],
              COLORS['face_standard'], alpha=0.25)

    # Standard face f:assurance:guidance-spec (GS-SG-GG)
    draw_face(ax, [positions['gs'], positions['sg'], positions['gg']],
              COLORS['face_standard'], alpha=0.25)

    # Draw edges
    # Coupling edges (purple, solid)
    draw_edge(ax, positions['ss'], positions['gs'], COLORS['coupling'], '-', 2)
    draw_edge(ax, positions['sg'], positions['gg'], COLORS['coupling'], '-', 2)
    draw_edge(ax, positions['sg'], positions['gs'], COLORS['coupling'], '-', 2)

    # Verification edges (green, solid with arrow)
    draw_edge(ax, positions['sg'], positions['ss'], COLORS['verification'], '-', 2, arrow=True)
    draw_edge(ax, positions['gs'], positions['sg'], COLORS['verification'], '-', 2, arrow=True)
    draw_edge(ax, positions['gg'], positions['sg'], COLORS['verification'], '-', 2, arrow=True)

    # Validation edges (red/orange, dashed with arrow)
    draw_edge(ax, positions['ss'], positions['gs'], COLORS['validation'], '--', 2, arrow=True)
    draw_edge(ax, positions['sg'], positions['gs'], COLORS['validation'], '--', 2, arrow=True)
    draw_edge(ax, positions['gs'], positions['gg'], COLORS['validation'], '--', 2, arrow=True)

    # Boundary edges to root (gray, dotted)
    draw_edge(ax, positions['ss'], positions['root'], COLORS['boundary'], ':', 1.5, arrow=True)
    draw_edge(ax, positions['gg'], positions['root'], COLORS['boundary'], ':', 1.5, arrow=True)
    draw_edge(ax, positions['root'], positions['gs'], COLORS['boundary'], ':', 1.5)
    draw_edge(ax, positions['root'], positions['sg'], COLORS['boundary'], ':', 1.5)

    # Draw vertices
    # Root (gold star)
    ax.scatter(*positions['root'], s=500, c=COLORS['root'], marker='*',
               edgecolors=COLORS['root_dark'], linewidths=1.5, zorder=10)

    # Spec vertices (green spheres)
    for v in ['ss', 'sg']:
        draw_sphere(ax, positions[v], 0.13, COLORS['spec'], alpha=0.9)

    # Guidance vertices (orange spheres)
    for v in ['gs', 'gg']:
        draw_sphere(ax, positions[v], 0.13, COLORS['guidance'], alpha=0.9)

    # Add short labels on vertices
    for vid, pos in positions.items():
        label = short_labels[vid]
        offset = np.array([0, 0, 0.22])
        if vid == 'root':
            offset = np.array([0, 0.25, 0])
        ax.text(pos[0]+offset[0], pos[1]+offset[1], pos[2]+offset[2],
                label, fontsize=11, fontweight='bold', ha='center',
                color=COLORS['text_dark'])

    # Add full labels below/beside vertices
    ax.text(positions['ss'][0]-0.15, positions['ss'][1]+0.3, positions['ss'][2]+0.35,
            full_labels['ss'], fontsize=8, ha='center', color='#555555')
    ax.text(positions['sg'][0]+0.15, positions['sg'][1]+0.3, positions['sg'][2]+0.35,
            full_labels['sg'], fontsize=8, ha='center', color='#555555')
    ax.text(positions['gs'][0]-0.15, positions['gs'][1]-0.35, positions['gs'][2],
            full_labels['gs'], fontsize=8, ha='center', color='#555555')
    ax.text(positions['gg'][0]+0.15, positions['gg'][1]-0.35, positions['gg'][2],
            full_labels['gg'], fontsize=8, ha='center', color='#555555')

    # Face type labels
    ax.text(-0.3, 0.1, 0.1, 'b2', fontsize=10, fontweight='bold',
            ha='center', color='#3498DB')
    ax.text(0.5, 0.1, 0.1, 'b2', fontsize=10, fontweight='bold',
            ha='center', color='#3498DB')
    ax.text(0, 0.3, 0.7, 'f', fontsize=10, fontweight='bold',
            ha='center', color='#27AE60')
    ax.text(0, -0.5, 0.5, 'f', fontsize=10, fontweight='bold',
            ha='center', color='#27AE60')

    # Set axis properties
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.5, 1.5)
    ax.set_zlim(-1.2, 1.5)

    ax.set_axis_off()
    ax.view_init(elev=20, azim=-45)

    # Legend
    legend_elements = [
        Line2D([0], [0], color=COLORS['verification'], linewidth=2, label='Verification'),
        Line2D([0], [0], color=COLORS['validation'], linewidth=2, linestyle='--', label='Validation'),
        Line2D([0], [0], color=COLORS['coupling'], linewidth=2, label='Coupling'),
        Line2D([0], [0], color=COLORS['boundary'], linewidth=2, linestyle=':', label='Boundary'),
        mpatches.Patch(facecolor=COLORS['face_boundary'], alpha=0.3, label='b2: Boundary face'),
        mpatches.Patch(facecolor=COLORS['face_standard'], alpha=0.3, label='f: Standard face'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', framealpha=0.9, fontsize=8)

    # Statistics
    stats_text = "V = 5, E = 12, F = 4\nχ = −3"
    ax.text2D(0.02, 0.02, stats_text, transform=ax.transAxes, fontsize=9,
              verticalalignment='bottom', fontfamily='monospace',
              bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))

    # Title
    ax.set_title('Figure 3: Boundary Complex Structure', fontsize=12, fontweight='bold', pad=10)

    # Save
    fig.savefig(output_path, format=fmt, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    return output_path


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Generate publication-quality 3D figures for INCOSE paper'
    )
    parser.add_argument(
        '--output-dir', '-o',
        type=str,
        default='figures',
        help='Output directory for figures (default: figures/)'
    )
    parser.add_argument(
        '--format', '-f',
        type=str,
        default='pdf',
        choices=['pdf', 'png', 'svg'],
        help='Output format (default: pdf)'
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    fmt = args.format

    print("Generating publication-quality 3D figures...")
    print(f"Output format: {fmt}")
    print()

    # Figure 1: Assurance Triangle
    fig1_path = output_dir / f'figure1-assurance-triangle-3d.{fmt}'
    generate_figure1(fig1_path, fmt)
    print(f"✓ Figure 1: {fig1_path}")

    # Figure 2: Audit Chart
    fig2_path = output_dir / f'figure2-audit-chart-3d.{fmt}'
    generate_figure2(fig2_path, fmt)
    print(f"✓ Figure 2: {fig2_path}")

    # Figure 3: Boundary Complex
    fig3_path = output_dir / f'figure3-boundary-complex-3d.{fmt}'
    generate_figure3(fig3_path, fmt)
    print(f"✓ Figure 3: {fig3_path}")

    print()
    print("All figures generated successfully!")
    print(f"Output directory: {output_dir.absolute()}")


if __name__ == '__main__':
    main()
