#!/bin/bash
set -eu

echo "Syncing the Database"
py manage.py makemigrations
py manage.py migrate
py manage.py ensuresuperuser --username devuser --email dev@mail.com --password devpass
py manage.py collectstatic --no-input

echo "Starting server"
py manage.py runserver
# gunicorn backend.wsgi -w 3 --bind 0.0.0.0:8000 --reload