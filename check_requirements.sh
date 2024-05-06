#!/bin/bash
if [ ! -d "venv" ]; then
    echo "Virtual environment being generated"
    python3 -m venv venv
fi
source venv/bin/activate
echo "Installing necessary files from requirements.txt"
pip install -r requirements.txt
deactivate
echo "files installed."