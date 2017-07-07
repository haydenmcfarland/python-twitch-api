from api.base import TwitchBase
from api.other.helper import dict_gen


class Games(TwitchBase):
    def get_top_games(self, limit=10, offset=0):
        request = 'games/top'
        params = dict_gen(limit=limit, offset=offset)
        return self._get(request, params=params)
