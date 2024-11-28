# setup.py

import os
import re
from setuptools import setup, find_packages

def read_version():
    with open(os.path.join('refractulator', '__init__.py'), 'r') as f:
        content = f.read()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")

setup(
    name='refractulator',
    version=read_version(),
    author='Scott Kilgore',
    author_email='kilgore.scott+github@gmail.com',
    description='A package to calculate and visualize light interactions with water droplets.',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ScottTpirate/refractulator',
    packages=find_packages(exclude=['tests', 'examples', 'docs']),
    install_requires=[
        'numpy',
        
    ],
    extras_require={
        'visualization': ['plotly']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
