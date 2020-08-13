from rest_framework import generics, viewsets, exceptions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from nomad_auto_advert.advert.utils import make_car_custom_options_json
from nomad_auto_advert.cars.filters import CarMarkFilter, CarModelFilter, CarGenerationFilter, CarSerieFilter, \
    CarModificationFilter, CarCharacteristicFilter, CarCharacteristicValueFilter, CarOptionValueFilter, CarOptionFilter, \
    CarEquipmentFilter
from nomad_auto_advert.cars.models import CarType, CarMark, CarModel, CarGeneration, CarSerie, CarModification, \
    CarCharacteristic, CarCharacteristicValue, CarOption, CarOptionValue, CarEquipment, Car, CarColor, MultipleOption, \
    Option
from nomad_auto_advert.cars.serializers import CarTypeSerializer, CarMarkSerializer, CarModelSerializer, \
    CarGenerationSerializer, CarSerieSerializer, CarModificationSerializer, CarCharacteristicSerializer, \
    CarCharacteristicValueSerializer, CarOptionSerializer, CarOptionValueSerializer, CarEquipmentSerializer, \
    CarSerializer, CarDetailSerializer, CarColorSerializer, MultipleOptionSerializer, OptionSerializer, \
    CarCreateSerializer
from django_filters import rest_framework as filters


class CarView(generics.ListAPIView):
    permission_classes = (AllowAny, )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = None


class CarColorView(CarView):
    serializer_class = CarColorSerializer
    queryset = CarColor.objects.all()


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

    def get_queryset(self):
        queryset = Car.objects.all().order_by('id')
        return queryset

class CarDetailView(generics.RetrieveAPIView):
    serializer_class = CarDetailSerializer

    def get_object(self):
        car = Car.objects.filter(id=self.kwargs.get('id'))
        if car.exists():
            return car.first()
        raise exceptions.NotFound('Car with given id not found')


class MyCarsViewSet(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.filter(profile=self.request.user)


class MultipleOptionView(generics.ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = MultipleOptionSerializer
    queryset = MultipleOption.objects.all()


class CustomOptionViewSet(viewsets.ModelViewSet):
    serializer_class = OptionSerializer
    queryset = Option.objects.all()

    def get_queryset(self):
        return Option.objects.filter(car__profile=self.request.user)


class CustomOptionListView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        result = {
            'Обзор': Option.get_overview_fields(),
            'Защита от угона': Option.get_anti_theft_fields(),
            'Салон': Option.get_salon_fields(),
            'Прочее': Option.get_other_fields(),
            'Элементы экстерьера': Option.get_exterior_elements(),
            'Мультимедиа': Option.get_multimedia_fields(),
            'Комфорт': Option.get_comfort_fields(),
            'Безопасность': Option.get_safety_fields()
        }
        return Response(result)


class CarCustomOptionsView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        options = Option.objects.filter(car=self.kwargs.get('car_id')).first()
        if options is not None:
            result = make_car_custom_options_json(options)
            return Response(result)
        return Response({'message': 'not found.'}, status=status.HTTP_404_NOT_FOUND)


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarCreateSerializer
