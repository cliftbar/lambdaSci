import json

def linearInterpolation(x, x1, x2, y1, y2):
    """
    :param x:
    :param x1:
    :param x2:
    :param y1:
    :param y2:
    :return: y
    """
    return (((y2 - y1) / (x2 - x1)) * (x - x1)) + y1

def linearHandler(event, context):
    try:
        try:
            payload = json.loads(event['body'])
            point1 = payload['point1']
            point2 = payload['point2']
            x = float(payload['x'])
        except Exception as e:
            raise Exception("Invalid json payload: " + str(e))
        
        y = linearInterpolation(x, point1['x'], point2['x'], point1['y'], point2['y'])

        data = {
            'y': y
        }
        ret = {'statusCode': 200,
                'body': json.dumps(data),
                'headers': {'Content-Type': 'application/json'}}
    except Exception as e:
        ret = {'statusCode': 500
                ,'body': str(e)
                ,'headers': {'Content-Type': 'application/json'}
            
            }
    return ret

def linearApiHelp(event, context):
    data = {'test:': "hello"}
    ret = {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}
    }
    return ret
