import requests
from twitchpy.other.constants import *
from twitchpy.other.helper import dict_gen


def return_on_ok(response):
    response.raise_for_status()
    if response.status_code == 200:
        return response.json()


class TwitchBase:
    def __init__(self, client_id, oauth_token=None):
        self._root = TWITCH_API_V5_ROOT
        self._client_id = client_id
        self._oauth_token = oauth_token
        self._headers = dict_gen(
            Accept=TWITCH_API_V5_ACCEPT,
            Authorization=self._oauth_token)
        self._headers['Client-ID'] = self._client_id

    def _get(self, path, params=None):
        response = requests.get(
            self._root + path,
            params=params,
            headers=self._headers)
        return return_on_ok(response)

    def _post(self, path, json=None, params=None):
        response = requests.post(
            self._root + path,
            json=json,
            params=params,
            headers=self._headers)
        return return_on_ok(response)

    def _put(self, path, json=None, params=None):
        response = requests.put(
            self._root + path,
            json=json,
            params=params,
            headers=self._headers)
        return return_on_ok(response)

    def _delete(self, path, params=None):
        response = requests.delete(
            self._root + path,
            params=params,
            headers=self._headers)
        return return_on_ok(response)
