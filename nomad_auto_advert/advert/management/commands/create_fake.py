from random import randrange
from django.core.management import BaseCommand
from nomad_auto_advert.advert.models import Advert
from nomad_auto_advert.cars.models import Car
from nomad_auto_advert.filters.models import CarBodyType, CarTransmissionType, CarDriveType, CarEngineType
from nomad_auto_advert.users.models import Profile


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Fake create started')
        profile = Profile.objects.get(phone='+77083495035')
        body_types = CarBodyType.objects.all()
        transmission_types = CarTransmissionType.objects.all()
        drive_types = CarDriveType.objects.all()
        engine_types = CarEngineType.objects.all()
        for i in range(10):
            car = Car()
            car.body_type = body_types.get(id=randrange(body_types.count())+1)
            car.transmission_type = transmission_types.get(id=randrange(transmission_types.count())+1)
            car.drive_type = drive_types.get(id=randrange(drive_types.count())+1)
            car.engine_type = engine_types.get(id=randrange(engine_types.count())+1)
            car.save()

            a = Advert.objects.create(
                user=profile,
                car=car,
                car_ext=0,
                car_condition_type=1,
                contact_name=f"Advert {i}",
                contact_email=f"Email {i}",
                description=f"Description {i}",
                price=(1000 + i)
            )
        self.stdout.write('Fake create ended')
