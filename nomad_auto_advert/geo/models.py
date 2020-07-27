from django.db import models


class Country(models.Model):
    name = models.CharField(
        max_length=80,
        unique=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Region(models.Model):
    country = models.ForeignKey(
        to='geo.Country',
        related_name='regions',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=80,
        unique=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class City(models.Model):
    region = models.ForeignKey(
        to='geo.Region',
        related_name='cities',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=80,
        unique=True
    )

    population = models.IntegerField(default=0)
    priority = models.PositiveIntegerField(default=1)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True, null=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
