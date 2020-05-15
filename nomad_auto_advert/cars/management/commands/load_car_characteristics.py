from django.core.management import BaseCommand
from nomad_auto_advert.cars.management.commands.utils.csv_abstract_loader import CSVAbstractLoader
from nomad_auto_advert.cars.models import CarCharacteristic


class CarCharacteristicDataLoader(CSVAbstractLoader):
    FILE_PATH = '/app/files/car_characteristic.csv'
    MODEL = CarCharacteristic

    @classmethod
    def normalize_row(cls, row) -> dict:
        name = row.get("'name'")[1:-1]
        ext = row.get("'id_car_characteristic'")[1:-1]

        parent_ext = row.get("'id_parent'")[1:-1]
        if not parent_ext.isdigit():
            parent_ext = None

        result = {
            'name': name,
            'parent_ext': parent_ext,
            'ext': ext
        }
        return result


class Command(BaseCommand):
    def handle(self, *args, **options):
        CarCharacteristicDataLoader.load()
