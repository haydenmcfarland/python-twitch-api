from twitchpy.other.constants import *
from twitchpy.other.decorators import oauth_required
from twitchpy.other.helper import dict_gen
from twitchpy.v5.base import TwitchBase


class Streams(TwitchBase):
    def get_stream_by_user(self, channel_id, stream_type=None):
        request = 'streams/{}'.format(channel_id)
        params = dict_gen(stream_type=stream_type)
        return self._get(request, params=params)

    def get_live_streams(self, channel=None, game=None, language=None, stream_type=None, limit=None, offset=None):
        request = 'streams/'
        params = dict_gen(channel=channel, game=game,
                          language=language, stream_type=stream_type, limit=limit, offset=offset)
        return self._get(request, params=params)

    def get_streams_summary(self, game=None):
        request = 'streams/summary'
        params = dict_gen(game=game)
        return self._get(request, params=params)

    def get_featured_streams(self, limit=None, offset=None):
        request = 'streams/feature'
        params = dict_gen(limit=limit, offset=offset)
        return self._get(request, params=params)

    @oauth_required(scope=SCOPE_USER_READ)
    def get_followed_streams(self, stream_type=None, limit=None, offset=None):
        request = 'streams/followed'
        params = dict_gen(stream_type=stream_type, limit=limit, offset=offset)
        return self._get(request, params=params)
