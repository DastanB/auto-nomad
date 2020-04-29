import sys
from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarCharacteristic, CarCharacteristicValue
from nomad_auto_advert.characteristics.models import TransmissionType


class Command(BaseCommand):
    def handle(self, *args, **options):
        transmission_types = ["Механика", "Автомат", "Вариатор", "Робот"]
        characteristics = CarCharacteristic.objects.get(ext=24)
        characteristics_values = CarCharacteristicValue.objects.filter(car_characteristic=characteristics)

        for t in transmission_types:
            transmission = TransmissionType.objects.get_or_create(name=t)
            print(transmission)
        print(f'Values count: {characteristics_values.count()}')

        count = 0
        for c in characteristics_values:
            transmission = TransmissionType.objects.get(name__icontains=c.value)
            if not c.transmission_type:
                c.transmission_type = transmission
                c.save()
                count += 1
                sys.stdout.write(f'Updated: {count}\r')
