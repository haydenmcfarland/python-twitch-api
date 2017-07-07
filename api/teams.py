from api.base import TwitchBase
from api.other.helper import dict_gen, parameter_check
from api.other.constants import *


class Teams(TwitchBase):
    def get_all_teams(self, limit=25, offset=DEFAULT_OFFSET):
        request = 'teams'
        params = dict_gen(limit=limit, offset=offset)
        return self._get(request, params=params)

    def get_team(self, team_name):
        request = 'teams/{}'.format(team_name)
        return self._get(request)
