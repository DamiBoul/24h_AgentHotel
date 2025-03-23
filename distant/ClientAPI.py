import httpx

from model import *
from private import *


class ClientAPI:
    def __init__(self):
        self.url = api_base_url()+"/clients/"
        self.headers = {"Authorization": token_api()}

    def getClients(self):
        return httpx.get(self.url, headers=self.headers).json()