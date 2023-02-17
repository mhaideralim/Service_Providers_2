from fastapi import HTTPException, APIRouter
from app.model import OrderModel
from app.model.OrderModel import order_data

order_router = APIRouter()


async def completed_order_data(status: str):
    try:
        for order_status in order_data:
            if status == "Completed":
                return order_status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def running_order_data(status: str):
    try:
        for order_status in order_data:
            if status == "Running":
                return order_status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def archived_order_data(status: str):
    try:
        for order_status in order_data:
            if status == "Archived":
                return order_status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@order_router.get("/view_orders_data")
async def view_order_data(order_id: int):
    try:
        data = await order_data.find_one({"order_id": order_id})
        if data:
            return {"Data Found"}
        else:
            return HTTPException(status_code=404, detail="ID Does Not Exists!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@order_router.post("/set_order_data")
async def set_order_data(orders: OrderModel.Order):
    try:
        data = await order_data.find_one({"order_id": orders.order_id})
        if data:
            return HTTPException(status_code=409, detail="ID Already Exists!")
        else:
            await order_data.insert_one(orders.dict())
            return {"Data Inserted Successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@order_router.delete("/delete_data")
async def delete_data(order_id: int):
    try:
        data = await order_data.find_one({"order_id": order_id})
        if data:
            await order_data.delete_one({"order_id": order_id})
            return HTTPException(status_code=201, detail="Data Deleted Successfully!")
        else:
            return {"ID Does Not Exists!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
