import requests
from pprint import pprint
API_KEY = "M_96d-q8y9mjB3_NrEDHwe_8A8g3G8V9"
SEARCH_KEY = "y30Ug0863wuSNFpXv0UXgQjHQX6K5rXY"
API_URL = "https://tequila-api.kiwi.com"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iata_code(self, city):
        search = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(f"{API_URL}/locations/query", headers={"apikey":API_KEY}, params=search).json()['locations']
        return response[0]['code']

    def get_lowest_price(self):
        search = {
            "fly_from": "ATL",
            "fly_to": "NYC",
            "dateFrom": "06/08/2022",
            "dateTo": "01/07/2023",
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "USD",
            "max_stopovers": 0
        }
        response = requests.get(f"{API_URL}/v2/search", headers={"apikey": SEARCH_KEY}, params=search).json()
        lowest_price = 0
        for data in response['data']:
            if lowest_price == 0:
                lowest_price = data["price"]
            elif data["price"] < lowest_price:
                lowest_price = data["price"]

        return lowest_price
