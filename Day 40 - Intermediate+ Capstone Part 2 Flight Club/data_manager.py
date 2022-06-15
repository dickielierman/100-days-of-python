import requests as req
from os import environ as env

# tequila pw 6J#tsLe7xaYqz!!

sheety_api = f'https://api.sheety.co/{env.get("SHEETY_USER")}/flightDeals'
SHEETY_HEADER = {"Content-Type": "application/json","Authorization": env.get("SHEETY_BEARER")}

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = self.current_sheet()

    def current_sheet(self):
        return req.get(f"{sheety_api}/prices", headers=SHEETY_HEADER).json()['prices']

    def update_iata_codes(self, row, data):
        upd = {
            "price": {
                "iataCode": data
            }
        }
        resp = req.put(f"{sheety_api}/prices/{row}", json=upd, headers=SHEETY_HEADER)

    def update_lowest_price(self, row, data):

        upd = {
            "price": {
                "lowestPrice": data
            }
        }
        resp = req.put(f"{sheety_api}/prices/{row}", json=upd, headers=SHEETY_HEADER)

    def user_email_available(self, email):
        res = req.get(f"{sheety_api}/users", headers=SHEETY_HEADER).json()['users']
        if len([item for item in res if item["email"] == email]) > 0:
            return False
        else:
            return True
    def add_user(self,first, last, email):
        j={
            "user":{
                "firstName": first,
                "lastName": last,
                "email": email
            }
        }
        res = req.post(f"{sheety_api}/users", headers=SHEETY_HEADER, json=j)

    def current_users(self):
        return req.get(f"{sheety_api}/users", headers=SHEETY_HEADER).json()['users']