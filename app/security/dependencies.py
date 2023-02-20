from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from app.security.securitys import MONGODB_URL

# Dependency to get the database connection
async def get_database():
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client["mydatabase"]
    yield db
    client.close()
