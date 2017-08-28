import getpass

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.management import BaseCommand
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = "To create API key for Accessing the APIs."

    # A command must define handle()
    def handle(self, *args, **options):
        username = input("Enter username:")
        password = getpass.getpass()
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                token, created = Token.objects.get_or_create(user=user)
                print("=====================API Key=====================")
                print(token)
                print("=====================END=====================")
            else:
                print("Wrong Password.")
        except ObjectDoesNotExist as e:
            print("User is not registered. Please registered it with : 'python manage.py create_user'")