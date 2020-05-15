from django.core.management import BaseCommand
from nomad_auto_advert.cars.management.commands.utils.csv_abstract_loader import CSVAbstractLoader
from nomad_auto_advert.cars.models import CarCharacteristicValue


class CarCharacteristicValueDataLoader(CSVAbstractLoader):
    FILE_PATH = '/app/files/car_characteristic_value.csv'
    MODEL = CarCharacteristicValue

    @classmethod
    def normalize_row(cls, row) -> dict:
        ext = row.get("'id_car_characteristic_value'")[1:-1]
        value = row.get("'value'")[1:-1]
        unit = row.get("'unit'")[1:-1]

        car_characteristic_ext = row.get("'id_car_characteristic'")[1:-1]
        if not car_characteristic_ext.isdigit():
            car_characteristic_ext = None
        car_modification_ext = row.get("'id_car_modification'")[1:-1]
        if not car_modification_ext.isdigit():
            car_modification_ext = None

        result = {
            'ext': ext,
            'value': value,
            'unit': unit,
            'car_characteristic_ext': car_characteristic_ext,
            'car_modification_ext': car_modification_ext
        }
        return result


class Command(BaseCommand):
    def handle(self, *args, **options):
        CarCharacteristicValueDataLoader.load()
