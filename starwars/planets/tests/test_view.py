from django.test import TestCase
from rest_framework.reverse import reverse


class ViewTest(TestCase):
    def setUp(self):
        """Tests initialize"""
        self.response = self.client.get(
            reverse('starwars-planets-show_message')
        )

    def test_list(self):
        self.assertEquals(200, self.response.status_code)
