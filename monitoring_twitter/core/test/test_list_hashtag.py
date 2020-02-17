from django.contrib.auth.models import User
from django.test import TestCase


class TestListTweet(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_user(username='user_test', email='test@gmail.com', password='2DF1SD2d2D2@D')
        self.client.login(username='user_test', password='2DF1SD2d2D2@D')
        data = {'hashtag': '#python', 'user_id': user.pk}
        self.client.post('/create_hashtag', data)
        self.resp = self.client.get('/list_hashtags')

    def test_template_list_hashtag(self):
        self.assertTemplateUsed(self.resp, 'list_hashtags.html')


