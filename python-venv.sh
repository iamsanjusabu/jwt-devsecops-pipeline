#!/bin/bash

# This script is for local run
# Assuming python3 and pip3 is installed. If not, install them first
# In EndeavourOS which im using or any Arch flavour its "sudo pacman -S python" (both python and pip gets installed with just this one command)

set -e

if [ ! -d "python-venv" ]; then
    python3 -m venv python-venv
fi

source python-venv/bin/activate

pip3 install --upgrade pip
pip3 install -r requirements.txt --no-cache-dir


# TO RUN THIS:
#### either make this file executable (chmod u+x python-venv.sh) or run it like this (bash python-venv.sh)