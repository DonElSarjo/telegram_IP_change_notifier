import requests
from requests import get
import time

def telegram_bot_sendtext(bot_message):
    bot_token = 'TOKEN'
    bot_chatID = 'CHAT_ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()

def changeIP(new_ip):
    global external_ip
    external_ip = new_ip

external_ip = ''

while True:
    new_external_ip = get('https://api.ipify.org').text

    if new_external_ip != external_ip:
        changeIP(new_external_ip)
        message = 'Die IP hat sich geändert:\n\n%s\n\nhttps://kis.hosteurope.de/' % external_ip
        telegram_bot_sendtext(message)
    else:
        time.sleep(3600)
