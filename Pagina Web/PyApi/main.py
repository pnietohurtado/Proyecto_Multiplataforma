from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Message
from database import initializeDB,add_message, get_all_messages
from models import WhoIs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def welcome(): 
    await initializeDB()
    await add_message(WhoIs.USER.value, 'Mensaje desde mongoDB')
    return {'message': 'Hello!'}


@app.post('/api/sendmessage/{chatRoom}/{sender}/{message}')
async def sendMessage(chatRoom: str, sender:str, message:str): 
    await add_message(WhoIs.USER.value, message, sender); 
    return {'message': 'Everything send correctly'}


@app.get('/api/getmessages/{username}')
async def getAllMessages(username: str): 
    messages = await get_all_messages(username) 
    return messages
