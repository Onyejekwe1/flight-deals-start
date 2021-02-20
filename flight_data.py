import os
import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

FLIGHT_SEARCH_URL = "https://tequila-api.kiwi.com/v2/search?fly_from=PRG&fly_to=LGW&dateFrom=18/11/2021&dateTo=12/12/2021"
FLIGHT_SEARCH_URL = "https://tequila-api.kiwi.com/v2/search"
FLIGHT_LOCATIONS_URL = "https://tequila-api.kiwi.com/locations/query"


now_date = datetime.now().strftime("%d/%m/%Y")
fut_date = (datetime.now() + relativedelta(months=+6)).strftime("%d/%m/%Y")

flight_headers = {
    "apikey": "ThhutH05Xh8OFtwiBsPApouNuEREcUaM"
}

class FlightSearch:
    def __init__(self):
        pass

    def get_iata_code(self, city):
        params = {
            "term": city
        }
        return requests.get(url=FLIGHT_LOCATIONS_URL, params=params, headers=flight_headers).json()['locations'][0]['code']

    def get_price(self, fly_to):
        params = {
            "fly_from": "EDI",
            "fly_to": fly_to,
            "dateFrom": now_date,
            "dateTo": fut_date
        }
        return requests.get(url=FLIGHT_SEARCH_URL, params=params, headers=flight_headers).json()['data']