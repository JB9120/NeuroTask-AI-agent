from jose import jwt
from passlib.context import CryptContext
import datetime

SECRET = "CHANGE_THIS_SECRET_TO_LONG_RANDOM_STRING"
ALGORITHM = "HS256"

# Use Argon2 instead of bcrypt
pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

def create_token(user_id: int) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)

def verify_token(token: str):
    return jwt.decode(token, SECRET, algorithms=[ALGORITHM])
