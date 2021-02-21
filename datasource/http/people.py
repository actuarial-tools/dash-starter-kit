import requests
from service.util import starwar_http_client


def all():
    result = starwar_http_client('people/')
    return result.json()


def get(id: int):
    result = starwar_http_client('people/{}'.format(id))
    return result.json()
