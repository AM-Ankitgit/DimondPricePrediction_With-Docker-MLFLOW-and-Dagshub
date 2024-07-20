
# The setup.py file is an essential part of Python projects, especially for those that are intended to be distributed and installed via package management systems like pip. It is used to provide metadata about the project and instructions on how to install it. Here are the primary uses of the setup.py file:

# 1. Package Distribution
# setup.py is used to define how a Python package is structured and distributed. It contains all the information needed to package the project, including its name, version, author, license, and dependencies.

# 2. Dependency Management
# You can specify the dependencies your project requires in the setup.py file. When someone installs your package, these dependencies will automatically be installed as well.

# 3. Installation
# Running python setup.py install installs the package. This command uses the information in setup.py to place the package in the appropriate location in the Python environment.

# 4. Metadata
# The setup.py file provides metadata about the project, such as the project name, version, author, license, and more. This metadata is used by package indexes like PyPI (Python Package Index).


# `5. Entry Points`
# If your project includes command-line scripts, you can define entry points in setup.py. This allows users to run your scripts as commands after installing your package.

from setuptools import find_packages,setup
from typing import List

setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='ankit',
    author_email='mahalleankit',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)