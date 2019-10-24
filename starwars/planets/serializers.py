from rest_framework import serializers

from . import models


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Planet
        fields = (
            'id',
            'name',
            'climate',
            'terrain',
            'films',
        )
