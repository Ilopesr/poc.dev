from rest_framework.test import APIRequestFactory
from django.test import Client
from django.test import TestCase
from apps.posts.models import Post
import json


class TestPostViews(TestCase):
    def setUp(self):
        posts = [Post(username=x, title=x, content=x) for x in range(0, 13)]
        Post.objects.bulk_create(posts)

        self.client = Client()
        self.factory = APIRequestFactory()

    def test_get_posts(self):
        factory_response = self.factory.get("/")
        client_response = self.client.get("/")

        self.assertTrue(factory_response)
        self.assertTrue(client_response)

    def test_post_posts(self):
        data = (
            "/",
            {
                "username": "igribeiro",
                "title": "POST want to return status 200",
                "content": "POST want to return status 200",
            },
        )

        factory_response = self.factory.post(
            *data,
            content_type="application/json",
        )
        client_response = self.client.post(
            *data,
            content_type="application/json",
        )

        client_response_content = json.loads(client_response.content.decode("utf-8"))

        self.assertTrue(factory_response)
        self.assertTrue(client_response)
        self.assertEqual(client_response_content["username"], "igribeiro")
        self.assertNotEqual(client_response_content["title"], "POST Fail")

    def test_patch_posts(self):
        post = Post.objects.get(id=1)
        data = (
            "/1/",
            json.dumps({"username": "igribeiro", "title": "PATCH", "content": "PATCH"}),
        )
        factory_response = self.factory.patch(*data, content_type="application/json")

        client_response = self.client.patch(*data, content_type="application/json")

        client_response_content = json.loads(client_response.content.decode("utf-8"))

        self.assertTrue(factory_response)
        self.assertTrue(client_response)

        self.assertNotEqual(client_response_content["username"], post.username)
        self.assertEqual(client_response_content["username"], "igribeiro")

    def test_delete_posts(self):
        factory_response = self.factory.delete("/1/")
        client_response = self.client.delete("/1/")

        post_exists = Post.objects.filter(id=1).exists()

        self.assertFalse(post_exists)
        self.assertTrue(factory_response)
        self.assertTrue(client_response)

        self.assertEqual(client_response.content, b"")
        self.assertEqual(client_response.status_code, 200)
