import requests


def fetch_api_val(key, val, header):
    """
    This function gets a url and an id and fetch a value from the API
    :param key:
    :param val:
    :param header:
    :return:
    """
    if isinstance(val, list):
        val = val[0]
    url = f'https://api.igdb.com/v4/{key}'
    query = f'fields id, name; where id = {val};'
    data = requests.post(url, headers=header, data=query).json()[0]['name']

    return data
