from django.urls import path, include
from rest_framework import routers
from nomad_auto_advert.microservices.views import ServicesViewSet, health_check_view, UpdateCarView, DeleteCarView

app_name = 'microservices'

router = routers.DefaultRouter()
router.register(r'', ServicesViewSet, base_name='microservices')

urlpatterns = [
    path('', include(router.urls)),
    path('health-check/', health_check_view, name="health-check"),
    path('car/update/', UpdateCarView.as_view()),
    path('car/delete/<int:car_ext>/', DeleteCarView.as_view()),
]
