from fastapi import APIRouter
from models.model import User
from config.config import usersCollection

userRouter = APIRouter()


@userRouter.post("/new/user")
async def newUser(user: User):
    exists = await usersCollection.find_one({"username": user.username})
    if not exists:
        usersCollection.insert_one(dict(user))
        return {"Message":"User Created Successfully"}
    return "User Already Exists"

@userRouter.post("/user/{username}")
async def newUser(username: str):
    exists = await usersCollection.find_one({"username": username})
    if exists:
        return {"Message":"User Found"}
    return "Invalid Username"

async def updateUserPoints(username: str,points: int):
    usersCollection.update_one({"username": username},{"$set":{"points": points}})
    return "Points Updated"