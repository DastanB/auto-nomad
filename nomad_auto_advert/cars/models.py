from django.db import models

from nomad_auto_advert.filters.models import CarBodyType, CarTransmissionType, CarDriveType, CarEngineType


class CarType(models.Model):
    ext = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CarMark(models.Model):
    ext = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    car_type = models.ForeignKey('CarType', related_name='car_marks', on_delete=models.CASCADE, null=True, blank=True)
    car_type_ext = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    ext = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    car_mark = models.ForeignKey('CarMark', related_name='car_models', on_delete=models.CASCADE,
                                 null=True, blank=True)
    car_mark_ext = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class CarGeneration(models.Model):
    ext = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    year_begin = models.CharField(max_length=15, blank=True)
    year_end = models.CharField(max_length=15, blank=True)

    car_model = models.ForeignKey('CarModel', related_name='car_generations', on_delete=models.CASCADE,
                                  null=True, blank=True)
    car_model_ext = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class CarSerie(models.Model):
    ext = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)

    car_generation = models.ForeignKey('CarGeneration', related_name='car_series', on_delete=models.CASCADE,
                                       null=True, blank=True)
    car_generation_ext = models.PositiveIntegerField(null=True, blank=True)
    car_model = models.ForeignKey('CarModel', related_name='car_series', on_delete=models.CASCADE,
                                  null=True, blank=True)
    car_model_ext = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class CarModification(models.Model):
    ext = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=300)

    car_serie = models.ForeignKey('CarSerie', related_name='car_modifications', on_delete=models.CASCADE,
                                  null=True, blank=True)
    car_serie_ext = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class CarOption(models.Model):
    ext = models.PositiveIntegerField(unique=True)
    name = models.TextField()

    parent = models.ForeignKey('self', related_name='children', on_delete=models.SET_NULL,
                               null=True, blank=True)
    parent_ext = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class CarOptionValue(models.Model):
    ext = models.PositiveIntegerField(unique=True)

    car_option = models.ForeignKey('CarOption', related_name='car_option_values', on_delete=models.CASCADE,
                                   null=True, blank=True)
    car_option_ext = models.PositiveIntegerField(null=True, blank=True)
    car_equipment = models.ForeignKey('CarEquipment', related_name='car_option_values', on_delete=models.CASCADE,
                                      null=True, blank=True)
    car_equipment_ext = models.PositiveIntegerField(null=True, blank=True)


class CarEquipment(models.Model):
    ext = models.PositiveIntegerField(unique=True)
    name = models.TextField()

    car_modification = models.ForeignKey(CarModification, related_name='car_equipments', on_delete=models.CASCADE,
                                         null=True, blank=True)
    car_modification_ext = models.PositiveIntegerField(null=True, blank=True)
    car_options = models.ManyToManyField('CarOption', blank=True, through='CarOptionValue')

    def __str__(self):
        return self.name


class CarCharacteristic(models.Model):
    ext = models.PositiveIntegerField(unique=True)
    name = models.TextField()

    parent = models.ForeignKey('self', related_name='children', on_delete=models.SET_NULL,
                               null=True, blank=True)
    parent_ext = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class CarCharacteristicValue(models.Model):
    ext = models.PositiveIntegerField(unique=True)

    value = models.CharField(max_length=200)
    unit = models.CharField(max_length=200, blank=True)

    car_characteristic = models.ForeignKey(CarCharacteristic, related_name='car_characteristic_values',
                                           on_delete=models.CASCADE, null=True, blank=True)
    car_characteristic_ext = models.PositiveIntegerField(null=True, blank=True)
    car_modification = models.ForeignKey(CarModification, related_name='car_characteristic_values',
                                         on_delete=models.CASCADE, null=True, blank=True)
    car_modification_ext = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.value} {self.unit}"


