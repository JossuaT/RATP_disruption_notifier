import requests
import secrets

from project.utils.functions import get_secret


host = "https://prim.iledefrance-mobilites.fr/marketplace"
path = "/disruptions_bulk/disruptions/v2"

url = host + path

payload = {}
headers = {
  'apiKey': get_secret("API_KEY")
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)