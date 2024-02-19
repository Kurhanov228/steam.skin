import time

import requests

from get_price import tuke_prise
from send_bot import *
from config import *


token = TOKEN
chat_id = CHAT_ID
message = MESSAGE

session = requests.Session()
session.proxies.update(PROXIES)


while True:
    for item_nameide, cena in ID_ITEMS.items():
        aktual = tuke_prise(item_nameide,session)
        if aktual <= cena:
            message  = f'Проснись, скин пора купить{item_nameide}'
            message_send(token, message + item_nameide ,chat_id)
        time.sleep(DILEY)
