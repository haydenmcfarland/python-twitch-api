# twitchpy [wip]
### A Python Implementation of Twitch's API (v5)
[Twitch API v5 Reference](https://dev.twitch.tv/docs/)

## Details

- Python 3
- Function parameters are the same as outlined in the Twitch API v5 Reference.
- Function names are easily translated from Twitch API v5 Reference
- All function calls return JSON objects

## Install

#### Install Dependency

```
$ pip install requirements.txt
```

#### Install *twitchpy*

```
$ python setup.py install
```

## Usage

```
from twitchpy.api import TwitchAPI

if __name__ == '__main__':
    client_id = '{client_id}'
    oauth_token = '{oauth_token}'
    api_caller = TwitchAPI(client_id, oauth_token)
    print(api_caller.chat.get_all_emoticons())
```
## TODO:
- Minimize Python Code
- Constants (Supported Languages...)
- Function docstrings (To help ease of use)
- Extenstions (Video Uploading...)
