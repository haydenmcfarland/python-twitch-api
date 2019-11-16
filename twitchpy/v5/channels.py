from twitchpy.other.constants import *
from twitchpy.other.decorators import oauth_required
from twitchpy.other.helper import dict_gen, parameter_check
from twitchpy.v5.base import TwitchBase


class Channel(TwitchBase):

    @oauth_required
    def get_channel(self):
        request = 'channel'
        self._get(request)

    def get_channel_by_id(self, channel_id):
        request = 'channels/{}'.format(channel_id)
        self._get(request)

    @oauth_required
    def update_channel(
            self,
            channel_id,
            status=None,
            game=None,
            delay=None,
            channel_feed_enabled=None):
        json = dict_gen(status=status, game=game, delay=delay,
                        channel_feed_enabled=channel_feed_enabled)
        channel_json = dict_gen(channel=json)
        request = 'channels/{}'.format(channel_id)
        return self._put(request, json=channel_json)

    @oauth_required
    def get_channel_editors(self, channel_id):
        request = 'channels/{}/editors'.format(channel_id)
        return self._get(request)

    def get_channel_followers(
            self,
            channel_id,
            limit=None,
            offset=None,
            cursor=None,
            direction=None):

        parameter_check(limit=limit, direction=direction)
        params = dict_gen(
            limit=limit,
            offset=offset,
            cursor=cursor,
            direction=direction)
        request = 'channels/{}/follows'.format(channel_id)
        return self._get(request, params=params)

    def get_channel_teams(self, channel_id):
        request = 'channels/{}/teams'.format(channel_id)
        return self._get(request)

    @oauth_required
    def get_channel_subscribers(
            self,
            channel_id,
            limit=None,
            offset=None,
            direction=None):
        parameter_check(limit=limit, direction=direction)
        params = dict_gen(limit=limit, offset=offset, direction=direction)
        request = 'channels/{}/subscriptions'.format(channel_id)
        return self._get(request, params=params)

    @oauth_required
    def get_channel_sub_by_user(self, channel_id, user_id):
        request = 'channels/{}/subscriptions/{}'.format(channel_id, user_id)
        return self._get(request)

    def get_channel_videos(
            self,
            channel_id,
            limit=None,
            offset=None,
            broadcast_type=None,
            language=None,
            sort=None):
        parameter_check(
            limit=limit,
            broadcast_type=broadcast_type,
            language=language,
            sort=sort)
        params = dict_gen(
            limit=limit,
            offset=offset,
            broadcast_type=broadcast_type,
            language=language,
            sort=sort)
        request = 'channels/{}/videos'.format(channel_id)
        return self._get(request, params=params)

    @oauth_required
    def start_channel_commercial(self, channel_id):
        request = 'channels/{}/commercial'.format(channel_id)
        self._post(request)

    @oauth_required
    def restart_channel_stream_key(self, channel_id):
        request = 'channels/{}/stream_key'.format(channel_id)
        self._delete(request)

    @oauth_required
    def get_channel_community(self, channel_id):
        request = 'channels/{}/community'.format(channel_id)
        self._get(request)

    @oauth_required
    def set_channel_community(self, channel_id, community_id):
        request = 'channels/{}/community/{}'.format(channel_id, community_id)
        self._put(request)

    def delete_channel_community(self, channel_id, community_id):
        request = 'channels/{}/community/{}'.format(channel_id, community_id)
        self._delete(request)
