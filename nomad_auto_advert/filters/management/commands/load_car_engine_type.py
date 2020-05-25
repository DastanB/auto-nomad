from django.core.management import BaseCommand
from nomad_auto_advert.filters.models import CarEngineType

ENGINE_EXT = 12


class Command(BaseCommand):
    def handle(self, *args, **options):
        engine_types = ["Бензиновый", "Бензиновый, Газ", "Бензиновый, Электрический", "Газ",
                        "Гибридный", "Дизельный", "Дизельный, Гибридный", "Электрический"]

        for e in engine_types:
            engine = CarEngineType.objects.get_or_create(name=e)
            print(engine)
