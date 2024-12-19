from fastapi import APIRouter
from models.model import Challenge
from config.config import challengesCollection

challengeRouter = APIRouter()

@challengeRouter.post("/new/challenge")
async def newChallenege(challenge: Challenge):
    cursor = await challengesCollection.find_one({"challengeId": challenge.challengeId})
    if cursor:
        return "Challenge Already Exists"
    challengesCollection.insert_one(dict(challenge))
    return {"Message":"Challenge Created Successfully"}