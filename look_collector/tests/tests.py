from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from look_collector.models import Outfit, OutfitItem, User


class TestApi(APITestCase):
    fixtures = ["my_fixture.json"]

    def setUp(self) -> None:
        pass
        # self.client.force_authenticate(self.user)

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="admin", password="admin")
        cls.post_data = {
            "outfit": [
                {
                    "type": "pants",
                    "brand": "sasds",
                    "price": 10.99,
                    "size": "asd",
                    "color": "test",
                    "link": "hi",
                    "image_id": None,
                },
                {
                    "type": "top",
                    "brand": "sasds",
                    "price": 29.98,
                    "size": "asd",
                    "color": "test",
                    "link": "hi",
                    "image_id": None,
                },
                {
                    "type": "accessory",
                    "brand": "sasds",
                    "price": 35.11,
                    "size": "asd",
                    "color": "test",
                    "link": "hi",
                    "image_id": None,
                },
                {
                    "type": "shoes",
                    "brand": "sasds",
                    "price": 34.88,
                    "size": "asd",
                    "color": "test",
                    "link": "hi",
                    "image_id": None,
                },
            ]
        }

    def test_create_outfit(self):
        url = reverse("outfit-list")
        self.client.force_authenticate(self.user)
        response = self.client.post(url, self.post_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {"outfit": {"outfit_id": 2}})

    def test_get_outfit(self):
        url = reverse("outfit-my-outfits")
        self.client.login(username="user", password="user")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)

    def test_patch_outfit(self):
        url = reverse("outfit-outfits-partial", args=["1", "2"])
        patch_data = {"brand": "NONAME"}
        response = self.client.patch(url, patch_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            OutfitItem.objects.filter(id=2).first().brand, patch_data["brand"]
        )

    def test_retrieve_outfit(self):
        url = reverse("outfit-my-outfit-retr", args=["1"])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)

    def test_delete_outfit(self):
        url = reverse("outfit-detail", args=["1"])
        url_query_param = "/api/outfit/1?shoes=1"
        response = self.client.delete(url, format="json")
        self.assertIsNone(Outfit.objects.get(id=1).look_id.filter(id=1).first())
        response_query_param = self.client.delete(url_query_param, format="json")
        self.assertEqual(list(Outfit.objects.get(id=1).look_id.all()), [])
