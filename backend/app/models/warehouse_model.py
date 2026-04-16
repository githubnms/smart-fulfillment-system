from sqlalchemy import Column, Integer, Float
from app.db.database import Base

class Warehouse(Base):
    __tablename__ = "warehouses"

    warehouse_id = Column(Integer, primary_key=True, index=True)
    location_x = Column(Float, nullable=False)
    location_y = Column(Float, nullable=False)