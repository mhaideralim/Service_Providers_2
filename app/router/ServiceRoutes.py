import json

from fastapi import HTTPException, APIRouter
from app.model import ServiceModel
from app.model.ServiceModel import service_data


service_router = APIRouter()


# Get API to search data from database and to show it.
@service_router.get("/get_services_data")
async def get_provided_services(service_id: str):
    try:
        data = await service_data.find_one({"service_id": service_id})
        if data:
            return {"Data Found!"}
        else:
            return HTTPException(status_code=404, detail="Id Does Not Exists!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# POST API to store data in database
@service_router.post("/set_services_data")
async def set_services_data(services: ServiceModel.Service):
    try:
        data = await service_data.find_one(
            {"service_id": services.service_id})
        # Query to find existing data to avoid data duplication
        if data:
            return {"ID Already Exists!"}
        else:
            await service_data.insert_one(services.dict())
            # Query to insert data in the DataBase
            return {"message": "Services Stored Successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
