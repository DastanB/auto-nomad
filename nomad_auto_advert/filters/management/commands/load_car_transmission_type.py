from django.core.management import BaseCommand
from nomad_auto_advert.filters.models import CarTransmissionType


TRANSMISSION_EXT = 24


class Command(BaseCommand):
    def handle(self, *args, **options):
        transmission_types = ["Механика", "Автомат", "Вариатор", "Робот"]

        for t in transmission_types:
            transmission = CarTransmissionType.objects.get_or_create(name=t)
            print(transmission)
