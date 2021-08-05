import requests


def fetch_api_val(key, val, header):
    if isinstance(val, list):
        val = val[0]
    url = f'https://api.igdb.com/v4/{key}'
    query = f'fields id, name; where id = {val};'
    data = requests.post(url, headers=header, data=query).json()[0]['name']

    return data
