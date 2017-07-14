from time import strftime
from twitchpy.other.helper import dict_gen
class EmbeddedChat:
    def __init__(self, channel, frameborder=0,  scrolling=True, height=500, width=500,):
        self.channel = channel
        self.frameborder = frameborder
        self.scrolling = scrolling
        self.height = height
        self.width = width

    @property
    def iframe(self):
        src_url = 'http://www.twitch.tv/{}/chat'.format(self.channel)
        iframe = '<iframe frameborder="{}" scrolling="{}" id="{}" src="{}" height="{}" width="{}"></iframe>'
        return iframe.format(self.frameborder, self.scrolling, self.channel, src_url, self.height, self.width)


class EmbeddedVideo:
    def __init__(self, channel, frameborder="0",  scrolling=None, allowfullscreen=True, height=500, width=500
                 , autoplay=True, muted=False, time=None):
        self.channel = channel
        self.frameborder = frameborder
        self.scrolling = scrolling
        self.height = height
        self.width = width
        self.allowfullscreen = allowfullscreen
        self.autoplay = autoplay
        self.muted = muted
        self.time = time

    @property
    def iframe(self):
        query_params = dict_gen(autoplay=self.autoplay, muted=self.muted, time=self.time)
        src_url = 'http://player.twitch.tv/?channel={}'.format(self.channel)
        if query_params:
            src_url += '&'+'&'.join('{}="{}"'.format(k, query_params[k]) for k in query_params)
        iframe = '<iframe {}></iframe>'
        params = dict_gen(frameborder=self.frameborder, scrolling=self.scrolling, allowfullscreen=self.allowfullscreen,
                          height=self.height, width=self.width, src=src_url)

        return iframe.format(' '.join('{}="{}"'.format(k, params[k]) for k in params))
