from fastapi import APIRouter
from datetime import datetime
import random

router = APIRouter()

@router.get("/recent")
def get_recent_logs():
    logs = [
        {"icon": "plus-circle", "message": "Order created", "time": "just now"},
        {"icon": "warehouse", "message": "Assigned to warehouse", "time": "2 sec ago"},
        {"icon": "truck", "message": "Out for delivery", "time": "5 sec ago"},
        {"icon": "check-circle", "message": "Order delivered", "time": "10 sec ago"},
    ]

    return random.sample(logs, k=3)