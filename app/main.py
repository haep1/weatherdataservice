from fastapi import FastAPI
from app.services import openmeteo

app = FastAPI()

@app.get('/')
async def index():
    return {"Real": "Python"}

@app.get('/weather/{latitude}/{longitude}')
async def weather(latitude: float, longitude: float):
    return openmeteo.get_weather(latitude, longitude)