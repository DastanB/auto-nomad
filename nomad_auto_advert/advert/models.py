from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from model_utils.models import TimeStampedModel

from nomad_auto_advert.cars.models import (
    Car,
    CarType,
    CarMark,
    CarModel,
    CarGeneration,
    CarSerie,
    CarModification,
    CarEquipment,
    CarColor
)
from nomad_auto_advert.microservices.models import Service


class AdvertManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .prefetch_related('advert_images', 'advert_phones')


class Advert(models.Model):
    user = models.ForeignKey(
        to='users.Profile',
        related_name='adverts',
        on_delete=models.CASCADE
    )
    car = models.ForeignKey(
        to='cars.Car',
        related_name='adverts',
        on_delete=models.CASCADE,
    )
    car_ext = models.PositiveIntegerField(blank=True, null=True)
    city = models.ForeignKey(
        to='geo.City',
        related_name='adverts',
        on_delete=models.SET_NULL,
        null=True
    )

    NEW, IN_MOTION, NON_RUNNER, DAMAGED = range(4)
    CONDITION_OPTION = (
        (NEW, 'Новый'),
        (IN_MOTION, 'На ходу'),
        (NON_RUNNER, 'Не на ходу'),
        (DAMAGED, 'Аварийная')
    )
    car_condition_type = models.IntegerField(
        'Состояние машины',
        choices=CONDITION_OPTION,
        null=True, blank=True
    )
    cleared_by_customs = models.BooleanField(
        'Растаможен',
        default=False
    )
    contact_name = models.CharField(
        'Контактное имя',
        max_length=100,
        null=True, blank=True
    )
    contact_email = models.CharField(
        'Контактная почта',
        max_length=100,
        null=True, blank=True
    )
    contact_phones = models.ManyToManyField(
        to='users.ContactPhone',
        related_name='contact_phones'
    )
    description = models.TextField(
        'Описание',
        null=True, blank=True
    )
    price = models.DecimalField(
        'Цена',
        max_digits=99,
        decimal_places=1
    )
    exchange = models.BooleanField('Возможен обмен', default=False)
    to_order = models.BooleanField('На заказ', default=False)

    RIGHT, LEFT = range(2)
    RULE_CHOICE = (
        (RIGHT, 'Справа'),
        (LEFT, 'Слева')
    )
    rule_type = models.IntegerField(
        'Тип руля',
        choices=RULE_CHOICE,
        null=True, blank=True,
        default=LEFT
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.PositiveIntegerField(default=0)

    def increment_views_count(self):
        self.views_count = self.views_count + 1
        self.save()

    def __str__(self):
        return f"ID: {self.id}, CONTACT: {self.contact_name}, CAR_ID: {self.car_ext}"


class AdvertImage(models.Model):
    advert = models.ForeignKey(
        to='advert.Advert',
        related_name='advert_images',
        on_delete=models.CASCADE
    )
    image = models.ImageField()
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 60}
    )


class CarBody(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarBodyState(models.Model):
    car_body = models.ForeignKey(
        to='advert.CarBody',
        related_name='car_body_state',
        on_delete=models.SET_NULL,
        null=True
    )
    advert = models.ForeignKey(
        to='advert.Advert',
        related_name='car_body_state',
        on_delete=models.CASCADE
    )
    description = models.TextField(blank=True, null=True, max_length=200)
    painted = models.BooleanField(default=False)
    scratched = models.BooleanField(default=False)
    dent = models.BooleanField(default=False)
    rust = models.BooleanField(default=False)


class AdvertFavourite(TimeStampedModel):
    advert = models.ForeignKey(
        to='advert.Advert',
        related_name='favourites',
        on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        to='users.Profile',
        related_name='favourites',
        on_delete=models.CASCADE
    )


class AdvertComplaint(TimeStampedModel):
    advert = models.ForeignKey(
        to='advert.Advert',
        related_name='complaints',
        on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        to='users.Profile',
        related_name='complaints',
        on_delete=models.CASCADE
    )
    is_spam = models.BooleanField(default=False)
    is_inappropriate_content = models.BooleanField(default=False)
    is_fake_information = models.BooleanField(default=False)

    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Жалоба'
        verbose_name_plural = 'Жалобы'


class AdvertComment(TimeStampedModel):
    advert = models.ForeignKey(
        to='advert.Advert',
        related_name='comments',
        on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        to='users.Profile',
        related_name='comments',
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        to='self',
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True
    )
    text = models.TextField()

    def __str__(self):
        return f'id={self.id}, text={self.text}'
