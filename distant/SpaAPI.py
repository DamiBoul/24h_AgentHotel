import requests
from private import *


class SpaAPI:
    def __init__(self):
        self.url = api_base_url()+"/spas/"
        self.headers = {"Authorization": token_api()}

    def getSpas(self):
        return requests.get(self.url, headers=self.headers).json()
