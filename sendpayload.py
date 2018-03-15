import requests
import json
import time

haversinePayload = {
    'lat1': 50.5
    ,'lat2': 58.5
    ,'lon1': 3.6
    ,'lon2': 3.4
    ,'unit': 'pounds'
}

linInterpPayload = {
    'point1': {'x': -1, 'y': 1}
    ,'point2': {'x': 3, 'y': -3}
    ,'x': 4
}
#local_url = 'http://localhost:3000/haversine'
local_url = 'http://localhost:3000/interpolation/linear'
live_url_haversine = 'https://0hed7331f9.execute-api.us-east-1.amazonaws.com/Prod/haversine'
live_url_interp = 'https://0hed7331f9.execute-api.us-east-1.amazonaws.com/Prod/interpolation/linear'


req = requests.post(live_url_haversine, json=haversinePayload)
print(req.status_code)
if req.status_code == 200:
    print(req.json())
else:
    print(req.text)

req = requests.post(live_url_interp, json=linInterpPayload)
print(req.status_code)
if req.status_code == 200:
    print(req.json())
else:
    print(req.text)