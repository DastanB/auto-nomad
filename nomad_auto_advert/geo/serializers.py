from rest_framework import serializers

from nomad_auto_advert.geo.models import Country, Region, City


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):

    region = RegionSerializer(read_only=True)

    class Meta:
        model = City
        fields = "__all__"
