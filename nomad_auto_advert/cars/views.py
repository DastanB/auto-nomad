from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from nomad_auto_advert.cars.filters import CarMarkFilter, CarModelFilter, CarGenerationFilter, CarSerieFilter, \
    CarModificationFilter, CarCharacteristicFilter, CarCharacteristicValueFilter, CarOptionValueFilter, CarOptionFilter, \
    CarEquipmentFilter
from nomad_auto_advert.cars.models import CarType, CarMark, CarModel, CarGeneration, CarSerie, CarModification, \
    CarCharacteristic, CarCharacteristicValue, CarOption, CarOptionValue, CarEquipment, Car
from nomad_auto_advert.cars.serializers import CarTypeSerializer, CarMarkSerializer, CarModelSerializer, \
    CarGenerationSerializer, CarSerieSerializer, CarModificationSerializer, CarCharacteristicSerializer, \
    CarCharacteristicValueSerializer, CarOptionSerializer, CarOptionValueSerializer, CarEquipmentSerializer, \
    CarSerializer
from django_filters import rest_framework as filters


class CarView(generics.ListAPIView):
    permission_classes = (AllowAny, )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = None


class CarTypeView(CarView):
    serializer_class = CarTypeSerializer
    queryset = CarType.objects.all()


class CarMarkView(CarView):
    serializer_class = CarMarkSerializer
    queryset = CarMark.objects.all()
    filterset_class = CarMarkFilter


class CarModelView(CarView):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarModelFilter


class CarGenerationView(CarView):
    serializer_class = CarGenerationSerializer
    queryset = CarGeneration.objects.all()
    filterset_class = CarGenerationFilter

    def get_queryset(self):
        return self.queryset.order_by('year_begin')


class CarSerieView(CarView):
    serializer_class = CarSerieSerializer
    queryset = CarSerie.objects.all()
    filterset_class = CarSerieFilter


class CarModificationView(CarView):
    serializer_class = CarModificationSerializer
    queryset = CarModification.objects.all()
    filterset_class = CarModificationFilter


class CarCharacteristicView(CarView):
    serializer_class = CarCharacteristicSerializer
    queryset = CarCharacteristic.objects.all()
    filterset_class = CarCharacteristicFilter


class CarCharacteristicValueView(CarView):
    serializer_class = CarCharacteristicValueSerializer
    queryset = CarCharacteristicValue.objects.all()
    filterset_class = CarCharacteristicValueFilter


class CarOptionView(CarView):
    serializer_class = CarOptionSerializer
    queryset = CarOption.objects.all()
    filterset_class = CarOptionFilter


class CarOptionValueView(CarView):
    serializer_class = CarOptionValueSerializer
    queryset = CarOptionValue.objects.all()
    filterset_class = CarOptionValueFilter


class CarEquipmentView(CarView):
    serializer_class = CarEquipmentSerializer
    queryset = CarEquipment.objects.all()
    filterset_class = CarEquipmentFilter


class CarViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