class CarColor(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


'''
Car Model
'''


class Car(models.Model):
    car_type = models.ForeignKey('CarType', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_mark = models.ForeignKey('CarMark', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_model = models.ForeignKey('CarModel', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_generation = models.ForeignKey('CarGeneration', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_serie = models.ForeignKey('CarSerie', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_modification = models.ForeignKey('CarModification', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_equipment = models.ForeignKey('CarEquipment', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_color = models.ForeignKey('CarColor', related_name='cars', on_delete=models.SET_NULL, null=True)

    body_type = models.ForeignKey('filters.CarBodyType', related_name='body_types',
                                  on_delete=models.SET_NULL, null=True)
    transmission_type = models.ForeignKey('filters.CarTransmissionType', related_name='transmission_types',
                                          on_delete=models.SET_NULL, null=True)
    drive_type = models.ForeignKey('filters.CarDriveType', related_name='drive_types',
                                   on_delete=models.SET_NULL, null=True)
    engine_type = models.ForeignKey('filters.CarEngineType', related_name='engine_types',
                                    on_delete=models.SET_NULL, null=True)
    engine_volume = models.FloatField(null=True, blank=True)
    engine_power = models.PositiveIntegerField(null=True, blank=True)
    trunk_volume = models.PositiveIntegerField(null=True, blank=True)
    road_clearance = models.PositiveIntegerField(null=True, blank=True)
    acceleration = models.FloatField(null=True, blank=True)
    mileage = models.PositiveIntegerField(null=True)
    year = models.PositiveIntegerField(null=True)

    def set_body_type(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=2,
                                                       car_modification=self.car_modification)
        if values.exists():
            b = CarBodyType.objects.filter(name__iexact=values.first().value)
            if b.exists():
                self.body_type = b.first()

    def set_engine_volume(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=13,
                                                       car_modification=self.car_modification)
        if values.exists():
            v = round(float(values.first().value)/1000, 1)
            self.engine_volume = v

    def set_engine_power(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=14,
                                                       car_modification=self.car_modification)
        if values.exists():
            p = int(values.first().value)
            self.engine_power = p

    def set_trunk_volume(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=44,
                                                       car_modification=self.car_modification)
        if values.exists():
            p = int(values.first().value)
            print(p)
            self.trunk_volume = p

    def set_road_clearance(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=38,
                                                       car_modification=self.car_modification)
        if values.exists():
            p = int(values.first().value)
            print(p)
            self.road_clearance = p

    def set_acceleration(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=33,
                                                       car_modification=self.car_modification)
        if values.exists():
            p = values.first().value
            print(p)
            self.acceleration = p

    def set_transmission_type(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=24,
                                                       car_modification=self.car_modification)
        if values.exists():
            b = CarTransmissionType.objects.filter(name__iexact=values.first().value)
            if b.exists():
                self.transmission_type = b.first()

    def set_drive_type(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=27,
                                                       car_modification=self.car_modification)
        if values.exists():
            b = CarDriveType.objects.filter(name__iexact=values.first().value)
            if b.exists():
                self.drive_type = b.first()

    def set_engine_type(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=12,
                                                       car_modification=self.car_modification)
        if values.exists():
            b = CarEngineType.objects.filter(name__iexact=values.first().value)
            if b.exists():
                self.engine_type = b.first()

    def create_car(self, data):
        if data:
            car_type = CarType.objects.filter(ext=data.get('car_type').get('ext'))
            if car_type.exists():
                self.car_type = car_type.first()
            car_mark = CarMark.objects.filter(ext=data.get('car_mark').get('ext'))
            if car_mark.exists():
                self.car_mark = car_mark.first()
            car_model = CarModel.objects.filter(ext=data.get('car_model').get('ext'))
            if car_model.exists():
                self.car_model = car_model.first()
            car_generation = CarGeneration.objects.filter(ext=data.get('car_generation').get('ext'))
            if car_generation.exists():
                self.car_generation = car_generation.first()
            car_serie = CarSerie.objects.filter(ext=data.get('car_serie').get('ext'))
            if car_serie.exists():
                self.car_serie = car_serie.first()
            car_modification = CarModification.objects.filter(ext=data.get('car_modification').get('ext'))
            if car_modification.exists():
                self.car_modification = car_modification.first()
            car_equipment = CarEquipment.objects.filter(ext=data.get('car_equipment').get('ext'))
            if car_equipment.exists():
                self.car_equipment = car_equipment.first()
            car_color = CarColor.objects.filter(name__icontains=data.get('car_color').get('name'))
            if car_color.exists():
                self.car_color = car_color.first()
            self.mileage = data.get('mileage')
            self.year = data.get("age")
            self.set_body_type()
            self.set_engine_volume()
            self.set_engine_power()
            self.set_transmission_type()
            self.set_drive_type()
            self.set_engine_type()
            self.set_trunk_volume()
            self.set_road_clearance()
            self.set_acceleration()

            self.save()
            return self
        print('Car info not found')

    def __str__(self):
        return f"{self.id}: {self.car_mark.name} {self.car_model.name}"
