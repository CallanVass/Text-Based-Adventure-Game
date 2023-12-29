#!/bin/bash

# Python Installation
if ! command -v python3 &>/dev/null; then
    echo "Python is not installed. Installing..."
    sudo apt update
    sudo apt install python3
else
    echo "Python is already installed."
fi

# Pip Installation
if ! command -v pip3 &>/dev/null; then
    echo "pip is not installed. Installing..."
    sudo apt install python3-pip
else
    echo "pip is already installed."
fi

# Create and Activate Virtual Environment
if [ ! -d venv ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

# Requirements.txt Installation
if [ -f requirements.txt ]; then
    echo "Installing Python packages from requirements.txt..."
    pip3 install -r requirements.txt
else
    echo "requirements.txt file not found. Skipping package installation."
fi

source classes.py
source functions.py
source notebook.txt

# Running Main
if [ -f main.py ]; then
    echo "Running main.py..."
    python3 main.py
else
    echo "main.py file not found. Skipping execution."
fi