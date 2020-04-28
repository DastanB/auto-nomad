from django.core.exceptions import ImproperlyConfigured, MultipleObjectsReturned
from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarSerie, CarModification
import os, sys
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        cars_csv_dir = os.environ.get('CARS_CSV_DIR')
        if not cars_csv_dir:
            raise ImproperlyConfigured('Please set `CARS_CSV_DIR` env variable')

        car_type_csv = '/app/files/car_modification.csv'

        car_type_filepath = os.path.join(cars_csv_dir, car_type_csv)

        count = 0

        with open(car_type_filepath, 'r') as car_type_file:
            r = csv.DictReader(car_type_file, quotechar="'")
            for i, row in enumerate(r, start=1):
                try:
                    obj, created = CarModification.objects.get_or_create(
                        ext=row['id_car_modification'], name=row['name'],
                        car_serie_id=CarSerie.objects.get(ext=row['id_car_serie']).id
                    )
                except MultipleObjectsReturned:
                    self.stdout.write(f'{row}')
                if created:
                    count += 1
                    sys.stdout.write(f'Created: {count}\r')
        self.stdout.write('Created {} objects'.format(count))
