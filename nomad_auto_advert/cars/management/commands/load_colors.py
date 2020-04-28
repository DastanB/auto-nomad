from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarColor
import sys


class Command(BaseCommand):
    def handle(self, *args, **options):
        colors = ['бронза', 'вишня', 'хамелеон', 'бежевый', 'белый', 'бирюзовый',
                  'бордовый', 'голубой', 'жёлтый', 'зелёный', 'золотистый', 'коричневый',
                  'красный', 'оранжевый', 'розовый', 'серебристый', 'серый', 'синий',
                  'сиреневый', 'фиолетовый', 'черный']
        count = 0
        for color in colors:
            obj, created = CarColor.objects.get_or_create(name=color)
            if created:
                count += 1
                sys.stdout.write(f'Created: {count}\r')
        self.stdout.write('Created {} objects'.format(count))
