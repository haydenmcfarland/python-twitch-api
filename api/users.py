from api.base import TwitchBase
from api.other.decorators import oauth_required
from api.other.helper import dict_gen, parameter_check
from api.other.constants import *


class Users(TwitchBase):

    @oauth_required(scope=SCOPE_USER_READ)
    def get_user(self):
        request = 'user'
        return self._get(request)

    def get_user_by_id(self, user_id):
        request = 'users/{}'.format(user_id)
        return self._get(request)

    @oauth_required(scope=SCOPE_USER_READ)
    def get_users(self, user_id):
        request = 'users'
        params = dict_gen(user_id=user_id)
        return self._get(request, params=params)

    @oauth_required(scope=SCOPE_USER_SUBSCRIPTIONS)
    def get_user_emotes(self, user_id):
        request = 'users/{}/emotes'.format(user_id)
        return self._get(request)

    @oauth_required(scope=SCOPE_USER_SUBSCRIPTIONS)
    def user_sub_by_channel(self, user_id, channel_id):
        request = 'users/{}/subscriptions/{}'.format(user_id, channel_id)
        return self._get(request)

    def get_user_follows(self, user_id, limit=25, offset=0, direction='desc', sortby='created_at'):
        request = 'users/{}/follows/channels'.format(user_id)
        params = dict_gen(limit=limit, offset=offset, direction=direction, sortby=sortby)
        return self._get(request, params)

    def user_follows_by_channel(self, user_id, channel_id):
        request = 'users/{}/follows/channels/{}'.format(user_id, channel_id)
        return self._get(request)

    @oauth_required(scope=SCOPE_USER_FOLLOWS_EDIT)
    def follow_channel(self, user_id, channel_id, notifications=False):
        request = 'users/{}/follows/channels/{}'.format(user_id, channel_id)
        json = dict_gen(notifications=notifications)
        return self._put(request, json=json)

    @oauth_required(scope=SCOPE_USER_FOLLOWS_EDIT)
    def un_follow_channel(self, user_id, channel_id):
        request = 'users/{}/follows/channels/{}'.format(user_id, channel_id)
        return self._delete(request)

    @oauth_required(scope=SCOPE_USER_BLOCKS_READ)
    def get_user_block_list(self, user_id, limit=25, offset=0):
        request = 'users/{}/blocks'.format(user_id)
        params = dict_gen(limit=limit, offset=offset)
        return self._get(request, params=params)

    @oauth_required(scope=SCOPE_USER_BLOCKS_EDIT)
    def block_user(self, source_user_id, target_user_id):
        request = 'users/{}/blocks/{}'.format(source_user_id, target_user_id)
        return self._put(request)

    @oauth_required(scope=SCOPE_USER_BLOCKS_EDIT)
    def un_block_user(self, source_user_id, target_user_id):
        request = 'users/{}/blocks/{}'.format(source_user_id, target_user_id)
        return self._delete(request)

    @oauth_required(scope=SCOPE_VIEWING_ACTIVITY_READ)
    def create_vhs(self, identifier):
        request = 'user/vhs'
        json = dict_gen(identifier=identifier)
        return self._put(request, json=json)

    @oauth_required(scope=SCOPE_USER_READ)
    def check_vhs(self):
        request = 'user/vhs'
        return self._get(request)

    @oauth_required(scope=SCOPE_VIEWING_ACTIVITY_READ)
    def delete_vhs(self):
        request = 'user/vhs'
        return self._delete(request)
