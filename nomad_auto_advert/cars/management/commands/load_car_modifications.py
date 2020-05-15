from django.core.management import BaseCommand
from nomad_auto_advert.cars.management.commands.utils.csv_abstract_loader import CSVAbstractLoader
from nomad_auto_advert.cars.models import CarModification


class CarModificationDataLoader(CSVAbstractLoader):
    FILE_PATH = '/app/files/car_modification.csv'
    MODEL = CarModification

    @classmethod
    def normalize_row(cls, row) -> dict:
        name = row.get("'name'")[1:-1]
        ext = row.get("'id_car_modification'")[1:-1]

        car_serie_ext = row.get("'id_car_serie'")[1:-1]
        if not car_serie_ext.isdigit():
            car_serie_ext = None

        result = {
            'name': name,
            'car_serie_ext': car_serie_ext,
            'ext': ext
        }
        return result


class Command(BaseCommand):
    def handle(self, *args, **options):
        CarModificationDataLoader.load()
