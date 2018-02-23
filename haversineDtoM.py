import json
import math
import enum

class distanceUnitsFromMeters(enum.Enum):
    meters = 1
    kilometers = 0.001
    miles = 0.000621371

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
    
def haversine(lat1, lon1, lat2, lon2, unit = distanceUnitsFromMeters.meters.name):
    d = haversineDegreesToMeters(lat1, lon1, lat2, lon2)
    c = distanceUnitsFromMeters[unit].value
    return d * c

def handler(event, context):
    ret = {}
    try:
        try:
            lat1 = float(event['queryStringParameters']['lat1'])
            lat2 = float(event['queryStringParameters']['lat2'])
            lon1 = float(event['queryStringParameters']['lon1'])
            lon2 = float(event['queryStringParameters']['lon2'])
        except Exception as e:
            raise Exception("Invalid query string: " + str(e))
        
        unit = None
        try:
            unit = event['pathParameters']['unit'] or 'meters'
        except:
            unit = 'meters'
            
        if unit not in distanceUnitsFromMeters.__members__:
            raise Exception("Invalid path parameter: " + unit)
        # if unit not in distanceUnitsFromMeters
        #     raise Exception("unit not available")
        d = haversine(lat1, lon1, lat2, lon2, unit)
        #d = haversineDegreesToMeters(lat1, lon1, lat2, lon2)
        
        data = {
            'distance': d
            ,'unit': unit
            #,'event': format(event)
        }
        ret = {'statusCode': 200,
                'body': json.dumps(data),
                'headers': {'Content-Type': 'application/json'}}
    except KeyError as e:
        ret = {'statusCode': 500
                ,'body': 'invalid path or : ' + str(e)
                ,'headers': {'Content-Type': 'application/json'}
            }
    except Exception as e:
        ret = {'statusCode': 500
                ,'body': str(e)
                ,'headers': {'Content-Type': 'application/json'}
            
            }
    return ret
            