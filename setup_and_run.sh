#!/bin/bash

# Define the Python file to run
PYTHON_FILE="start.py" # Replace with your actual Python file name
VENV_DIR=".venv"

sudo apt update

# Check if the virtual environment directory exists
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists."
else
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"

    echo "Virtual environment created."
fi
echo "Activating the virtual environment..."
source .venv/bin/activate


# Run docker-compose up
echo "Starting Docker containers with docker-compose..."
docker-compose up -d

# Install packages from requirements.txt
if [[ -f "requirements.txt" ]]; then
    echo "Installing packages from requirements.txt..."
    pip install -r requirements.txt
else
    echo "No requirements.txt found."
fi

# Run the specified Python file
if [ -f "$PYTHON_FILE" ]; then
    echo "Running the Python file: $PYTHON_FILE..."
    python3 $PYTHON_FILE
else
    echo "Python file $PYTHON_FILE not found!"
    exit 1
fi

# # Deactivate the virtual environment
# echo "Deactivating the virtual environment..."
# deactivate

echo "Script completed successfully."