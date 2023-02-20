from fastapi import HTTPException, APIRouter
from app.model import order_model
from app.security.dependencies import get_database

order_router = APIRouter()


# Function to check the Order Status == "Completed" and return respected Data to user
async def completed_order_data(status: str):
    try:
        for order_status in get_database.db:
            if status == "Completed":
                return HTTPException(status_code=200, detail={"order_status": order_status})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Function to check the Order Status == "Running" and return respected Data to user
async def running_order_data(status: str, db=None):
    try:
        for order_status in get_database.db:
            if status == "Running":
                return HTTPException(status_code=200, detail={"order_status": order_status})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Function to check the Order Status == "Archived" and return respected Data to user
async def archived_order_data(status: str):
    try:
        for order_status in get_database.db:
            if status == "Archived":
                return HTTPException(status_code=200, detail={"order_status": order_status})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# API to Show Order data to users
@order_router.get("/view_orders_data")
async def view_order_data(order_id: int, db=None):
    try:
        data = await get_database(db).find_one({"order_id": order_id})
        if data:
            return HTTPException(status_code=200, detail="Data Found!")
        else:
            return HTTPException(status_code=404, detail="ID Does Not Exists!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# API to set new order and data to DataBase
@order_router.post("/set_order_data")
async def set_order_data(orders: order_model.Order, db=None):
    try:
        data = await get_database(db).find_one({"order_id": orders.order_id})
        if data:
            return HTTPException(status_code=409, detail="ID Already Exists!")
        else:
            await get_database.db.insert_one(orders.dict())
            return HTTPException(status_code=200, detail="Data Inserted Successfully!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# API to Delete an order and its data from DataBase
@order_router.delete("/delete_data")
async def delete_data(order_id: int, db=None):
    try:
        data = await get_database(db).find_one({"order_id": order_id})
        if data:
            await get_database.db.delete_one({"order_id": order_id})
            return HTTPException(status_code=201, detail="Data Deleted Successfully!")
        else:
            return HTTPException(status_code=404, detail="ID Not Found!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
