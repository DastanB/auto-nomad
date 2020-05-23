from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from nomad_auto_advert.filters.models import CarBodyType, CarTransmissionType, CarDriveType, CarEngineType
from nomad_auto_advert.filters.serializers import CarBodyTypeSerializer, CarTransmissionTypeSerializer, \
    CarDriveTypeSerializer, CarEngineTypeSerializer


class CarBodyTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarBodyTypeSerializer
    permission_classes = (AllowAny, )
    queryset = CarBodyType.objects.all()


class CarTransmissionTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarTransmissionTypeSerializer
    permission_classes = (AllowAny, )
    queryset = CarTransmissionType.objects.all()


class CarDriveTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarDriveTypeSerializer
    permission_classes = (AllowAny, )
    queryset = CarDriveType.objects.all()


class CarEngineTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarEngineTypeSerializer
    permission_classes = (AllowAny, )
    queryset = CarEngineType.objects.all()
