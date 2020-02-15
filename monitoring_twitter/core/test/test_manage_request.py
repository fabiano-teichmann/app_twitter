import time
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.test import TestCase


from core.manage_request_twitter import ManagerRequestApiTwitter
from core.models import Hashtag


class TestManageRequestApiTwitter(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_user(username='user_test', email='test@gmail.com', password='2DF1SD2d2D2@D')
        self.client.login(username='user_test', password='2DF1SD2d2D2@D')
        self.data = {'hashtag': '#python', 'user_id': user.pk}
        self.client.post('/create_hashtag', self.data)

    def test_not_have_updates(self):
        """Must be return 0 hashtag updated because last updated a less 2 minutes"""
        date = datetime.now() - timedelta(seconds=119)
        hashtag = Hashtag.objects.get(hashtag="#python")
        hashtag.updated_at = date
        hashtag.save()
        hashtags = ManagerRequestApiTwitter().get_hashtags_for_update()
        self.assertEqual(len(hashtags), 0)

    def test_update_tweets(self):
        """Must be return list hashtag updated content in list hashtag #python"""
        date = datetime.now() - timedelta(seconds=121)
        hashtag = Hashtag.objects.get(hashtag="#python")
        hashtag.updated_at = date
        hashtag.save()
        hashtags = ManagerRequestApiTwitter().get_hashtags_for_update()
        self.assertEqual(hashtags[0], '#python')