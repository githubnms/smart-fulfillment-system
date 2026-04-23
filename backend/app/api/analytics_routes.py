from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

# DB
from app.db.database import SessionLocal

# Models
from app.models.order_model import Order
from app.models.inventory_model import Inventory
from app.models.warehouse_model import Warehouse

router = APIRouter()

# Dependency to get DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==============================
# 🔥 METRICS API
# ==============================
@router.get("/metrics")
def get_metrics(db: Session = Depends(get_db)):

    total_orders = db.query(func.count(Order.order_id)).scalar() or 0
    warehouses = db.query(func.count(Warehouse.warehouse_id)).scalar() or 0
    inventory_count = db.query(func.sum(Inventory.stock)).scalar() or 0

    throughput = round(total_orders * 0.05 + 120, 2)

    return {
        "total_orders": total_orders,
        "warehouses": warehouses,
        "inventory_count": inventory_count,
        "throughput": throughput,
        "growth": 12.5,
        "instock_status": "healthy",
        "throughput_percent": 98.2,
        "sorted_count": total_orders
    }

from datetime import datetime, timedelta

# ==============================
# 📊 ORDERS ANALYTICS (REAL DATA)
# ==============================
@router.get("/analytics/orders")
def get_orders_analytics(db: Session = Depends(get_db)):

    # Last 7 days
    last_7_days = datetime.utcnow() - timedelta(days=7)

    orders = (
        db.query(Order)
        .filter(Order.created_at >= last_7_days)
        .all()
    )

    # Prepare daily count (7 days)
    daily_orders = [0] * 7

    for order in orders:
        days_ago = (datetime.utcnow() - order.created_at).days
        if 0 <= days_ago < 7:
            daily_orders[6 - days_ago] += 1

    return {
        "daily_orders": daily_orders
    }