from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from motor.motor_asyncio import AsyncIOMotorClient
from jose import jwt
import asyncio

router = APIRouter()

JWT_SECRET = "mysecretkey"
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION = 3600  # 1 hour

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["service-provider"]
users_collection = db["users_data"]


async def get_user(email: str):
    user = await users_collection.find_one({"email": email})
    return user


async def create_user(email: str, password: str):
    user = await users_collection.insert_one({"email": email, "password": password})
    return user


async def authenticate_user(email: str, password: str):
    user = await get_user(email)
    if user and user["password"] == password:
        payload = {"sub": email}
        encoded_jwt = await asyncio.to_thread(jwt.encode, payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return encoded_jwt
    else:
        raise HTTPException(status_code=400, detail="Incorrect Email or password")


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    try:
        payload = jwt.decode(credentials.credentials, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = payload["sub"]
        user = await get_user(email)
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")


@router.post("/signup")
async def signup(email: str, password: str):
    user = await get_user(email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        await create_user(email, password)
        return {"message": "User created successfully"}


@router.post("/login_new")
async def login(email: str, password: str):
    access_token = await authenticate_user(email, password)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me")
async def get_current_user_details(user: dict = Depends(get_current_user)):
    return user
