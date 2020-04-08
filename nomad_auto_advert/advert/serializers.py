from rest_framework import serializers
from nomad_auto_advert.advert.models import Advert, AdvertImage


class AdvertSerializer(serializers.ModelSerializer):
    car = serializers.SerializerMethodField()

    @staticmethod
    def get_car(obj):
        return obj.get_car()

    class Meta:
        model = Advert
        read_only_fields = ('user', )
        fields = ('id', 'car', 'car_condition_type', 'cleared_by_customs',
                  'city_ext', 'contact_name', 'contact_email', 'price', 'exchange',
                  'to_order', 'rule_type', 'description', ) + read_only_fields


class AdvertImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertImage
        fields = "__all__"
        extra_kwargs = {
            'advert': {'required': True}
        }
