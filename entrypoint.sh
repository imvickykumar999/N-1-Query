#!/bin/sh
set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Seed sample data if database has no authors
echo "Checking sample data..."
python manage.py shell -c "from core.models import Author; import sys; sys.exit(0 if Author.objects.exists() else 1)" || python manage.py seed_sample_data

# Execute the container's main command
exec "$@"
