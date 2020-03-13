from django.contrib.auth.models import User
from nomad_auto_advert.users.models import Profile
from rest_framework import serializers


class NativeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GarageProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
