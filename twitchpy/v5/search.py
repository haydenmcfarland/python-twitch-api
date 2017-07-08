from twitchpy.other.helper import dict_gen
from twitchpy.v5.base import TwitchBase


class Search(TwitchBase):
    def search_channels(self, query, limit=None, offset=None):
        request = 'search/channels'
        params = dict_gen(query=query, limit=limit, offset=offset)
        return self._get(request, params=params)

    def search_channels(self, query, live=False):
        request = 'search/games'
        params = dict_gen(query=query, live=live)
        return self._get(request, params=params)

    def search_streams(self, query, limit=None, offset=None, hls=None):
        request = 'search/streams'
        params = dict_gen(query=query, limit=limit, offset=offset, hls=hls)
        return self._get(request, params=params)
