from fastapi import FastAPI
from app.router import ServiceRoutes, OrderRoutes, ProfileRoutes, AuthenticateRoutes

app = FastAPI()


app.include_router(AuthenticateRoutes.router)
app.include_router(ServiceRoutes.service_router)
app.include_router(OrderRoutes.order_router)
app.include_router(ProfileRoutes.profile_router)
