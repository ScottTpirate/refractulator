# refractulator/visualization.py

import plotly.graph_objs as go
import numpy as np

def visualize(rays, mode='3d', sphere_radius=1.0, sphere_center=(0, 0, 0)):
    """
    Visualize rays using Plotly.

    Parameters:
    - rays: List of rays to visualize. Each ray should be a dict with 'color' and 'path'.
    - mode: '2d' or '3d' visualization.
    - sphere_radius: Radius of the sphere (water droplet).
    - sphere_center: Center of the sphere.
    """
    if mode == '3d':
        return visualize_3d(rays, sphere_radius, sphere_center)
    elif mode == '2d':
        return visualize_2d(rays, sphere_radius, sphere_center)
    else:
        raise ValueError("Mode must be '2d' or '3d'.")

def visualize_3d(rays, sphere_radius=1.0, sphere_center=(0, 0, 0)):
    """
    Visualize rays in 3D using Plotly.

    Parameters:
    - rays: List of rays to visualize.
    - sphere_radius: Radius of the sphere.
    - sphere_center: Center of the sphere.
    """
    # Create the sphere surface for visualization
    theta_sphere = np.linspace(0, 2 * np.pi, 50)
    phi_sphere = np.linspace(0, np.pi, 50)
    theta_sphere, phi_sphere = np.meshgrid(theta_sphere, phi_sphere)
    x_sphere = sphere_center[0] + sphere_radius * np.sin(phi_sphere) * np.cos(theta_sphere)
    y_sphere = sphere_center[1] + sphere_radius * np.sin(phi_sphere) * np.sin(theta_sphere)
    z_sphere = sphere_center[2] + sphere_radius * np.cos(phi_sphere)

    sphere_trace = go.Surface(
        x=x_sphere,
        y=y_sphere,
        z=z_sphere,
        colorscale='Blues',
        opacity=0.5,
        showscale=False,
        name='Water Droplet',
        hoverinfo='skip'
    )

    # Prepare traces
    traces = [sphere_trace]

    # Process the rays to create traces
    for ray in rays:
        color = ray.get('color', 'black')  # Default to black if color not specified
        path = ray.get('path', {})
        for segment in path.values():
            if not segment:
                continue  # Skip empty segments
            x_vals = [point[0] for point in segment]
            y_vals = [point[1] for point in segment]
            z_vals = [point[2] for point in segment]

            trace = go.Scatter3d(
                x=x_vals,
                y=y_vals,
                z=z_vals,
                mode='lines',
                line=dict(color=color, width=3),
                hoverinfo='skip',
                showlegend=False
            )
            traces.append(trace)

    # Create the figure with all traces
    fig = go.Figure(data=traces)

    # Update layout settings
    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=True, range=[-10, 10], title='X'),
            yaxis=dict(visible=True, range=[-10, 10], title='Y'),
            zaxis=dict(visible=True, range=[-10, 10], title='Z'),
            aspectmode='cube'
        ),
        showlegend=False,
        margin=dict(l=0, r=0, b=0, t=50)
    )

    fig.show()

def visualize_2d(ray, sphere_radius=1.0, sphere_center=(0, 0)):
    """
    Visualize a single ray in 2D using Plotly.

    Parameters:
    - ray: A single ray to visualize.
    - sphere_radius: Radius of the sphere.
    - sphere_center: Center of the sphere.
    """
    # Create the circle (sphere in 2D)
    circle_theta = np.linspace(0, 2 * np.pi, 100)
    x_circle = sphere_center[0] + sphere_radius * np.cos(circle_theta)
    y_circle = sphere_center[1] + sphere_radius * np.sin(circle_theta)

    circle_trace = go.Scatter(
        x=x_circle,
        y=y_circle,
        mode='lines',
        line=dict(color='blue', width=2),
        name='Water Droplet',
        hoverinfo='skip'
    )

    # Prepare traces
    traces = [circle_trace]

    # Process the ray to create traces
    color = ray.get('color', 'black')  # Default to black if color not specified
    path = ray.get('path', {})
    for segment in path.values():
        if not segment:
            continue  # Skip empty segments
        x_vals = [point[0] for point in segment]
        y_vals = [point[1] for point in segment]

        trace = go.Scatter(
            x=x_vals,
            y=y_vals,
            mode='lines',
            line=dict(color=color, width=2),
            hoverinfo='skip',
            showlegend=False
        )
        traces.append(trace)

    # Create the figure with all traces
    fig = go.Figure(data=traces)

    # Update layout settings
    fig.update_layout(
        xaxis=dict(visible=True, range=[-5, 5], title='X'),
        yaxis=dict(visible=True, range=[-5, 5], title='Y'),
        aspectratio=dict(x=1, y=1),
        showlegend=False,
        margin=dict(l=0, r=0, b=0, t=50)
    )

    fig.show()
