import logging
from nomad_auto_advert.microservices.models import Service
from nomad_auto_advert.cars.models import (
    CarColor,
    Car,
    CarType,
    CarMark,
    CarModel,
    CarGeneration,
    CarSerie,
    CarModification,
    CarEquipment
)
from nomad_auto_advert.users.models import ContactPhone

logger = logging.getLogger(__name__)


def update_car(data):
    car = Car.objects.filter(car_ext=data.get('car_id')).first()
    if car is not None:
        if data.get('car_color'):
            car.car_color = CarColor.objects.get(ext=data.get('car_color'))
        if data.get('car_type'):
            car.car_type = CarType.objects.get(ext=data.get('car_type'))
        if data.get('car_mark'):
            car.car_mark = CarMark.objects.get(ext=data.get('car_mark'))
        if data.get('car_model'):
            car.car_model = CarModel.objects.get(ext=data.get('car_model'))
        if data.get('car_generation'):
            car.car_generation = CarGeneration.objects.get(ext=data.get('car_generation'))
        if data.get('car_serie'):
            car.car_serie = CarSerie.objects.get(ext=data.get('car_serie'))
        if data.get('car_modification'):
            car.car_modification = CarModification.objects.get(ext=data.get('car_modification'))
        if data.get('car_equipment'):
            car.car_equipment = CarEquipment.objects.get(ext=data.get('car_equipment'))
        if data.get('mileage'):
            car.mileage = data.get('mileage')
        if data.get('age'):
            car.year = data.get('age')
        car.save()
    return car


def get_service(name: str):
    service = Service.objects.filter(name=name).first()
    if service is not None:
        try:
            health_check = service.remote_call('get', '/api/microservices/health-check/')
            if health_check.ok:
                return service
        except ConnectionError as exception:
            logger.exception(exception)
            return
    return


def set_phone_number(profile):
    contact_phone = ContactPhone.objects.filter(profile=profile, phone=profile.phone).first()
    if contact_phone is None:
        ContactPhone.objects.create(profile=profile, phone=profile.phone)
