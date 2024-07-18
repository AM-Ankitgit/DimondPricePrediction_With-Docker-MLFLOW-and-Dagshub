#!/bin/bash

echo [$(date)]: "START"

# Source the Conda initialization script
echo [$(date)]: "Initializing Conda"
source /c/Users/BW_ML_1/anaconda3/etc/profile.d/conda.sh

echo [$(date)]: "Creating conda env with python 3.8"
conda create --prefix ./.env python=3.8 -y

echo [$(date)]: "Activating env"
source activate ./.env

echo [$(date)]: "Installing dev requirements"
pip install -r requirements_dev.txt

echo [$(date)]: "END"

