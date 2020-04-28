from django.urls import path, include
from rest_framework import routers
from nomad_auto_advert.advert.views import AdvertViewSet, AdvertImageViewSet, CarBodyStateViewSet, CarBodyListView, \
    AdvertSearchView

app_name = 'advert'

router = routers.DefaultRouter()
router.register(r'images', AdvertImageViewSet, basename='advert_image')
router.register(r'car-body-states', CarBodyStateViewSet, basename='car_body_state')
router.register(r'', AdvertViewSet, basename='advert')


urlpatterns = (
    path(r'car-bodies/', CarBodyListView.as_view()),
    path(r'search/', AdvertSearchView.as_view()),

    path('', include(router.urls))
)
