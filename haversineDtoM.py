import json
import math

def haversineDegreesToMeters(lat_1, lon_1, lat_2, lon_2):
    """
    Haversine equation for finding the distance between two lat-lon points in meters.
    :param lat_1: first latitude point
    :param lon_1: first longitude point
    :param lat_2: second latitude point
    :param lon_2: second longitude point
    :returns: distance in meters
    :reference: http://www.movable-type.co.uk/scripts/latlong.html
    :reference: http://stackoverflow.com/questions/4102520/how-to-transform-a-distance-from-degrees-to-metres
    """
    r = 6371000
    delta_lat = math.radians(lat_2 - lat_1)
    delta_lon = math.radians(lon_2 - lon_1)

    a = ((math.sin(delta_lat / 2) ** 2) +
         math.cos(math.radians(lat_1)) * math.cos(math.radians(lat_2)) *
         (math.sin(delta_lon / 2) ** 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return r * c

def handler(event, context):
    # e = event["x"]
    
    lat1 = float(event['queryStringParameters']['lat1'])
    lat2 = float(event['queryStringParameters']['lat2'])
    lon1 = float(event['queryStringParameters']['lon1'])
    lon2 = float(event['queryStringParameters']['lon2'])
    
    d = haversineDegreesToMeters(lat1, lon1, lat2, lon2)
    
    data = {
        'distance': d,
        'event': format(event)
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}