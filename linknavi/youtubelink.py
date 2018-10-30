import re
from apiclient.discovery import build

VIDEO_ID_RE = re.compile(r'(v=|ci=|be/)(.*)')

VIDEO = "video"
CHANNEL = "channel"

class YoutubeLink(object):

    def __init__(self, type_, url, video_id, title, channel, raw):
        self.url = url
        self.type = type_
        self.video_id = video_id
        self.title = title
        self.channel = channel
        self.raw = raw
        if raw:
            self.active = True
        else:
            self.active = False

    def json(self):
        return {
            "type": self.type,
            "active": self.active,
            "video_id": self.video_id,
            "title": self.title,
            "channel": self.channel
        }


class YoutubeLinkFactory(object):

    def __init__(self, youtube_api_key):
        self.API = build('youtube', 'v3', developerKey=youtube_api_key)


    def __call__(self, url):

        if "/channel/" in url:
            #deal with channel
            pass

        video_id = self._extract_video_id(url)

        if not video_id:
            return None

        meta = self._get_video_metadata(video_id)
        if not meta:
            return YoutubeLink(VIDEO, url, video_id, None, None, None)
        else:
            title = meta["snippet"]["title"]
            if not "channelTitle" in meta["snippet"]:
                channel = self._get_channel_title(meta["snippet"]["channelId"])
            else:
                channel = meta["snippet"]["channelTitle"]
            return YoutubeLink(VIDEO, url, video_id, title, channel, meta )


    def _extract_video_id(self, url):

        video_id = VIDEO_ID_RE.findall(url)
        if video_id:
            video_id = video_id[0][1]
            if video_id:
                return video_id.split("&")[0].split("?")[0]
        
        return None

    def _get_video_metadata(self, video_id):
        video_data = self.API.videos().list(
                part="id,recordingDetails,snippet,statistics,status,topicDetails,contentDetails",
                id=video_id
                ).execute()  
        if len(video_data["items"]) > 0:
            return video_data["items"][0]
        else:
            return None   

    def _get_channel_title(self, channel_id):
        channel_data = self.API.channels().list(
            part="contentDetails,snippet",
            id=channel_id
            ).execute()
        if len(channel_data["items"]) > 0:
            return channel_data["items"][0]["snippet"]["title"]
        else:
            return None