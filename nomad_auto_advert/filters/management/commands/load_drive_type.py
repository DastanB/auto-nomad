from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarCharacteristic, CarCharacteristicValue
from nomad_auto_advert.filters.models import CharacteristicType


CAR_DRIVE_EXT = 27


class Command(BaseCommand):
    def handle(self, *args, **options):
        drive_types = ["Задний", "Передний", "Полный", "Полный подключаемый"]
        characteristic = CarCharacteristic.objects.get(ext=CAR_DRIVE_EXT)

        for e in drive_types:
            drive = CharacteristicType.objects.get_or_create(name=e, characteristic=characteristic)
            print(drive)
