from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="kutnogorskiy77@gmail.ru",
            first_name='Milan',
            last_name='Kutnogorskiy',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('123456')
        user.save()