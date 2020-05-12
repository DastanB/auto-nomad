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
    engine_volume_begin = filters.CharFilter()  # Объем двигателя
    engine_volume_end = filters.CharFilter()  # Объем двигателя
    drive_type = filters.CharFilter(method='drive_type_filter')  # Привод машины
    power = filters.CharFilter()  # Мощность л.с.
    mileage_begin = filters.CharFilter(method='mileage_begin_gte')  # Пробег
    mileage_end = filters.CharFilter(method='mileage_end_lte')  # Пробег

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
            return queryset.filter(car__car_generation__year_begin__gte=year)
        pass

    @staticmethod
    def year_end_lte(queryset, value, *args, **kwargs):
        year = args[0]
        if year.isdigit():
            year = int(year)
            return queryset.filter(car__car_generation__year_end__lte=year)
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
        return queryset.filter(car__car_modification__car_characteristic_values__transmission_type=transmission_type)

    @staticmethod
    def filter_by_car_body_type(queryset, value, *args, **kwargs):
        body = args[0]
        return queryset.filter(car__car_modification__car_characteristic_values__body_type=body)

    @staticmethod
    def filter_by_engine_type(queryset, value, *args, **kwargs):
        engine = args[0]
        return queryset.filter(car__car_modification__car_characteristic_values__engine_type=engine)

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
        return queryset.filter(car__car_modification__car_characteristic_values__drive_type=drive)

