from django.core.management import BaseCommand
from nomad_auto_advert.cars.management.commands.utils.csv_abstract_loader import CSVAbstractLoader
from nomad_auto_advert.cars.models import CarModel


class CarModelDataLoader(CSVAbstractLoader):
    FILE_PATH = '/app/files/car_model.csv'
    MODEL = CarModel

    @classmethod
    def normalize_row(cls, row) -> dict:
        name = row.get("'name'")[1:-1]
        name_ru = row.get("'name_rus'")[1:-1]
        ext = row.get("'id_car_model'")[1:-1]
        car_mark_ext = row.get("'id_car_mark'")[1:-1]
        result = {
            'name': name,
            'name_ru': name_ru,
            'ext': ext,
            'car_mark_ext': car_mark_ext
        }
        return result


class Command(BaseCommand):
    def handle(self, *args, **options):
        CarModelDataLoader.load()
