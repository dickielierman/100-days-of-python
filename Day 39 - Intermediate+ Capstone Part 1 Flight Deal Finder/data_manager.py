import requests as req
from os import environ as env

# tequila pw 6J#tsLe7xaYqz!!

sheety_api = f'https://api.sheety.co/{env.get("SHEETY_USER")}/flightDeals/prices'
SHEETY_HEADER = {"Content-Type": "application/json","Authorization": env.get("SHEETY_BEARER")}

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = self.current_sheet()

    def current_sheet(self):
        return req.get(sheety_api, headers=SHEETY_HEADER).json()['prices']

    def update_iata_codes(self, row, data):
        upd = {
            "price": {
                "iataCode": data
            }
        }
        resp = req.put(f"{sheety_api}/{row}", json=upd, headers=SHEETY_HEADER)

    def update_lowest_price(self, row, data):
        upd = {
            "price": {
                "lowestPrice": data
            }
        }
        resp = req.put(f"{sheety_api}/{row}", json=upd, headers=SHEETY_HEADER)
