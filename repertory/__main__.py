from fastapi import FastAPI

import distant

app = FastAPI()

restaurantAPI = distant.RestaurantAPI.RestaurantAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/restaurants/")
async def getRestaurants():
    return restaurantAPI.getRestaurants()
