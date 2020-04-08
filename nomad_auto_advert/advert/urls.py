from django.urls import path, include
from rest_framework import routers
from nomad_auto_advert.advert.views import AdvertView, AdvertImageViewSet

app_name = 'advert'

router = routers.DefaultRouter()
router.register(r'images', AdvertImageViewSet, basename='advert_image')


urlpatterns = (
    path(r'', AdvertView.as_view()),

    path('', include(router.urls))
)
