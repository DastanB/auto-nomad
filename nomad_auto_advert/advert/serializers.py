from rest_framework import serializers, exceptions
from nomad_auto_advert.advert.models import Advert, AdvertImage, CarBodyState, CarBody
from nomad_auto_advert.cars.models import Car
from nomad_auto_advert.cars.serializers import CarSerializer
from nomad_auto_advert.geo.serializers import CitySerializer
from nomad_auto_advert.microservices.models import Service
from nomad_auto_advert.utils.serializers import ChoiceValueDisplayField


class AdvertSerializer(serializers.ModelSerializer):
    car_condition_type = ChoiceValueDisplayField()
    rule_type = ChoiceValueDisplayField()
    car = CarSerializer(read_only=True)
    city = CitySerializer(read_only=True)

    class Meta:
        model = Advert
        read_only_fields = ('user', 'car',)
        fields = ('id', 'car_ext', 'car_condition_type', 'cleared_by_customs',
                  'city', 'contact_name', 'contact_email', 'price', 'exchange',
                  'to_order', 'rule_type', 'description',) + read_only_fields

    @staticmethod
    def generate_exception_for_base_buy(name: str):
        raise exceptions.ValidationError(detail={
            'success': False,
            'message': f'[{name}] must be given',
            'description': f'Set [{name}] in Garage Project'
        })

    def validate_base_buy(self, data):
        if not data.get('car_type'):
            self.generate_exception_for_base_buy(name='car_type')
        if not data.get('car_mark'):
            self.generate_exception_for_base_buy(name='car_mark')
        if not data.get('car_model'):
            self.generate_exception_for_base_buy(name='car_model')
        if not data.get('car_generation'):
            self.generate_exception_for_base_buy(name='car_generation')
        if not data.get('car_serie'):
            self.generate_exception_for_base_buy(name='car_serie')
        if not data.get('car_modification'):
            self.generate_exception_for_base_buy(name='car_modification')
        if not data.get('car_color'):
            self.generate_exception_for_base_buy(name='car_color')

    def create(self, validated_data):
        garage = Service.objects.get(name='garage')
        response = garage.remote_call('GET', f'/api/microservices/car/{validated_data.get("car_ext")}/')
        if response.ok:
            data = response.json()
            data['car_ext'] = validated_data.get('car_ext')
            self.validate_base_buy(data)
            car = Car().create_car(data=data)
            validated_data['car'] = car
        else:
            raise exceptions.NotFound(detail={
                'success': False,
                'message': f"Car with id={validated_data.get('car_ext')} not found."
            })

        return super().create(validated_data)


class AdvertUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ('id', 'car_condition_type', 'cleared_by_customs',
                  'city', 'contact_name', 'contact_email', 'price', 'exchange',
                  'to_order', 'rule_type', 'description',)


class AdvertImageSerializer(serializers.ModelSerializer):
    image_thumbnail = serializers.SerializerMethodField(read_only=True)

    def get_image_thumbnail(self, obj: AdvertImage):
        try:
            return obj.image_thumbnail.url
        except:
            return

    class Meta:
        model = AdvertImage
        fields = ('id', 'advert', 'image', 'image_thumbnail',)


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
