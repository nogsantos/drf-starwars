# -*- coding: utf-8 -*-
from json import JSONDecodeError

import requests

from starwars.planets.models import Film


class GetFilmByPlanet:
    BASE_URL = 'https://swapi.co/api/planets/?search='

    def __init__(self, planet):
        self.planet = planet

    def search(self):
        planet_name = self.planet.name
        address = f'{self.BASE_URL}{planet_name}'

        try:
            data = requests.get(address).json()
            films = data['results'][0]['films']

            self.planet.diameter = data['results'][0]['diameter']
            self.planet.rotation_period = data['results'][0]['rotation_period']
            self.planet.orbital_period = data['results'][0]['orbital_period']
            self.planet.gravity = data['results'][0]['gravity']
            self.planet.population = data['results'][0]['population']
            self.planet.surface_water = data['results'][0]['surface_water']

            for url in films:
                self.persist(url)
        except JSONDecodeError:
            pass

    def persist(self, film_address):
        try:
            film = requests.get(film_address).json()
            created = Film.objects.create(
                title=film['title'],
                episode_id=(film['episode_id'] or None),
                opening_crawl=(film['opening_crawl'] or None),
                director=(film['director'] or None),
                producer=(film['producer'] or None),
                release_date=(film['release_date'] or None)
            )
            self.planet.films.add(created)
            self.planet.save()
        except JSONDecodeError:
            pass
