# python-twitch-api
### A Python Implementation of Twitch's API (v5)
[Twitch API v5 Reference](https://dev.twitch.tv/docs/)

## Details

- Function names are similar to Twitch API v5 Reference
- All function calls return the JSON objects described in the API

## Usage Example

```

from twitch_api import TwitchAPI

if __name__ == '__main__':
    client_id = '[client_id_here]'
    oauth_token = None
    api_caller = TwitchAPI(client_id, oauth_token)
    print(api_caller.chat.get_all_emoticons())
    
```
## TODO:
- Minimize Python Code
- Function Parameter Type Validation
- Data/Query Parameter Validation
- Constants (Supported Languages...)
- Function docstrings
- Extenstions (Embedded Chat, Video Uploading...)
