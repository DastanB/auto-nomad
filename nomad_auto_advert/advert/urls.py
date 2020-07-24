from django.urls import path, include
from rest_framework import routers
from nomad_auto_advert.advert.views import AdvertViewSet, AdvertImageViewSet, CarBodyStateViewSet, CarBodyListView, \
    AdvertSearchView

app_name = 'advert'

router = routers.DefaultRouter()
router.register(r'images', AdvertImageViewSet, basename='advert_images')
router.register(r'car-body-states', CarBodyStateViewSet, basename='car_body_states')
router.register(r'', AdvertViewSet, basename='adverts')


urlpatterns = (
    path(r'car-body-types/', CarBodyListView.as_view()),
    path(r'search/', AdvertSearchView.as_view()),

    path('', include(router.urls))
)
