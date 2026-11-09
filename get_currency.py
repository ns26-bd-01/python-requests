from requests import get


url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/'

response = get(url)
data = response.json()

print(data)

