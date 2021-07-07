from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

my_location = "WAS"

today = datetime.today()
tomorrow = (today + timedelta(days=1)).strftime('%d/%m/%Y')
six_months = (today + timedelta(days=182)).strftime('%d/%m/%Y')

sheet_manager = DataManager()
flight_manager = FlightSearch()
notification_manager = NotificationManager()

# sheet_data = sheet_manager.get_data()
# For efficiency in testing, I copy and pasted the data that sheet_manager.get_data() retrieves from Sheety.
sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 1000, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 1000, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 1000, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 1000, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 1000, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 1000, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 1000, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 1000, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 1000, 'id': 10}, {'city': 'Bali', 'iataCode': 'DPS', 'lowestPrice': 501, 'id': 11}]



# for entry in sheet_data:
#     entry_num = entry["id"]
#     city = entry["city"]
#     lowest_price = entry["lowestPrice"]
#     if entry["iataCode"] == "":
#         loc_json = {
#             "term": city,
#             "location_types": "city",
#         }
#         tequila_response = flight_manager.find_location(loc_json)
#         iata_code = tequila_response.json()["locations"][0]["code"]
#         update_json = {
#             "price": {
#                 "iataCode": iata_code,
#             }
#         }
#         update = sheet_manager.update_sheet(update_json, entry_num)

for entry in sheet_data:
    entry_num = entry["id"]
    city = entry["city"]
    lowest_price = entry["lowestPrice"]
    iata = entry["iataCode"]
    search_json = {
        "fly_from": my_location,
        "fly_to": iata,
        "date_from": tomorrow,
        "date_to": six_months,
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "one_for_city": 1,
        "max_stopovers": 0,
        "curr": "USD",
    }
    data = flight_manager.search_for_flight(search_json)
    try:
        found_data = data[0]
    except IndexError:
        search_json["max_stopovers"] = 1
        data = flight_manager.search_for_flight(search_json)
        try:
            found_data = data[0]
            print(found_data)
        except IndexError:
            found_data = {
                "price": 10000
            }
    finally:
        if found_data["price"] < lowest_price:
            notification_manager.send_email(found_data)