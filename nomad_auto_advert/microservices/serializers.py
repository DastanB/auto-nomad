from rest_framework import serializers

from nomad_auto_advert.microservices.models import Service


class MicroServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
