from uuid import UUID

from django.test import TestCase

from starwars.planets.models import Film


class FilmModelTest(TestCase):

    def setUp(self):
        self.film = Film.objects.create(
            title='A New Hope'
        )

    def test_create(self):
        """Should create a new planet"""
        self.assertTrue(Film.objects.exists())

    def test_str(self):
        """Should return film title as string"""
        self.assertEqual('A New Hope', str(self.film))

    def test_id(self):
        """Should film id as uuid format"""
        self.assertIsInstance(self.film.id, UUID)

    def test_ordering(self):
        """Should ensure the default list order"""
        self.assertListEqual(['-id'], Film._meta.ordering)

    def test_fields_null_or_blank(self):
        """Should ensure the fields can be null or blank"""
        fields = [
            'episode_id',
            'opening_crawl',
            'director',
            'producer',
            'release_date',
        ]
        for field in fields:
            with self.subTest():
                field = Film._meta.get_field(field)
                self.assertTrue(field.blank)
                self.assertTrue(field.null)
