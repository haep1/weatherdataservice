from fastapi import FastAPI
from app.services import openmeteo
from app.services import openaichat

app = FastAPI()

@app.get('/')
async def index():
    return {"Real": "Python"}

@app.get('/weather/{latitude}/{longitude}')
async def weather(latitude: float, longitude: float):
    return openmeteo.get_weather(latitude, longitude)

@app.get('/openaichat')
async def openai_chat(chat: str):
    return openaichat.start_chat(chat)