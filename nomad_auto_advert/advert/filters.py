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
    price_begin = filters.CharFilter()
    price_end = filters.CharFilter()
    transmission = filters.CharFilter()  # Коробка передач
    body = filters.CharFilter()  # Кузов
    engine = filters.CharFilter()  # Двигатель
    engine_volume_begin = filters.CharFilter()  # Объем двигателя
    engine_volume_end = filters.CharFilter()  # Объем двигателя
    drive_type = filters.CharFilter()  # Привод машины
    power = filters.CharFilter()  # Мощность л.с.
    mileage_begin = filters.CharFilter()  # Пробег
    mileage_end = filters.CharFilter()  # Пробег

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

    # @staticmethod
