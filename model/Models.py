from pydantic import BaseModel


class ClientModel(BaseModel):
    name: str
    phone_number: str
    room_number: str
    special_requests: str


class MessageModel(BaseModel):
    message: str

class RestaurantReservationModel(BaseModel):
    clientId: int
    restaurantId: int
    mealId: int
    date: str
    special_requests: str
    number_of_guest: int