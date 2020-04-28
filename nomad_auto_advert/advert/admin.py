from django.contrib import admin
from nomad_auto_advert.advert.models import CarBody, CarBodyState


@admin.register(CarBody)
class CarBodyAdmin(admin.ModelAdmin):
    pass


@admin.register(CarBodyState)
class CarBodyStateAdmin(admin.ModelAdmin):
    pass
