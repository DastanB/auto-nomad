from django.core.management import BaseCommand
from nomad_auto_advert.cars.management.commands.utils.csv_abstract_loader import CSVAbstractLoader
from nomad_auto_advert.cars.models import CarMark


class CarMarkDataLoader(CSVAbstractLoader):
    FILE_PATH = '/app/files/car_mark.csv'
    MODEL = CarMark

    @classmethod
    def normalize_row(cls, row) -> dict:
        name = row.get("'name'")[1:-1]
        name_ru = row.get("'name_rus'")[1:-1]
        ext = row.get("'id_car_mark'")[1:-1]
        car_type_ext = row.get("'id_car_type'")[1:-1]
        result = {
            'name': name,
            'name_ru': name_ru,
            'ext': ext,
            'car_type_ext': car_type_ext
        }
        return result


class Command(BaseCommand):
    def handle(self, *args, **options):
        CarMarkDataLoader.load()
