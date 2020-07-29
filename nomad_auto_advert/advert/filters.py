from django_filters import rest_framework as filters
from nomad_auto_advert.advert.models import AdvertImage, CarBodyState, Advert
from nomad_auto_advert.microservices.models import Service


class AdvertImageFilter(filters.FilterSet):
    class Meta:
        model = AdvertImage
        fields = {
            'advert': ('exact', ),
        }


class CarBodyStateFilter(filters.FilterSet):
    class Meta:
        model = CarBodyState
        fields = {
            'advert': ('exact', ),
        }


class AdvertSearchFilter(filters.FilterSet):
    mark_ext = filters.NumberFilter(method='filter_by_mark')
    model_ext = filters.NumberFilter(method='filter_by_model')
    generation_ext = filters.NumberFilter(method='filter_by_generation')
    year_begin = filters.CharFilter(method='year_begin_gte')
    year_end = filters.CharFilter(method='year_end_lte')
    price_begin = filters.CharFilter(method='price_gte')
    price_end = filters.CharFilter(method='price_lte')
    transmission = filters.CharFilter(method='filter_by_transmission_type')             # Коробка передач
    body = filters.CharFilter(method='filter_by_car_body_type')                         # Кузов
    engine = filters.CharFilter(method='filter_by_engine_type')                         # Двигатель
    engine_volume_begin = filters.CharFilter(method="engine_volume_gte")                # Объем двигателя
    engine_volume_end = filters.CharFilter(method="engine_volume_lte")                  # Объем двигателя
    drive_type = filters.CharFilter(method='drive_type_filter')                         # Привод машины
    power_begin = filters.CharFilter(method='engine_power_gte')                         # Мощность л.с.
    power_end = filters.CharFilter(method='engine_power_gte')                           # Мощность л.с.
    mileage_begin = filters.CharFilter(method='mileage_begin_gte')                      # Пробег
    mileage_end = filters.CharFilter(method='mileage_end_lte')                          # Пробег
    color = filters.NumberFilter(method="filter_by_color")
    trunk_volume_begin = filters.CharFilter(method='trunk_volume_gte')                  # обьем багажа литр
    clearance_begin = filters.CharFilter(method='road_clearance_gte')                   # клиренс мм
    acceleration_begin = filters.CharFilter(method='acceleration_gte')                  # ускорение сек
    acceleration_end = filters.CharFilter(method='acceleration_lte')                    # ускорение сек
    fuel_consumption_end = filters.CharFilter(method='fuel_consumption_lte')            # расход топдива
    rule_type = filters.CharFilter(method='steering_wheel_type')                        # руль
    max_speed_begin = filters.CharFilter(method='max_speed_gte')                        # максимальная скорость
    max_speed_end = filters.CharFilter(method='max_speed_lte')                          # максимальная скорость
    max_torque_begin = filters.CharFilter(method='max_torque_gte')                      # максимальный крутящий момент
    max_torque_end = filters.CharFilter(method='max_torque_lte')                        # максимальный крутящий момент
    image_filter = filters.BooleanFilter(method='filter_by_image')
    cleared_by_customs = filters.BooleanFilter(method="filter_cleared_by_customs")      # Растоможен
    exchange = filters.BooleanFilter(method="filter_exchange")                          # Обмен
    condition_type = filters.NumberFilter(method="filter_condition_type")               # Состояние авто

    def filter_by_mark(self, queryset, value, *args, **kwargs):
        ext = args[0]
        return queryset.filter(car__car_mark__ext=ext)

    def filter_by_model(self, queryset, value, *args, **kwargs):
        ext = args[0]
        return queryset.filter(car__car_model__ext=ext)

    def filter_by_generation(self, queryset, value, *args, **kwargs):
        ext = args[0]
        return queryset.filter(car__car_generation__ext=ext)

    def year_begin_gte(self, queryset, value, *args, **kwargs):
        year = args[0]
        if year.isdigit():
            year = int(year)
            return queryset.filter(car__year__gte=year)
        pass

    def year_end_lte(self, queryset, value, *args, **kwargs):
        year = args[0]
        if year.isdigit():
            year = int(year)
            return queryset.filter(car__year__lte=year)
        pass

    def price_gte(self, queryset, value, *args, **kwargs):
        price = args[0]
        return queryset.filter(price__gte=price)

    def price_lte(self, queryset, value, *args, **kwargs):
        price = args[0]
        return queryset.filter(price__lte=price)

    def filter_by_transmission_type(self, queryset, value, *args, **kwargs):
        transmission_type = args[0]
        return queryset.filter(car__transmission_type=transmission_type)

    def filter_by_car_body_type(self, queryset, value, *args, **kwargs):
        body = args[0]
        return queryset.filter(car__body_type=body)

    def filter_by_engine_type(self, queryset, value, *args, **kwargs):
        engine = args[0]
        return queryset.filter(car__engine_type=engine)

    def mileage_begin_gte(self, queryset, value, *args, **kwargs):
        mileage = args[0]
        return queryset.filter(car__mileage__gte=mileage)

    def mileage_end_lte(self, queryset, value, *args, **kwargs):
        mileage = args[0]
        return queryset.filter(car__mileage__lte=mileage)

    def drive_type_filter(self, queryset, value, *args, **kwargs):
        drive = args[0]
        return queryset.filter(car__drive_type=drive)

    def engine_volume_gte(self, queryset, value, *args, **kwargs):
        volume = args[0]
        return queryset.filter(car__engine_volume__gte=volume)

    def engine_volume_lte(self, queryset, value, *args, **kwargs):
        volume = args[0]
        return queryset.filter(car__engine_volume__lte=volume)

    def engine_power_gte(self, queryset, value, *args, **kwargs):
        power = args[0]
        return queryset.filter(car__engine_power__gte=power)

    def engine_power_lte(self, queryset, value, *args, **kwargs):
        power = args[0]
        return queryset.filter(car__engine_power__lte=power)

    def filter_by_color(self, queryset, value, *args, **kwargs):
        color = args[0]
        return queryset.filter(car__car_color=color)

    def trunk_volume_gte(self, queryset, value, *args, **kwargs):
        volume = args[0]
        return queryset.filter(car__trunk_volume__gte=volume)

    def road_clearance_gte(self, queryset, value, *args, **kwargs):
        clearance = args[0]
        return queryset.filter(car__road_clearance__gte=clearance)

    def acceleration_gte(self, queryset, value, *args, **kwargs):
        acceleration = args[0]
        return queryset.filter(car__acceleration__gte=acceleration)

    def acceleration_lte(self, queryset, value, *args, **kwargs):
        acceleration = args[0]
        return queryset.filter(car__acceleration__lte=acceleration)

    def fuel_consumption_lte(self, queryset, value, *args, **kwargs):
        fuel = args[0]
        return queryset.filter(car__fuel_consumption__lte=fuel)

    def steering_wheel_type(self, queryset, value, *args, **kwargs):
        wheel = args[0]
        return queryset.filter(rule_type=wheel)

    def max_speed_gte(self, queryset, value, *args, **kwargs):
        speed = args[0]
        return queryset.filter(car__max_speed__gte=speed)

    def max_speed_lte(self, queryset, value, *args, **kwargs):
        speed = args[0]
        return queryset.filter(car__max_speed__lte=speed)

    def max_torque_gte(self, queryset, value, *args, **kwargs):
        torque = args[0]
        return queryset.filter(car__max_torque__gte=torque)

    def max_torque_lte(self, queryset, value, *args, **kwargs):
        torque = args[0]
        return queryset.filter(car__max_torque__lte=torque)

    def filter_by_image(self, queryset, value, *args, **kwargs):
        image = args[0]
        if image:
            return queryset.filter(advert_images__isnull=False)
        return queryset

    def filter_cleared_by_customs(self, queryset, value, *args, **kwargs):
        state = args[0]
        return queryset.filter(cleared_by_customs=state)

    def filter_exchange(self, queryset, value, *args, **kwargs):
        state = args[0]
        return queryset.filter(exchange=state)

    def filter_condition_type(self, queryset, value, *args, **kwargs):
        type = args[0]
        return queryset.filter(car_condition_type=type)
