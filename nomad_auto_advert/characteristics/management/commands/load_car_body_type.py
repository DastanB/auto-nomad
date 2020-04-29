import sys
from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarCharacteristic, CarCharacteristicValue
from nomad_auto_advert.characteristics.models import CarBodyType


class Command(BaseCommand):
    def handle(self, *args, **options):
        car_body_types = ["Внедорожник", "Кабриолет", "Кроссовер", "Купе",
                          "Лимузин", "Лифтбэк", "Минивэн", "Пикап",
                          "Родстер", "Седан", "Тарга", "Универсал",
                          "Фастбэк", "Хардтоп", "Хетчбэк"]
        characteristics = CarCharacteristic.objects.get(ext=2)
        characteristics_values = CarCharacteristicValue.objects.filter(car_characteristic=characteristics)

        for b in car_body_types:
            body = CarBodyType.objects.get_or_create(name=b)
            print(body)
        print(f'Values count: {characteristics_values.count()}')

        count = 0
        for c in characteristics_values:
            body = CarBodyType.objects.get(name__icontains=c.value)
            if not c.body_type:
                c.body_type = body
                c.save()
                count += 1
                sys.stdout.write(f'Updated: {count}\r')
