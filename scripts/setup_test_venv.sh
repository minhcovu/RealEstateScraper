#!/bin/bash

# Run this script in the main project directory 
# where requirements.txt is located 

# This script is required to run pytest

set -e

# Create venv if folder doesnt exist
if [ ! -d "test_venv" ]; then
  python3 -m venv test_venv
  echo "Virtual test environment created."
else
  echo "Virtual test environment already exists."
fi

# Activate the venv
source test_venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
  echo "Dependencies installed."
else
  echo "No requirements.txt found."
fi

# Install pytest
pip install pytest
echo "Pytest Installed"
