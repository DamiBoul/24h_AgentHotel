import requests
from private import *


class ReservationAPI:
    def __init__(self):
        self.url = api_base_url()+"/reservations/"
        self.headers = {"Authorization": token_api()}

    def getReservations(self):
        return requests.get(self.url, headers=self.headers).json()
