from rest_framework import serializers
from nomad_auto_advert.cars.models import CarType, CarMark, CarModel, CarGeneration, CarSerie, CarModification, \
    CarCharacteristic, CarCharacteristicValue, CarOption, CarOptionValue, CarEquipment, Car, CarColor
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
