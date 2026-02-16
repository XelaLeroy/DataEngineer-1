import requests
import json
import psycopg2

api_url = 'https://api.openweathermap.org/data/2.5/weather?lat=43.55&lon=-0.317&appid=79ff85364874a4f637c5817fea6f8bd9&lang=FR&units=metric'


with requests.get(api_url) as response:
    data = response.json()

json_data = json.dumps(data)

weather=data['main']
wind=data['wind']

temperature=weather['temp']
wind_speed=wind['speed']
humidity=weather['humidity']

connection = psycopg2.connect(database="weather", user="alexandre", password="", host="localhost", port=5433)

with connection.cursor() as cur :
    cur.execute("INSERT INTO weather_city (temperature,wind_speed,humidity) VALUES (%s,%s,%s)",(temperature,wind_speed,humidity))
    cur.execute("SELECT * from weather_city")
    # Fetch all rows from database
    record = cur.fetchall()

print("Data from Database:- ", record)

connection.commit()

print(wind_speed,humidity)

# print(temperature)
