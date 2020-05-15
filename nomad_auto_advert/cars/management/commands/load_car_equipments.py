from django.core.management import BaseCommand
from nomad_auto_advert.cars.management.commands.utils.csv_abstract_loader import CSVAbstractLoader
from nomad_auto_advert.cars.models import CarEquipment


class CarEquipmentDataLoader(CSVAbstractLoader):
    FILE_PATH = '/app/files/car_equipment.csv'
    MODEL = CarEquipment

    @classmethod
    def normalize_row(cls, row) -> dict:
        name = row.get("'name'")[1:-1]
        ext = row.get("'id_car_equipment'")[1:-1]

        car_modification_ext = row.get("'id_car_modification'")[1:-1]
        if not car_modification_ext.isdigit():
            car_modification_ext = None
        result = {
            'name': name,
            'ext': ext,
            'car_modification_ext': car_modification_ext
        }
        return result


class Command(BaseCommand):
    def handle(self, *args, **options):
        CarEquipmentDataLoader.load()
