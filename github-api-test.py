#get requirements
#2022-04-15 hjinshin

import pprint
import requests

r = requests.get('https://api.github.com/users/hjinshin')

if r.status_code == 200:
    json_data = r.json()
    pprint.pprint(json_data)
