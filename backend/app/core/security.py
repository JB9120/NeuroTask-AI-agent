
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password[:72])

def verify_password(password:str, hashed:str):
    return pwd_context.verify(password[:72], hashed)

def create_token(data:dict):
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp":expire})
    return jwt.encode(data, settings.SECRET_KEY, algorithm="HS256")
