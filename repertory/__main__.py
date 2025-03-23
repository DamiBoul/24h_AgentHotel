import httpx
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from distant import *
from model import Models
from lang.ChatInstance import ChatInstance
import lang.emotiontoolcall 
import lang.posttoolcall

from private import *

app = FastAPI()

restaurantAPI = RestaurantAPI.RestaurantAPI()
clientAPI = ClientAPI.ClientAPI()

chat = ChatInstance(
        [
            (
                "system",
                "you are an agent that take care of the clients of an hotel, the hôtel california of Le Mans, Sarthe, France. You must help them, you can ask them questions \
                but you can't tell them something wrong, you need to take sources from safe datasets\
                you should answer in the language of the client\
                don't send markdown\
                these are all the last messages {old_messages}, \
                you also need to ouput an image from theses STATE = [CUISINE, SPA, TOURISME, CRY] \
                they are essentials tho you need to chose one and use the right one \
                if you don't have the right answer, don't say anything dumb"
            ),
            ("human", "{input}"),
        ],
        lang.emotiontoolcall.endpoint + lang.posttoolcall.datarequest
    )

base_url = api_base_url()
headers = {"Authorization": token_api()}

# origines que vous souhaitez autoriser
origins = [
    "http://localhost:4200",  # l'URL de l'application Angular
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

@app.post("/reservation/")
async def postReservation(reservation: Models.RestaurantReservationModel):
    reservation_data = {
        "meal": reservation.mealId,
        "restaurant": reservation.restaurantId,
        "client": reservation.clientId,
        "number_of_guests": reservation.number_of_guest,
        "date": reservation.date,
        "special_requests": reservation.special_requests
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(base_url+"/reservations/", json=reservation_data, headers=headers)
    if response.status_code != 201:
        raise Exception(response.text)
    return {"message": "Réservation crée avec succès", "reservation": reservation_data, "response": response.content}

@app.post("/client/")
async def postClient(client: Models.ClientModel):
    client_data = {
        "name": client.name,
        "phone_number": client.phone_number,
        "room_number": client.room_number,
        "special_requests": client.special_requests
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(base_url+"/clients/", json=client_data, headers=headers)
    if response.status_code != 201:
        raise Exception(response.text)
    return {"message": "Client crée avec succès", "client": client_data, "response": response.content}


@app.post("/message/")
async def postMessage(message: Models.MessageModel):
    
    print(message)
    try:
        out = chat.ask(
            {
            "input": message.message
            }
        )
        print(out)
        if out.tool_calls == []:
            emo = "NORMAL"
            ans = out.content
        else:
            temp = out.tool_calls[0]
            emo = temp['name']
            print(emo)
            temp = temp["args"]
            ans = temp['answer']
            print(ans)
            if not emo in ["CUISINE", "SPA", "TOURISME", "CRY"]:
                if emo.startwith("post") :
                    if emo == "posthotel":
                        ClientAPI.ClientAPI().reserverClient(temp["name"],temp["phone_number"],temp["room_number"],temp["special_requests"])
                    else:
                        #await RestaurantAPI.RestaurantAPI.postReservation(temp,temp,temp,temp,temp)
                        pass
                
                    
                emo = "NORMAL"
    except:
        ans = 'error'
        emo = "DEAD"
        
    return {"message": "Message envoyé avec succès", "reponse": ans, "emotion": emo}