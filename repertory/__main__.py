import httpx
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from distant import *
from model import Models

app = FastAPI()

restaurantAPI = RestaurantAPI.RestaurantAPI()
clientAPI = ClientAPI.ClientAPI()


# Remplacez par les origines que vous souhaitez autoriser
origins = [
    "http://localhost:4200",  # Par exemple, l'URL de votre application Angular
    # Ajoutez d'autres origines si nécessaire
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes
    allow_headers=["*"],  # Autorise tous les en-têtes
)

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


@app.post("/message/")
async def postMessage(message: Models.MessageModel):
    print(message)