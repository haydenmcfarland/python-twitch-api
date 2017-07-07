import requests

from api.other.constants import ROOT, ACCEPT
from api.other.helper import dict_gen


class TwitchBase:
    """ Base class for requests using Twitch API v5 """
    def __init__(self, cid, oauth_token=None):
        self._root = ROOT
        self._cid = cid
        self._oauth_token = oauth_token
        self._headers = dict_gen(Accept=ACCEPT, Authorization=self._oauth_token)
        self._headers['Client-ID'] = self._cid

    @staticmethod
    def _return_on_ok(response):
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()

    def _request(self, req_type, path, json=None, params=None):
        req_type = req_type.lower()
        if req_type == "get":
            request = requests.get(self._root+path, params=params, headers=self._headers)
            return TwitchBase._return_on_ok(request)
        elif req_type == "post":
            request = requests.post(self._root+path, json=json, params=params, headers=self._headers)
            return TwitchBase._return_on_ok(request)
        elif req_type == "put":
            request = requests.put(self._root+path, json=json, params=params, headers=self._headers)
            return TwitchBase._return_on_ok(request)
        elif req_type == "delete":
            request = requests.delete(self._root+path, params=params, headers=self._headers)
            return TwitchBase._return_on_ok(request)
        else:
            raise Exception("Invalid request type. Valid: {get, post, put, delete}")
