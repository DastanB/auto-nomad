from rest_framework import serializers

from nomad_auto_advert.geo.models import Country, Region, City


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = "__all__"


class CityBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = "__all__"


class RegionBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ('id', 'country', 'name', )


class RegionSerializer(RegionBaseSerializer):

    cities = CityBaseSerializer(many=True)

    class Meta(RegionBaseSerializer.Meta):
        fields = RegionBaseSerializer.Meta.fields + ('cities', )


class CitySerializer(CityBaseSerializer):

    region = RegionBaseSerializer(read_only=True)
