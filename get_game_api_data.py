import requests
from fetch_api_val import fetch_api_val


def get_game_api_data(game, api_header):
    """
    This function gets a game's name and a header to fetch data from the IGBN database
    """

    api_data_dict = {}
    # format game info
    game = f'"{game}"'
    url_game = 'https://api.igdb.com/v4/games'
    query = f'search {game}; fields name, franchises,game_engines,player_perspectives; where version_parent ' \
            f'= n; limit 1; '
    game_data = requests.post(url_game, headers=api_header, data=query)
    if game_data.json():
        for col in ['franchises', 'game_engines', 'player_perspectives']:
            if col in set(game_data.json()[0].keys()):
                api_data_dict[col] = fetch_api_val(col, game_data.json()[0][col][0], api_header)
            else:
                api_data_dict[col] = None

    return api_data_dict



