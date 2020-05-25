from django.core.management import BaseCommand
from nomad_auto_advert.filters.models import CarDriveType

CAR_DRIVE_EXT = 27


class Command(BaseCommand):
    def handle(self, *args, **options):
        drive_types = ["Задний", "Передний", "Полный", "Полный подключаемый"]

        for d in drive_types:
            drive = CarDriveType.objects.get_or_create(name=d)
            print(drive)
