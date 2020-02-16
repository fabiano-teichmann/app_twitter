from django.contrib.auth.models import User
from django.test import TestCase

from core.models import Hashtag, Tweet


class TestCreateHashTags(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_user(username='user_test', email='test@gmail.com', password='2DF1SD2d2D2@D')
        self.client.login(username='user_test', password='2DF1SD2d2D2@D')
        self.data = {'hashtag': '#python', 'user_id': user.pk}
        self.resp = self.client.post('/create_hashtag', self.data)

    def test_post(self):
        self.assertEqual(self.resp.status_code, 302)

    def test_get_hashtag(self):
        hashtag = Hashtag.objects.get(hashtag="#python")
        self.assertEqual(hashtag.hashtag, '#python')

    def test_block_hashtag(self):
        """Must be block hashtag if hashtag exist"""
        self.client.post('/create_hashtag', self.data)
        hashtags = Hashtag.objects.filter(hashtag='#python').count()
        self.assertEqual(hashtags, 1)

    def test_get_tweets(self):
        """Must be insert database Tweets"""
        tweets = Tweet.objects.all().count()
        self.assertNotEqual(tweets, 0)