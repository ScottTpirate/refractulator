# Refractulator

Refractulator is a Python package that calculates and visualizes how light interacts with water droplets (or any medium given the appropriate refraction data).

## Installation

```bash
pip install refractulator
```

## Usage
```python
from refractulator import Refractulator
import numpy as np

# Initialize Refractulator
refr = Refractulator(radius=1.0)

# Define incoming direction
D = np.array([1.0, 0.0, 0.0])

# Generate ray origins (example)
ray_origins = np.random.uniform(-0.5, 0.5, size=(100, 3))

# Calculate rays
rays = refr.calculate_rays_cylinder(ray_origins, D)

# Print the number of rays calculated
print(f"Number of rays calculated: {len(rays)}")
```

## Features
- Calculate refracted and reflected rays interacting with a spherical medium.
- Support for multiple colors with different refractive indices.
- (Optional) Visualization tools for ray paths.


## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Copyright (c) 2024 Scott Kilgore