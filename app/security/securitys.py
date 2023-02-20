# JWT Secret Key
import os

# Credentials for JWT token generation and encryption methode using user data
JWT_SECRET = os.getenv("JWT_SECRET", "secret_key")
JWT_ALGORITHM = "HS256"

# origins which should be followed when database will be connected
BACKEND_CORS_ORIGINS = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
# MongoDB connection URL
# MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGODB_URL = "mongodb://localhost:27017"
