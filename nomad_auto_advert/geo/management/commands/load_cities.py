import csv
from django.core.management.base import BaseCommand
from nomad_auto_advert.geo.models import City, Region, Country


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Starting ...')

        path = '/app/files/kz_cities_with_coords.csv'

        with open(path) as file:
            country, _ = Country.objects.get_or_create(name='Казахстан')
            reader = csv.DictReader(file)
            number = 0
            for count, row in enumerate(reader):
                region, _ = Region.objects.get_or_create(
                    country=country,
                    name=row.get('region') if row.get('region') != '' else 'Город республиканского значения'
                )
                _, created = City.objects.get_or_create(
                    name=row.get('name_ru'),
                    region=region,
                    population=row.get('population'),
                    priority=row.get('priority'),
                    latitude=row.get('Latitude'),
                    longitude=row.get('Longitude')
                )
                if created:
                    number += 1
            self.stdout.write(f'Created {number} City objects')
