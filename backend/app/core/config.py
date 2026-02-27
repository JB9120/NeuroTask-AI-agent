
import os

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY","supersecretkey")
    ACCESS_TOKEN_EXPIRE_MINUTES = 15

settings = Settings()
