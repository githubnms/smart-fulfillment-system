from sqlalchemy.orm import Session
from app.models.product_model import Product
from app.models.warehouse_model import Warehouse
from app.models.inventory_model import Inventory

def seed_database(db: Session):
    # Check if data already exists
    if db.query(Product).first():
        return

    # Warehouses (coordinates represent locations)
    w1 = Warehouse(location_x=10.0, location_y=20.0)  # Chennai
    w2 = Warehouse(location_x=15.0, location_y=25.0)  # Bangalore
    w3 = Warehouse(location_x=30.0, location_y=40.0)  # Mumbai

    db.add_all([w1, w2, w3])
    db.commit()

    # Products
    p1 = Product(name="Laptop")
    p2 = Product(name="Mobile")

    db.add_all([p1, p2])
    db.commit()

    # Inventory
    inventory_data = [
        Inventory(warehouse_id=1, product_id=1, stock=10),
        Inventory(warehouse_id=2, product_id=1, stock=5),
        Inventory(warehouse_id=3, product_id=1, stock=20),

        Inventory(warehouse_id=1, product_id=2, stock=15),
        Inventory(warehouse_id=2, product_id=2, stock=0),
        Inventory(warehouse_id=3, product_id=2, stock=25),
    ]

    db.add_all(inventory_data)
    db.commit()

    print("Sample data inserted!")