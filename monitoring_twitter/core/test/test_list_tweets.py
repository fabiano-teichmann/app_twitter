from django.contrib.auth.models import User
from django.test import TestCase


class TestListTweets(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_user(username='user_test', email='test@gmail.com', password='2DF1SD2d2D2@D')
        self.client.login(username='user_test', password='2DF1SD2d2D2@D')
        self.data = {'hashtag': '#python', 'user_id': user.pk}
        self.resp = self.client.post('/create_hashtag', self.data)

    def test_fail_updates_tweets(self):
        resp = self.client.get('/ajax_call/update_tweets')
        resp = resp.json()
        self.assertEqual(resp['status'], 'fail')

    def test_update_tweets(self):
        resp = self.client.get('/ajax_call/update_tweets', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        resp = resp.json()
        self.assertEqual(resp['status'], 'success')

    def test_list_tweets(self):
        resp = self.client.get('/')
        self.assertTemplateUsed(resp, 'list_tweets.html')
