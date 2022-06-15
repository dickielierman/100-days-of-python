import requests
from datetime import datetime as dt, timedelta
from pprint import pprint
API_KEY = "M_96d-q8y9mjB3_NrEDHwe_8A8g3G8V9"
SEARCH_KEY = "y30Ug0863wuSNFpXv0UXgQjHQX6K5rXY"
API_URL = "https://tequila-api.kiwi.com"
class FlightData:
    def __init__(self):
        self.api_url = "https://tequila-api.kiwi.com"
        self.tomorrow = (dt.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        self.end = (dt.now() + timedelta(days=(6*30))).strftime("%d/%m/%Y")
        self.base_loc = "ATL"
    #This class is responsible for structuring the flight data.

    def get_lowest_price(self, fly_to):
        search = {
            "fly_from": self.base_loc,
            "fly_to": fly_to,
            "dateFrom": self.tomorrow,
            "dateTo": self.end,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "USD",
            "max_stopovers": 0
        }

        response = requests.get(f"{self.api_url}/v2/search", headers={"apikey": SEARCH_KEY}, params=search).json()
        lowest_price = 0
        if len(response['data']) > 0:
            for data in response['data']:
                if lowest_price == 0:
                    return_data = {
                        "fly_from": data["flyFrom"],
                        "city_from": data["cityFrom"],
                        "fly_to": data["flyTo"],
                        "city_to": data["cityTo"],
                        "price": data["price"],
                        "depart": data["route"][0]["local_departure"].split("T")[0],
                        "return": data["route"][1]["local_departure"].split("T")[0]
                    }
                    lowest_price = data["price"]
                elif data["price"] < lowest_price:
                    return_data = {
                        "fly_from": data["flyFrom"],
                        "city_from": data["cityFrom"],
                        "fly_to": data["flyTo"],
                        "city_to": data["cityTo"],
                        "price": data["price"],
                        "depart": data["route"][0]["local_departure"].split("T")[0],
                        "return": data["route"][1]["local_departure"].split("T")[0]
                    }
            return return_data
        else:
            return {"error": "no results"}
