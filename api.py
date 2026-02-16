import requests
import json

api_url = 'https://api.openweathermap.org/data/2.5/weather?lat=43.55&lon=-0.317&appid=79ff85364874a4f637c5817fea6f8bd9&lang=FR&units=metric'


with requests.get(api_url) as response:
    data = response.json()

temp=data['main']



print(data)
