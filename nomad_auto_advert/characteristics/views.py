from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from nomad_auto_advert.characteristics.models import TransmissionType, CarBodyType, EngineType
from nomad_auto_advert.characteristics.serializers import TransmissionTypeSerializer, CarBodyTypeSerializer, \
    EngineTypeSerializer


class TransmissionTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TransmissionTypeSerializer
    queryset = TransmissionType.objects.all()
    permission_classes = (AllowAny, )


class CarBodyTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarBodyTypeSerializer
    queryset = CarBodyType.objects.all()
    permission_classes = (AllowAny, )


class EngineTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EngineTypeSerializer
    queryset = EngineType.objects.all()
    permission_classes = (AllowAny, )
