from rest_framework import serializers
from nomad_auto_advert.filters.models import CarBodyType


class CarBodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBodyType
        fields = "__all__"
