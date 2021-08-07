import requests
from fetch_api_val import fetch_api_val

# todo: arrange nicely.


def get_game_api_data(game, api_header):

    # # twitch token get
    # urlTwitch = 'https://id.twitch.tv/oauth2/token'
    # headersTwitch = {'client_id': 'a146740t3ncae5ov0u7pjwwl12zrpm',
    #                  'client_secret': 'rai1tprpb8cgc81ty05moimuk2fneo',
    #                  'grant_type': 'client_credentials'}
    # r = requests.post(urlTwitch, data=headersTwitch)
    # access_token = r.json()['access_token']
    # headersIGDB = {'Client-ID': 'a146740t3ncae5ov0u7pjwwl12zrpm',
    #                'Authorization': 'Bearer ' + access_token}

    # get game info
    game = f'"{game}"'
    url_game = 'https://api.igdb.com/v4/games'
    api_data_dict = {}

    query = f'search {game}; fields name, franchises,game_engines,player_perspectives; where version_parent ' \
            f'= n; limit 1; '

    game_data = requests.post(url_game, headers=api_header, data=query)
    # if exists: r3.json() = [{'id': 1029, 'franchises': [596], 'game_engines': [1051],
    #                          'name': 'The Legend of Zelda: Ocarina of Time', 'player_perspectives': [2]}]
    if game_data.json():
        # return game_data.json()[0]
        for col in ['franchises', 'game_engines', 'player_perspectives']:
            if col in set(game_data.json()[0].keys()):
                api_data_dict[col] = fetch_api_val(col, game_data.json()[0][col][0], api_header)
            else:
                api_data_dict[col] = None

    return api_data_dict

        # try:
        #     franchise_num = game_data.json()[0]['franchises'][0]
        #     # Get franchises
        #     urlfranchise = 'https://api.igdb.com/v4/franchises'
        #     dataQuery_game = f'fields id, name; where id = {franchise_num};'
        #
        #     r4 = requests.post(urlfranchise, headers=headersIGDB, data=dataQuery_game)
        #
        #     franchises_name = r4.json()[0]['name']
        # except KeyError:
        #     franchise_num = None
        #     franchises_name = None

    #     try:
    #
    #         game_eng_num = r3.json()[0]['game_engines'][0]
    #         # Get game engines
    #
    #         urlgame_engine = 'https://api.igdb.com/v4/game_engines'
    #         dataQuery_game_engines = f'fields id, name; where id = {game_eng_num};'
    #
    #         r5 = requests.post(urlgame_engine, headers=headersIGDB, data=dataQuery_game_engines)
    #
    #         game_engines_name = r5.json()[0]['name']
    #     except KeyError:
    #         game_eng_num = None
    #         game_engines_name = None
    #
    #     try:
    #         plr_prspctv_num = r3.json()[0]['player_perspectives']
    #
    #         # Get player_perspectives
    #         player_perspectives_name = []
    #         for i in range(len(plr_prspctv_num)):
    #             urlgame_engine = 'https://api.igdb.com/v4/player_perspectives'
    #             dataQuery_game_engines = f'fields id, name; where id = {plr_prspctv_num[i]};'
    #
    #             r6 = requests.post(urlgame_engine, headers=headersIGDB, data=dataQuery_game_engines)
    #
    #             player_perspectives_name.append(r6.json()[0]['name'])
    #     except KeyError:
    #         plr_prspctv_num = None
    #         player_perspectives_name = None
    #
    # return franchise_num, game_eng_num, plr_prspctv_num, franchises_name, game_engines_name, player_perspectives_name


