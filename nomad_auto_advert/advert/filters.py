from django_filters import rest_framework as filters
from nomad_auto_advert.advert.models import AdvertImage


class AdvertImageFilter(filters.FilterSet):
    class Meta:
        model = AdvertImage
        fields = {
            'advert': ('exact', ),
        }
