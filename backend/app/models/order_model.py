from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    quantity = Column(Integer)
    location = Column(String)
    priority = Column(String)