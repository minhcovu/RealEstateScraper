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

# Install dependencies
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
  echo "Dependencies installed."
else
  echo "No requirements.txt found."
fi

