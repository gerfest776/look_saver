import null as null
from django.urls import reverse
from psycopg2.sql import NULL
from rest_framework import status
from rest_framework.test import APITestCase

from look_collector.models import Outfit, OutfitItem


class TestApi(APITestCase):
    # fixtures = ["my_fixture.json"]

    @classmethod
    def setUpTestData(cls):
        cls.user = 'admin'

        cls.post_data = {
            "outfit": [
                {
                    "type": "pants",
                    "brand": "sasds",
                    "price": 10.99,
                    "size": "asd",
                    "color": "test",
                    "link": "hi",
                    "image_id": None
                },
                {
                    "type": "top",
                    "brand": "sasds",
                    "price": 29.98,
                    "size": "asd",
                    "color": "test",
                    "link": "hi",
                    "image_id": None
                },
                {
                    "type": "accessory",
                    "brand": "sasds",
                    "price": 35.11,
                    "size": "asd",
                    "color": "test",
                    "link": "hi",
                    "image_id": None
                },
                {
                    "type": "shoes",
                    "brand": "sasds",
                    "price": 34.88,
                    "size": "asd",
                    "color": "test",
                    "link": "hi",
                    "image_id": None
                }
            ]
        }

    def test_create_outfit(self):
        url = reverse("outfit-list")
        post_data = self.post_data
        user = self.user
        response = self.client.post(url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
