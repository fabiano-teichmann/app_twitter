from datetime import datetime, timedelta
from django.test import TestCase


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
        since = datetime.now() - timedelta(days=3)
        since = since.strftime('%Y-%m-%d')
        self.hashtag = '#python'
        self.tweets = ApiTwitter(self.credential).get_tweets(hashtag=self.hashtag, since=since)

    def test_get_date_publish(self):
        """Must be return date publish with instance datetime"""
        for tweet in self.tweets:
            self.assertIsInstance(tweet['date_publish'], datetime)

    def test_get_message(self):
        """Must be return message content hash tag #Python """
        for tweet in self.tweets:
            self.assertIn(self.hashtag, tweet['message'].lower())

    def test_get_author(self):
        """Must be return string for author"""
        for tweet in self.tweets:
            self.assertIsInstance(tweet['author'], str)
