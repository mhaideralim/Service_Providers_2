from fastapi import HTTPException, APIRouter
from app.model import profile_model
from app.security.dependencies import get_database

profile_router = APIRouter()


# API to View profile of User from database
@profile_router.get("/get_profile_data")
async def view_user_data(user_id: int, db=None):
    try:
        data = await get_database(db).find_one({"user_id": user_id})
        if data:
            return HTTPException(status_code=200, detail="Data Found!")
        else:
            return HTTPException(status_code=404, detail="Id Does Not Exists!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# API to save User and Profile Data to DataBase
@profile_router.post("/set_profile_data")
async def set_user_data(users: profile_model.UserProfile, db=None):
    try:
        data = await get_database(db).find_one({"user_id": users.user_id})
        if data:
            return HTTPException(status_code=409, detail="ID Already Exists!")
        else:
            get_database(db).insert_one(users.dict())
            return HTTPException(status_code=200, detail="Data Inserted Successfully!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
