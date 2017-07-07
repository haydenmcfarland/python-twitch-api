from api.base import TwitchBase
from api.other.decorators import oauth_required
from api.other.helper import dict_gen
from api.other.constants import *


class Videos(TwitchBase):
    def get_video(self, video_id):
        request = 'videos/{}'.format(video_id)
        return self._get(request)

    def get_top_videos(self, limit=10, offset=0, game=None, period='week', broadcast_type=DEFAULT_BROADCAST,
                       language='', sort=None):
        request = 'videos/top'
        params = dict_gen(limit=limit, offset=offset, game=game, period=period, broadcast_type=broadcast_type,
                          language=language, sort=sort)
        return self._get(request, params=params)

    @oauth_required(scope=SCOPE_USER_READ)
    def get_followed_videos(self, limit=10, offset=0, broadcast_type=DEFAULT_BROADCAST, language='', sort=None):
        request = 'videos/followed'
        params = dict_gen(limit=limit, offset=offset, broadcast_type=broadcast_type, language=language, sort=sort)
        return self._get(request, params=params)
