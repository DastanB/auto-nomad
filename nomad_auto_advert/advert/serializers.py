from rest_framework import serializers, exceptions
from nomad_auto_advert.advert.models import Advert, AdvertImage, CarBodyState, CarBody
from nomad_auto_advert.cars.models import Car
from nomad_auto_advert.cars.serializers import CarSerializer
from nomad_auto_advert.microservices.models import Service
from nomad_auto_advert.utils.serializers import ChoiceValueDisplayField


class AdvertSerializer(serializers.ModelSerializer):
    car_condition_type = ChoiceValueDisplayField()
    rule_type = ChoiceValueDisplayField()
    car = serializers.SerializerMethodField(read_only=True)

    def get_car(self, obj):
        return CarSerializer(obj.car).data

    class Meta:
        model = Advert
        read_only_fields = ('user', 'car',)
        fields = ('id', 'car_ext', 'car_condition_type', 'cleared_by_customs',
                  'city_ext', 'contact_name', 'contact_email', 'price', 'exchange',
                  'to_order', 'rule_type', 'description',) + read_only_fields

    def validate_basebuy(self, data):
        if not data.get('car_type'):
            raise exceptions.ValidationError(detail='[car_type] must be given')
        if not data.get('car_mark'):
            raise exceptions.ValidationError(detail='[car_mark] must be given')
        if not data.get('car_model'):
            raise exceptions.ValidationError(detail='[car_model] must be given')
        if not data.get('car_generation'):
            raise exceptions.ValidationError(detail='[car_generation] must be given')
        if not data.get('car_serie'):
            raise exceptions.ValidationError(detail='[car_serie] must be given')
        if not data.get('car_modification'):
            raise exceptions.ValidationError(detail='[car_modification] must be given')
        if not data.get('car_color'):
            raise exceptions.ValidationError(detail='[car_color] must be given')

    def create(self, validated_data):
        garage = Service.objects.get(name='garage')
        response = garage.remote_call('GET', f'/api/microservices/car/{validated_data.get("car_ext")}/')
        if response.ok:
            data = response.json()
            self.validate_basebuy(data)
            car = Car().create_car(data=data)
            validated_data['car'] = car

        return super().create(validated_data)


class AdvertImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertImage
        fields = "__all__"
        extra_kwargs = {
            'advert': {'required': True}
        }


class CarBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBody
        fields = "__all__"


class CarBodyStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBodyState
        fields = ("id", "car_body", "advert", "description",
                  "painted", "scratched", "dent", "rust")
        extra_kwargs = {
            "car_body": {"required": True},
        }


class CarBodyStateReadSerializer(CarBodyStateSerializer):
    car_body = CarBodySerializer()
