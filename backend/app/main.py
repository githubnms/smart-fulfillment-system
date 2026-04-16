from fastapi import FastAPI
from app.db.database import engine, Base

# Import all models
from app.models import order_model, product_model, warehouse_model, inventory_model

app = FastAPI()

@app.on_event("startup")
def startup():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

@app.get("/")
def read_root():
    return {"message": "System Ready"}