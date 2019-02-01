import json
import requests
from writeas import NewClient

from settings import auth_token, w_token
from arena import getBlock



def block2Post(id):
    c = NewClient()
    c.setToken(w_token)

    block = getBlock(id)

    body = block['content']
    title = block['title']

    post = c.createPost(body, title)

    return post

def post2Block(id, channel):
    c = NewClient()
    c.setToken(w_token)

    post = c.retrievePost(id)


    title = post["title"]
    content = post["body"]

    data = {
        "content" : content,
        "title": title,
        }

    try:
        uri = 'https://api.are.na/v2/channels/' + '%s/blocks' % channel

        r = requests.post(uri, data=json.dumps(data),
        headers={"Authorization": "Bearer %s" % auth_token,
            "Content-Type": "application/json"}
                )

    except Exception as e:
        print "Exception in createBlock: %s" % e
        return e

    return r.json()
