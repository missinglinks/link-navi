import requests

TWEET = "tweet"
ACCOUNT = "account"

class TwitterLink(object):

    def __init__(self, url, handle, tweet_id, suspended):
        self.url = url
        self.handle = handle
        self.tweet_id = tweet_id
        if not tweet_id:
            self.type = ACCOUNT
        else:
            self.type = TWEET

    def json(self):
        return {
            "type": self.type,
            "url": self.url,
            "handle": self.handle,
            "tweet_id": self.tweet_id
        }


class TwitterLinkFactory(object):

    def __init__(self):
        self.session = requests.Session()

    def _forwarded_url(self, url):
        try:
            resp = self.session.head(url, allow_redirects=True)
            return resp.url
        except:
            return url        

    def __call__(self, url):

        handle = url.split("tter.com/")[-1].split("/")[0]
        if not handle or handle in ["i", "RETRACTED"]:
            return None

        fwd = self._forwarded_url(url)

        if fwd == "https://twitter.com/account/suspended":
            suspended = True
        else:
            suspended = False

        tweet_id = url.split("/status/")[-1]

        return TwitterLink(url, handle, tweet_id, suspended)