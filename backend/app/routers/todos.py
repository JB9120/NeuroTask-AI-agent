
from fastapi import APIRouter

router = APIRouter()

todos = []

@router.get("/")
def get_todos():
    return todos

@router.post("/")
def add_todo(todo:str):
    todos.append(todo)
    return {"message":"added"}
