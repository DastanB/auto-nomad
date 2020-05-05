from django.urls import path, include
from rest_framework import routers
from nomad_auto_advert.characteristics.views import TransmissionTypeViewSet, CarBodyTypeViewSet, EngineTypeViewSet, \
    DriveTypeViewSet

app_name = 'characteristics'
router = routers.DefaultRouter()
router.register('transmission-type', TransmissionTypeViewSet)
router.register('car-body-type', CarBodyTypeViewSet)
router.register('engine-type', EngineTypeViewSet)
router.register('drive-type', DriveTypeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
