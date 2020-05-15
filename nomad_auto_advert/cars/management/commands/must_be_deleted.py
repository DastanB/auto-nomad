from django.core.exceptions import ImproperlyConfigured
from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarModification, CarOption, CarEquipment, CarOptionValue, \
    CarCharacteristic, CarCharacteristicValue
import os, csv, sys


class Command(BaseCommand):
    def handle(self, *args, **options):
        cars_csv_dir = os.environ.get('CARS_CSV_DIR')

        if not cars_csv_dir:
            raise ImproperlyConfigured('Please set `CARS_CSV_DIR` env variable')

        car_type_csv = '/app/files/car_option.csv'
        self.stdout.write('options')
        car_type_filepath = os.path.join(cars_csv_dir, car_type_csv)

        count = 0

        with open(car_type_filepath, 'r') as car_type_file:
            r = csv.DictReader(car_type_file, quotechar="'")
            for row in r:
                obj, created = CarOption.objects.get_or_create(
                    ext=row['id_car_option'], name=row['name'],
                )
                if created:
                    count += 1
                    sys.stdout.write(f'Created: {count}\r')
        self.stdout.write('Created {} objects'.format(count))

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

        car_type_csv = '/app/files/car_option_value.csv'
        self.stdout.write('option_value')
        car_type_filepath = os.path.join(cars_csv_dir, car_type_csv)

        count = 0

        with open(car_type_filepath, 'r') as car_type_file:
            r = csv.DictReader(car_type_file, quotechar="'")
            for row in r:
                try:
                    obj, created = CarOptionValue.objects.get_or_create(
                        ext=row['id_car_option_value'], car_option=CarOption.objects.get(ext=row['id_car_option']),
                        car_equipment=CarEquipment.objects.get(ext=row['id_car_equipment'])
                    )
                    if created:
                        count += 1
                        sys.stdout.write(f'Created: {count}\r')
                except Exception as e:
                    print(row['id_car_equipment'], e)
        self.stdout.write('Created {} objects'.format(count))

        car_type_csv = '/app/files/car_characteristic.csv'
        self.stdout.write('characteristic')
        car_type_filepath = os.path.join(cars_csv_dir, car_type_csv)

        count = 0

        with open(car_type_filepath, 'r') as car_type_file:
            r = csv.DictReader(car_type_file, quotechar="'")
            for row in r:
                parent = row['id_parent']
                try:
                    parent = CarCharacteristic.objects.get(ext=int(parent))
                except:
                    parent = None
                obj, created = CarCharacteristic.objects.get_or_create(
                    ext=row['id_car_characteristic'], name=row['name'],
                    parent=parent
                )
                if created:
                    count += 1
                    sys.stdout.write(f'Created: {count}\r')
        self.stdout.write('Created {} objects'.format(count))

        car_type_csv = '/app/files/car_characteristic_value.csv'
        self.stdout.write('characteristic_value')
        car_type_filepath = os.path.join(cars_csv_dir, car_type_csv)

        count = 0

        with open(car_type_filepath, 'r') as car_type_file:
            r = csv.DictReader(car_type_file, quotechar="'")
            for row in r:
                try:
                    obj, created = CarCharacteristicValue.objects.get_or_create(
                        ext=row['id_car_characteristic_value'], value=row['value'],
                        unit=(row['unit'] if not row['unit'] == 'NULL' else ''),
                        car_modification=CarModification.objects.get(ext=row['id_car_modification']),
                        car_characteristic=CarCharacteristic.objects.get(ext=row['id_car_characteristic'])
                    )
                    if created:
                        count += 1
                        sys.stdout.write(f'Created: {count}\r')
                except Exception as e:
                    print(row['id_car_modification'], e)
        self.stdout.write('Created {} objects'.format(count))
