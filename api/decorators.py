from api.exceptions import TwitchOauthError


def oauth_required(func):
    def wrapper(*args, **kwargs):
        if not args[0]._oauth_token:
            raise TwitchOauthError
        return func(*args, **kwargs)
    return wrapper
