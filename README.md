<p align="center">
    <img src="rainbow_computer.png" width="200" height="200">
</p>

<h1 align="center">Refractulator</h1>
<h3 align="center">More than a simple refraction calculator, refractulator is a Python package that calculates and visualizes how light interacts with water droplets (or any medium given the appropriate refraction data). 
</h3>


## Installation

```bash
pip install refractulator
```

To install with visualization support:

```bash
pip install refractulator[visualization]
```


## What's New in Version 0.2.0
- Visualization Module: Added support for 2D and 3D visualizations using Plotly.
- Data Generator Class: Simplified data generation with the new RefractulatorDataGenerator class.
- Examples: See the examples/ directory for usage examples.

## Usage
```python
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


```

## Features
- Calculate refracted and reflected rays interacting with a spherical medium.
- Support for multiple colors with different refractive indices.
- (Optional) Visualization tools for ray paths.

## Acknowledgements
This project was inspired by Dr. Brian Pasko, my math professor at ENMU. 

As well as this article decribing the whole process in detail:
Janke, S. (1999). Somewhere Within the Rainbow (UMAP). Consortium for Mathematics and its Applications (COMAP). https://www.comap.com/membership/member-resources/item/somewhere-within-the-rainbow-umap

Other resources I appreciate:
- https://javalab.org/en/rainbow_by_raindrops_en/
- https://ux1.eiu.edu/~cfadd/3050/Adventures/chapter_17/ch17_3.htm
- http://hyperphysics.phy-astr.gsu.edu/hbase/atmos/rbowpath.html
- http://hyperphysics.phy-astr.gsu.edu/hbase/atmos/rbowpath.html#c2


## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Copyright (c) 2024 Scott Kilgore