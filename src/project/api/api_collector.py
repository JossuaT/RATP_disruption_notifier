import requests, json

from project.utils.functions import get_secret, save_as_json


host = "https://prim.iledefrance-mobilites.fr"
path = "/marketplace/disruptions_bulk/disruptions/v2"

url = host + path

# RER A
# C01742
# id > line:IDFM:C01742
# Métro 4
# C01374
# id > line:IDFM:C01374

# La Défense (Grande Arche) - M1
# 
# La DéfenseIDFM:463193 - RER A
# IDFM:monomodalStopPlace:470549

# Disruptions - line A
url=host+"/marketplace/v2/navitia/line_reports/lines/line%3AIDFM%3AC01742/line_reports?count=100"

# Nav
url=host+"/marketplace/v2/navitia/isochrones"

# 
#url=host+"/marketplace/iboo/lines.json"

payload = {}
headers = {
  'apiKey': get_secret("API_KEY")
}

response = requests.request("GET", url, headers=headers, data=payload)


save_as_json(response, 'outputs/data_itineraire.json')