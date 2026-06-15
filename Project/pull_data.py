
import requests

headers = {
    "User-Agent" : "OSRS-Price-Tracker/1.0"
}

mapping_url = "https://prices.runescape.wiki/api/v1/osrs/mapping"
latest_url = "https://prices.runescape.wiki/api/v1/osrs/latest"

mapping = requests.get(
    mapping_url,
    headers=headers
).json()

latest = requests.get(
    latest_url,
    headers=headers
).json()["data"]

print("Downloaded", len(mapping), "items")


print(mapping[0])
print(latest['2'])