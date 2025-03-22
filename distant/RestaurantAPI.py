import requests


class RestaurantAPI:
    def __init__(self):
        self.url = "https://app-584240518682.europe-west9.run.app/api/restaurants/"

    def getRestaurants(self):
        return requests.get(self.url, headers={"Authorization": "Token bvmgSMAjLpqk6PAyWJ86s62sxdXlbWlC"}).json()
