from rest_framework import generics, viewsets
from rest_framework.parsers import MultiPartParser
from django_filters import rest_framework as filters

from nomad_auto_advert.advert.filters import AdvertImageFilter
from nomad_auto_advert.advert.models import Advert, AdvertImage
from nomad_auto_advert.advert.serializers import AdvertSerializer, AdvertImageSerializer


class AdvertView(generics.ListCreateAPIView):
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
        queryset = AdvertImage.objects.filter(advert__user=self.request.user)
        return queryset
