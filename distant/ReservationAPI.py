import httpx

from model import Models
from private import *


class ReservationAPI:
    def __init__(self):
        self.url = api_base_url() + "/reservations/"
        self.headers = {"Authorization": token_api()}

    def getReservations(self):
        return httpx.get(self.url, headers=self.headers).json()

    async def postReservation(self, reservation: Models.RestaurantReservationModel):
        reservation_data = {
            "meal": reservation.mealId,
            "restaurant": reservation.restaurantId,
            "client": reservation.clientId,
            "number_of_guest": reservation.number_of_guest,
            "date": reservation.date,
            "special_requests": reservation.special_requests
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.url, json=reservation_data, headers=self.headers)
        if response.status_code != 201:
            raise Exception(response.text)
        return {"message": "Réservation crée avec succès", "reservation": reservation_data}

    def reserverRestaurant(self, clientId, restaurantId, mealId, number_of_guests, date, special_requests):
        modelReservation = Models.RestaurantReservationModel()
        modelReservation.clientId = clientId
        modelReservation.restaurantId = restaurantId
        modelReservation.mealId = mealId
        modelReservation.number_of_guest = number_of_guests
        modelReservation.date = date
        modelReservation.special_requests = special_requests
        return self.postReservation(modelReservation)
