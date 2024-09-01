from fastapi import FastAPI
from app.services import openmeteo

app = FastAPI()

@app.get('/')
async def index():
    return {"Real": "Python"}

@app.get('/sampleWeather')
async def weather():
    return openmeteo.get_weather(13.41, 52.52)

@app.get('/weather/{longitude}/{latitude}')
async def weather(longitude: float, latitude: float):
    return openmeteo.get_weather(longitude, latitude)