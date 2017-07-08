# python-twitch-api
### A Python Implementation of Twitch's API (v5)
[Twitch API v5 Reference](https://dev.twitch.tv/docs/)

## Details

- Functional
- Function parameters are the same as outlined in the Twitch API v5 Reference.
- Function names are similar to Twitch API v5 Reference
- All function calls return the JSON objects

## Install

#### Install Dependency

```
$ pip install requests
```

#### Not setup as a package yet.

## Usage Example

```

from twitch_api import TwitchAPI

if __name__ == '__main__':
    client_id = '[client_id_here]'
    oauth_token = '[oauth_token]'
    api_caller = TwitchAPI(client_id, oauth_token)
    print(api_caller.chat.get_all_emoticons())
    
```
## TODO:
- Minimize Python Code
- Data/Query Parameter Validation
- Oauth Scope Checking
- Constants (Supported Languages...)
- Function docstrings
- Extenstions (Embedded Chat, Video Uploading...)
