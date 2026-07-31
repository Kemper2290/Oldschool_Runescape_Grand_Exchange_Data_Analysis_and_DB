
import requests
import json

headers = {
    "User-Agent" : "OSRS-Price-Tracker/1.0"
}

mapping_url = "https://prices.runescape.wiki/api/v1/osrs/mapping"
latest_url = "https://prices.runescape.wiki/api/v1/osrs/latest"

#returns the item list
mapping = requests.get(
    mapping_url,
    headers=headers
).json()

pretty_mapping = json.dumps(mapping[:5],indent=4)
print(pretty_mapping)

#returns the current GE prices
prices = requests.get(
    latest_url,
    headers=headers
).json()["data"]

pretty_prices = json.dumps(dict(list(prices.items())[:5]),indent=4)
print(pretty_prices)

print("Downloaded", len(mapping), "items")


print(mapping[0])
print(prices['4151'])

print(type(mapping))
print(type(prices))