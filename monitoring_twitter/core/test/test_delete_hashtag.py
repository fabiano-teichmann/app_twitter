from django.contrib.auth.models import User
from django.test import TestCase

from core.models import Hashtag


class TestDeleteHashtag(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_user(username='test', email='test@test.com', password='T1@ff1Dds1')
        self.client.login(username='test', password='T1@ff1Dds1')
        self.hashtag = Hashtag.objects.create(hashtag='#Unittest', user_id=user.pk)

    def test_delete_hastag(self):
        resp = self.client.get(f"/delete_hashtag/{self.hashtag.pk}")
        self.assertEqual(resp.status_code, 302)