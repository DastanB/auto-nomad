import sys

from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarModification, CarEquipment
import os
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        cars_csv_dir = os.environ.get('CARS_CSV_DIR')

        car_type_csv = '/app/files/car_equipment.csv'
        self.stdout.write('equipment')
        car_type_filepath = os.path.join(cars_csv_dir, car_type_csv)

        count = 0

        with open(car_type_filepath, 'r') as car_type_file:
            r = csv.DictReader(car_type_file, quotechar="'")
            for row in r:
                try:
                    obj, created = CarEquipment.objects.get_or_create(
                        ext=row['id_car_equipment'], name=row['name'],
                        car_modification=CarModification.objects.get(ext=row['id_car_modification'])
                    )
                    if created:
                        count += 1
                        sys.stdout.write(f'Created: {count}\r')
                except Exception as e:
                    print(row['id_car_modification'], e)
        self.stdout.write('Created {} objects'.format(count))
