import requests

token = '6705796825:AAF_-mcvB6AtmBVFhBfevnpx9pJTU6Awj-I'
method = 'sendMessage'

url = f'https://api.telegram.org/bot{token}/{method}'
data = {
    'text': 'ok',
    'chat_id': 1258594598
}

requests.post(url=url, json=data)
