from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarCharacteristic, CarCharacteristicValue
from nomad_auto_advert.filters.models import CharacteristicType


TRANSMISSION_EXT = 24


class Command(BaseCommand):
    def handle(self, *args, **options):
        transmission_types = ["Механика", "Автомат", "Вариатор", "Робот"]
        characteristic = CarCharacteristic.objects.get(ext=TRANSMISSION_EXT)

        for t in transmission_types:
            transmission = CharacteristicType.objects.get_or_create(name=t, characteristic=characteristic)
            print(transmission)

        characteristic_values = CarCharacteristicValue.objects.filter(car_characteristic=characteristic)
        for value in characteristic_values:
            transmission = CharacteristicType.objects.get(name__contains=value.value)
            value.type = transmission
            value.save()
            print(f"{value.value}: {value.type}")
