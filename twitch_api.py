from api.bits import Bits
from api.channel_feed import ChannelFeed
from api.channels import Channel
from api.chat import Chat
from api.clips import Clips
from api.collections import Collections
from api.communities import Communities
from api.games import Games
from api.ingests import Ingests
from api.search import Search
from api.streams import Streams
from api.teams import Teams
from api.users import Users
from api.videos import Videos


class TwitchAPI:

    def __init__(self, client_id, oauth_token):
        self._client_id = client_id
        self._oauth_token = oauth_token
        self._bits = None
        self._channel_feed = None
        self._channel = None
        self._chat = None
        self._clips = None
        self._collections = None
        self._communities = None
        self._games = None
        self._ingests = None
        self._search = None
        self._streams = None
        self._teams = None
        self._users = None
        self._videos = None

    @property
    def bits(self):
        if not self._bits:
            self._bits = Bits(self._client_id, self._oauth_token)
        return self._bits

    @property
    def channel_feed(self):
        if not self._channel_feed:
            self._channel_feed = ChannelFeed(self._client_id, self._oauth_token)
        return self._channel_feed

    @property
    def channel(self):
        if not self._channel:
            self._channel = Channel(self._client_id, self._oauth_token)
        return self._channel

    @property
    def chat(self):
        if not self._chat:
            self._chat = Chat(self._client_id, self._oauth_token)
        return self._chat

    @property
    def clips(self):
        if not self._clips:
            self._clips = Clips(self._client_id, self._oauth_token)
        return self._clips

    @property
    def collections(self):
        if not self._collections:
            self._collections = Collections(self._client_id, self._oauth_token)
        return self._collections

    @property
    def communities(self):
        if not self._communities:
            self._communities = Communities(self._client_id, self._oauth_token)
        return self._communities

    @property
    def games(self):
        if not self._games:
            self._games = Games(self._client_id, self._oauth_token)
        return self._games

    @property
    def ingests(self) -> Ingests:
        if not self._ingests:
            self._ingests = Ingests(self._client_id, self._oauth_token)
        return self._ingests

    @property
    def search(self):
        if not self._search:
            self._search = Search(self._client_id, self._oauth_token)
        return self._search

    @property
    def streams(self):
        if not self._streams:
            self._streams = Streams(self._client_id, self._oauth_token)
        return self._streams

    @property
    def teams(self):
        if not self._teams:
            self._teams = Teams(self._client_id, self._oauth_token)
        return self._teams

    @property
    def users(self):
        if not self._users:
            self._users = Users(self._client_id, self._oauth_token)
        return self._users

    @property
    def videos(self):
        if not self._videos:
            self._videos = Videos(self._client_id, self._oauth_token)
        return self._videos
