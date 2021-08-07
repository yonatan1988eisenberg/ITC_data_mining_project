import requests


def update_twitch_header():
    """
    This function gets the twitch token and integrates its into the header which it returns
    """

    # get twitch token
    twitch_url = 'https://id.twitch.tv/oauth2/token'
    twitch_header = {'client_id': 'a146740t3ncae5ov0u7pjwwl12zrpm',
                     'client_secret': 'rai1tprpb8cgc81ty05moimuk2fneo',
                     'grant_type': 'client_credentials'}
    r = requests.post(twitch_url, data=twitch_header)
    access_token = r.json()['access_token']

    igdb_header = {'Client-ID': 'a146740t3ncae5ov0u7pjwwl12zrpm',
                   'Authorization': 'Bearer ' + access_token}
    return igdb_header
