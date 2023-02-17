from pydantic import BaseModel
from app.databse.db_connection import client

db = client["service_provider"]
service_data = db["services_info"]


class Service(BaseModel):
    service_id: str
    service_name: str | None = None
    service_rating: str | None = None
    service_rate: str | None = None
    service_category: str | None = None
    service_desc: str | None = None
    service_provider: str | None = None
    service_review: str | None = None
