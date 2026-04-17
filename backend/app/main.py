from fastapi import FastAPI
from app.db.database import engine, Base

# Import models
from app.models import order_model, product_model, warehouse_model, inventory_model

# Import routers
from app.api import order_routes, inventory_routes, simulation_routes

app = FastAPI(
    title="Smart Fulfillment System",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    print("Tables ready!")

# Include routers
app.include_router(order_routes.router)
app.include_router(inventory_routes.router)
app.include_router(simulation_routes.router)

@app.get("/")
def root():
    return {"message": "API running "}