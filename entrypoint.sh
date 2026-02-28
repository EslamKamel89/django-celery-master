#!/bin/ash
set -e

echo "Applying database migrations..."
python3 manage.py migrate --noinput

echo "Starting server..."
exec "$@"
