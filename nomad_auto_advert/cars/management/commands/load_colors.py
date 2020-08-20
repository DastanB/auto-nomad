from django.core.management import BaseCommand
from nomad_auto_advert.cars.models import CarColor
import sys


class Command(BaseCommand):
    def handle(self, *args, **options):
        CarColor.objects.all().delete()
        colors = (
            {'id': 1, 'name': 'бронза', 'rgb': (63, 33, 9)},
            {'id': 2, 'name': 'вишня', 'rgb': (128, 0, 64)},
            {'id': 3, 'name': 'хамелеон', 'rgb': (0, 0, 0)},
            {'id': 4, 'name': 'бежевый', 'rgb': (234, 235, 222)},
            {'id': 5, 'name': 'белый', 'rgb': (255, 255, 255)},
            {'id': 6, 'name': 'бирюзовый', 'rgb': (6, 194, 172)},
            {'id': 7, 'name': 'бордовый', 'rgb': (176, 0, 0)},
            {'id': 8, 'name': 'голубой', 'rgb': (179, 250, 255)},
            {'id': 9, 'name': 'жёлтый', 'rgb': (255, 255, 20)},
            {'id': 10, 'name': 'зелёный', 'rgb': (21, 176, 26)},
            {'id': 11, 'name': 'золотистый', 'rgb': (212, 175, 55)},
            {'id': 12, 'name': 'коричневый', 'rgb': (101, 55, 0)},
            {'id': 13, 'name': 'красный', 'rgb': (255, 0, 0)},
            {'id': 14, 'name': 'оранжевый', 'rgb': (139, 90, 0)},
            {'id': 15, 'name': 'розовый', 'rgb': (255, 129, 192)},
            {'id': 16, 'name': 'серебристый', 'rgb': (	197, 201, 199)},
            {'id': 17, 'name': 'серый', 'rgb': (128, 128, 128)},
            {'id': 18, 'name': 'синий', 'rgb': (0, 0, 255)},
            {'id': 19, 'name': 'сиреневый', 'rgb': (196, 142, 253)},
            {'id': 20, 'name': 'фиолетовый', 'rgb': (154, 14, 234)},
            {'id': 21, 'name': 'черный', 'rgb': (0, 0, 0)},
            {'id': 22, 'name': 'белый жемчуг', 'rgb': (234, 224, 200)}
        )  # len = 22
        count = 0
        for val in colors:
            obj, created = CarColor.objects.get_or_create(
                ext=val['id'],
                name=val['name'],
                r_abbreviation=val['rgb'][0],
                g_abbreviation=val['rgb'][1],
                b_abbreviation=val['rgb'][2]
            )
            if created:
                count += 1
                sys.stdout.write(f'Created: {count}\r')
        self.stdout.write('Created {} objects'.format(count))
