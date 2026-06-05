import requests
import json
from datetime import datetime

headers = {
    "User-Agent": "weather-map"
}

output = {
    "generated_at": datetime.utcnow().isoformat() + "Z",
    "office": "BOU",
    "gridpoints": {}
}

for x in range(40, 70):
    for y in range(60, 110):

        url = f"https://api.weather.gov/gridpoints/BOU/{x},{y}/forecast/hourly"

        try:

            r = requests.get(url, headers=headers, timeout=20)

            if r.status_code != 200:
                continue

            forecast = r.json()

            periods = forecast["properties"]["periods"][:24]

            cell_data = []

            for p in periods:

                cell_data.append({
                    "time": p["startTime"],
                    "temperature": p["temperature"],
                    "windSpeed": p["windSpeed"],
                    "windDirection": p["windDirection"]
                })

            output["gridpoints"][f"{x}_{y}"] = cell_data

            print(f"Downloaded {x},{y}")

        except Exception as e:

            print(f"Failed {x},{y}: {e}")

with open("data/weather.json", "w") as f:

    json.dump(output, f, indent=2, sort_keys=True)
