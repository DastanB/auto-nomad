from django.urls import path, include
from rest_framework import routers

from nomad_auto_advert.geo.views import CountryListView, RegionListView, CityListView


app_name = 'geo'
router = routers.DefaultRouter()

urlpatterns = (
    path('countries/', CountryListView.as_view()),
    path('regions/', RegionListView.as_view()),
    path('cities/', CityListView.as_view()),
    path('', include(router.urls))
)
