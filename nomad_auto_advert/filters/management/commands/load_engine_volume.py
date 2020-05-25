from django.core.management import BaseCommand
from nomad_auto_advert.filters.models import EngineVolumeType


CAR_BODY_EXT = 13


class Command(BaseCommand):
    def handle(self, *args, **options):
        engine_volume_types = [0.2, 0.4, 0.6, 0.8, 1.0,
                               1.2, 1.4, 1.6, 1.8, 2.0,
                               2.2, 2.4, 2.6, 2.8, 3.0,
                               3.5, 4.0, 4.5, 5.0, 5.5,
                               6.0, 7.0, 8.0, 9.0, 10.0]

        for v in engine_volume_types:
            volume = EngineVolumeType.objects.get_or_create(amount=v)
            print(volume)
