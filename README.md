### twitchpy: A Python Implementation of Twitch's API (v5) (NOT MAINTAINED)
[Twitch API v5 Reference](https://dev.twitch.tv/docs/)

## Install

#### Install Dependency

```
> pip install requirements.txt
```

#### Install *twitchpy*

```
> python setup.py install
```

## Usage

```
from twitchpy.api import TwitchAPI

if __name__ == '__main__':
    client_id = '{client_id}'
    oauth_token = 'OAuth {oauth_token}'
    api_caller = TwitchAPI(client_id, oauth_token)
    print(api_caller.chat.get_all_emoticons())
```

## Other:
- ```outh_token``` should be a string of the form: ```OAuth {{GENERATED_OAUTH_TOKEN}}```
