import requests

url = "https://api.weather.gov/gridpoints/BOU/61,66/forecast/hourly"

response = requests.get(
    url,
    headers={"User-Agent": "colorado-weather-map"}
)

data = response.json()

temperature = []
wind_speed = []
wind_direction = []
dewpoint = []
time = []

for period in data["properties"]["periods"][:24]:

    time.append(period["startTime"])
    temperature.append(period["temperature"])
    wind_speed.append(period["windSpeed"])
    wind_direction.append(period["windDirection"])
    dewpoint.append(period["dewpoint"]["value"])

print(temperature)
