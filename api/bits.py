from api.base import TwitchBase
from api.helper import dict_gen


class Bits(TwitchBase):
    def get_cheermotes(self, channel_id=None):
        request = 'bits/actions'
        params = dict_gen(channel_id=channel_id)
        return self._request('get', request, params=params)
