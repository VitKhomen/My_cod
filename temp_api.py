import requests

api_url = "https://api.openweathermap.org/data/2.5/weather"

city = input('Город? ')

params = {
    'q': city,
    'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7',
    'units': 'metric'
}

res = requests.get(api_url, params=params)

print(res.status_code)


temp = res.json()
print(temp)
print(temp['main']['temp'])

print(f"Температура в {city} {temp['main']['temp']}")
