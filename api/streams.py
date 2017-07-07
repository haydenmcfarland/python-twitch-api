from api.base import TwitchBase
from api.other.decorators import oauth_required
from api.other.helper import dict_gen


class Streams(TwitchBase):
    def get_stream_by_user(self, channel_id, stream_type='live'):
        request = 'streams/{}'.format(channel_id)
        params = dict_gen(stream_type=stream_type)
        return self._request('get', request, params=params)

    def get_live_streams(self, channel=None, game=None, language=None, stream_type='live', limit=25, offset=0):
        request = 'streams/'
        params = dict_gen(channel=channel, game=game,
                          language=language, stream_type=stream_type, limit=limit, offset=offset)
        return self._request('get', request, params=params)

    def get_streams_summary(self, game=None):
        request = 'streams/summary'
        params = dict_gen(game=game)
        return self._request('get', request, params=params)

    def get_featured_streams(self, limit=25, offset=0):
        request = 'streams/feature'
        params = dict_gen(limit=limit, offset=offset)
        return self._request('get', request, params=params)

    @oauth_required
    def get_followed_streams(self, stream_type='live', limit=25, offset=0):
        request = 'streams/followed'
        params = dict_gen(stream_type=stream_type, limit=limit, offset=offset)
        return self._request('get', request, params=params)
