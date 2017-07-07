from api.base import TwitchBase
from api.other.constants import DEFAULT_VIDEO_LIMIT
from api.other.decorators import oauth_required
from api.other.helper import dict_gen, parameter_check


class ChannelFeed(TwitchBase):
    def get_multiple_feed_posts(self, channel_id, limit=DEFAULT_VIDEO_LIMIT, cursor=None, comments=5):
        parameter_check(limit=limit, comments=comments)
        params = dict_gen(limit=limit, cursor=cursor, comments=comments)
        request = 'feed/{}/posts'.format(channel_id)
        return self._request('get', request, params=params)

    @oauth_required
    def create_feed_post(self, channel_id, content, share=False):
        request = 'feed/{}/posts'.format(channel_id)
        params = dict_gen(share=share)
        json = dict_gen(content=content)
        return self._request('post', request, json=json, params=params)

    @oauth_required
    def delete_feed_post(self, channel_id, post_id):
        request = 'feed/{}/posts/{}'.format(channel_id, post_id)
        return self._request('delete', request)

    @oauth_required
    def _type_feed_reaction(self, req_type, channel_id, post_id, emote_value):
        request = 'feed/{}/posts/{}/reactions'.format(channel_id, post_id)
        params = dict_gen(emote_id=emote_value)
        return self._request(req_type, request, params=params)

    def create_feed_reaction(self, channel_id, post_id, emote_value):
        return self._type_feed_reaction('post', channel_id, post_id, emote_value)

    def delete_feed_reaction(self, channel_id, post_id, emote_value):
        return self._type_feed_reaction('delete', channel_id, post_id, emote_value)

    def get_feed_comments(self, channel_id, post_id, limit=10, cursor=None):
        parameter_check(limit=limit)
        request = 'feed/{}/posts/{}/comments'.format(channel_id, post_id)
        params = dict_gen(limit=limit, cursor=cursor)
        return self._request('get', request, params=params)

    @oauth_required
    def create_feed_comment(self, channel_id, post_id, content):
        request = 'feed/{}/posts/{}/comments'.format(channel_id, post_id)
        json = dict_gen(content=content)
        return self._request('post', request, json=json)

    @oauth_required
    def delete_feed_comment(self, channel_id, post_id, comment_id):
        request = 'feed/{}/posts/{}/comments/{}'.format(channel_id, post_id, comment_id)
        return self._request('delete', request)

    @oauth_required
    def _type_feed_comment_reaction(self, req_type, channel_id, post_id, comment_id, emote_value):
        request = 'feed/{}/posts/{}/comments/{}/reactions'.format(channel_id, post_id, comment_id)
        params = dict_gen(emote_id=emote_value)
        return self._request(req_type, request, params=params)

    def create_feed_comment_reaction(self, channel_id, post_id, comment_id, emote_value):
        return self._type_feed_comment_reaction('post', channel_id, post_id, comment_id, emote_value)

    def delete_feed_comment_reaction(self, channel_id, post_id, comment_id, emote_value):
        return self._type_feed_comment_reaction('delete', channel_id, post_id, comment_id, emote_value)
