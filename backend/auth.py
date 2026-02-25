from jose import jwt
from passlib.context import CryptContext
import datetime
import hashlib

SECRET = "CHANGE_THIS_SECRET"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# SHA256 pre-hash to avoid bcrypt 72 byte limit
def normalize_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def hash_password(password):
    normalized = normalize_password(password)
    return pwd_context.hash(normalized)


def verify_password(password, hashed):
    normalized = normalize_password(password)
    return pwd_context.verify(normalized, hashed)


def create_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)


def verify_token(token):
    return jwt.decode(token, SECRET, algorithms=[ALGORITHM])
