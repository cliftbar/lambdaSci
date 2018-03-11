import json
import math
import enum
import pint

ureg = pint.UnitRegistry()

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

def haversine(lat1, lon1, lat2, lon2, unit = 'meters'):
    d = haversineDegreesToMeters(lat1, lon1, lat2, lon2) * ureg.meter
    converted = d.to(unit)

    return converted

def handler(event, context):
    try:
        try:
            payload = json.loads(event['body'])
            lat1 = float(payload['lat1'])
            lat2 = float(payload['lat2'])
            lon1 = float(payload['lon1'])
            lon2 = float(payload['lon2'])
        except Exception as e:
            raise Exception("Invalid json payload: " + str(e))
        
        try:
            unit = payload['unit'] or 'meters'
        except:
            unit = 'meters'

        try:
            ureg.parse_unit_name(unit)
        except:
            raise Exception("Invalid path parameter: " + unit)

        d = haversine(lat1, lon1, lat2, lon2, unit)

        data = {
            'distance': d.magnitude
            ,'unit': str(d.units)
            #,'event': format(event)
        }
        ret = {'statusCode': 200,
                'body': json.dumps(data),
                'headers': {'Content-Type': 'application/json'}}
    except KeyError as e:
        ret = {'statusCode': 500
                ,'body': 'invalid path for : ' + str(e)
                ,'headers': {'Content-Type': 'application/json'}
            }
    except Exception as e:
        ret = {'statusCode': 500
                ,'body': str(e)
                ,'headers': {'Content-Type': 'application/json'}
            
            }
    return ret
    
def apihelphandler(event, context):
    data = {
        '/haversine': {
            'queryString': {
                'lat1': 'first point latitude'
                ,'lon1': 'first point longitude'
                ,'lat2': 'second point latitude'
                ,'lon2': 'second point longitude'
            }
            ,'return': 'distance from point 1 to point 2 in meters'
        }
        ,'/haversine/{unit}': {
            'queryString': {
                'lat1': 'first point latitude'
                ,'lon1': 'first point longitude'
                ,'lat2': 'second point latitude'
                ,'lon2': 'second point longitude'
                ,'description': 'lat and lon for points 1 and 2'
            }
            ,'path param "{unit}': {
                'options': ['meters', 'kilometers', 'miles']
                ,'description': 'return unit of distance'
            }
            ,'returns': 'distance and unit from point 1 to point 2'
        }
        ,'haversine/api': 'api information'
    }
    ret = {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}
    }
    return ret