from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from nomad_auto_advert.filters.models import CarBodyType
from nomad_auto_advert.filters.serializers import CarBodyTypeSerializer


class CarBodyTypeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CarBodyTypeSerializer
    permission_classes = (AllowAny, )
    queryset = CarBodyType.objects.all()
