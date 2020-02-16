import time
from datetime import datetime, timedelta

from core.api_twitter import ApiTwitter
from core.models import Tweet, Hashtag, RequestAPI
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
        self.api = ApiTwitter(self.credential)

    def update_tweets(self, hashtag):
        self.handle_rate_limit()
        tweets = self.api.get_tweets(hashtag=hashtag.hashtag, since=self.since)
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
        date = now - timedelta(seconds=60)
        list_hashtags = []
        hashtags = Hashtag.objects.filter(updated_at__lt=date).order_by('-updated_at')
        for hashtag in hashtags:
            self.update_tweets(hashtag)
            list_hashtags.append(hashtag.hashtag)
        return list_hashtags

    @staticmethod
    def handle_rate_limit():
        """Controls number of API requests not allow more 450 in window 15 minutes"""
        now = datetime.now()
        requests = RequestAPI.objects.last()
        if requests is None:
            requests = RequestAPI.objects.create(total_request=1, date=now)

        date_windows_request = now - requests.date
        if date_windows_request.seconds >= 900:
           RequestAPI.objects.create(total_request=1, date=now)
        elif requests.total_request < 450:
            requests.total_request = requests.total_request + 1
            requests.save()
        else:
            sleep = 901 - date_windows_request.seconds
            time.sleep(sleep)
            RequestAPI.objects.create(total_request=1, date=datetime.now())
