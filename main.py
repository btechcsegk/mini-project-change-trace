from fastapi import FastAPI
from routes.userRoute import userRouter
from routes.challengeRoute import challengeRouter

app = FastAPI()

app.include_router(userRouter)
app.include_router(challengeRouter)

@app.get('/')
def index():
    return {"name": "Govind Kashyap"}
