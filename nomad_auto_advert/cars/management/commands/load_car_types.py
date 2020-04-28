import sys

from django.core.exceptions import ImproperlyConfigured
from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarType
import os
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        cars_csv_dir = os.environ.get('CARS_CSV_DIR')

        if not cars_csv_dir:
            raise ImproperlyConfigured('Please set `CARS_CSV_DIR` env variable')

        car_type_csv = '/app/files/car_type.csv'

        car_type_filepath = os.path.join(cars_csv_dir, car_type_csv)

        count = 0

        with open(car_type_filepath, 'r') as car_type_file:
            r = csv.DictReader(car_type_file, quotechar="'")
            for row in r:
                obj, created = CarType.objects.get_or_create(ext=row['id_car_type'], name=row['name'])
                if created:
                    count += 1
                    sys.stdout.write(f'Created: {count}\r')
        self.stdout.write('Created {} objects'.format(count))
