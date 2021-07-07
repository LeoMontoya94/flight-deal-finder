# This class is responsible for talking to the Google Sheet.
import requests


class DataManager:

    def __init__(self):
        self.sheet_bearer_token = "Bearer *************************************"
        self.prices_endpoint = "https://api.sheety.co/0e0b6e5d309efb59e34c256a0bedadc9/flightDeals/prices"
        self.users_endpoint = "https://api.sheety.co/0e0b6e5d309efb59e34c256a0bedadc9/flightDeals/users"
        self.sheet_header = {
            "Authorization": self.sheet_bearer_token,
        }

    def get_data(self):
        response = requests.get(url=self.prices_endpoint, headers=self.sheet_header)
        data = response.json()["prices"]
        return data

    def update_sheet(self, update_json, entry_num):
        response = requests.put(url=f"{self.prices_endpoint}/{entry_num}", json=update_json, headers=self.sheet_header)

    def get_users(self):
        response = requests.get(url=self.users_endpoint, headers=self.sheet_header)
        data = response.json()["users"]
        return data
