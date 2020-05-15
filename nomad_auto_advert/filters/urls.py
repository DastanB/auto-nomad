from django.urls import path, include
from rest_framework import routers
from nomad_auto_advert.filters.views import CarBodyTypeViewSet


app_name = 'filters'
router = routers.DefaultRouter()
router.register(r'body-types', CarBodyTypeViewSet, basename='body-types')


urlpatterns = [
    path(r'', include(router.urls)),
]
