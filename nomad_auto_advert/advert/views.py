from rest_framework import generics
from nomad_auto_advert.advert.models import Color
from nomad_auto_advert.advert.serializers import ColorSerializer


class ColorListView(generics.ListAPIView):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
