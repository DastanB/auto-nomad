from django.contrib.auth.models import User
from nomad_auto_advert.users.models import Profile, ContactPhone
from rest_framework import serializers


class NativeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GarageProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ContactPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPhone
        read_only_fields = ('profile', )
        fields = ('id', 'phone', ) + read_only_fields

    def create(self, validated_data):
        phone = ContactPhone.objects.filter(
            phone=validated_data.get('phone'),
            profile=self.context.get('request').user
        ).first()
        if phone is not None:
            return phone
        return super().create(validated_data)
