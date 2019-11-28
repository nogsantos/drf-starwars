from uuid import UUID

from django.test import TestCase
from model_bakery import baker

from starwars.planets.models import Planet


class PlanetModelTest(TestCase):

    def setUp(self):
        self.planet = baker.make(Planet, name='Tatooine')

    def test_create(self):
        """Should create a new planet"""
        self.assertTrue(Planet.objects.exists())
        self.assertEqual(Planet.objects.count(), 1)

    def test_has_films(self):
        """Should planet has films"""
        self.planet.films.create(
            title='A New Hope'
        )
        self.assertEqual(1, self.planet.films.count())

    def test_str(self):
        """Should return planet name as string"""
        self.assertEqual('Tatooine', str(self.planet))

    def test_id(self):
        """Should planet id as uuid format"""
        self.assertIsInstance(self.planet.id, UUID)

    def test_ordering(self):
        """Should ensure the default list order"""
        self.assertListEqual(['-id'], Planet._meta.ordering)

    def test_fields_null_or_blank(self):
        """Should ensure the fields can be null or blank"""
        fields = [
            'diameter',
            'rotation_period',
            'orbital_period',
            'gravity',
            'population',
            'surface_water',
        ]
        for field in fields:
            with self.subTest():
                field = Planet._meta.get_field(field)
                self.assertTrue(field.blank)
                self.assertTrue(field.null)
