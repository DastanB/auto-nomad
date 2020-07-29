from django.urls import path, include
from rest_framework import routers
from nomad_auto_advert.advert.views import AdvertViewSet, AdvertImageViewSet, CarBodyStateViewSet, CarBodyListView, \
    AdvertSearchView

app_name = 'adverts'

router = routers.DefaultRouter()
router.register('all', AdvertSearchView, basename='all')


my_router = routers.DefaultRouter()
my_router.register('car-body-states', CarBodyStateViewSet, basename='car_body_states')
my_router.register('images', AdvertImageViewSet, basename='advert_images')
my_router.register('', AdvertViewSet, basename='adverts')


urlpatterns = (
    path('car-body-types/', CarBodyListView.as_view()),
    path('my/', include(my_router.urls)),
    path('', include(router.urls))
)

