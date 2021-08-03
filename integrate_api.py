import requests

def integrate_api(game):

    # twitch token get
    urlTwitch = 'https://id.twitch.tv/oauth2/token'
    headersTwitch = {'client_id': 'a146740t3ncae5ov0u7pjwwl12zrpm',
                     'client_secret': 'rai1tprpb8cgc81ty05moimuk2fneo',
                     'grant_type': 'client_credentials'}
    r = requests.post(urlTwitch, data=headersTwitch)
    access_token = r.json()['access_token']

    # get game info
    game = '"' + f'{game}' + '"'

    urlgame = 'https://api.igdb.com/v4/games'

    headersIGDB = {'Client-ID': 'a146740t3ncae5ov0u7pjwwl12zrpm',
                   'Authorization': 'Bearer ' + access_token}

    dataQuery_game = f'search {game}; fields name, franchises,game_engines,player_perspectives; where version_parent ' \
                     f'= n; limit 1; '

    r3 = requests.post(urlgame, headers=headersIGDB, data=dataQuery_game)

    if r3.json() == []:
        franchise_num = None
        game_eng_num = None
        plr_prspctv_num = None
        franchises_name = None
        game_engines_name = None
        player_perspectives_name = None
    else:

        try:
            franchise_num = r3.json()[0]['franchises'][0]
            # Get franchises
            urlfranchise = 'https://api.igdb.com/v4/franchises'
            dataQuery_game = f'fields id, name; where id = {franchise_num};'

            r4 = requests.post(urlfranchise, headers=headersIGDB, data=dataQuery_game)

            franchises_name = r4.json()[0]['name']
        except KeyError:
            franchise_num = None
            franchises_name = None

        try:

            game_eng_num = r3.json()[0]['game_engines'][0]
            # Get game engines

            urlgame_engine = 'https://api.igdb.com/v4/game_engines'
            dataQuery_game_engines = f'fields id, name; where id = {game_eng_num};'

            r5 = requests.post(urlgame_engine, headers=headersIGDB, data=dataQuery_game_engines)

            game_engines_name = r5.json()[0]['name']
        except KeyError:
            game_eng_num = None
            game_engines_name = None

        try:
            plr_prspctv_num = r3.json()[0]['player_perspectives']

            # Get player_perspectives
            player_perspectives_name = []
            for i in range(len(plr_prspctv_num)):
                urlgame_engine = 'https://api.igdb.com/v4/player_perspectives'
                dataQuery_game_engines = f'fields id, name; where id = {plr_prspctv_num[i]};'

                r6 = requests.post(urlgame_engine, headers=headersIGDB, data=dataQuery_game_engines)

                player_perspectives_name.append(r6.json()[0]['name'])
        except KeyError:
            plr_prspctv_num = None
            player_perspectives_name = None

    return franchise_num, game_eng_num, plr_prspctv_num, franchises_name, game_engines_name, player_perspectives_name


