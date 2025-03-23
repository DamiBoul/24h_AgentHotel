import httpx

from model import *
from private import *


class ClientAPI:
    def __init__(self):
        self.url = api_base_url()+"/clients/"
        self.headers = {"Authorization": token_api()}

    def getClients(self):
        return httpx.get(self.url, params={"search":1}, headers=self.headers).json()

    async def postClient(self, client: Models.ClientModel):
        client_data = {
            "name": client.name,
            "phone_number": client.phone_number,
            "room_number": client.room_number,
            "special_requests": client.special_requests
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.url, json=client_data, headers=self.headers)
        if response.status_code != 201:
            raise Exception(response.text)
        return {"message": "Client crée avec succès", "client": client_data}

    def reserverClient(self, name, phone_number, room_number, special_requests):
        modelClient = Models.ClientModel()
        modelClient.name = name
        modelClient.phone_number = phone_number
        modelClient.room_number = room_number
        modelClient.special_requests = special_requests
        return self.postClient(modelClient)