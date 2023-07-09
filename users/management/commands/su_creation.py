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
            is_active=True,
        )

        user.set_password('661104')
        user.save()
