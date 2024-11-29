# Changelog

All notable changes to this project will be documented in this file.


## [0.3.0] - 2024-11-28


## 📦 Refractulator v0.3.0

**Release Date:** 2024-11-28

### 🎉 New Features

- **High-Level Ray Calculation and Visualization:**
  - **`calculate_and_visualize_rays` Method:**
    - Introduced a new high-level method within the `Refractulator` class that encapsulates the entire process of calculating and visualizing rays.
    - Simplifies usage by allowing users to perform complex ray calculations and generate visualizations with a single method call.
    - Parameters include the number of rays, cylinder radius, incident angles (theta and phi), and visualization mode (2D or 3D).

- **Cylindrical Ray Origin Generation:**
  - **`generate_cylinder_ray_origins` Method:**
    - Added a method to generate ray origins forming a cylindrical beam of parallel rays.
    - Parameters such as the number of rays, cylinder radius, direction vector, and starting distance from the sphere are configurable.
  
### 🛠️ Improvements

- **Simplified Example Usage:**
  - Refactored the `example_usage.py` script to utilize the new high-level method, significantly reducing the amount of code required.
  - Users no longer need to interact directly with NumPy or manage complex calculations, making the example more accessible and easier to understand.

- **Enhanced `Refractulator` Class:**
  - Integrated the ray calculation logic into the `Refractulator` class, promoting better encapsulation and modularity.
  - Improved docstrings and comments for better code readability and maintainability.

### 📚 Documentation

- **Updated Documentation:**
  - Revised the documentation to include detailed descriptions of the new methods (`calculate_and_visualize_rays` and `generate_cylinder_ray_origins`).
  - Provided updated usage examples reflecting the simplified approach introduced in this version.

### 🐛 Bug Fixes

- **N/A:** No bug fixes in this release. All existing functionalities remain stable and reliable.

### 🔧 Configuration

- **`pyproject.toml` Updates:**
  - Ensured that the `pyproject.toml` is correctly formatted and adheres to TOML specifications.
  - Updated the `urls` section to use nested tables for better compatibility and parsing.

### 🚀 Getting Started

For users upgrading from a previous version, here’s a quick guide to utilizing the new features:

1. **Import the `Refractulator` Class:**

   ```python
   from refractulator import Refractulator
   ```

2. **Create an Instance:**

   ```python
   refractulator = Refractulator(radius=1.0)
   ```

3. **Calculate and Visualize Rays with a Single Method Call:**

   ```python
   refractulator.calculate_and_visualize_rays(
       num_rays=100,            # Number of rays
       cylinder_radius=0.5,     # Radius of the cylindrical beam
       theta_deg=120,           # Azimuth angle
       phi_deg=-30,             # Elevation angle
       mode='3d'                # Visualization mode ('2d' or '3d')
   )
   ```



## [0.2.0] - 2024-11-28

### Added

- **Visualization Module:** Added a new `visualization.py` module to provide 2D and 3D visualization functions using Plotly.
- **Data Generator Class:** Introduced `RefractulatorDataGenerator` class in `data_generator.py` for data generation and JSON serialization.
- **Examples:** Added example scripts in the `examples/` directory to demonstrate package usage.

### Changed

- **Refactored Code:** Moved calculation logic into the `Refractulator` class for better modularity and maintainability.
- **Updated Scripts:** Modified `toJSON_3d.py` and `dash_app.py` to use the `Refractulator` class from the package.

### Fixed

- [If any bug fixes were made, list them here.]

## [0.1.0] - 2024-11-25

- Initial release.
