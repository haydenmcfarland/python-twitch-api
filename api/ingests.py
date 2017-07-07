from api.base import TwitchBase


class Ingests(TwitchBase):
    def get_ingest_server_list(self):
        request = 'ingests'
        return self._request('get', request)

