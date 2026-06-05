import requests
import json
from datetime import datetime

headers = {
    "User-Agent": "weather-map"
}

output = {
    
    "office": "BOU",
    "boundaries": {}
}

for x in range(40, 70):
    for y in range(60, 110):

        url = f"https://api.weather.gov/gridpoints/BOU/{x},{y}/"

        try:

            r = requests.get(url, headers=headers, timeout=20)

            if r.status_code != 200:
                continue

            forecast = r.json()

            geometry = forecast["geometry"]

            

            key = f"{x}_{y}"
            output["boundaries"][key] = geometry

            

        except Exception as e:

            print(f"Failed {x},{y}: {e}")

with open("data/boundaries.json", "w") as f:

    json.dump(output, f, indent=2, sort_keys=True)
