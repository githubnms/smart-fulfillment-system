from app.models.order_model import Order

def create_order(db, order_data):
    new_order = Order(**order_data.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order