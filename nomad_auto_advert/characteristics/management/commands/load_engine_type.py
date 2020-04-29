import sys
from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarCharacteristic, CarCharacteristicValue
from nomad_auto_advert.characteristics.models import EngineType


class Command(BaseCommand):
    def handle(self, *args, **options):
        engine_types = ["Бензиновый", "Бензиновый, Газ", "Бензиновый, Электрический", "Газ",
                        "Гибридный", "Дизельный", "Дизельный, Гибридный", "Электрический"]
        characteristics = CarCharacteristic.objects.get(ext=12)
        characteristics_values = CarCharacteristicValue.objects.filter(car_characteristic=characteristics)

        for e in engine_types:
            engine = EngineType.objects.get_or_create(name=e)
            print(engine)
        print(f'Values count: {characteristics_values.count()}')

        count = 0
        for c in characteristics_values:
            engine = EngineType.objects.get(name__exact=c.value)
            if not c.engine_type:
                c.engine_type = engine
                c.save()
                count += 1
                sys.stdout.write(f'Updated: {count}\r')
