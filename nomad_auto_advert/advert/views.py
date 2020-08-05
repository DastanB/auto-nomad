from drf_yasg.utils import swagger_auto_schema
from django_filters import rest_framework as filters

from rest_framework import generics, viewsets, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from nomad_auto_advert.advert.const import ADVERT_CREATE_DESCRIPTION
from nomad_auto_advert.advert.filters import AdvertImageFilter, CarBodyStateFilter, AdvertSearchFilter
from nomad_auto_advert.advert.models import Advert, AdvertImage, CarBodyState, CarBody, AdvertFavourite, AdvertComplaint
from nomad_auto_advert.advert.serializers import AdvertSerializer, AdvertImageSerializer, CarBodyStateSerializer, \
    CarBodySerializer, CarBodyStateReadSerializer, AdvertUpdateSerializer, AdvertBaseSerializer, \
    AdvertFavouriteBaseSerializer, AdvertFavouriteSerializer, AdvertComplaintSerializer
from nomad_auto_advert.utils.mixins import MultiSerializerViewSetMixin


class AdvertViewSet(MultiSerializerViewSetMixin,
                    viewsets.ModelViewSet):
    serializer_class = AdvertSerializer
    serializer_action_classes = {
        'list': AdvertSerializer,
        'retrieve': AdvertSerializer,
        'create': AdvertBaseSerializer,
        'update': AdvertUpdateSerializer,
        'partial_update': AdvertUpdateSerializer
    }
    queryset = Advert.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @swagger_auto_schema(operation_description=ADVERT_CREATE_DESCRIPTION)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class AdvertImageViewSet(MultiSerializerViewSetMixin,
                         viewsets.ModelViewSet):
    serializer_class = AdvertImageSerializer
    parser_classes = (MultiPartParser, )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = AdvertImageFilter

    def get_queryset(self):
        queryset = AdvertImage.objects.filter(advert__user=self.request.user)
        return queryset


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
        queryset = CarBodyState.objects.filter(advert__user=self.request.user)
        return queryset


class AdvertSearchView(viewsets.ReadOnlyModelViewSet):
    serializer_class = AdvertSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = AdvertSearchFilter

    def get_queryset(self):
        return Advert.objects.all().select_related(
            'car',
            'car__body_type',
            'car__drive_type',
            'car__transmission_type',
            'car__engine_type'
        )

    def get_object(self):
        obj = super(AdvertSearchView, self).get_object()
        obj.increment_views_count()
        return obj


class AdvertFavouriteView(MultiSerializerViewSetMixin,
                          generics.CreateAPIView,
                          generics.ListAPIView,
                          generics.RetrieveAPIView,
                          generics.DestroyAPIView,
                          viewsets.GenericViewSet):
    serializer_action_classes = {
        'create': AdvertFavouriteBaseSerializer,
        'list': AdvertFavouriteSerializer,
        'retrieve': AdvertFavouriteSerializer
    }

    def get_queryset(self):
        return AdvertFavourite.objects.filter(profile=self.request.user)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'success'}, status=status.HTTP_200_OK)


class AdvertComplaintViewSet(MultiSerializerViewSetMixin,
                             generics.CreateAPIView,
                             generics.ListAPIView,
                             generics.RetrieveAPIView,
                             viewsets.GenericViewSet):
    serializer_class = AdvertComplaintSerializer

    def get_queryset(self):
        return AdvertComplaint.objects.filter(profile=self.request.user)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user)
