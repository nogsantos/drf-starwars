from unittest.mock import patch

from django.test import TestCase

from starwars.planets.serializers import FilmSerializer


class FilmSerializerTest(TestCase):

    @patch('starwars.planets.models.Film')
    def test_serialized_fields(self, film):
        """Should get default serialized fields"""

        film.return_value = None

        serializer = FilmSerializer(film)
        serializer_fields = serializer.data.keys()

        expected_fields = [
            'id',
            'title',
            'episode_id',
            'opening_crawl',
            'director',
            'producer',
            'release_date',
        ]

        self.assertEqual(set(serializer_fields), set(expected_fields))
