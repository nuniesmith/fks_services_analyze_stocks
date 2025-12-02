#!/bin/bash
# Entrypoint script for fks_stocks

set -e

# Default values
SERVICE_NAME=${SERVICE_NAME:-fks_stocks}
SERVICE_PORT=${SERVICE_PORT:-8016}
HOST=${HOST:-0.0.0.0}

echo "Starting ${SERVICE_NAME} on ${HOST}:${SERVICE_PORT}"

# Run the service from src directory
exec python -m src.main
