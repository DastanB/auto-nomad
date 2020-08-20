from django_filters import rest_framework as filters


class CityFilter(filters.FilterSet):
    regions = filters.CharFilter(method='filter_by_regions')

    def filter_by_regions(self, queryset, value, *args, **kwargs):
        regions = args[0].split(',')
        return queryset.filter(region__in=regions)
