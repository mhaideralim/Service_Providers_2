from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient('mongodb://localhost:27017')

try:
    client.admin.command('ismaster')
    print("Connected to the database successfully.")

except Exception as e:
    print(f"Could not connect to the database: {e}")


# app.add_middleware(
#    CORSMiddleware,
#    allow_origins = settings.BACKEND_CORS_ORIGINS,
#    allow_credentials = True,
#    allow_methods = ["*"],
#    allow_headers = ["*",]
# )
# @app.on_event("startup")
# async def app_init():
# initialize application services


# db_client = AsyncIOMotorClient (settings.MONGO_CONNECTION_STRING).fastapitemplate


# def init_beaine(database, document_models):
#   pass


# await init_beaine(
#    database = db_client,
#    document_models=[
#        authenticate,
#        order,
#        service,
#        user_profile
#    ]
# )

# print("initialize application services")
# CheckSystemLogs.pass_logs("intialize Applcation Services",log_level=2)
