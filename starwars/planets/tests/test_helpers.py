# -*- coding: utf-8 -*-
from json import JSONDecodeError
from unittest.mock import patch

import requests
from django.test import TestCase

from starwars.planets.helpers import GetFilmByPlanet
from starwars.planets.models import Planet


class HelperGetFilmByPlanetTest(TestCase):

    def setUp(self):
        fake_planet = Planet(name='some')
        self.helper = GetFilmByPlanet(fake_planet)

    @patch.object(requests, 'get')
    def test_get_request_error(self, get):
        """Should raise an exception when request has errors"""
        self.helper.search()
        get.return_value = []
        self.assertRaises(JSONDecodeError)

    @patch.object(GetFilmByPlanet, 'persist')
    @patch.object(requests, 'get')
    def test_get(self, get, persist):
        """Raise exception when request error"""
        get_response = {
            "results": [{
                "diameter": "10465",
                "rotation_period": "23",
                "orbital_period": "304",
                "gravity": "1 standard",
                "population": "200000",
                "surface_water": "1",
                "films": [
                    "https://swapi.co/api/films/5/",
                ]
            }],
        }

        get.return_value.json.return_value = get_response

        self.helper.search()

        persist.assert_called()

    @patch.object(GetFilmByPlanet, 'persist')
    @patch.object(requests, 'get')
    def test_get_without_persist(self, get, persist):
        """Should not persist values when has no film on result"""
        get_response = {
            "results": [{
                "diameter": "10465",
                "rotation_period": "23",
                "orbital_period": "304",
                "gravity": "1 standard",
                "population": "200000",
                "surface_water": "1",
                "films": []
            }],
        }

        get.return_value.json.return_value = get_response

        self.helper.search()

        persist.assert_not_called()
