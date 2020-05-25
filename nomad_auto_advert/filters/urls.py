from django.urls import path, include
from rest_framework import routers
from nomad_auto_advert.filters.views import CarBodyTypeViewSet, CarDriveTypeViewSet, CarTransmissionTypeViewSet, CarEngineTypeViewSet


app_name = 'filters'
router = routers.DefaultRouter()
router.register(r'body-types', CarBodyTypeViewSet, basename='body-types')
router.register(r'transmission-types', CarTransmissionTypeViewSet, basename='transmission-types')
router.register(r'drive-types', CarDriveTypeViewSet, basename='drive-types')
router.register(r'engine-types', CarEngineTypeViewSet, basename='engine-types')



urlpatterns = [
    path(r'', include(router.urls)),
]
