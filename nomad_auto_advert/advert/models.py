from django.db import models
from nomad_auto_advert.cars.models import Car, CarType, CarMark, CarModel, CarGeneration, CarSerie, CarModification, \
    CarEquipment, CarColor
from nomad_auto_advert.microservices.models import Service


class Advert(models.Model):
    user = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    car = models.ForeignKey('cars.Car', related_name='adverts', on_delete=models.SET_NULL, null=True)
    car_ext = models.PositiveIntegerField()

    # состояние авто
    NEW, IN_MOTION, NON_RUNNER, DAMAGED = range(4)
    CONDITION_OPTION = (
        (NEW, 'Новый'),
        (IN_MOTION, 'На ходу'),
        (NON_RUNNER, 'Не на ходу'),
        (DAMAGED, 'Аварийная')
    )
    car_condition_type = models.IntegerField(choices=CONDITION_OPTION, null=True, blank=True)
    # cleared by customs = растаможен
    cleared_by_customs = models.BooleanField(default=False)

    # city_id in CAPS
    city_ext = models.PositiveIntegerField(null=True, blank=True)
    contact_name = models.CharField(max_length=100, null=True, blank=True)
    contact_email = models.CharField(max_length=100, null=True, blank=True)

    price = models.DecimalField(max_digits=99, decimal_places=1)
    exchange = models.BooleanField(default=False)

    # на заказ = to order
    to_order = models.BooleanField(default=False)
    RIGHT, LEFT = range(2)
    RULE_CHOICE = (
        (RIGHT, 'Справа'),
        (LEFT, 'Слева')
    )
    rule_type = models.IntegerField(choices=RULE_CHOICE, null=True, blank=True, default=LEFT)

    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"ID: {self.id}, CONTACT: {self.contact_name}, CAR_ID: {self.car_ext}"


class AdvertContactPhone(models.Model):
    advert = models.ForeignKey(Advert, related_name='advert_phones', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)


class AdvertImage(models.Model):
    advert = models.ForeignKey(Advert, related_name='advert_images', on_delete=models.CASCADE, null=True)
    image = models.ImageField()


class CarBody(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarBodyState(models.Model):
    car_body = models.ForeignKey('CarBody', related_name='car_body_state', on_delete=models.SET_NULL, null=True)
    advert = models.ForeignKey('Advert', related_name='car_body_state', on_delete=models.CASCADE)

    description = models.TextField(blank=True, null=True, max_length=200)
    painted = models.BooleanField(default=False)
    scratched = models.BooleanField(default=False)
    dent = models.BooleanField(default=False)
    rust = models.BooleanField(default=False)
