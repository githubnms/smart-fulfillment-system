from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 🔐 Replace password with your PostgreSQL password
DATABASE_URL = "postgresql://postgres:NMS%40123nms%23456@localhost:5432/fulfillment_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()