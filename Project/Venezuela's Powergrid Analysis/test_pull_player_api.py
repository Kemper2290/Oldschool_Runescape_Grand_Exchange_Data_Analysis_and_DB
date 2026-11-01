import requests

url = "https://www.osrsplayercount.com/api/history?start=2026-06-29T20%3A21%3A00.000Z&end=2026-07-06T20%3A21%3A00.000Z&unit=hour&agg=max"

params = {
    "start": "2026-06-29T20:21:00.000Z",
    "end": "2026-07-06T20:21:00.000Z",
    "unit": "hour",
    "agg": "max"
}

response = requests.get(url, params=params)

print(response.json())




