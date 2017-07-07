# Twitch v5 API Base Configuration
ROOT = 'https://api.twitch.tv/kraken/'
ACCEPT = 'application/vnd.twitchtv.v5+json'

# Temporary Client Identifier for Testing
CID = 'NONE'

# Twitch v5 API Constants - (Need to redo and make them relegated to specific groups)
DIRECTION_ASC = 'asc'
DIRECTION_DESC = 'desc'
VALID_DIRECTIONS = [DIRECTION_ASC, DIRECTION_DESC]
MAX_OBJECT_LIMIT = 100
DEFAULT_OBJECT_LIMIT = 25
DEFAULT_VIDEO_LIMIT = 10
DEFAULT_OFFSET = 0
BROADCAST_TYPES = ['archive', 'highlight', 'upload']
DEFAULT_BROADCAST = ','.join(BROADCAST_TYPES)
LANGUAGES = ['en', 'es']
DEFAULT_LANGUAGES = ','.join(LANGUAGES)
SORT_TYPES = ['views', 'time']
DEFAULT_SORT = 'time'

