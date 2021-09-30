import requests as rq

URL_BASE = "https://api.agify.io/?name"

def search_name(name):
    response = rq.get(f'{URL_BASE}={name}')
    return response.json()
   