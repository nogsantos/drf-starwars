from django.test import TestCase
from unittest.mock import patch

from starwars.planets.serializers import PlanetSerializer


class PlanetSerializerTest(TestCase):

    @patch('starwars.planets.models.Planet')
    def test_serialized_fields(self, planet):
        """Should get default serialized fields"""

        planet.return_value = None

        serializer = PlanetSerializer(planet)
        serializer_fields = serializer.data.keys()

        expected_fields = [
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
        ]

        self.assertEqual(set(serializer_fields), set(expected_fields))
