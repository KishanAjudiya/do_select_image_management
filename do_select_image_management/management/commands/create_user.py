import getpass

from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import IntegrityError


class Command(BaseCommand):
    help = "To create new User."

    # A command must define handle()
    def handle(self, *args, **options):
        username = input("Enter username:")
        password = getpass.getpass()
        try:
            user = User.objects.create_user(username=username, password=password)
            print("User created.")
        except IntegrityError as e:
            print("Username already exists.")
        except Exception as e:
            print(repr(e))