from app.models.warehouse_model import Warehouse
from app.models.inventory_model import Inventory
from sqlalchemy.orm import Session
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def allocate_order(db: Session, product_id: int, quantity: int, user_x: float, user_y: float):
    warehouses = db.query(Warehouse).all()
    
    best_warehouse = None
    min_distance = float("inf")

    for wh in warehouses:
        inventory = db.query(Inventory).filter_by(
            warehouse_id=wh.warehouse_id,
            product_id=product_id
        ).first()

        if inventory and inventory.stock >= quantity:
            distance = calculate_distance(wh.location_x, wh.location_y, user_x, user_y)

            if distance < min_distance:
                min_distance = distance
                best_warehouse = wh

    return best_warehouse