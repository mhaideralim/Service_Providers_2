from fastapi import HTTPException, APIRouter

from app.model import service_model
from app.security.dependencies import get_database

service_router = APIRouter()


# Get API to search data from database and to show it.
@service_router.get("/get_services_data")
async def get_provided_services(service_id: str, db=None):
    try:
        data = await get_database(db).find_one({"service_id": service_id})
        if data:
            return HTTPException(status_code=200, detail="Data Found!")
        else:
            return HTTPException(status_code=404, detail="Id Does Not Exists!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# POST API to store data in database
@service_router.post("/set_services_data")
async def set_services_data(services: service_model.Service, db=None):
    try:
        data = await get_database(db).find_one(
            {"service_id": services.service_id})
        # Query to find existing data to avoid data duplication
        if data:
            return HTTPException(status_code=500, detail="ID Already Exists!")
        else:
            await get_database(db).insert_one(services.dict())
            # Query to insert data in the DataBase
            return HTTPException(status_code=200, detail="DATA Saved Successfully")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
