import re
from .youtubelink import YoutubeLinkFactory
from .genericlink import GenericLinkFactory
from .twitterlink import TwitterLinkFactory

class LinkNavi(object):

    def __init__(self, youtube_api_key=None):
        self._YOUTUBE = YoutubeLinkFactory(youtube_api_key)
        self._TWITTER = TwitterLinkFactory()
        self._LINK = GenericLinkFactory()

    def _extract_urls(self, text):
        for token in text.split():
            if token.startswith("http") and len(token) > 10:
                yield token

    def parse(self, text):
        
        if "http" not in text:
            return None

        record = LinkRecord()

        for url in self._extract_urls(text):

            if "youtu" in url:
                link = self._YOUTUBE(url)
                if link:
                    record.add_youtube(link)
                    continue

            if "twitter.com" in url:
                link = self._TWITTER(url)
                if link:
                    record.add_twitter(link)
                    continue

            link = self._LINK(url)
            record.add_link(link)
            

        return record


class LinkRecord(object):

    def __init__(self):
        self.links = []
        self.youtube = []
        self.twitter = []


    def add_link(self, link):
        self.links.append(link)

    def add_youtube(self, youtube_link):
        self.youtube.append(youtube_link)

    def add_twitter(self, twitter_link):
        self.twitter.append(twitter_link)

    def json(self):
        links = [ l.json() for l in self.links ]
        yt = [ l.json() for l in self.youtube ]
        tw = [ l.json() for l in self.twitter ]
        return {
            "links": links,
            "youtube": yt,
            "twitter": tw
        }



