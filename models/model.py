from typing import List, Optional
from pydantic import BaseModel
from datetime import date
from datetime import datetime
from random import randint


class User(BaseModel):
    username: str
    password: str
    name: str
    role: str = "user"
    points: int = 0
    badges: List[str] = []
    challenges: List[dict] = []
    
class Challenge(BaseModel):
    challengeId: int = randint(100000,999999)
    title: str
    desc: str
    img: str
    points: int
    challengers: int = 0
    ratings: float = 0.0
    created_at: date = datetime.today()