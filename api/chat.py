from api.base import TwitchBase


class Chat(TwitchBase):
    def get_badges_by_channel(self, channel_id):
        request = 'chat/{}/badges'.format(channel_id)
        return self._request('get', request)

    def get_emoticons_by_set(self, emotesets=None):
        params = dict()
        params['emotesets'] = emotesets
        request = 'chat/emoticon_images'
        return self._request('get', request, params=params)

    def get_all_emoticons(self):
        request = 'chat/emoticons'
        return self._request('get', request)
