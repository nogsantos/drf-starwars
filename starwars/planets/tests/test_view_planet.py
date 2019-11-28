from unittest.mock import patch

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse

from starwars.planets.helpers import GetFilmByPlanet
from starwars.planets.models import Planet


class PlanetViewTest(TestCase):

    def setUp(self):
        self.planet = Planet.objects.create(
            name='Tatooine',
            terrain='Dessert',
            climate='Arid',
        )

        self.base_name = 'planets'

    def test_list(self):
        """Should list all planets"""
        response = self.client.get(
            reverse(f'{self.base_name}-list')
        )
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    @patch.object(GetFilmByPlanet, 'search')
    def test_create(self, search):
        """Should create a new planet"""
        planet = dict(
            name='Alderaan',
            terrain='grasslands, mountains',
            climate='temperate',
        )

        response = self.client.post(
            reverse(f'{self.base_name}-list'),
            planet
        )

        search.assert_called_once()
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_remove(self):
        """Should remove an planet"""
        planet_to_remove = Planet.objects.create(
            name='Yavin IV',
            terrain='jungle, rainforests',
            climate='temperate, tropical',
        )
        response = self.client.delete(
            reverse(f'{self.base_name}-detail',
                    kwargs={'pk': planet_to_remove.pk})
        )
        self.assertEquals(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_filter_by_name(self):
        """Should filter planet by name"""
        response = self.client.get(
            reverse(f'{self.base_name}-list'),
            {'name': 'Tatooine'}
        )

        result = response.json()

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(1, result['count'])

    def test_filter_by_id(self):
        """Should filter planet by primary key (UUID)"""
        response = self.client.get(
            reverse(f'{self.base_name}-list'),
            {'id': self.planet.pk}
        )

        result = response.json()

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(1, result['count'])
