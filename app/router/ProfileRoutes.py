from fastapi import HTTPException, APIRouter
from app.model import ProfileModel
from app.model.ProfileModel import profile_data


profile_router = APIRouter()


@profile_router.get("/get_profile_data")
async def view_user_data(user_id: int):
    try:
        data = await profile_data.find_one({"user_id": user_id})
        if data:
            return {"Data Found!"}
        else:
            return HTTPException(status_code=404, detail="Id Does Not Exists!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@profile_router.post("/set_profile_data")
async def set_user_data(users: ProfileModel.UserProfile):
    try:
        data = await profile_data.find_one({"user_id": users.user_id})
        if data:
            return HTTPException(status_code=409, detail="ID Already Exists!")
        else:
            profile_data.insert_one(users.dict())
            return {"Data Inserted Successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



