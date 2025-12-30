#!/usr/bin/env python3
"""
Create interactive 3D visualization of chart from JSON.

Usage:
    python scripts/visualize_chart.py charts/test-tetrahedron.json

Output:
    charts/test-tetrahedron.html
"""

import sys
import json
from pathlib import Path
import plotly.graph_objects as go
import networkx as nx


def load_chart_json(json_path: Path) -> dict:
    """Load chart JSON data."""
    with open(json_path, 'r') as f:
        return json.load(f)


def build_network_graph(chart_data: dict) -> nx.MultiDiGraph:
    """Build NetworkX graph for layout computation."""
    # Use MultiDiGraph to preserve self-loops and multiple edges
    G = nx.MultiDiGraph()

    # Add vertices
    for vertex in chart_data['elements']['vertices']:
        G.add_node(vertex['id'], **vertex)

    # Add edges
    for edge in chart_data['elements']['edges']:
        G.add_edge(edge['source'], edge['target'], **edge)

    return G


def compute_3d_layout(G: nx.MultiDiGraph) -> dict:
    """Compute 3D spring layout positions."""
    # Use NetworkX spring layout for nice force-directed positioning
    # Convert to undirected for layout to avoid directional bias
    G_undirected = G.to_undirected()
    pos = nx.spring_layout(G_undirected, dim=3, seed=42, k=0.5, iterations=50)
    return pos


