from api.base import TwitchBase
from api.other.decorators import oauth_required
from api.other.helper import dict_gen, parameter_check
from api.other.constants import *


class Channel(TwitchBase):

    @oauth_required(scope=SCOPE_CHANNEL_EDITOR)
    def get_channel(self):
        request = 'channel'
        self._get(request)

    def get_channel_by_id(self, channel_id):
        request = 'channels/{}'.format(channel_id)
        self._get(request)

    @oauth_required(scope=SCOPE_CHANNEL_EDITOR)
    def update_channel(self, channel_id, status=None, game=None, delay=None, channel_feed_enabled=None):
        json = dict_gen(status=status, game=game, delay=delay, channel_feed_enabled=channel_feed_enabled)
        channel_json = dict_gen(channel=json)
        request = 'channels/{}'.format(channel_id)
        return self._put(request, json=channel_json)

    @oauth_required(scope=SCOPE_CHANNEL_READ)
    def get_channel_editors(self, channel_id):
        request = 'channels/{}/editors'.format(channel_id)
        return self._get(request)

    def get_channel_followers(self, channel_id, limit=DEFAULT_OBJECT_LIMIT, offset=0, cursor=None, direction='desc'):

        parameter_check(limit=limit, direction=direction)
        params = dict_gen(limit=limit, offset=offset, cursor=cursor, direction=direction)
        request = 'channels/{}/follows'.format(channel_id)
        return self._get(request, params=params)

    def get_channel_teams(self, channel_id):
        request = 'channels/{}/teams'.format(channel_id)
        return self._get(request)

    @oauth_required(scope=SCOPE_CHANNEL_SUBSCRIPTIONS)
    def get_channel_subscribers(self, channel_id, limit=DEFAULT_OBJECT_LIMIT, offset=0, direction='asc'):
        parameter_check(limit=limit, direction=direction)
        params = dict_gen(limit=limit, offset=offset, direction=direction)
        request = 'channels/{}/subscriptions'.format(channel_id)
        return self._get(request, params=params)

    @oauth_required(scope=SCOPE_CHANNEL_CHECK_SUBSCRIPTION)
    def get_channel_sub_by_user(self, channel_id, user_id):
        request = 'channels/{}/subscriptions/{}'.format(channel_id, user_id)
        return self._get(request)

    def get_channel_videos(self, channel_id, limit=DEFAULT_VIDEO_LIMIT, offset=0, broadcast_type=DEFAULT_BROADCAST,
                           language=DEFAULT_LANGUAGES, sort=DEFAULT_SORT):
        parameter_check(limit=limit, broadcast_type=broadcast_type, language=language, sort=sort)
        params = dict_gen(limit=limit, offset=offset, broadcast_type=broadcast_type, language=language, sort=sort)
        request = 'channels/{}/videos'.format(channel_id)
        return self._get(request, params=params)

    @oauth_required(scope=SCOPE_CHANNEL_COMMERCIAL)
    def start_channel_commercial(self, channel_id):
        request = 'channels/{}/commercial'.format(channel_id)
        self._post(request)

    @oauth_required(scope=SCOPE_CHANNEL_STREAM)
    def restart_channel_stream_key(self, channel_id):
        request = 'channels/{}/stream_key'.format(channel_id)
        self._delete(request)

    @oauth_required(scope=SCOPE_CHANNEL_EDITOR)
    def get_channel_community(self, channel_id):
        request = 'channels/{}/community'.format(channel_id)
        self._get(request)

    @oauth_required(scope=SCOPE_CHANNEL_EDITOR)
    def set_channel_community(self, channel_id, community_id):
        request = 'channels/{}/community/{}'.format(channel_id, community_id)
        self._put(request)

    def delete_channel_community(self, channel_id, community_id):
        request = 'channels/{}/community/{}'.format(channel_id, community_id)
        self._delete(request)
