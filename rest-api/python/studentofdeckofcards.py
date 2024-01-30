import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
