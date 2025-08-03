#!/bin/bash

# Run this script in the main project directory 
# where requirements.txt is located 

set -e

# Create venv if folder doesnt exist
if [ ! -d "venv" ]; then
  python3 -m venv venv
  echo "Virtual environment created."
else
  echo "Virtual environment already exists."
fi

# Activate the venv
source venv/bin/activate

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

