from typing_extensions import Annotated, TypedDict

class getSpas(TypedDict):
    """if the client wants to know something about the spas  
    """
    answer: Annotated[str, ..., "the answer to the client"]

class getClient(TypedDict):
    """if the client wants to know something about the hotel reservations
    """
    answer: Annotated[str, ..., "the answer to the client"]

class getrestaurants(TypedDict):
    """if the client wants to know something about the restaurant
    """
    answer: Annotated[str, ..., "the answer to the client"]

class getMeals(TypedDict):
    """if the client wants to know something about the meals served
    """
    answer: Annotated[str, ..., "the answer to the client"]

class getReservations(TypedDict):
    """if the client wants to know something about the restaurants reservations
    """
    answer:  Annotated[str, ..., "the answer to the client"]

datasend = [getClient, getrestaurants, getSpas, getMeals, getReservations]