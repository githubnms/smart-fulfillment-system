from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.order_schema import OrderCreate, OrderResponse
from app.services.order_service import create_order
from app.services.decision_engine import process_order

router = APIRouter()

@router.post("/create-order", response_model=OrderResponse)
def create_new_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order)


@router.post("/process-order")
def process(order: OrderCreate, db: Session = Depends(get_db)):
    # Temporary location (we will improve later)
    user_x, user_y = 10.0, 20.0

    return process_order(db, order, user_x, user_y)