import requests
import os
from dotenv import load_dotenv

load_dotenv()


def find_biz(ll, spn, request, locale="ru_RU"):
    server = 'http://search-maps.yandex.ru/v1/'
    params = {'apikey': os.getenv("API_KEY_FINDBIZ"),
              'text': request,
              'lang': locale,
              'll': ll,
              'spn': ','.join((spn, spn)),
              'type': 'biz'}
    response = requests.get(server, params=params).json()
    return [tuple(map(str, response['features'][0]['geometry']['coordinates'])),
            response['features'][0]['properties']['description'],
            response['features'][0]['properties']['CompanyMetaData']['name'],
            response['features'][0]['properties']['CompanyMetaData']['Hours']['text']]
