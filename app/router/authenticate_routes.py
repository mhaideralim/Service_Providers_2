from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
import asyncio
from app.security.dependencies import get_database
from app.security.securitys import JWT_SECRET, JWT_ALGORITHM

router = APIRouter()


# Function to Find the user from DataBase
async def get_user(email: str, db=None):
    user = await get_database(db).find_one({"email": email})
    if user:
        raise HTTPException(status_code=200, detail={"User": user})
    else:
        raise HTTPException(status_code=404, detail="DATA NOT FOUND!")


# Function to Create user in DataBase
async def create_user(email: str, password: str, db=None):
    user = await get_database(db).insert_one({"email": email, "password": password})
    return user


# Function to Authenticate User and Generate Token
async def authenticate_user(email: str, password: str):
    user = await get_user(email)
    if user and user["password"] == password:
        payload = {"sub": email}
        encoded_jwt = await asyncio.to_thread(jwt.encode, payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return encoded_jwt
    else:
        raise HTTPException(status_code=400, detail="Incorrect Email or password")


# Function to get User Credentials to return current User
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


# API for Signup and to set new user data in database
@router.post("/signup")
async def signup(email: str, password: str):
    user = await get_user(email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        await create_user(email, password)
        return HTTPException(status_code=200, detail="User Created Successfully!")


# Login API for login to check user credentials and access to next page
@router.post("/login_new")
async def login(email: str, password: str):
    access_token = await authenticate_user(email, password)
    return {"access_token": access_token, "token_type": "bearer"}


# APi to get credentials of current user running
@router.get("/me")
async def get_current_user_details(user: dict = Depends(get_current_user)):
    return user
