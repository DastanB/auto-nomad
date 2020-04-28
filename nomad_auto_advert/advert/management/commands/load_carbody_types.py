from django.core.management import BaseCommand

from nomad_auto_advert.advert.models import CarBody


class Command(BaseCommand):
    def handle(self, *args, **options):
        types = ['Передний бампер', 'Задний бампер',
                 'Капот', 'Крыша', 'Дверь багажника',
                 'Лобовое стекло', 'Левое зеркало', 'Правое зеркало',
                 'Переднее левое крыло', 'Передняя левая дверь', 'Задняя левая дверь', 'Заднее левое крыло',
                 'Переднее правое крыло', 'Передняя правая дверь', 'Задняя правая дверь', 'Заднее правое крыло']
        count = 0
        for type_name in types:
            obj, created = CarBody.objects.get_or_create(name=type_name)
            if created:
                count += 1
        self.stdout.write('Created {} objects'.format(count))
