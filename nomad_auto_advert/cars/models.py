from django.db import models


class CarType(models.Model):
    ext = models.PositiveIntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CarMark(models.Model):
    ext = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    car_type = models.ForeignKey(CarType, related_name='car_marks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    ext = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    car_mark = models.ForeignKey(CarMark, related_name='car_models', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CarGeneration(models.Model):
    ext = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    year_begin = models.CharField(max_length=15, blank=True)
    year_end = models.CharField(max_length=15, blank=True)

    car_model = models.ForeignKey(CarModel, related_name='car_generations', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CarSerie(models.Model):
    ext = models.PositiveIntegerField()
    name = models.CharField(max_length=50)

    car_generation = models.ForeignKey(CarGeneration, related_name='car_series', on_delete=models.CASCADE,
                                       null=True, blank=True)
    car_model = models.ForeignKey(CarModel, related_name='car_series', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CarModification(models.Model):
    ext = models.PositiveIntegerField()
    name = models.CharField(max_length=300)

    car_serie = models.ForeignKey(CarSerie, related_name='car_modifications', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CarOption(models.Model):
    ext = models.PositiveIntegerField()
    name = models.TextField()

    def __str__(self):
        return self.name


class CarOptionValue(models.Model):
    ext = models.PositiveIntegerField()

    car_option = models.ForeignKey(CarOption, related_name='car_option_values', on_delete=models.CASCADE)
    car_equipment = models.ForeignKey('CarEquipment', related_name='car_option_values', on_delete=models.CASCADE)


class CarEquipment(models.Model):
    ext = models.PositiveIntegerField()
    name = models.TextField()

    car_modification = models.ForeignKey(CarModification, related_name='car_equipments', on_delete=models.CASCADE)
    car_options = models.ManyToManyField(CarOption, blank=True, through='CarOptionValue')

    def __str__(self):
        return self.name


class CarCharacteristic(models.Model):
    ext = models.PositiveIntegerField()
    name = models.TextField()

    parent = models.ForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class CarCharacteristicValue(models.Model):
    ext = models.PositiveIntegerField()

    value = models.CharField(max_length=200)
    unit = models.CharField(max_length=200, blank=True)

    car_characteristic_ext = models.PositiveIntegerField(default=0)
    car_modification_ext = models.PositiveIntegerField(default=0)

    car_characteristic = models.ForeignKey(CarCharacteristic, related_name='car_characteristic_values',
                                           on_delete=models.CASCADE)
    car_modification = models.ForeignKey(CarModification, related_name='car_characteristic_values',
                                         on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.value} {self.unit}"


class CarColor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    car_type = models.ForeignKey('CarType', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_mark = models.ForeignKey('CarMark', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_model = models.ForeignKey('CarModel', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_generation = models.ForeignKey('CarGeneration', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_serie = models.ForeignKey('CarSerie', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_modification = models.ForeignKey('CarModification', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_equipment = models.ForeignKey('CarEquipment', related_name='cars', on_delete=models.SET_NULL, null=True)
    car_color = models.ForeignKey('CarColor', related_name='cars', on_delete=models.SET_NULL, null=True)

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

            self.save()
            return self
        print('Car info not found')
