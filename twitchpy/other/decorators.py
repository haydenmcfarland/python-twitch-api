from twitchpy.other.exceptions import TwitchOauthError


def oauth_required(func):
    def wrapper(*args, **kwargs):
        if not args[0]._oauth_token:
            raise TwitchOauthError("Invalid oauth token: {}".format(args[0]._oauth_token))
        return func(*args, **kwargs)
    return wrapper
