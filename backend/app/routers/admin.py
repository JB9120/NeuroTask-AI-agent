
from fastapi import APIRouter

router = APIRouter()

@router.get("/stats")
def stats():
    return {
        "total_users": 1,
        "total_todos": 0,
        "system_status":"ok"
    }
