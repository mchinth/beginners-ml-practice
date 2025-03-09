#!/usr/bin/env bash
# Setup script for Machine Learning environment with unique per-system venv

set -e  # Exit on error

# Get the current script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Generate a unique virtual environment name based on the system hostname
HOSTNAME=$(hostname)
ENV_DIR="$SCRIPT_DIR/.venv_$HOSTNAME"

# Check if the virtual environment exists
if [ -d "$ENV_DIR" ]; then
    echo "✅ Virtual environment already exists at: $ENV_DIR"
    echo "👉 To activate it, run:"
    echo "   source $ENV_DIR/bin/activate"
    exit 0
else
    echo "Creating new virtual environment in: $ENV_DIR"
    python3 -m venv "$ENV_DIR"
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source "$ENV_DIR/bin/activate"

# Upgrade pip safely inside venv (without --break-system-packages)
echo "Upgrading pip..."
python3 -m pip install --upgrade pip setuptools wheel

# Install common ML libraries inside venv
echo "Installing ML libraries..."
python3 -m pip install --no-cache-dir \
    numpy \
    pandas \
    matplotlib \
    scikit-learn \
    scipy \
    seaborn \
    jupyter \
    ipython \
    notebook \
    tensorflow \
    torch \
    torchvision \
    torchaudio \
    keras \
    transformers \
    opencv-python \
    tensorflow-datasets \
    torchtext \
    timm

# Deactivate the environment
echo "Deactivating virtual environment..."
deactivate

# Print activation message
echo "✅ Setup complete!"
echo "👉 To start using the environment, run:"
echo "   source $ENV_DIR/bin/activate"
