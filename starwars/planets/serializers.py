from rest_framework import serializers

from starwars.planets.models import Planet, Film


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = (
            'id',
            'name',
            'diameter',
            'rotation_period',
            'orbital_period',
            'gravity',
            'population',
            'surface_water',
            'climate',
            'terrain',
            'films',
        )


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = (
            'id',
            'title',
            'episode_id',
            'opening_crawl',
            'director',
            'producer',
            'release_date',
        )
