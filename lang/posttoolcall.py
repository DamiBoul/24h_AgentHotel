from typing_extensions import Annotated, TypedDict

class posthotel(TypedDict):
    """if the client wants to make a reservation for a room
    ask more questions if you don't have enough info on the client
    """
    name: Annotated[str, ..., "the name of the client"]
    phone_number: Annotated[str, ..., "the phone numbre of the client"]
    room_number: Annotated[str, ..., "the room the client wants"]
    special_requests: Annotated[str, ..., "any special request from the client"]
    answer: Annotated[str, ..., "confirm the request to the client"]

class postrestaurant(TypedDict):
    """if the client wants to make a reservation for a restaurant
    ask more questions if you don't have enough info on the client
    """
    restaurant_id: Annotated[str, ..., "the id of a restaurant"]
    client_id: Annotated[str, ..., "the id of a client"]
    date: Annotated[str, ..., "the date of the reservation"]
    meal_id: Annotated[str, ..., "any special request from the client"]
    number_of_people: Annotated[str, ..., "any special request from the client"]
    special_requests: Annotated[str, ..., "any special request from the client"]
    answer: Annotated[str, ..., "confirm the request to the client"]



datarequest = [posthotel, postrestaurant]