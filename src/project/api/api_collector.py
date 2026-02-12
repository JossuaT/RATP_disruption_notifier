import requests, json

from functions import get_secret


host = "https://prim.iledefrance-mobilites.fr/marketplace"
path = "/disruptions_bulk/disruptions/v2"

url = host + path

# RER A
# C01742
# Métro 4
# C01374

url="https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/line_reports/lines/line%3AIDFM%3AC01742/line_reports?count=100"

payload = {}
headers = {
  'apiKey': get_secret("API_KEY")
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()

with open('data.json', 'w', encoding="utf-8") as f:
  json.dump(data, f, indent=4, ensure_ascii=False, sort_keys=True)
