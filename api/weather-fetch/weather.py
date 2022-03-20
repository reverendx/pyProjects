import requests
API_KEY = "ADD YOUR TOKEN HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Pick a city!: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data ["weather"][0]["description"]
    temperature = data["main"]["temp"]
    print("Weather: ", weather)
    print("Temperature: ",temperature)
else:
    print("OOPS! Couldn't fetch that City, try again")
