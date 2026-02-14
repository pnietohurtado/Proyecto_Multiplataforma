from pydantic import BaseModel, Field 
from typing import Optional
from datetime import datetime 
from enum import Enum 

class WhoIs(Enum): 
    USER="user"
    OTHER="other"

class Data(BaseModel): 
    message: str 
    date:  Optional[datetime] = Field(default_factory=datetime.now)
    who: str # Changed from WhoIs to str to avoid validation errors if we want to be flexible, but WhoIs is fine if we map it. Let's keep WhoIs for now but we might need to change it on retrieval. Actually, the goal is to return "user" or "other".
    sender: str

class Message(BaseModel): 
    _id: Optional[int] = None
    chatRoom: str 
    messages:Data = []
