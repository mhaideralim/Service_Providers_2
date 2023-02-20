from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from app.security.securitys import MONGODB_URL

app = FastAPI()

# Connect to the database using AsyncIOMotorClient
@app.on_event("startup")
async def connect_to_db():
    app.mongodb_client = AsyncIOMotorClient(MONGODB_URL)
    app.mongodb = app.mongodb_client["mydatabase"]

@app.on_event("shutdown")
async def close_db_connection():
    app.mongodb_client.close()

# CORS middleware
origins = ["http://localhost", "http://localhost:8080", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

