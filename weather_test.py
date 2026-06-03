import requests

url = "https://api.weather.gov/gridpoints/BOU/61,66/forecast/hourly"

response = requests.get(
    url,
    headers={"User-Agent": "colorado-weather-map"}
)

data = response.json()

for period in data["properties"]["periods"][:24]:
    print(
        period["startTime"],
        period["temperature"],
        period["windSpeed"]
    )
