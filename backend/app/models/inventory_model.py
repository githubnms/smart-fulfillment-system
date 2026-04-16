from sqlalchemy import Column, Integer, ForeignKey
from app.db.database import Base

class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True, index=True)
    warehouse_id = Column(Integer, ForeignKey("warehouses.warehouse_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    stock = Column(Integer, nullable=False)