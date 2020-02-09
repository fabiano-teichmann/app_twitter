from django.test import TestCase
from twitter import TwitterError

from core.api_twitter import ApiTwitter
from monitoring_twitter.settings import env_config


class TestApiTwitter(TestCase):
    def setUp(self) -> None:
        consumer_key = env_config.get('consumer_key')

        consumer_secret = env_config.get('consumer_secret')
        access_token_key = env_config.get('access_token_key')
        access_token_secret = env_config.get('access_token_secret')
        self.credential = {'consumer_key': consumer_key,
                           'consumer_secret': consumer_secret,
                           'access_token_key': access_token_key,
                           'access_token_secret': access_token_secret
                           }

    def test_credential_twitter(self):
        resp = ApiTwitter(self.credential).check_credentials()
        self.assertIsInstance(resp.verified, bool)

    def test_error_credentials(self):
        self.credential.update({'consumer_key': 'tdsd2dsdsds'})
        resp = ApiTwitter(self.credential).check_credentials()
        self.assertEqual(resp[0]['code'], 32)