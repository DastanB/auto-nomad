from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarCharacteristic
from nomad_auto_advert.filters.models import CharacteristicType


ENGINE_EXT = 12


class Command(BaseCommand):
    def handle(self, *args, **options):
        engine_types = ["Бензиновый", "Бензиновый, Газ", "Бензиновый, Электрический", "Газ",
                        "Гибридный", "Дизельный", "Дизельный, Гибридный", "Электрический"]
        characteristic = CarCharacteristic.objects.get(ext=ENGINE_EXT)

        for e in engine_types:
            engine = CharacteristicType.objects.get_or_create(name=e, characteristic=characteristic)
            print(engine)
