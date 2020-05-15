from django.core.management import BaseCommand
from nomad_auto_advert.cars.management.commands.utils.csv_abstract_loader import CSVAbstractLoader
from nomad_auto_advert.cars.models import CarSerie


class CarSerieDataLoader(CSVAbstractLoader):
    FILE_PATH = '/app/files/car_serie.csv'
    MODEL = CarSerie

    @classmethod
    def normalize_row(cls, row) -> dict:
        name = row.get("'name'")[1:-1]
        ext = row.get("'id_car_serie'")[1:-1]

        car_generation_ext = row.get("'id_car_generation'")[1:-1]
        if not car_generation_ext.isdigit():
            car_generation_ext = None

        car_model_ext = row.get("'id_car_model'")[1:-1]
        if not car_model_ext.isdigit():
            car_model_ext = None

        result = {
            'name': name,
            'car_generation_ext': car_generation_ext,
            'car_model_ext': car_model_ext,
            'ext': ext
        }
        return result


class Command(BaseCommand):
    def handle(self, *args, **options):
        CarSerieDataLoader.load()
