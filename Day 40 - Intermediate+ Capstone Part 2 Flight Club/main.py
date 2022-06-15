# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from validate_email import validate_email
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()
sheet_data = data_manager.sheet_data
current_users = data_manager.current_users()
# Check for missing iata codes
no_code = [data for data in sheet_data if data['iataCode'] == '']
no_code_count = 0
for val in no_code:
    no_code_count += 1
    flight_search.get_iata_code(val['city'])
    data_manager.update_iata_codes(val['id'], flight_search.get_iata_code(val['city']))
sheet_data = data_manager.current_sheet()
# Completed the missing codes check and refreshing list.

# check for lower prices
for location in sheet_data:
    new_info = flight_data.get_lowest_price(location['iataCode'])
    if "error" not in new_info:
        if new_info['price'] < location["lowestPrice"]:
            data_manager.update_lowest_price(location['id'], new_info['price'])
            message = f"Low price alert! Only {'${:,.2f}'.format(new_info['price'])} to fly from {new_info['city_from']}-{new_info['fly_from']} to {new_info['city_to']}-{new_info['fly_to']}, from {new_info['depart']} to {new_info['return']}."
            for user in current_users:
                notification_manager.send_email(user['email'], message)
            notification_manager.send_note(message)


