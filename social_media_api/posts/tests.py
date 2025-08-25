from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class PostAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="kevin", password="test1234")
        self.client.login(username="kevin", password="test1234")
        for i in range(15):
            Post.objects.create(author=self.user, title=f"Post {i}", content="Content here")

    def test_pagination(self):
        url = reverse("post-list")  # comes from DRF router
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        self.assertLessEqual(len(response.data["results"]), 10)  # matches PAGE_SIZE

    def test_search(self):
        url = reverse("post-list")
        response = self.client.get(url, {"search": "Post 1"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Post 1" in p["title"] for p in response.data["results"]))

