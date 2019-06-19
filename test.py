from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '10',
    'convert': 'USD',
    'sort': 'volume_24h'

}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '9ceb39d2-4c14-43db-8635-1a61ae7f5882',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
