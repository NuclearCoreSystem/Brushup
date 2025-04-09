import requests

api_key = "your_api_key"
city = input("Enter city: ")

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}$appid={api_key}")
weather_data = response.json

print(f"Current Weather in {city}: {weather_data['weather'][0]['description']}")
