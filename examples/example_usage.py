# example_usage.py

import numpy as np
from refractulator import Refractulator, visualize

# Create an instance of Refractulator
refractulator = Refractulator(radius=1.0)

# Define the incident direction
theta_deg = 120
phi_deg = -30
D = refractulator.compute_incident_direction(theta_deg, phi_deg)

# Generate multiple ray origins
V1, V2 = refractulator.get_perpendicular_vectors(D)
num_rays = 100
cylinder_radius = 0.5
theta_values_ray = np.linspace(0, 2 * np.pi, num_rays, endpoint=False)
ray_origins = []
r = cylinder_radius
for theta in theta_values_ray:
    offset = r * np.cos(theta) * V1 + r * np.sin(theta) * V2
    P0 = refractulator.center - D * 5.0  # Start rays before the sphere
    origin = P0 + offset
    ray_origins.append(origin)

# Calculate rays
rays = refractulator.calculate_rays_cylinder(ray_origins, D)

# Visualize the rays in 3D
visualize(rays, mode='3d')
