from twitchpy.other.exceptions import TwitchOauthError


def oauth_required(scope=None):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            # Need to add scope check
            if not args[0]._oauth_token:
                raise TwitchOauthError("Invalid oauth token: {}".format(args[0]._oauth_token))
            return func(*args, **kwargs)
        return wrapper
    return real_decorator
