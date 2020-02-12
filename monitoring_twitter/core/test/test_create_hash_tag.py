from django.contrib.auth.models import User
from django.test import TestCase

from core.models import HashTag


class TestCreateHashTags(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_user(username='user_test', email='test@gmail.com', password='2DF1SD2d2D2@D')
        data = {'hash_tag': '#python', 'user_id': user.pk}
        self.resp = self.client.post('/create_hash_tag', data)

    def test_post(self):
        self.assertEqual(self.resp.status_code, 302)

    def test_get(self):
        resp = self.client.get('/create_hash_tag')
        self.assertEqual(resp.status_code, 200)

    def test_get_hash_tag(self):
        hash_tag = HashTag.objects.get(hash_tag="#python")
        self.assertEqual(hash_tag.hash_tag, '#python')
