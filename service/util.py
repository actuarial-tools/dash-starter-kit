import json
import base64
import os
import sys
import requests

STARWARS_URL = 'https://swapi.dev/api/'

def starwars_http_client(params):
    return requests.get('{}{}'.format(STARWARS_URL, params))

def decodeBase64_message(base64_message):
    result = base64_message
    if result:
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        result = json.loads(message_bytes.decode('ascii'))

    return result

# resolve issue with where you call the start scripts
def get_src_path():
    return os.path.dirname(sys.argv[0])


def get_user_id(cookies):
    _cookies = dict(cookies)
    # the id of your cookie
    user_cookie = _cookies.get('_name_of_your_cookie')
    current_user = decodeBase64_message(user_cookie) if user_cookie else None
    return current_user.get('User') if current_user else 'test'
