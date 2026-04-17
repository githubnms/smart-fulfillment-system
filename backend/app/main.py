from fastapi import FastAPI
from app.db.database import engine, Base, SessionLocal
from app.db.seed_data import seed_database

# Import models
from app.models import order_model, product_model, warehouse_model, inventory_model

# Import routers
from app.api import order_routes, inventory_routes, simulation_routes

# FIRST define app
app = FastAPI(
    title="Smart Fulfillment System",
    version="1.0.0"
)

# THEN use app
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    seed_database(db)
    db.close()

    print("Tables + Sample Data ready!")

# Include routers
app.include_router(order_routes.router)
app.include_router(inventory_routes.router)
app.include_router(simulation_routes.router)

@app.get("/")
def root():
    return {"message": "API running"}