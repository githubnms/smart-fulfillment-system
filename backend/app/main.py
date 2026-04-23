from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ========== DATABASE ==========
from app.db.database import engine, Base, SessionLocal
from app.db.seed_data import seed_database

# ========== ROUTERS ==========
from app.api import order_routes
from app.api import inventory_routes
from app.api import simulation_routes
from app.api import analytics_routes   # NEW (metrics API)
from app.api import logs_routes

# ========== APP INIT ==========
app = FastAPI(
    title="Smart Fulfillment System",
    version="2.0.0"
)

# ========== CORS ==========
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # restrict later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== STARTUP ==========
@app.on_event("startup")
def startup():
    print("Starting Smart Fulfillment System...")

    # Create tables
    Base.metadata.create_all(bind=engine)

    # Seed data
    db = SessionLocal()
    try:
        seed_database(db)
    except Exception as e:
        print("Seeding skipped:", e)
    finally:
        db.close()

    print("Database Ready with Sample Data")

# ========== ROUTES ==========
app.include_router(order_routes.router, prefix="/api/orders", tags=["Orders"])
app.include_router(inventory_routes.router, prefix="/api/inventory", tags=["Inventory"])
app.include_router(simulation_routes.router, prefix="/api/simulation", tags=["Simulation"])

# NEW ROUTE FOR METRICS
app.include_router(analytics_routes.router, prefix="/api", tags=["Analytics"])
app.include_router(logs_routes.router, prefix="/api/logs", tags=["Logs"])

# ========== ROOT ==========
@app.get("/")
def root():
    return {
        "message": "Smart Fulfillment System API Running",
        "version": "2.0.0",
        "status": "live"
    }