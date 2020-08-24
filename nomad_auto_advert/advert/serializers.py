from rest_framework import serializers, exceptions
from nomad_auto_advert.advert.models import Advert, AdvertImage, CarBodyState, CarBody, AdvertFavourite, \
    AdvertComplaint, AdvertComment
from nomad_auto_advert.cars.models import Car
from nomad_auto_advert.cars.serializers import CarSerializer
from nomad_auto_advert.geo.serializers import CitySerializer
from nomad_auto_advert.microservices.models import Service
from nomad_auto_advert.users.serializers import ContactPhoneSerializer
from nomad_auto_advert.utils.serializers import ChoiceValueDisplayField


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


class AdvertBaseSerializer(serializers.ModelSerializer):
    contact_phones = ContactPhoneSerializer(required=False, many=True)

    class Meta:
        model = Advert
        read_only_fields = ('id', 'user', 'views_count', )
        fields = read_only_fields + \
                 ('car_ext', 'car',
                  'car_condition_type', 'cleared_by_customs', 'city',
                  'contact_name', 'contact_email', 'contact_phones', 'price',
                  'exchange', 'to_order', 'rule_type', 'description',)
        extra_kwargs = {
            'car': {'required': False}
        }

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

    def check_if_exists(self):
        if Car.objects.filter(car_ext=self.validated_data.get('car_ext')).exists():
            raise exceptions.ValidationError(detail={
                'success': False,
                'message': f"Advert with car_ext={self.validated_data.get('car_ext')} already exists"
            })

    def validate_car_fields(self):
        if not (self.validated_data.get('car_ext') or self.validated_data.get('car')):
            raise exceptions.ValidationError(detail={
                'success': False,
                'message': "[car_ext] or [car] must be given."
            })

    def create(self, validated_data):
        self.validate_car_fields()

        if validated_data.get('car_ext'):
            self.check_if_exists()

            garage = Service.objects.get(name='garage')
            response = garage.remote_call('GET', f'/api/microservices/car/{validated_data.get("car_ext")}/')

            if response.ok:
                data = response.json()
                data['car_ext'] = validated_data.get('car_ext')
                self.validate_base_buy(data)
                car = Car().create_car(data=data, user=self.context.get('request').user)
                validated_data['car'] = car
            else:
                raise exceptions.NotFound(detail={
                    'success': False,
                    'message': f"Car with id={validated_data.get('car_ext')} not found."
                })

        return super().create(validated_data)


class AdvertSerializer(AdvertBaseSerializer):
    car_condition_type = ChoiceValueDisplayField()
    rule_type = ChoiceValueDisplayField()
    car = CarSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    images = serializers.SerializerMethodField()
    in_fav = serializers.SerializerMethodField()
    contact_phones = ContactPhoneSerializer(many=True)

    def get_in_fav(self, obj: Advert):
        return getattr(obj, "in_fav")

    def get_images(self, obj: Advert):
        return AdvertImageSerializer(obj.advert_images.all(), many=True).data

    class Meta(AdvertBaseSerializer.Meta):
        fields = AdvertBaseSerializer.Meta.fields + \
                 ('images', 'in_fav', 'created_at', 'updated_at')


class AdvertUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ('id', 'car_condition_type', 'cleared_by_customs',
                  'city', 'contact_name', 'contact_email', 'contact_phones',
                  'price', 'exchange', 'to_order', 'rule_type', 'description',)


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


class AdvertFavouriteBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertFavourite
        fields = ("id", "advert")

    def create(self, validated_data):
        favourite = AdvertFavourite.objects.filter(
            advert=self.validated_data.get('advert'),
            profile=self.context.get('request').user
        ).first()

        if favourite is not None:
            return favourite
        return super().create(validated_data)


class AdvertFavouriteSerializer(AdvertFavouriteBaseSerializer):
    advert = AdvertSerializer(read_only=True)


class AdvertComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertComplaint
        fields = ('id', 'advert', 'description',
                  'is_spam', 'is_inappropriate_content', 'is_fake_information',
                  'created', 'modified')


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class AdvertCommentBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertComment
        read_only_fields = ('profile', 'created', 'modified', )
        fields = ('id', 'advert', 'parent', 'text') + read_only_fields


class AdvertCommentSerializer(AdvertCommentBaseSerializer):
    parent = AdvertCommentBaseSerializer()
    profile = serializers.SerializerMethodField()

    def get_profile(self, obj: AdvertComment):
        return obj.profile.first_name + ' ' + obj.profile.last_name


