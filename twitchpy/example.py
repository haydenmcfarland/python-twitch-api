from twitchpy.api import TwitchAPI

if __name__ == '__main__':
    client_id = '{client_id}'
    oauth_token = '{oauth_token}'
    api_caller = TwitchAPI(client_id, oauth_token)
    print(api_caller.chat.get_all_emoticons())
