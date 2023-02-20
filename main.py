from fastapi import FastAPI
from app.router import service_routes, order_routes, profile_routes, authenticate_routes
from app.databse import db_connections
app = FastAPI()

# Routes to run API in the respected Router Files


# Authentication API Route
app.include_router(authenticate_routes.router)
# Service API Route
app.include_router(service_routes.service_router)
# Order API Routes
app.include_router(order_routes.order_router)
# Profile API Route
app.include_router(profile_routes.profile_router)