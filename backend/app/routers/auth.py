
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.security import hash_password, verify_password, create_token

router = APIRouter()

fake_db = {}

class Register(BaseModel):
    email:str
    password:str

class Login(BaseModel):
    email:str
    password:str

@router.post("/register")
def register(data:Register):
    if data.email in fake_db:
        raise HTTPException(400,"User exists")
    fake_db[data.email] = hash_password(data.password)
    return {"message":"registered"}

@router.post("/login")
def login(data:Login):
    if data.email not in fake_db:
        raise HTTPException(401,"Invalid credentials")
    if not verify_password(data.password, fake_db[data.email]):
        raise HTTPException(401,"Invalid credentials")
    token = create_token({"sub":data.email,"role":"USER"})
    return {"access_token":token}
