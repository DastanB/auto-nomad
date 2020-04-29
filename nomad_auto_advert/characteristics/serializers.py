from rest_framework import serializers
from nomad_auto_advert.characteristics.models import TransmissionType, CarBodyType, EngineType


class TransmissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmissionType
        fields = "__all__"


class CarBodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBodyType
        fields = "__all__"


class EngineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineType
        fields = "__all__"
