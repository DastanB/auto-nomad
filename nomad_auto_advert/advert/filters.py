from django_filters import rest_framework as filters
from nomad_auto_advert.advert.models import AdvertImage, CarBodyState
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
    transmission = filters.CharFilter(method='filter_by_transmission_type')  # Коробка передач
    body = filters.CharFilter(method='filter_by_car_body_type')  # Кузов
    engine = filters.CharFilter(method='filter_by_engine_type')  # Двигатель
    engine_volume_begin = filters.CharFilter(method="engine_volume_gte")  # Объем двигателя
    engine_volume_end = filters.CharFilter(method="engine_volume_lte")  # Объем двигателя
    drive_type = filters.CharFilter(method='drive_type_filter')  # Привод машины
    power_begin = filters.CharFilter(method='engine_power_gte')  # Мощность л.с.
    power_end = filters.CharFilter(method='engine_power_gte')  # Мощность л.с.
    mileage_begin = filters.CharFilter(method='mileage_begin_gte')  # Пробег
    mileage_end = filters.CharFilter(method='mileage_end_lte')  # Пробег
    color = filters.NumberFilter(method="filter_by_color")

    @staticmethod
    def filter_by_mark(queryset, value, *args, **kwargs):
        ext = args[0]
        return queryset.filter(car__car_mark__ext=ext)

    @staticmethod
    def filter_by_model(queryset, value, *args, **kwargs):
        ext = args[0]
        return queryset.filter(car__car_model__ext=ext)

    @staticmethod
    def filter_by_generation(queryset, value, *args, **kwargs):
        ext = args[0]
        return queryset.filter(car__car_generation__ext=ext)

    @staticmethod
    def year_begin_gte(queryset, value, *args, **kwargs):
        year = args[0]
        if year.isdigit():
            year = int(year)
            return queryset.filter(car__year__gte=year)
        pass

    @staticmethod
    def year_end_lte(queryset, value, *args, **kwargs):
        year = args[0]
        if year.isdigit():
            year = int(year)
            return queryset.filter(car__year__lte=year)
        pass

    @staticmethod
    def price_gte(queryset, value, *args, **kwargs):
        price = args[0]
        return queryset.filter(price__gte=price)

    @staticmethod
    def price_lte(queryset, value, *args, **kwargs):
        price = args[0]
        return queryset.filter(price__lte=price)

    @staticmethod
    def filter_by_transmission_type(queryset, value, *args, **kwargs):
        transmission_type = args[0]
        return queryset.filter(car__car_modification__car_characteristic_values__car_characteristic__type=transmission_type)

    @staticmethod
    def filter_by_car_body_type(queryset, value, *args, **kwargs):
        body = args[0]
        return queryset.filter(car__body_type=body)

    @staticmethod
    def filter_by_engine_type(queryset, value, *args, **kwargs):
        engine = args[0]
        return queryset.filter(car__car_modification__car_characteristic_values__car_characteristic__type=engine)

    @staticmethod
    def mileage_begin_gte(queryset, value, *args, **kwargs):
        mileage = args[0]
        return queryset.filter(car__mileage__gte=mileage)

    @staticmethod
    def mileage_end_lte(queryset, value, *args, **kwargs):
        mileage = args[0]
        return queryset.filter(car__mileage__lte=mileage)

    @staticmethod
    def drive_type_filter(queryset, value, *args, **kwargs):
        drive = args[0]
        return queryset.filter(car__car_modification__car_characteristic_values__car_characteristic__type=drive)

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
