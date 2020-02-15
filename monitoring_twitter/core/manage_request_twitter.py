import time
from datetime import datetime, timedelta

from core.api_twitter import ApiTwitter
from core.models import Tweet, Hashtag
from monitoring_twitter.settings import env_config


class ManagerRequestApiTwitter:
    def __init__(self):
        consumer_key = env_config.get('consumer_key')
        consumer_secret = env_config.get('consumer_secret')
        access_token_key = env_config.get('access_token_key')
        access_token_secret = env_config.get('access_token_secret')
        self.credential = {'consumer_key': consumer_key,
                           'consumer_secret': consumer_secret,
                           'access_token_key': access_token_key,
                           'access_token_secret': access_token_secret
                           }
        since = datetime.now() - timedelta(days=1)
        self.since = since.strftime('%Y-%m-%d-%m%s')

    def update_tweets(self, hashtag):
        tweets = ApiTwitter(self.credential).get_tweets(hashtag=hashtag.hashtag, since=self.since)
        for tweet in tweets:
            Tweet.objects.create(**tweet)
        hashtag.updated_at = datetime.now()
        hashtag.save()
        return len(tweets)

    def get_hashtags_for_update(self):
        """
        Get hashtags for update only hashtags with more 1 minute is actualizada
        :return: list
        """
        now = datetime.now()
        date = now - timedelta(seconds=120)
        list_hashtags = []
        hashtags = Hashtag.objects.filter(updated_at__lt=date).order_by('updated_at')
        for hashtag in hashtags:
            self.update_tweets(hashtag)
            list_hashtags.append(hashtag.hashtag)
        return list_hashtags

