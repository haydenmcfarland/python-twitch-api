from twitchpy.other.constants import *
from twitchpy.other.decorators import oauth_required
from twitchpy.other.helper import dict_gen
from twitchpy.v5.base import TwitchBase


class Videos(TwitchBase):
    def get_video(self, video_id):
        request = 'videos/{}'.format(video_id)
        return self._get(request)

    def get_top_videos(self, limit=None, offset=None, game=None, period=None, broadcast_type=None,
                       language=None, sort=None):
        request = 'videos/top'
        params = dict_gen(limit=limit, offset=offset, game=game, period=period, broadcast_type=broadcast_type,
                          language=language, sort=sort)
        return self._get(request, params=params)

    @oauth_required
    def get_followed_videos(self, limit=None, offset=None, broadcast_type=None, language=None, sort=None):
        request = 'videos/followed'
        params = dict_gen(limit=limit, offset=offset, broadcast_type=broadcast_type, language=language, sort=sort)
        return self._get(request, params=params)
