# refractulator/__init__.py

from .calculate import Refractulator
from .data_generator import RefractulatorDataGenerator
from .visualization import visualize, visualize_2d, visualize_3d
from ._version import version as __version__




__version__ = "0.2.0-beta.1"  # Ensure this matches pyproject.toml

__all__ = ['Refractulator']
