#!/bin/sh
python manage.py makemigrations &&
python manage.py migrate &&
gunicorn bibliophile.wsgi:application --bind 0.0.0.0:${APP_PORT}