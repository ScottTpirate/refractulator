# refractulator/data_generator.py

import numpy as np
import json
import os
from .calculate import Refractulator  # Import the Refractulator class

class EnhancedJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder to handle NumPy data types."""
    def default(self, o):
        if isinstance(o, (np.integer, np.int_, int)):
            return int(o)
        elif isinstance(o, (np.floating, np.float_, float)):
            return float(o)
        elif isinstance(o, np.ndarray):
            return o.tolist()
        else:
            return super().default(o)

class RefractulatorDataGenerator:
    def __init__(self, refractulator: Refractulator):
        self.refractulator = refractulator

    def generate_data(self, azimuth_angles, elevation_angles, cylinder_radii, num_rays=100):
        """
        Generate ray data for given azimuth and elevation angles and cylinder radii.
        """
        data = {}
        for theta_value in azimuth_angles:
            print(f"Processing θ={theta_value}°")
            data_theta = {}
            for phi_value in elevation_angles:
                print(f"  Processing φ={phi_value}°")
                data_entry = {}
                data_entry["rays"] = {}

                # Compute the incoming light direction vector D
                D = self.refractulator.compute_incident_direction(theta_value, phi_value)

                # Compute orthonormal basis vectors perpendicular to D
                V1, V2 = self.refractulator.get_perpendicular_vectors(D)

                # Loop over cylinder radii
                for cylinder_radius in cylinder_radii:
                    print(f"    Processing Cylinder Radius: {cylinder_radius}")
                    rays_list = []

                    # Generate rays on the surface of a cylinder
                    theta_values_ray = np.linspace(0, 2 * np.pi, num_rays, endpoint=False)
                    ray_origins = []
                    r = cylinder_radius
                    for theta in theta_values_ray:
                        offset = r * np.cos(theta) * V1 + r * np.sin(theta) * V2
                        P0 = self.refractulator.center - D * 5.0  # Start rays before the sphere
                        origin = P0 + offset
                        ray_origins.append(origin)

                    # Collect rays
                    rays = self.refractulator.calculate_rays_cylinder(ray_origins, D)

                    for ray in rays:
                        color = ray['color']
                        path = ray['path']
                        ray_entry = {
                            "color": color,
                            "path": path  # path is a dict with segments and points
                        }
                        rays_list.append(ray_entry)

                    # Store rays for the current cylinder radius
                    cylinder_radius_key = f"radius_{cylinder_radius:.1f}"
                    data_entry["rays"][cylinder_radius_key] = rays_list

                # Store data entry for the current elevation angle
                phi_key = f"phi_{phi_value}"
                data_theta[phi_key] = data_entry
            data[f"theta_{theta_value}"] = data_theta
        return data

    def save_data_to_json(self, data, output_directory='.'):
        """
        Save the generated data to JSON files.
        """
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        for theta_key, theta_data in data.items():
            theta_value = theta_key.split('_')[1]
            filename = f'rainbow_data_theta_{theta_value}.json'
            filepath = os.path.join(output_directory, filename)
            with open(filepath, 'w') as file:
                json.dump(theta_data, file, cls=EnhancedJSONEncoder)
            print(f"Data saved to {filepath}")
