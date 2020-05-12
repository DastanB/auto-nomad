import sys
from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarCharacteristic, CarCharacteristicValue
from nomad_auto_advert.characteristics.models import DriveType


class Command(BaseCommand):
    def handle(self, *args, **options):
        drive_types = ["Задний", "Передний", "Полный", "Полный подключаемый"]
        characteristics = CarCharacteristic.objects.get(ext=27)
        characteristics_values = CarCharacteristicValue.objects.filter(car_characteristic=characteristics)

        for e in drive_types:
            drive = DriveType.objects.get_or_create(name=e)
            print(drive)
        print(f'Values count: {characteristics_values.count()}')

        count = 0
        for c in characteristics_values:
            drive = DriveType.objects.get(name__exact=c.value)
            if not c.drive_type:
                c.drive_type = drive
                c.save()
                count += 1
                sys.stdout.write(f'Updated: {count}\r')
