from django.core.management import BaseCommand
from nomad_auto_advert.cars.management.commands.utils.csv_abstract_loader import CSVAbstractLoader
from nomad_auto_advert.cars.models import CarOptionValue


class CarOptionValueDataLoader(CSVAbstractLoader):
    FILE_PATH = '/app/files/car_option_value.csv'
    MODEL = CarOptionValue

    @classmethod
    def normalize_row(cls, row) -> dict:
        ext = row.get("'id_car_option_value'")[1:-1]

        car_option_ext = row.get("'id_car_option'")[1:-1]
        if not car_option_ext.isdigit():
            car_option_ext = None

        car_equipment_ext = row.get("'id_car_equipment'")[1:-1]
        if not car_equipment_ext.isdigit():
            car_equipment_ext = None

        result = {
            'ext': ext,
            'car_option_ext': car_option_ext,
            'car_equipment_ext': car_equipment_ext
        }
        return result


class Command(BaseCommand):
    def handle(self, *args, **options):
        CarOptionValueDataLoader.load()
