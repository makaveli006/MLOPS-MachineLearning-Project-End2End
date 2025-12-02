"""
When you write "-e ." in the "requirements.txt" it looks for setup.py file to install the package in editable mode.
This file is necessary for pip to understand how to install your package.

So that you can do "from us_visa.components.data_ingestion import DataIngestion" from anywhere in your system after installing the package.
It is called local package installation, but in editable mode.
More details are inside "project_structure.ipynb"

"""

from setuptools import setup, find_packages

setup(
    name="us_visa",
    version="0.0.0",
    author="subin",
    author_email="test@gmail.com",
    packages=find_packages()
)