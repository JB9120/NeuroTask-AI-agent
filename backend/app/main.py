
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, todos, admin, health
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(title="NeuroTask Enterprise SaaS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(todos.router, prefix="/todos", tags=["todos"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(health.router, tags=["health"])

@app.get("/")
def root():
    return {"message": "NeuroTask Enterprise running"}
