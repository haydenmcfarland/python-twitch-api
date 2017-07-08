from twitchpy.other.helper import dict_gen
from twitchpy.v5.base import TwitchBase


class Chat(TwitchBase):
    def get_badges_by_channel(self, channel_id):
        request = 'chat/{}/badges'.format(channel_id)
        return self._get(request)

    def get_emoticons_by_set(self, emotesets=None):
        params = dict_gen(emotesets=emotesets)
        request = 'chat/emoticon_images'
        return self._get(request, params=params)

    def get_all_emoticons(self):
        request = 'chat/emoticons'
        return self._get(request)
