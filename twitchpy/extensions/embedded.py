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
