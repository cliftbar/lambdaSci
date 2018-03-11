import json
import pint
ureg = pint.UnitRegistry()

def handler(event, context):
    ret = {}
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

        print(unit)
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