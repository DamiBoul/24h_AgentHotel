import requests
from private import *


class MealAPI:
    def __init__(self):
        self.url = api_base_url()+"/meals/"
        self.headers = {"Authorization": token_api()}

    def getMeals(self):
        return requests.get(self.url, headers=self.headers).json()
