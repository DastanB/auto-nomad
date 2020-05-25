from rest_framework import serializers
from nomad_auto_advert.filters.models import CarBodyType, CarTransmissionType, CarDriveType, CarEngineType


class CarBodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBodyType
        fields = "__all__"


class CarTransmissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTransmissionType
        fields = "__all__"


class CarDriveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDriveType
        fields = "__all__"


class CarEngineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarEngineType
        fields = "__all__"
