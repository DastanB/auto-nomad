from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from nomad_auto_advert.filters.models import CarBodyType, CarTransmissionType, CarDriveType, CarEngineType
from nomad_auto_advert.filters.serializers import CarBodyTypeSerializer, CarTransmissionTypeSerializer, \
    CarDriveTypeSerializer, CarEngineTypeSerializer, TypeSerializer


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


class RuleTypeView(APIView):
    @swagger_auto_schema(responses={'200': TypeSerializer})
    def get(self, request, *args, **kwargs):
        rule_types = (
            {"id": 0, 'type': 'Справа'},
            {"id": 1, "type": 'Слева'}
        )
        return Response(rule_types)


class CarConditionTypeView(APIView):
    @swagger_auto_schema(responses={'200': TypeSerializer})
    def get(self, request, *args, **kwargs):
        condition_types = (
            {"id": 0, "type": "Новый"},
            {"id": 1, "type": "На ходу"},
            {"id": 2, "type": "Не на ходу"},
            {"id": 3, "type": "Аварийная"},
        )
        return Response(condition_types)
