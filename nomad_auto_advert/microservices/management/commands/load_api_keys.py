from django.conf import settings
from django.core.management.base import BaseCommand

from nomad_auto_advert.microservices.models import APIKey


class Command(BaseCommand):
    help = 'Load default `x-api-key`'

    def handle(self, *args, **options):
        default_key = settings.COMMON_API_KEY
        APIKey.objects.get_or_create(name='default', key=default_key)
        self.stdout.write("Default key loaded!")
