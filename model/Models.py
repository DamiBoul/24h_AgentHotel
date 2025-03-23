from pydantic import BaseModel


class ClientModel(BaseModel):
    name: str
    phone_number: str
    room_number: str
    special_requests: str


class MessageModel(BaseModel):
    message: str
