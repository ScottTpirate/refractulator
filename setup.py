# setup.py

from setuptools import setup, find_packages

setup(
    name='refractulator',
    version='0.1.0',
    author='Scott Kilgore',
    author_email='kilgore.scott+github@gmail.com',
    description='A package to calculate and visualize light interactions with water droplets.',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ScottTpirate/refractulator',
    packages=find_packages(),
    install_requires=[
        'numpy',
        
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Change if using a different license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
