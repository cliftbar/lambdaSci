import requests
import json

payload = {
    'lat1': 50.5
    ,'lat2': 58.5
    ,'lon1': 3.6
    ,'lon2': 3.4
    ,'unit': 'kilometers'
}
local_url = 'http://localhost:3000/haversine'
#live_url = 'https://0hed7331f9.execute-api.us-east-1.amazonaws.com/Prod/haversine'

#req = requests.get(url, json=payload)
#req = requests.get(url)
#req = requests.post(live_url, json=payload)
req = requests.post(local_url, json=payload)

print(req.status_code)
if req.status_code == 200:
    print(req.json())
else:
    print(req.text)