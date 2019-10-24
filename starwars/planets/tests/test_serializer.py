from django.test import TestCase
from unittest.mock import patch

from starwars.planets.serializers import PlanetSerializer


class SerializerTest(TestCase):

    @patch('starwars.planets.models.Planet')
    def test_serialized_fields(self, planet):
        """Shold get default serialized fields"""

        planet.return_value = None

        serializer = PlanetSerializer(planet)
        serializer_fields = serializer.data.keys()

        expected_fields = [
            'id',
            'name',
            'climate',
            'terrain',
            'films',
        ]

        self.assertEqual(set(serializer_fields), set(expected_fields))
