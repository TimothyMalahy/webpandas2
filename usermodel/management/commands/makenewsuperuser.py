from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            u = None
            email = 'timothymalahy@gmail.com'
            new_password = get_random_string()

            u = User.objects.create_superuser(email, new_password)
            print(f"===================================")
            print(f"A superuser was created with email {email} and password {new_password}")
            print(f"===================================")
            print(u)
        except Exception as e:
            print(f"There was an error: {e}")