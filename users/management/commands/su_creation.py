from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@project.org',
            first_name='Admin',
            last_name='django_learning',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('1234')
        user.save()