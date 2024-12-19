from pymongo.mongo_client import MongoClient
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

uri = "mongodb+srv://govind8061:gk806161@changetrace.hgnnz.mongodb.net/?retryWrites=true&w=majority&appName=changetrace"
# Create a new client and connect to the server
client = AsyncIOMotorClient(uri)


db = client['myDB']

usersCollection = db['users']
challengesCollection = db['challenges']
