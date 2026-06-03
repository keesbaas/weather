import requests
import json
from datetime import datetime

URL = "https://api.weather.gov/gridpoints/BOU/61,66/forecast/hourly"

headers = {
    "User-Agent": "colorado-weather-map (your-email@example.com)"
}

r = requests.get(URL, headers=headers)
data = r.json()

periods = data["properties"]["periods"][:24]

out = {
    "generated_at": datetime.utcnow().isoformat() + "Z",
    "location": "BOU/61,66",
    "hours": []
}

for p in periods:
    out["hours"].append({
        "time": p["startTime"],
        "temperature": p["temperature"],
        "windSpeed": p["windSpeed"],
        "windDirection": p["windDirection"],
        "dewpoint": p.get("dewpoint", {}).get("value")
    })

# overwrite file every run
with open("data/weather.json", "w") as f:
    json.dump(out, f, indent=2)
