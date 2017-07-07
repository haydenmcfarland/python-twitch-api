from api.base import TwitchBase
from api.other.helper import dict_gen


class Bits(TwitchBase):
    def get_cheermotes(self, channel_id=None):
        request = 'bits/actions'
        params = dict_gen(channel_id=channel_id)
        return self._get(request, params=params)
