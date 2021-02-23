from service.util import starwars_http_client


def all():
    result = starwars_http_client('people/')
    return result.json()


def get(id: int):
    result = starwars_http_client('people/{}'.format(id))
    return result.json()
