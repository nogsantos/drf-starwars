from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework import status


class ViewTest(TestCase):
    def setUp(self):
        """Tests initialize"""
        self.response = self.client.get(
            reverse('starwars-planets-list')
        )

    def test_list(self):
        self.assertEquals(status.HTTP_200_OK, self.response.status_code)
