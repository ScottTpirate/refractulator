# example_usage.py

from refractulator import Refractulator

# Create an instance of Refractulator
refractulator = Refractulator(radius=1.0)

# Use the high-level method to calculate and visualize rays
refractulator.calculate_and_visualize_rays(
    num_rays=100,            # Number of rays
    cylinder_radius=0.5,     # Radius of the cylindrical beam
    theta_deg=120,           # Azimuth angle
    phi_deg=-30,             # Elevation angle
    mode='3d'                # Visualization mode
)

