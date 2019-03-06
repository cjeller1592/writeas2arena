import requests
import json
from settings import auth_token



def createBlock(title, content, channel):
    data = {
    "title" : title,
    "content" : content
    }

    try:
        uri = 'https://api.are.na/v2/channels/' + '%s/blocks' % channel

        r = requests.post('https://api.are.na/v2/channels/test-qptctmuz02a/blocks', data=json.dumps(data),
        headers={"Authorization": "Bearer %s" % auth_token,
        "Content-Type": "application/json"}
            )

    except Exception as e:
        print "Exception in createBlock: %s" % e
        return e


    return r.json()




def getBlock(id):

    uri = 'https://api.are.na/v2/blocks/' + id

    try:
        r = requests.get(uri)

    except Exception as e:
        print "Exception in getBlock: %s" % e
        return e

    b = r.json()

    return b
