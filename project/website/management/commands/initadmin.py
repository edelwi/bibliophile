import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # based on https://stackoverflow.com/questions/30027203/create-django-super-user-in-a-docker-container-without-inputting-password
    def handle(self, *args, **options):
        username = os.getenv('DJANGO_SUPERUSER_USERNAME') or 'admin'
        email = os.getenv('DJANGO_SUPERUSER_EMAIL') or 'admin@example.com'
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD') or '_1234567890-'

        if not User.objects.filter(username=username).exists():
            print(f'Creating account for {username} ({email})')
            User.objects.create_superuser(
                email=email, username=username, password=password)
        else:
            print('Admin account has already been initialized.')
