#!/bin/bash

# Run this script in the main project directory 
# where requirements.txt is located 

# This script is required to run pytest

set -e

# Create venv if folder doesnt exist
if [ ! -d "test_venv" ]; then
  python3 -m venv test_venv
  echo "Virtual environment created."
else
  echo "Virtual environment already exists."
fi

# Activate the venv
source test_venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install project as python package
if [ -f "setup.py" ]; then
  pip install -e .
  echo $'\nreal_estate_scraper installed. Run these commands to start the server:\n'
  echo "source venv/bin/activate"
  echo "real_estate_scraper"
else
  echo "No setup.py found."
fi


# Install pytest
pip install pytest
echo "Pytest Installed"
echo "To run the test suite:"
echo "source test_venv/bin/activate"
echo "pytest tests"
