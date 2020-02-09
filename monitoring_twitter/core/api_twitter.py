import tweepy


class ApiTwitter:
    def __init__(self, credential):
        self.consumer_key = credential.get('consumer_key')
        self.consumer_secret = credential.get('consumer_secret')
        self.access_token_secret = credential.get('access_token_secret')
        self.access_token_key = credential.get('access_token_key')
        self.api = self.auth()

    def auth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token_key, self.access_token_secret)
        return tweepy.API(auth, wait_on_rate_limit=True)

    def get_tweets(self, hash_tag: str, since: str) -> list:
        """
        Get tweets content specific hash tag from a defined date
        :param hash_tag: str
        :param since: str example 2020-02-09
        :return: list content tweets
        """
        list_tweets = []
        for tweet in tweepy.Cursor(self.api.search, q=hash_tag, count=100,
                                   lang="pt-br", since=since, tweet_mode='extended').items():
            try:
                text = tweet.retweeted_status.full_text
            except AttributeError:
                text = tweet.full_text
            list_tweets.append({'message': text, 'author': tweet.author.name,
                                'date_publish': tweet.created_at})
        return list_tweets




