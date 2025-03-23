import httpx
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from distant import *
from model import Models
from lang.ChatInstance import ChatInstance
import lang.emotiontoolcall 


app = FastAPI()

restaurantAPI = RestaurantAPI.RestaurantAPI()
clientAPI = ClientAPI.ClientAPI()

chat = ChatInstance(
        [
            (
                "system",
                "you are an agent that take care of the clients of an hotel, you must help them, you can ask them questions \
                but you can't tell them something wrong, you need to take sources from safe datasets\
                these are all the last messages {old_messages}, \
                you also need to ouput an image from theses STATE = [CUISINE, SPA, TOURISME, CRY] \
                they are essentials tho you need to chose one and use the right one \
                if you don't have the right answer, don't say anything dumb"
            ),
            ("human", "{input}"),
        ],
        lang.emotiontoolcall.STATE
    )


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
            emo = out.tool_calls[0]['name']
            print(emo)
            ans = out.tool_calls[0]["args"]['answer']
            print(ans)
    except:
        ans = 'error'
        emo = "DEAD"
        
    return {"message": "Message envoyé avec succès", "reponse": ans, "emotion": emo}