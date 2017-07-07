from api.constants import MAX_OBJECT_LIMIT, VALID_DIRECTIONS, BROADCAST_TYPES, LANGUAGES, SORT_TYPES
from api.exceptions import TwitchParameterError


# DEPRECATED - Need to create a better parameter checker based on specific groups after API is fully implemented
def parameter_check(limit=None, direction=None, broadcast_type=None, language=None, sort=None, comments=None):
    if limit:
        if limit > MAX_OBJECT_LIMIT:
            raise TwitchParameterError("Maximum number of objects to return is {}.".format(MAX_OBJECT_LIMIT))
    if direction:
        if direction not in VALID_DIRECTIONS:
            raise TwitchParameterError("Invalid direction specified. Valid values:{}".format(VALID_DIRECTIONS))
    if broadcast_type:
        broadcast_type = broadcast_type.split(',')
        if not all(b in BROADCAST_TYPES for b in broadcast_type):
            message = "broadcast_type must be any combination of {} separated by commas.".format(BROADCAST_TYPES)
            raise TwitchParameterError(message)
    if language:
        language = language.split(',')
        if not all(l in LANGUAGES for l in language):
            raise TwitchParameterError("Invalid language specified. Valid values:{}".format(LANGUAGES))
    if sort:
        if sort not in SORT_TYPES:
            raise TwitchParameterError("Invalid sort specified. Valid values:{}".format(SORT_TYPES))
    if comments:
        if comments > 5:
            raise TwitchParameterError("Invalid comments quantity specified. Maximum value is 5.")


def dict_gen(**kwargs):
    filtered_dict = dict()
    for k in kwargs:
        if kwargs[k]:
            filtered_dict[k] = kwargs[k]
    return filtered_dict

