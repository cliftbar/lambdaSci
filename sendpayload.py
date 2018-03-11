import requests
import json

payload = {
    'lat1': 50.5
    ,'lat2': 58.5
    ,'lon1': 3.6
    ,'lon2': 3.4
    ,'unit': 'kilometers'
}
url = 'http://localhost:3000/haversine'

#req = requests.get(url, json=payload)
#req = requests.get(url)
req = requests.post(url, json=payload)

print(req.status_code)
if req.status_code == 200:
    print(req.json())
else:
    print(req.text)