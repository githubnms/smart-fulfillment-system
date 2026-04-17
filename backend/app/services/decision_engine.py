from app.services.allocation_engine import allocate_order
from app.services.delivery_engine import calculate_delivery

def process_order(db, order, user_x, user_y):
    warehouse = allocate_order(
        db,
        order.product_id,
        order.quantity,
        user_x,
        user_y
    )

    if not warehouse:
        return {"error": "No warehouse available"}

    distance = ((warehouse.location_x - user_x)**2 + (warehouse.location_y - user_y)**2) ** 0.5

    delivery = calculate_delivery(distance, order.priority)

    return {
        "warehouse_id": warehouse.warehouse_id,
        "delivery_time": delivery["time"],
        "delivery_cost": delivery["cost"]
    }