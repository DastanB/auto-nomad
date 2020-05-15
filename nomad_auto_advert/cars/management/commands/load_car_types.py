from django.core.management import BaseCommand
from nomad_auto_advert.cars.management.commands.utils.csv_abstract_loader import CSVAbstractLoader
from nomad_auto_advert.cars.models import CarType


class CarTypeDataLoader(CSVAbstractLoader):
    FILE_PATH = '/app/files/car_type.csv'
    MODEL = CarType

    @classmethod
    def normalize_row(cls, row):
        name = row.get("'name'")[1:-1]
        ext = row.get("'id_car_type'")[1:-1]
        result = {
            'name': name,
            'ext': ext
        }
        return result


class Command(BaseCommand):
    def handle(self, *args, **options):
        CarTypeDataLoader.load()
