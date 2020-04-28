from rest_framework import generics, viewsets
from rest_framework.parsers import MultiPartParser
from django_filters import rest_framework as filters
from rest_framework.views import APIView

from nomad_auto_advert.advert.filters import AdvertImageFilter, CarBodyStateFilter, AdvertSearchFilter
from nomad_auto_advert.advert.models import Advert, AdvertImage, CarBodyState, CarBody
from nomad_auto_advert.advert.serializers import AdvertSerializer, AdvertImageSerializer, CarBodyStateSerializer, \
    CarBodySerializer, CarBodyStateReadSerializer
from nomad_auto_advert.utils.mixins import MultiSerializerViewSetMixin


class AdvertViewSet(viewsets.ModelViewSet):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class AdvertImageViewSet(viewsets.ModelViewSet):
    serializer_class = AdvertImageSerializer
    parser_classes = (MultiPartParser, )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = AdvertImageFilter

    def get_queryset(self):
        advert = self.request.query_params.get('advert')
        queryset = AdvertImage.objects.all()
        if advert:
            return queryset.filter(advert_id=advert, advert__user=self.request.user)
        return queryset.none()


class CarBodyListView(generics.ListAPIView):
    serializer_class = CarBodySerializer
    queryset = CarBody.objects.all()


class CarBodyStateViewSet(MultiSerializerViewSetMixin,
                          viewsets.ModelViewSet):
    serializer_action_classes = {
        'list': CarBodyStateReadSerializer,
        'retrieve': CarBodyStateReadSerializer,
        'create': CarBodyStateSerializer,
        'update': CarBodyStateSerializer,
        'partial_update': CarBodyStateSerializer
    }
    serializer_class = CarBodyStateSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CarBodyStateFilter

    def get_queryset(self):
        advert = self.request.query_params.get('advert')
        queryset = CarBodyState.objects.all()
        if advert:
            return queryset.filter(advert_id=advert)
        return queryset.none()


class AdvertSearchView(generics.ListAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = AdvertSearchFilter
