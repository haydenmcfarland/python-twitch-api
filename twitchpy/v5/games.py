from twitchpy.other.helper import dict_gen
from twitchpy.v5.base import TwitchBase


class Games(TwitchBase):
    def get_top_games(self, limit=None, offset=None):
        request = 'games/top'
        params = dict_gen(limit=limit, offset=offset)
        return self._get(request, params=params)
