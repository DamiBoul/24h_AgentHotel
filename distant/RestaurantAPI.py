import requests

from private import api_base_url, token_api


class RestaurantAPI:
    def __init__(self):
        self.url = api_base_url()+"/restaurants/"
        self.headers = {"Authorization": token_api()}

    def getRestaurants(self):
        return requests.get(self.url, headers=self.headers).json()
