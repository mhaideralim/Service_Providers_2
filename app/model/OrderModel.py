from pydantic import BaseModel
from app.databse.db_connection import client

db = client["service_provider"]
order_data = db["orders_data"]


class Order(BaseModel):
    order_id: int
    order_name: str | None = None
    delivery_add: str | None = None
    datetime: str | None = None
    order_type: str | None = None
    order_status: str | None = None
    payment_method: str | None = None
    price: str | None = None
    tax: str | None = None
    total: str | None = None
