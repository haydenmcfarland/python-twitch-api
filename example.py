from twitch_api import TwitchAPI

if __name__ == '__main__':
    client_id = '[client_id_here]'
    oauth_token = None
    api_caller = TwitchAPI(client_id, oauth_token)
    print(api_caller.chat.get_all_emoticons())
