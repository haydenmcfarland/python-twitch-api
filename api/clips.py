from api.base import TwitchBase
from api.other.decorators import oauth_required
from api.other.helper import dict_gen
from api.other.constants import *


class Clips(TwitchBase):
    def get_clip(self, slug):
        request = 'clips/{}'.format(slug)
        return self._get(request)

    def get_top_clips(self, channel=None, cursor=None, game=None, language="", limit=10, period='week', trending=False):
        request = 'clips/top'
        params = dict_gen(channel=channel, cursor=cursor, game=game,
                          language=language, limit=limit, period=period,
                          trending=trending)
        return self._get(request, params=params)

    @oauth_required(scope=SCOPE_USER_READ)
    def get_followed_clips(self, limit=10, cursor=None, trending=False):
        request = 'clips/followed'
        params = dict_gen(limit=limit, cursor=cursor, trending=trending)
        return self._get(request, params=params)
