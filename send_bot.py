import requests
import time
from config import *
def message_send(token, message,chat_id):
    send_text = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
    while True:
    
        try:
            response = requests.get(send_text)
            response.raise_for_status()
            return (response)
        except:
            time.sleep(DILEY2)