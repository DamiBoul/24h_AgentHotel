import requests


class ClientAPI:
    def __init__(self):
        self.url = "https://app-584240518682.europe-west9.run.app/api/clients/"

    def getClient(self, id):
        return requests.get(self.url + "1")
