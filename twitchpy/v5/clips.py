from twitchpy.other.constants import *
from twitchpy.other.decorators import oauth_required
from twitchpy.other.helper import dict_gen
from twitchpy.v5.base import TwitchBase


class Clips(TwitchBase):
    def get_clip(self, slug):
        request = 'clips/{}'.format(slug)
        return self._get(request)

    def get_top_clips(self, channel=None, cursor=None, game=None, language=None, limit=None, period=None, trending=None):
        request = 'clips/top'
        params = dict_gen(channel=channel, cursor=cursor, game=game,
                          language=language, limit=limit, period=period,
                          trending=trending)
        return self._get(request, params=params)

    @oauth_required(scope=SCOPE_USER_READ)
    def get_followed_clips(self, limit=None, cursor=None, trending=None):
        request = 'clips/followed'
        params = dict_gen(limit=limit, cursor=cursor, trending=trending)
        return self._get(request, params=params)
