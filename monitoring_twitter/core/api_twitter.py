import twitter
from twitter import TwitterError


class ApiTwitter:
    def __init__(self, credential):
        self.consumer_key = credential.get('consumer_key')
        self.consumer_secret = credential.get('consumer_secret')
        self.access_token_secret = credential.get('access_token_secret')
        self.access_token_key = credential.get('access_token_key')
        self.api = self.connect()

    def connect(self):
        api = twitter.Api(consumer_key=self.consumer_key,
                          consumer_secret=self.consumer_secret,
                          access_token_secret=self.access_token_secret,
                          access_token_key=self.access_token_key)
        return api

    def check_credentials(self):
        try:
            check = self.api.VerifyCredentials()
        except Exception as e:
            return  e.message
        return check