from pydantic import BaseModel
from app.databse.db_connection import client

db = client["service_provider"]
profile_data = db["users_data"]


class UserProfile(BaseModel):
    user_id: int
    username: str
    email: str
    phone: int
    password: str
    img: str
