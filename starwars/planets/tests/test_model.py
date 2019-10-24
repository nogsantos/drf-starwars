from uuid import UUID

from django.test import TestCase

from starwars.planets.models import Planet


class PlanetModelTest(TestCase):

    def setUp(self):
        self.planet = Planet(
            name='Tatooine',
            terrain='Dessert',
            climate='Arid',
        )
        self.planet.save()

    def test_create(self):
        """Should create a new planet"""
        self.assertTrue(Planet.objects.exists())

    def test_str(self):
        """Should return planet name as string"""  # noqa
        self.assertEqual('Tatooine', str(self.planet))

    def test_id(self):
        """Should planet id as uuid format"""  # noqa
        self.assertIsInstance(self.planet.id, UUID)
