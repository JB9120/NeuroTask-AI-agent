
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from backend.auth import hash_password, verify_password, create_token, verify_token
from backend.memory import init_db, create_user, get_user, add_todo
from backend.parser import parse_datetime
from backend.scheduler import start_scheduler

app = FastAPI()

init_db()
start_scheduler()

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h2>NeuroTask SaaS Running</h2>"

@app.post("/register")
def register(email: str = Form(...), password: str = Form(...)):
    try:
        hashed = hash_password(password)
        create_user(email, hashed)
        return {"message": "User created"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login")
def login(email: str = Form(...), password: str = Form(...)):
    user = get_user(email)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email")
    if not verify_password(password, user[1]):
        raise HTTPException(status_code=401, detail="Invalid password")
    token = create_token(user[0])
    return {"token": token}

@app.post("/add_todo")
def add_todo_api(text: str = Form(...), token: str = Form(...)):
    data = verify_token(token)
    date = parse_datetime(text)
    if not date:
        raise HTTPException(status_code=400, detail="Could not parse date")
    add_todo(data["user_id"], text, str(date), "MEDIUM")
    return {"message": "Todo added"}
