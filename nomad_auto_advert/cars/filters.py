from django_filters import rest_framework as filters
from nomad_auto_advert.cars.models import CarModel, CarMark, CarGeneration, CarSerie, CarModification, CarEquipment, \
    CarCharacteristic, CarCharacteristicValue, CarOption, CarOptionValue


class CarMarkFilter(filters.FilterSet):
    mark_name = filters.CharFilter(method='search_by_name')

    @staticmethod
    def search_by_name(queryset, value, *args, **kwargs):
        mark = args[0]
        return queryset.filter(name__istartswith=mark)


class CarModelFilter(filters.FilterSet):
    model_name = filters.CharFilter(method='search_by_name')
    mark_id = filters.NumberFilter(method='search_by_mark_id')

    @staticmethod
    def search_by_name(queryset, value, *args, **kwargs):
        model = args[0]
        return queryset.filter(name__istartswith=model)

    @staticmethod
    def search_by_mark_id(queryset, value, *args, **kwargs):
        mark_id = args[0]
        return queryset.filter(car_mark_id=mark_id)


class CarGenerationFilter(filters.FilterSet):
    generation_name = filters.CharFilter(method='search_by_name')
    model_id = filters.NumberFilter(method='search_by_model_id')
    year_begin = filters.CharFilter(method='year_begin_gte')
    year_end = filters.CharFilter(method='year_end_lte')

    @staticmethod
    def search_by_name(queryset, value, *args, **kwargs):
        generation = args[0]
        return queryset.filter(name__icontains=generation)

    @staticmethod
    def search_by_model_id(queryset, value, *args, **kwargs):
        model_id = args[0]
        return queryset.filter(car_model_id=model_id)

    @staticmethod
    def year_begin_gte(queryset, value, *args, **kwargs):
        year = args[0]
        if year.isdigit():
            year = int(year)
            return queryset.filter(year_end__gte=year)
        pass

    @staticmethod
    def year_end_lte(queryset, value, *args, **kwargs):
        year = args[0]
        if year.isdigit():
            year = int(year)
            return queryset.filter(year_begin__lte=year)
        pass


class CarSerieFilter(filters.FilterSet):
    serie_name = filters.CharFilter(method='search_by_name')
    model_id = filters.NumberFilter(method='search_by_model_id')
    generation_id = filters.NumberFilter(method='search_by_generation_id')

    @staticmethod
    def search_by_name(queryset, value, *args, **kwargs):
        serie = args[0]
        return queryset.filter(name__icontains=serie)

    @staticmethod
    def search_by_model_id(queryset, value, *args, **kwargs):
        model_id = args[0]
        return queryset.filter(car_model_id=model_id)

    @staticmethod
    def search_by_generation_id(queryset, value, *args, **kwargs):
        generation_id = args[0]
        return queryset.filter(car_generation_id=generation_id)


class CarModificationFilter(filters.FilterSet):
    modification_name = filters.CharFilter(method='search_by_name')
    serie_id = filters.NumberFilter(method='search_by_serie_id')

    @staticmethod
    def search_by_name(queryset, value, *args, **kwargs):
        modification = args[0]
        return queryset.filter(name__icontains=modification)

    @staticmethod
    def search_by_serie_id(queryset, value, *args, **kwargs):
        serie_id = args[0]
        return queryset.filter(car_serie_id=serie_id)


class CarCharacteristicFilter(filters.FilterSet):
    class Meta:
        model = CarCharacteristic
        fields = {
            'name': ('contains', )
        }


class CarCharacteristicValueFilter(filters.FilterSet):
    class Meta:
        model = CarCharacteristicValue
        fields = {
            'car_characteristic_id': ('exact', ),
            'car_modification': ('exact', ),
        }


class CarEquipmentFilter(filters.FilterSet):
    class Meta:
        model = CarEquipment
        fields = {
            'car_modification_id': ('exact', ),
        }


class CarOptionFilter(filters.FilterSet):
    class Meta:
        model = CarOption
        fields = {
            'name': ('exact', ),
        }


class CarOptionValueFilter(filters.FilterSet):
    class Meta:
        model = CarOptionValue
        fields = {
            'car_option_id': ('exact', ),
            'car_equipment_id': ('exact', ),
        }
