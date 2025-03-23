from typing_extensions import Annotated, TypedDict

class getspa(TypedDict):
    """if the client wants to know something about the spas  
    """
    name: Annotated[str, ..., "the name of the client"]
    phone_number: Annotated[str, ..., "the phone numbre of the client"]
    room_number: Annotated[str, ..., "the room the client wants"]
    special_requests: Annotated[str, ..., "any special request from the client"]
    answer: Annotated[str, ..., "confirm the request to the client"]

class gethotel(TypedDict):
    """if the client wants to know something about the hotel  
    """
    name: Annotated[str, ..., "the name of the client"]
    phone_number: Annotated[str, ..., "the phone numbre of the client"]
    room_number: Annotated[str, ..., "the room the client wants"]
    special_requests: Annotated[str, ..., "any special request from the client"]
    answer: Annotated[str, ..., "confirm the request to the client"]

class getrestaurant(TypedDict):
    """if the client wants to know something about the restaurant
    """
    restaurant_id: Annotated[str, ..., "the id of a restaurant"]
    client_id: Annotated[str, ..., "the id of a client"]
    date: Annotated[str, ..., "the date of the reservation"]
    meal_id: Annotated[str, ..., "any special request from the client"]
    number_of_people: Annotated[str, ..., "any special request from the client"]
    special_requests: Annotated[str, ..., "any special request from the client"]
    answer: Annotated[str, ..., "confirm the request to the client"]



datarequest = [gethotel, getrestaurant, getspa]