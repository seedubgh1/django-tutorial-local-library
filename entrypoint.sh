#!/bin/sh

# python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input

gunicorn locallibrary.wsgi:application --bind 0.0.0.0:8080 --workers 3