def create_visualization(chart_data: dict) -> go.Figure:
    """Create 3D Plotly visualization."""
    # Build graph and compute layout
    G = build_network_graph(chart_data)
    pos_3d = compute_3d_layout(G)

    # Create figure
    fig = go.Figure()

    # Add edges as lines
    edge_traces = []
    for edge in chart_data['elements']['edges']:
        source_id = edge['source']
        target_id = edge['target']

        if source_id in pos_3d and target_id in pos_3d:
            x0, y0, z0 = pos_3d[source_id]
            x1, y1, z1 = pos_3d[target_id]

            # Color edges by type
            edge_color = '#888888'  # Default gray
            if 'coupling' in edge['type']:
                edge_color = '#9b59b6'  # Purple for coupling
            elif 'verification' in edge['type']:
                edge_color = '#3498db'  # Blue for verification
            elif 'validation' in edge['type']:
                edge_color = '#e74c3c'  # Red for validation
            elif 'test' in edge['id']:
                edge_color = '#95a5a6'  # Gray for test edges

            trace = go.Scatter3d(
                x=[x0, x1],
                y=[y0, y1],
                z=[z0, z1],
                mode='lines',
                line=dict(width=4, color=edge_color),
                hovertext=edge['name'],
                hoverinfo='text',
                showlegend=False
            )
            edge_traces.append(trace)

    for trace in edge_traces:
        fig.add_trace(trace)

    # Add vertices as scatter points
    vertex_x = []
    vertex_y = []
    vertex_z = []
    vertex_text = []
    vertex_colors = []
    vertex_hover = []

    for vertex in chart_data['elements']['vertices']:
        v_id = vertex['id']
        if v_id in pos_3d:
            x, y, z = pos_3d[v_id]
            vertex_x.append(x)
            vertex_y.append(y)
            vertex_z.append(z)

            # Extract short name from vertex ID
            # Use abbreviations from spec: root, SS, SG, GS, GG
            # Add abbreviations for chart types: SC, SAA, GC, GAA
            if v_id == 'b0:root':
                short_name = 'root'
            elif v_id == 'v:spec:spec':
                short_name = 'SS'
            elif v_id == 'v:spec:guidance':
                short_name = 'SG'
            elif v_id == 'v:spec:chart':
                short_name = 'SC'
            elif v_id == 'v:spec:assurance_audit':
                short_name = 'SAA'
            elif v_id == 'v:guidance:spec':
                short_name = 'GS'
            elif v_id == 'v:guidance:guidance':
                short_name = 'GG'
            elif v_id == 'v:guidance:chart':
                short_name = 'GC'
            elif v_id == 'v:guidance:assurance_audit':
                short_name = 'GAA'
            else:
                # Fallback: use last part of name
                short_name = vertex['name'].split()[-1] if ' ' in vertex['name'] else vertex['name']
            vertex_text.append(short_name)

            # Color by type
            vertex_color = '#3498db'  # Default blue
            if 'spec' in vertex['type']:
                vertex_color = '#2ecc71'  # Green for specs
            elif 'guidance' in vertex['type']:
                vertex_color = '#f39c12'  # Orange for guidance
            elif 'test' in vertex['id']:
                vertex_color = '#95a5a6'  # Gray for test vertices

            vertex_colors.append(vertex_color)
            vertex_hover.append(f"{vertex['name']}<br>ID: {vertex['id']}<br>Type: {vertex['type']}")

    vertex_trace = go.Scatter3d(
        x=vertex_x,
        y=vertex_y,
        z=vertex_z,
        mode='markers+text',
        marker=dict(
            size=12,
            color=vertex_colors,
            line=dict(width=2, color='white')
        ),
        text=vertex_text,
        textposition='top center',
        textfont=dict(size=10, color='black'),
        hovertext=vertex_hover,
        hoverinfo='text',
        name='Vertices'
    )
    fig.add_trace(vertex_trace)

    # Add faces as semi-transparent triangular meshes
    # Assign RGB colors explicitly to test faces
    test_face_colors = {
        'f:test:alpha:beta:gamma': 'red',
        'f:test:alpha:beta:delta': 'green',
        'f:test:alpha:gamma:delta': 'blue',
        'f:test:beta:gamma:delta': 'yellow'  # This one should be missing
    }

    # Assign colors for boundary-kernel assurance faces
    # Blue for self-referential (nonstandard), green for cross-domain (standard)
    boundary_kernel_colors = {
        'f:assurance:spec-spec': '#3498db',  # Blue - self-referential
        'f:assurance:guidance-guidance': '#3498db',  # Blue - self-referential
        'f:assurance:spec-guidance': '#2ecc71',  # Green - cross-domain
        'f:assurance:guidance-spec': '#2ecc71',  # Green - cross-domain
    }

    # Assign colors for boundary faces (b2) in boundary-complex
    # Blue for boundary faces with root
    boundary_face_colors = {
        'b2:spec-spec': '#3498db',  # Blue - boundary face with root
        'b2:guidance-guidance': '#3498db',  # Blue - boundary face with root
    }

    # Assign colors for chart-types-audit assurance faces
    # Different shades of green for different chart type assurances
    chart_types_assurance_colors = {
        'f:assurance:chart': '#27ae60',  # Green - chart type assurance
        'f:assurance:assurance_audit': '#16a085',  # Teal - assurance_audit type assurance
    }

    for face in chart_data['elements']['faces']:
        face_vertices = face.get('vertices', [])

        # Only render triangular faces (3 vertices)
        if len(face_vertices) == 3:
            # Get positions of all three vertices
            positions = []
            valid = True
            for v_id in face_vertices:
                if v_id in pos_3d:
                    positions.append(pos_3d[v_id])
                else:
                    valid = False
                    break

            if valid and len(positions) == 3:
                x_coords = [p[0] for p in positions]
                y_coords = [p[1] for p in positions]
                z_coords = [p[2] for p in positions]

                # Color faces - explicit colors by chart type
                face_id = face['id']
                if face_id in test_face_colors:
                    face_color = test_face_colors[face_id]
                elif face_id in boundary_face_colors:
                    face_color = boundary_face_colors[face_id]
                elif face_id in boundary_kernel_colors:
                    face_color = boundary_kernel_colors[face_id]
                elif face_id in chart_types_assurance_colors:
                    face_color = chart_types_assurance_colors[face_id]
                elif 'assurance' in face['type']:
                    face_color = '#27ae60'  # Default green for other assurance
                else:
                    face_color = '#95a5a6'  # Default gray

                mesh_trace = go.Mesh3d(
                    x=x_coords,
                    y=y_coords,
                    z=z_coords,
                    i=[0],
                    j=[1],
                    k=[2],
                    color=face_color,
                    opacity=0.5,
                    hovertext=f"{face['name']}<br>{face_color.upper()}",
                    hoverinfo='text',
                    showlegend=False
                )
                fig.add_trace(mesh_trace)

    # Update layout
    title_text = f"{chart_data['name']}"
    if chart_data.get('description'):
        title_text += f"<br><sub>{chart_data['description']}</sub>"

    euler_char = chart_data['topology']['euler_characteristic']
    v_count = chart_data['element_counts']['vertices']
    e_count = chart_data['element_counts']['edges']
    f_count = chart_data['element_counts']['faces']

    fig.update_layout(
        title=dict(
            text=title_text,
            x=0.5,
            xanchor='center'
        ),
        scene=dict(
            xaxis=dict(showgrid=False, zeroline=False, visible=False),
            yaxis=dict(showgrid=False, zeroline=False, visible=False),
            zaxis=dict(showgrid=False, zeroline=False, visible=False),
            bgcolor='#ffffff'
        ),
        showlegend=False,
        width=1200,
        height=800,
        margin=dict(l=0, r=0, t=100, b=0),
        annotations=[
            dict(
                text=f"V={v_count}, E={e_count}, F={f_count}, χ={euler_char}",
                xref="paper",
                yref="paper",
                x=0.02,
                y=0.98,
                showarrow=False,
                font=dict(size=12, color='#7f8c8d'),
                bgcolor='rgba(255, 255, 255, 0.8)',
                borderpad=4
            )
        ]
    )

    return fig


def main():
    """Generate visualization from chart JSON."""
    if len(sys.argv) < 2:
        print("Usage: python scripts/visualize_chart.py charts/test-tetrahedron.json")
        sys.exit(1)

    json_path = Path(sys.argv[1])

    if not json_path.exists():
        print(f"Error: JSON file not found: {json_path}")
        print("Run: python scripts/export_chart_direct.py charts/test-tetrahedron.md first")
        sys.exit(1)

    # Load chart data
    print(f"Loading: {json_path.name}")
    chart_data = load_chart_json(json_path)

    # Create visualization
    print(f"Creating visualization...")
    fig = create_visualization(chart_data)

    # Save HTML
    output_path = json_path.with_suffix('.html')
    fig.write_html(str(output_path))

    print(f"✓ Visualization saved to: {output_path.name}")
    print(f"  Open in browser to view")


if __name__ == '__main__':
    main()
