from rest_framework import generics
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters

from nomad_auto_advert.geo.filters import CityFilter
from nomad_auto_advert.geo.models import Country, Region, City
from nomad_auto_advert.geo.serializers import (
    CountrySerializer,
    RegionSerializer,
    CitySerializer,
)


class CountryListView(generics.ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    permission_classes = (AllowAny, )


class RegionListView(generics.ListAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    permission_classes = (AllowAny, )


class CityListView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    permission_classes = (AllowAny, )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = CityFilter
