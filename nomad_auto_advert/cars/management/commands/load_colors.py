from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarColor
import sys


class Command(BaseCommand):
    def handle(self, *args, **options):
        CarColor.objects.all().delete()
        colors = {
            1: 'бронза', 2: 'вишня', 3: 'хамелеон', 4: 'бежевый', 5: 'белый',
            6: 'бирюзовый', 7: 'бордовый', 8: 'голубой', 9: 'жёлтый', 10: 'зелёный',
            11: 'золотистый', 12: 'коричневый', 13: 'красный', 14: 'оранжевый', 15: 'розовый',
            16: 'серебристый', 17: 'серый', 18: 'синий', 19: 'сиреневый', 20: 'фиолетовый',
            21: 'черный'
        }  # len = 21
        count = 0
        for key in colors:
            obj, created = CarColor.objects.get_or_create(ext=key, name=colors[key])
            if created:
                count += 1
                sys.stdout.write(f'Created: {count}\r')
        self.stdout.write('Created {} objects'.format(count))
