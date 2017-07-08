from twitchpy.other.helper import dict_gen
from twitchpy.v5.base import TwitchBase


class Teams(TwitchBase):
    def get_all_teams(self, limit=None, offset=None):
        request = 'teams'
        params = dict_gen(limit=limit, offset=offset)
        return self._get(request, params=params)

    def get_team(self, team_name):
        request = 'teams/{}'.format(team_name)
        return self._get(request)
