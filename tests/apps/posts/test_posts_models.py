from django.test import TestCase
from apps.posts.models import Post


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(username="igribeiro", title="test1", content="test1")

    def test_posts_are_created(self):

        post = Post.objects.get(username="igribeiro")

        self.assertTrue(post)
        self.assertEqual(post.username, "igribeiro")
