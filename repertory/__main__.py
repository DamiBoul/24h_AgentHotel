from fastapi import FastAPI
import httpx

from distant import *
import distant
from model.ClientModel import ClientModel

app = FastAPI()

restaurantAPI = distant.RestaurantAPI.RestaurantAPI()
clientAPI = distant.ClientAPI.ClientAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

url = "https://app-584240518682.europe-west9.run.app/api/clients/"
headers = {"Authorization": "Token bvmgSMAjLpqk6PAyWJ86s62sxdXlbWlC"}

@app.get("/restaurants/")
async def getRestaurants():
    return restaurantAPI.getRestaurants()

@app.get("/clients/")
async def getClients():
    return clientAPI.getClients()

@app.post("/client/")
async def postClient():
    client_data = {
        "name": "toto",
        "phone_number": "0606060606",
        "room_number": "21",
        "special_requests": "none"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=client_data, headers=headers)
    if response.status_code != 201:
        raise Exception(response.text)
    return {"message": "Client crée avec succès", "client": client_data}