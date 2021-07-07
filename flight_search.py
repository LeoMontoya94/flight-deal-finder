import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.tequila_api_key = "**********************************"
        self.tequila_location_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.tequila_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.tequila_header = {
            "apikey": self.tequila_api_key,
        }

    def find_location(self, loc_json):
        response = requests.get(url=self.tequila_location_endpoint, params=loc_json, headers=self.tequila_header)
        return response

    def search_for_flight(self, json):
        response = requests.get(url=self.tequila_search_endpoint, headers=self.tequila_header, params=json)
        return response.json()["data"]
