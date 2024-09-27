#!/bin/bash

# Define the Python file to run
PYTHON_FILE="start.py" # Replace with your actual Python file name

# Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating the virtual environment..."
source venv\Scripts\activate

# Install packages from requirements.txt
if [[ -f "requirements.txt" ]]; then
    echo "Installing packages from requirements.txt..."
    python3 -m pip install -r requirements.txt

else
    echo "requirements.txt not found!"
    exit 1
fi

# Run docker-compose up
echo "Starting Docker containers with docker-compose..."
docker-compose up -d

# Run the specified Python file
if [[ -f "$PYTHON_FILE" ]]; then
    echo "Running the Python file: $PYTHON_FILE..."
    python3 $PYTHON_FILE
else
    echo "Python file $PYTHON_FILE not found!"
    exit 1
fi

# Deactivate the virtual environment
echo "Deactivating the virtual environment..."
deactivate

echo "Script completed successfully."
