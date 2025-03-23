import httpx
import logging

from model import *

class ClientAPI:
    def __init__(self):
        self.url = "https://app-584240518682.europe-west9.run.app/api/clients/"
        self.headers = {"Authorization": "Token bvmgSMAjLpqk6PAyWJ86s62sxdXlbWlC"}

    def getClients(self):
        return httpx.get(self.url, headers=self.headers).json()

    async def postClient(self, data: Models.ClientModel):
        client_data = {
            "name": "toto",
            "phone_number": "0606060606",
            "room_number": "21",
            "special_requests": "none"
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.url, json=client_data, headers=self.headers)
        if response.status_code != 201:
            raise Exception(response.text)
        return {"message": "Client crée avec succès", "client": data}