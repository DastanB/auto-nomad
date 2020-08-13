from rest_framework import serializers
from nomad_auto_advert.cars.models import CarType, CarMark, CarModel, CarGeneration, CarSerie, CarModification, \
    CarCharacteristic, CarCharacteristicValue, CarOption, CarOptionValue, CarEquipment, Car, CarColor, MultipleOption, \
    Option
from nomad_auto_advert.filters.serializers import CarBodyTypeSerializer, CarTransmissionTypeSerializer, \
    CarDriveTypeSerializer, CarEngineTypeSerializer


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = '__all__'


class CarMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMark
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarGenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarGeneration
        fields = '__all__'


class CarSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSerie
        fields = '__all__'


class CarModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModification
        fields = '__all__'


class CarCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCharacteristic
        fields = "__all__"


class CarCharacteristicValueSerializer(serializers.ModelSerializer):
    car_characteristic = CarCharacteristicSerializer()

    class Meta:
        model = CarCharacteristicValue
        fields = "__all__"


class CarOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOption
        fields = "__all__"


class CarOptionValueSerializer(serializers.ModelSerializer):
    car_option = CarOptionSerializer()

    class Meta:
        model = CarOptionValue
        fields = "__all__"


class CarEquipmentSerializer(serializers.ModelSerializer):
    car_options = CarOptionSerializer(many=True)

    class Meta:
        model = CarEquipment
        fields = ("id", "ext", "name", "car_modification", "car_options")


class CarColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarColor
        fields = "__all__"


class CarBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarSerializer(CarBaseSerializer):
    car_type = CarTypeSerializer()
    car_mark = CarMarkSerializer()
    car_model = CarModelSerializer()
    car_generation = CarGenerationSerializer()
    car_serie = CarSerieSerializer()
    car_modification = CarModificationSerializer()
    car_color = CarColorSerializer()
    body_type = CarBodyTypeSerializer()
    transmission_type = CarTransmissionTypeSerializer()
    drive_type = CarDriveTypeSerializer()
    engine_type = CarEngineTypeSerializer()


class CarDetailSerializer(CarSerializer):
    car_equipment = CarEquipmentSerializer()
    car_characteristics = serializers.SerializerMethodField()

    def get_car_characteristics(self, obj):
        if not obj.car_modification:
            return
        modification_id = obj.car_modification.id
        car_characteristics = CarCharacteristicValue.objects.filter(car_modification_id=modification_id)
        return CarCharacteristicValueSerializer(car_characteristics, many=True).data


class CarUpdateSerializer(CarBaseSerializer):
    def update(self, instance, validated_data):
        if validated_data.get('car_color'):
            validated_data['car_color'] = CarColor.objects.get(ext=validated_data.get('car_color'))
        print(validated_data)
        return super(CarUpdateSerializer, self).update(instance, validated_data)


class MultipleOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleOption
        fields = "__all__"


class OptionSerializer(serializers.ModelSerializer):
    electric_heating = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MultipleOption.objects.filter(separator_id=1)
    )
    seat_electric_adjustment = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MultipleOption.objects.filter(separator_id=2)
    )
    heated_seat = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MultipleOption.objects.filter(separator_id=3)
    )
    seat_ventilation = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MultipleOption.objects.filter(separator_id=4)
    )
    suspension = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MultipleOption.objects.filter(separator_id=5)
    )
    power_window = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MultipleOption.objects.filter(separator_id=6)
    )
    steering_wheel_adjustment = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MultipleOption.objects.filter(separator_id=7)
    )
    parking_assistance_system = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MultipleOption.objects.filter(separator_id=8)
    )
    airbag = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MultipleOption.objects.filter(separator_id=9)
    )
    isofix_fastening_system = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MultipleOption.objects.filter(separator_id=10)
    )
    support_system = serializers.PrimaryKeyRelatedField(
        many=True, queryset=MultipleOption.objects.filter(separator_id=11)
    )

    class Meta:
        model = Option
        fields = "__all__"


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'car_type', 'car_mark', 'car_model',
                  'car_generation', 'car_serie', 'car_modification',
                  'car_equipment', 'car_color', 'mileage', 'year')

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.set_all_characteristics()
        instance.save()
        return instance
