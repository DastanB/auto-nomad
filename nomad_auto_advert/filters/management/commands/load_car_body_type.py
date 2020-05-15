from django.core.management import BaseCommand
from nomad_auto_advert.filters.models import CarBodyType


CAR_BODY_EXT = 2


class Command(BaseCommand):
    def handle(self, *args, **options):
        car_body_types = ["Внедорожник", "Кабриолет", "Кроссовер", "Купе",
                          "Лимузин", "Лифтбэк", "Минивэн", "Пикап",
                          "Родстер", "Седан", "Тарга", "Универсал",
                          "Фастбэк", "Хардтоп", "Хетчбэк"]

        for b in car_body_types:
            body = CarBodyType.objects.get_or_create(name=b)
            print(body)
