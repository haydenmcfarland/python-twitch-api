from twitchpy.other.helper import dict_gen
from twitchpy.v5.base import return_on_ok
import requests


class Oauth:
    @staticmethod
    def acf_connect_link(
            client_id,
            redirect_uri,
            scope=None,
            force_verify=None,
            nonce=None,
            state=None):
        request = 'https://api.twitch.tv/kraken/oauth2/authorize?'
        params = dict_gen(
            client_id=client_id,
            redirect_uri=redirect_uri,
            response_type='code',
            scope=scope,
            force_verify=force_verify,
            nonce=nonce,
            state=state)
        params_str = '&'.join(
            '{}={}'.format(
                k, params[k]) for k in params.keys())
        return request + params_str

    @staticmethod
    def acf_request(client_id, client_secret, code, redirect_uri, state=None):
        request = 'https://api.twitch.tv/kraken/oauth2/token'
        params = dict_gen(
            client_id=client_id,
            client_secret=client_secret,
            code=code,
            grant_type='authorization_code',
            redirect_uri=redirect_uri,
            state=state)
        return return_on_ok(requests.post(request, params=params))
