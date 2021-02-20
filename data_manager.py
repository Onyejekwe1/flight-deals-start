import os
import requests

SHEETY_API_URL = "https://api.sheety.co/2a910e6bf759cd9eaf52575d521dadbd/flightDeals/prices"
SHEETY_AUTH = os.environ['SHEETY_AUTH']

sheety_headers = {
    "Authorization": SHEETY_AUTH
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.data = ""

    def get_data(self):
        self.data = requests.get(url=SHEETY_API_URL, headers=sheety_headers).json()['prices']
        print(self.data)

    def set_data(self, data):
        sheet_data = {'price': data}
        self.response = requests.put(url=f"{SHEETY_API_URL}/{data['id']}", json=sheet_data, headers=sheety_headers).json()
        print(self.response)