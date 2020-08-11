from django.db import models

from nomad_auto_advert.cars.constants import HEADLIGHTS_TYPES, SIGNALING_TYPES, SEAT_COUNT_TYPES, \
    INTERIOR_MATERIAL_TYPES, INTERIOR_COLOR_TYPES, SEAT_TYPES, SPARE_WHEEL_TYPES, DISC_TYPES, DISC_SIZE_TYPES, \
    AUDIO_SYSTEM_TYPES, CONDITIONER_TYPES, POWER_STEERING_TYPES, CRUISE_CONTROL_TYPES, CAMERA_TYPES
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
    ext = models.PositiveSmallIntegerField(unique=True, null=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    car_ext = models.PositiveIntegerField(unique=True, null=True)
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
    max_speed = models.FloatField(null=True, blank=True)
    max_torque = models.FloatField(null=True, blank=True)
    fuel_consumption = models.FloatField(null=True, blank=True)
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
            self.trunk_volume = p

    def set_road_clearance(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=38,
                                                       car_modification=self.car_modification)
        if values.exists():
            p = int(values.first().value)
            self.road_clearance = p

    def set_acceleration(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=33,
                                                       car_modification=self.car_modification)
        if values.exists():
            p = values.first().value
            self.acceleration = p

    def set_max_speed(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=32,
                                                       car_modification=self.car_modification)
        if values.exists():
            p = values.first().value
            self.max_speed = p

    def set_max_torque(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=16,
                                                       car_modification=self.car_modification)
        if values.exists():
            p = values.first().value
            self.max_torque = p

    def set_fuel_consumption(self):
        values = CarCharacteristicValue.objects.filter(car_characteristic__ext=52,
                                                       car_modification=self.car_modification)
        if values.exists():
            p = values.first().value
            self.fuel_consumption = p

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
            self.car_ext = data.get('car_ext')
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
            if data.get('car_equipment'):
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
            self.set_fuel_consumption()
            self.set_max_speed()
            self.set_max_torque()

            self.save()
            return self
        print('Car info not found')

    def __str__(self):
        mark = self.car_mark.name if self.car_mark else "Fake"
        model = self.car_model.name if self.car_model else "-"
        return f"{self.id}: {mark} {model}"


class MultipleOption(models.Model):
    name = models.CharField(max_length=100)
    separator_id = models.PositiveSmallIntegerField()


class Option(models.Model):
    car = models.ForeignKey('cars.Car', related_name='options', on_delete=models.CASCADE, null=True)

    headlights = models.PositiveSmallIntegerField(
        'Фары',
        choices=HEADLIGHTS_TYPES,
        null=True
    )

    electric_heating = models.ManyToManyField(
        to='cars.MultipleOption',
        related_name='electric_heating'
    )

    daytime_running_lights = models.BooleanField('Дневные ходовые огни', default=False)
    fog_lights = models.BooleanField('Противотуманные фары', default=False)
    automatic_headlight_range_control = models.BooleanField('Автоматический корректор фар', default=False)
    headlight_washer = models.BooleanField('Омыватель фар', default=False)
    adaptive_lighting_system = models.BooleanField('Система адаптивного освещения', default=False)
    high_beam_control_system = models.BooleanField('Система управления дальним светом', default=False)
    rain_sensor = models.BooleanField('Датчик дождя', default=False)
    light_sensor = models.BooleanField('Датчик света', default=False)

    signaling = models.PositiveSmallIntegerField(
        'Сигнализация',
        choices=SIGNALING_TYPES,
        null=True
    )

    central_locking = models.BooleanField('Центральный замок', default=False)
    immobilizer = models.BooleanField('Иммобилайзер', default=False)
    interior_penetration_sensor = models.BooleanField('Датчик проникновения в салон (датчик объема)', default=False)

    seat_count = models.PositiveSmallIntegerField(
        'Количество мест',
        choices=SEAT_COUNT_TYPES,
        null=True
    )

    interior_material = models.PositiveSmallIntegerField(
        'Материал салона',
        choices=INTERIOR_MATERIAL_TYPES,
        null=True
    )

    interior_color = models.PositiveSmallIntegerField(
        'Цвет салона',
        choices=INTERIOR_COLOR_TYPES,
        null=True
    )

    seat_height_adjustment = models.PositiveSmallIntegerField(
        'Регулировка сидений по высоте',
        choices=SEAT_TYPES,
        null=True
    )

    seat_electric_adjustment = models.ManyToManyField(
        to='cars.MultipleOption',
        related_name='seat_electric_adjustments'
    )

    seat_position_memory = models.PositiveSmallIntegerField(
        'Память положения сидений',
        choices=SEAT_TYPES,
        null=True
    )

    heated_seat = models.ManyToManyField(
        to='cars.MultipleOption',
        related_name='heated_seats'
    )

    seat_ventilation = models.ManyToManyField(
        to='cars.MultipleOption',
        related_name='seats_ventilation'
    )

    front_sport_seats = models.BooleanField('Спортивные передние сиденья', default=False)
    seat_with_massage = models.BooleanField('Сиденья с массажем', default=False)
    heated_steering_wheel = models.BooleanField('Обогрев рулевого колеса', default=False)
    leather_steering_wheel = models.BooleanField('Отделка кожей рулевого колеса', default=False)
    gear_lever_leather_trim = models.BooleanField('Отделка кожей рычага КПП', default=False)
    luke = models.BooleanField('Люк', default=False)
    panoramic_roof = models.BooleanField('Панорамная крыша / лобовое стекло', default=False)
    ceiling_trim_in_black_fabric = models.BooleanField('Отделка потолка чёрной тканью', default=False)
    front_center_armrest = models.BooleanField('Передний центральный подлокотник', default=False)
    third_rear_headrest = models.BooleanField('Третий задний подголовник', default=False)
    third_row_of_seats = models.BooleanField('Третий ряд сидений', default=False)
    folding_rear_seats = models.BooleanField('Складывающееся заднее сиденье', default=False)
    passenger_backrest_folding_function = models.BooleanField(
        'Функция складывания спинки сиденья пассажира',
        default=False
    )
    folding_table_on_the_backs_of_the_front_seats = models.BooleanField(
        'Складной столик на спинках передних сидений',
        default=False
    )
    tinted_glass = models.BooleanField('Тонированные стекла', default=False)
    sun_blinds_in_rear_doors = models.BooleanField('Солнцезащитные шторки в задних дверях', default=False)
    rear_window_sun_blind = models.BooleanField('Солнцезащитная шторка на заднем стекле', default=False)
    interior_lighting = models.BooleanField('Декоративная подсветка салона', default=False)
    decorative_pedals = models.BooleanField('Декоративные накладки на педали', default=False)
    door_sills = models.BooleanField('Накладки на пороги', default=False)

    suspension = models.ManyToManyField(
        to='cars.MultipleOption',
        related_name='suspensions'
    )

    spare_wheel = models.PositiveSmallIntegerField(
        'Запасное колесо',
        choices=SPARE_WHEEL_TYPES,
        null=True
    )

    towbar = models.BooleanField('Фаркоп', default=False)
    crankcase_protection = models.BooleanField('Защита картера', default=False)

    disc_type = models.PositiveSmallIntegerField(
        'Тип дисков',
        choices=DISC_TYPES,
        null=True
    )

    disc_size = models.PositiveSmallIntegerField(
        'Размер дисков',
        choices=DISC_SIZE_TYPES,
        null=True
    )

    airbrushing = models.BooleanField('Аэрография', default=False)
    decorative_moldings = models.BooleanField('Декоративные молдинги', default=False)
    roof_rails = models.BooleanField('Рейлинги на крыше', default=False)

    audio_system = models.PositiveSmallIntegerField(
        'Аудиосистема',
        choices=AUDIO_SYSTEM_TYPES,
        null=True
    )

    aux = models.BooleanField('AUX', default=False)
    bluetooth = models.BooleanField('Bluetooth', default=False)
    usb = models.BooleanField('USB', default=False)
    rear_seat_multimedia_system = models.BooleanField('Мультимедиа система для задних пассажиров', default=False)
    navigation_system = models.BooleanField('Навигационная система', default=False)
    voice_control = models.BooleanField('Голосовое управление', default=False)
    android_auto = models.BooleanField('Android Auto', default=False)
    car_play = models.BooleanField('CarPlay', default=False)
    yandex_auto = models.BooleanField('Яндекс.Авто', default=False)
    wireless_charge_for_phone = models.BooleanField('Беспроводная зарядка для смартфона', default=False)
    socket_12v = models.BooleanField('Розетка 12V', default=False)
    socket_220v = models.BooleanField('Розетка 220V', default=False)

    power_window = models.ManyToManyField(
        to='cars.MultipleOption',
        related_name='power_windows'
    )

    conditioner = models.PositiveSmallIntegerField(
        'Кондиционер',
        choices=CONDITIONER_TYPES,
        null=True
    )

    power_steering = models.PositiveSmallIntegerField(
        'Усилитель руля',
        choices=POWER_STEERING_TYPES,
        null=True
    )

    steering_wheel_adjustment = models.ManyToManyField(
        to='cars.MultipleOption',
        related_name='steering_wheel_adjustments'
    )

    cruise_control = models.PositiveSmallIntegerField(
        'Круиз-контроль',
        choices=CRUISE_CONTROL_TYPES,
    )

    parking_assistance_system = models.ManyToManyField(
        to='cars.MultipleOption',
        related_name='parking_assistance_systems'
    )

    camera = models.PositiveSmallIntegerField(
        'Камера',
        choices=CAMERA_TYPES,
        null=True
    )

    ob_board_computer = models.BooleanField('Бортовой компьютер', default=False)
    electronic_dashboard = models.BooleanField('Электронная приборная панель', default=False)
    head_up_display = models.BooleanField('Проекционный дисплей', default=False)
    keyless_access_system = models.BooleanField('Система доступа без ключа', default=False)
    start_engine_by_button = models.BooleanField('Запуск двигателя с кнопки', default=False)
    start_stop_system = models.BooleanField('Система «старт-стоп»', default=False)
    remote_engine_start = models.BooleanField('Дистанционный запуск двигателя', default=False)
    programmable_pre_heater = models.BooleanField('Программируемый предпусковой отопитель', default=False)
    electric_boot_lid = models.BooleanField('Электропривод крышки багажника', default=False)
    open_truck_without_hands = models.BooleanField('Открытие багажника без помощи рук', default=False)
    power_mirrors = models.BooleanField('Электропривод зеркал', default=False)
    electric_folding_mirrors = models.BooleanField('Электроскладывание зеркал', default=False)
    multifunctional_steering_wheel = models.BooleanField('Мультифункциональное рулевое колесо', default=False)
    paddle_shifters = models.BooleanField('Подрулевые лепестки переключения передач', default=False)
    cooled_glove_box = models.BooleanField('Охлаждаемый перчаточный ящик', default=False)
    adjustable_pedal_assembly = models.BooleanField('Регулируемый педальный узел', default=False)
    door_closer = models.BooleanField('Доводчик дверей', default=False)
    cigarette_lighter_and_ashtray = models.BooleanField('Прикуриватель и пепельница', default=False)

    airbag = models.ManyToManyField(
        to='cars.MultipleOption',
        related_name='airbags'
    )

    isofix_fastening_system = models.ManyToManyField(
        to='cars.MultipleOption',
        related_name='isofix_fastening_systems'
    )

    support_system = models.ManyToManyField(
        to='cars.MultipleOption',
        related_name='support_systems'
    )

    abs = models.BooleanField('Антиблокировочная система (ABS)', default=False)
    esp = models.BooleanField('Система стабилизации (ESP)', default=False)
    tire_pressure_sensor = models.BooleanField('Датчик давления в шинах', default=False)
    rear_door_block = models.BooleanField('Блокировка замков задних дверей', default=False)
    era_glonass = models.BooleanField('ЭРА-ГЛОНАСС', default=False)
    armored_body = models.BooleanField('Бронированный кузов', default=False)

    @classmethod
    def get_overview_fields(cls):
        single_fields = {
            'daytime_running_lights': 'Дневные ходовые огни',
            'fog_lights': 'Противотуманные фары',
            'automatic_headlight_range_control': 'Автоматический корректор фар',
            'headlight_washer': 'Омыватель фар',
            'adaptive_lighting_system': 'Система адаптивного освещения',
            'high_beam_control_system': 'Система управления дальним светом',
            'rain_sensor': 'Датчик дождя',
            'light_sensor': 'Датчик света'
        }

        choice_fields = {
            'headlights': {
                'name_ru': 'Фары',
                'fields': HEADLIGHTS_TYPES
                }
            }

        electric_heating = MultipleOption.objects.filter(separator_id=1)
        electric_heating_objects = {x.id: x.name for x in electric_heating}

        multiple_fields = {
            'electric_heating': {
                'name_ru': 'Электрообогрев',
                'fields': electric_heating_objects
            }
        }

        result = {
            'single_fields': single_fields,
            'choice_fields': choice_fields,
            'multiple_fields': multiple_fields
        }
        return result

    @classmethod
    def get_anti_theft_fields(cls):
        single_fields = {
            'central_locking': 'Центральный замок',
            'immobilizer': 'Иммобилайзер',
            'interior_penetration_sensor': 'Датчик проникновения в салон (датчик объема)',
        }
        choice_fields = {
            'signaling': {
                'name_ru': 'Сигнализация',
                'fields': SIGNALING_TYPES
            }
        }
        multiple_fields = {}

        result = {
            'single_fields': single_fields,
            'choice_fields': choice_fields,
            'multiple_fields': multiple_fields
        }
        return result

    @classmethod
    def get_salon_fields(cls):
        single_fields = {
            'front_sport_seats': 'Спортивные передние сиденья',
            'seat_with_massage': 'Сиденья с массажем',
            'heated_steering_wheel': 'Обогрев рулевого колеса',
            'leather_steering_wheel': 'Отделка кожей рулевого колеса',
            'gear_lever_leather_trim': 'Отделка кожей рычага КПП',
            'luke': 'Люк',
            'panoramic_roof': 'Панорамная крыша / лобовое стекло',
            'ceiling_trim_in_black_fabric': 'Отделка потолка чёрной тканью',
            'front_center_armrest': 'Передний центральный подлокотник',
            'third_rear_headrest': 'Третий задний подголовник',
            'third_row_of_seats': 'Третий ряд сидений',
            'folding_rear_seats': 'Складывающееся заднее сиденье',
            'passenger_backrest_folding_function': 'Функция складывания спинки сиденья пассажира',
            'folding_table_on_the_backs_of_the_front_seats': 'Складной столик на спинках передних сидений',
            'tinted_glass': 'Тонированные стекла',
            'sun_blinds_in_rear_doors': 'Солнцезащитные шторки в задних дверях',
            'rear_window_sun_blind': 'Солнцезащитная шторка на заднем стекле',
            'interior_lighting': 'Декоративная подсветка салона',
            'decorative_pedals': 'Декоративные накладки на педали',
            'door_sills': 'Накладки на пороги',
        }
        choice_fields = {
            'seat_count': {
                'name_ru': 'Количество мест',
                'fields': SEAT_COUNT_TYPES
            },
            'interior_material': {
                'name_ru': 'Материал салона',
                'fields': INTERIOR_MATERIAL_TYPES
            },
            'interior_color': {
                'name_ru': 'Цвет салона',
                'fields': INTERIOR_COLOR_TYPES
            },
            'seat_height_adjustment': {
                'name_ru': 'Регулировка сидений по высоте',
                'fields': SEAT_TYPES
            },
            'seat_position_memory': {
                'name_ru': 'Память положения сидений',
                'fields': SEAT_TYPES
            }
        }

        seat_electric_adjustment = MultipleOption.objects.filter(separator_id=2)
        seat_electric_adjustment_objects = {x.id: x.name for x in seat_electric_adjustment}
        heated_seat = MultipleOption.objects.filter(separator_id=3)
        heated_seat_objects = {x.id: x.name for x in heated_seat}
        seat_ventilation = MultipleOption.objects.filter(separator_id=4)
        seat_ventilation_objects = {x.id: x.name for x in seat_ventilation}

        multiple_fields = {
            'seat_electric_adjustment': {
                'name_ru': 'Электрорегулировка сидений',
                'fields': seat_electric_adjustment_objects
            },
            'heated_seat': {
                'name_ru': 'Подогрев сидений',
                'fields': heated_seat_objects
            },
            'seat_ventilation': {
                'name_ru': 'Вентиляция сидений',
                'fields': seat_ventilation_objects
            }
        }

        result = {
            'single_fields': single_fields,
            'choice_fields': choice_fields,
            'multiple_fields': multiple_fields
        }
        return result

    @classmethod
    def get_other_fields(cls):
        single_fields = {
            'towbar': 'Фаркоп',
            'crankcase_protection': 'Защита картера',
        }
        choice_fields = {
            'spare_wheel': {
                'name_ru': 'Запасное колесо',
                'fields': SPARE_WHEEL_TYPES
            }
        }

        suspension = MultipleOption.objects.filter(separator_id=5)
        suspension_objects = {x.id: x.name for x in suspension}

        multiple_fields = {
            'suspension': {
                'name_ru': 'Подвеска',
                'fields': suspension_objects
            }
        }

        result = {
            'single_fields': single_fields,
            'choice_fields': choice_fields,
            'multiple_fields': multiple_fields
        }
        return result

    @classmethod
    def get_exterior_elements(cls):
        single_fields = {
            'airbrushing': 'Аэрография',
            'decorative_moldings': 'Декоративные молдинги',
            'roof_rails': 'Рейлинги на крыше',
        }
        choice_fields = {
            'disc_type': {
                'name_ru': 'Тип дисков',
                'fields': DISC_TYPES
            },
            'disc_size': {
                'name_ru': 'Размер дисков',
                'fields': DISC_SIZE_TYPES
            }
        }
        multiple_fields = {}

        result = {
            'single_fields': single_fields,
            'choice_fields': choice_fields,
            'multiple_fields': multiple_fields
        }
        return result

    @classmethod
    def get_multimedia_fields(cls):
        single_fields = {
            'aux': 'AUX',
            'bluetooth': 'Bluetooth',
            'usb': 'USB',
            'rear_seat_multimedia_system': 'Мультимедиа система для задних пассажиров',
            'navigation_system': 'Навигационная система',
            'voice_control': 'Голосовое управление',
            'android_auto': 'Android Auto',
            'car_play': 'CarPlay',
            'yandex_auto': 'Яндекс.Авто',
            'wireless_charge_for_phone': 'Беспроводная зарядка для смартфона',
            'socket_12v': 'Розетка 12V',
            'socket_220v': 'Розетка 220V',
        }
        choice_fields = {
            'audio_system': {
                'name_ru': 'Аудиосистема',
                'fields': AUDIO_SYSTEM_TYPES
            }
        }
        multiple_fields = {}

        result = {
            'single_fields': single_fields,
            'choice_fields': choice_fields,
            'multiple_fields': multiple_fields
        }
        return result

    @classmethod
    def get_comfort_fields(cls):
        single_fields = {
            "ob_board_computer": "Бортовой компьютер",
            "electronic_dashboard": "Электронная приборная панель",
            "head_up_display": "Проекционный дисплей",
            "keyless_access_system": "Система доступа без ключа",
            "start_engine_by_button": "Запуск двигателя с кнопки",
            "start_stop_system": "Система «старт-стоп»",
            "remote_engine_start": "Дистанционный запуск двигателя",
            "programmable_pre_heater": "Программируемый предпусковой отопитель",
            "electric_boot_lid": "Электропривод крышки багажника",
            "open_truck_without_hands": "Открытие багажника без помощи рук",
            "power_mirrors": "Электропривод зеркал",
            "electric_folding_mirrors": "Электроскладывание зеркал",
            "multifunctional_steering_wheel": "Мультифункциональное рулевое колесо",
            "paddle_shifters": "Подрулевые лепестки переключения передач",
            "cooled_glove_box": "Охлаждаемый перчаточный ящик",
            "adjustable_pedal_assembly": "Регулируемый педальный узел",
            "door_closer": "Доводчик дверей",
            "cigarette_lighter_and_ashtray": "Прикуриватель и пепельница",
        }
        choice_fields = {
            'conditioner': {
                'name_ru': 'Кондиционер',
                'fields': CONDITIONER_TYPES
            },
            'power_steering': {
                'name_ru': 'Усилитель руля',
                'fields': POWER_STEERING_TYPES
            },
            'cruise_control': {
                'name_ru': 'Круиз-контроль',
                'fields': CRUISE_CONTROL_TYPES
            },
            'camera': {
                'name_ru': 'Камера',
                'fields': CAMERA_TYPES
            }
        }

        power_window = MultipleOption.objects.filter(separator_id=6)
        power_window_objects = {x.id: x.name for x in power_window}
        steering_wheel_adjustment = MultipleOption.objects.filter(separator_id=7)
        steering_wheel_adjustment_objects = {x.id: x.name for x in steering_wheel_adjustment}
        parking_assistance_system = MultipleOption.objects.filter(separator_id=8)
        parking_assistance_system_objects = {x.id: x.name for x in parking_assistance_system}

        multiple_fields = {
            'power_window': {
                'name_ru': 'Электростеклоподъёмники',
                'fields': power_window_objects
            },
            'steering_wheel_adjustment': {
                'name_ru': 'Регулировка руля',
                'fields': steering_wheel_adjustment_objects
            },
            'parking_assistance_system': {
                'name_ru': 'Система помощи при парковке',
                'fields': parking_assistance_system_objects
            }
        }

        result = {
            'single_fields': single_fields,
            'choice_fields': choice_fields,
            'multiple_fields': multiple_fields
        }
        return result

    @classmethod
    def get_safety_fields(cls):
        single_fields = {
            "abs": "Антиблокировочная система (ABS)",
            "esp": "Система стабилизации (ESP)",
            "tire_pressure_sensor": "Датчик давления в шинах",
            "rear_door_block": "Блокировка замков задних дверей",
            "era_glonass": "ЭРА-ГЛОНАСС",
            "armored_body": "Бронированный кузов",
        }
        choice_fields = {}

        airbag = MultipleOption.objects.filter(separator_id=9)
        airbag_objects = {x.id: x.name for x in airbag}
        isofix_fastening_system = MultipleOption.objects.filter(separator_id=10)
        isofix_fastening_system_objects = {x.id: x.name for x in isofix_fastening_system}
        support_system = MultipleOption.objects.filter(separator_id=11)
        support_system_objects = {x.id: x.name for x in support_system}

        multiple_fields = {
            'airbag': {
                'name_ru': 'Подушки безопасности',
                'fields': airbag_objects
            },
            'isofix_fastening_system': {
                'name_ru': 'Система крепления Isofix',
                'fields': isofix_fastening_system_objects
            },
            'support_system': {
                'name_ru': 'Вспомогательные системы',
                'fields': support_system_objects
            }
        }

        result = {
            'single_fields': single_fields,
            'choice_fields': choice_fields,
            'multiple_fields': multiple_fields
        }
        return result
