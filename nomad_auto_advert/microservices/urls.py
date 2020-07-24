from django.urls import path, include
from rest_framework import routers
from nomad_auto_advert.microservices.views import ServicesViewSet, health_check_view, UpdateCarView

app_name = 'microservices'

router = routers.DefaultRouter()
router.register(r'microservices', ServicesViewSet, base_name='microservices')

urlpatterns = [
    path('', include(router.urls)),
    path('health-check/', health_check_view, name="health-check"),
    path('update/car/', UpdateCarView.as_view())
]
