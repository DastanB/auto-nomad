from django.core.management import BaseCommand
from nomad_auto_advert.cars.management.commands.utils.csv_abstract_loader import CSVAbstractLoader
from nomad_auto_advert.cars.models import CarGeneration


class CarGenerationDataLoader(CSVAbstractLoader):
    FILE_PATH = '/app/files/car_generation.csv'
    MODEL = CarGeneration

    @classmethod
    def normalize_row(cls, row) -> dict:
        name = row.get("'name'")[1:-1]
        year_begin = row.get("'year_begin'")[1:-1]
        year_end = row.get("'year_end'")[1:-1]
        ext = row.get("'id_car_generation'")[1:-1]
        car_model_ext = row.get("'id_car_model'")[1:-1]
        result = {
            'name': name,
            'year_begin': year_begin,
            'year_end': year_end,
            'ext': ext,
            'car_model_ext': car_model_ext
        }
        return result


class Command(BaseCommand):
    def handle(self, *args, **options):
        CarGenerationDataLoader.load()
