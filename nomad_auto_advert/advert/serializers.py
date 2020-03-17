from rest_framework import serializers
from nomad_auto_advert.advert.models import Color


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name', )



