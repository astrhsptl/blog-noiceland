#!/usr/bin/env sh

python manage.py collectstatic --noinput

python manage.py makemigrations

python manage.py migrate

celery -A server worker -l info --detach

python manage.py runserver 0.0.0.0:4000