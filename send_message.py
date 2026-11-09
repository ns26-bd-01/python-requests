from os import getenv

from dotenv import load_dotenv
import requests


load_dotenv('.env')

token = getenv('TOKEN')
method = 'sendMessage'

url = f'https://api.telegram.org/bot{token}/{method}'
data = {
    'text': 'ok',
    'chat_id': 1258594598
}

requests.post(url=url, json=data)
