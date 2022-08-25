import requests

city = input('Input the city name: ')
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)
print(res.text)