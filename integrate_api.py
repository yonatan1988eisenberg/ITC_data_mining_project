import requests
import json

# twitch token get
urlTwitch = 'https://id.twitch.tv/oauth2/token'
headersTwitch = {'client_id': 'a146740t3ncae5ov0u7pjwwl12zrpm',
                 'client_secret': 'rai1tprpb8cgc81ty05moimuk2fneo',
                 'grant_type': 'client_credentials'}
r = requests.post(urlTwitch, data=headersTwitch)
access_token = r.json()['access_token']

# get game info
game = '"Half-Life 2"'
release_date = 	1428872400
urlgame = 'https://api.igdb.com/v4/games'
headersIGDB = {'Client-ID': 'a146740t3ncae5ov0u7pjwwl12zrpm',
               'Authorization': 'Bearer ' + access_token}

dataQuery_game = f'search {game}; fields name, first_release_date,franchises,expansions,game_engines; where version_parent = n; limit 1;'

r3 = requests.post(urlgame, headers=headersIGDB, data=dataQuery_game)
print(r3.json())
#Get franchises
urlfranchise = 'https://api.igdb.com/v4/franchises'
dataQuery_game = f'fields id, name; where id = 425;'

r4 = requests.post(urlfranchise, headers=headersIGDB, data= dataQuery_game)

print(r4.json())

#Get game engines

urlgame_engine = 'https://api.igdb.com/v4/game_engines'
dataQuery_game_engines = f'fields id, name; where id = 3;'

r5 = requests.post(urlgame_engine, headers=headersIGDB, data= dataQuery_game_engines)

print(r5.json())