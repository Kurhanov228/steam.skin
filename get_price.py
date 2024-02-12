import requests
from config import *
import time
from pprint import pprint
def tuke_prise(item_nameid,session):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'country': 'RU',
        'language': 'russian',
        'currency': '1',
        'item_nameid': item_nameid,
    }
    response = session.get('https://steamcommunity.com/market/itemordershistogram', params=params, headers=headers, proxies=PROXIES,)
    response.raise_for_status()
    return response.json()["sell_order_graph"][0][0]

