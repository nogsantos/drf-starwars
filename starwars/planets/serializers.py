from abc import ABC

from rest_framework import serializers

from starwars.planets.models import Planet, Film


class FilmRelatedField(serializers.RelatedField, ABC):
    def to_representation(self, obj):
        return {
            "id": obj.id,
            "title": obj.title
        }


class PlanetSerializer(serializers.ModelSerializer):
    films = FilmRelatedField(queryset=Film.objects.all(), many=True)
    films_number_of_appearances = serializers.SerializerMethodField()

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
            'films_number_of_appearances',
            'films',
        )

    def get_films_number_of_appearances(self, obj):
        return obj.films.count()


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
